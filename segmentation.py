# paint_app/utils/segmentation.py

import cv2
import numpy as np
from PIL import Image
import io


def generate_mask_color_based(image_array):
    """
    Simple color-based wall detection (fast, no ML).
    Args:
        image_array: numpy array (BGR format from cv2)
    Returns:
        mask as numpy array (255=wall, 0=not wall)
    """
    hsv = cv2.cvtColor(image_array, cv2.COLOR_BGR2HSV)

    # Detect light colors (common for walls)
    lower_light = np.array([0, 0, 150])
    upper_light = np.array([180, 50, 255])
    mask = cv2.inRange(hsv, lower_light, upper_light)

    # Clean up noise
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Smooth edges
    mask = cv2.GaussianBlur(mask, (9, 9), 0)

    return mask


def generate_mask_grabcut(image_array):
    """
    GrabCut segmentation (better quality, moderate speed).
    Args:
        image_array: numpy array (BGR format from cv2)
    Returns:
        mask as numpy array (255=wall, 0=not wall)
    """
    # Create initial mask
    mask = np.zeros(image_array.shape[:2], np.uint8)

    # Background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define rectangle (assuming wall is in the outer area)
    h, w = image_array.shape[:2]
    rect = (10, 10, w - 20, h - 20)

    # Apply GrabCut algorithm
    cv2.grabCut(image_array, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create binary mask (0 and 2 are background, 1 and 3 are foreground)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    wall_mask = mask2 * 255

    return wall_mask


def apply_color_to_image(image_array, mask_array, color_hex, opacity=0.7):
    """
    Apply paint color to wall area only.
    Preserves texture and lighting.

    Args:
        image_array: numpy array (BGR format)
        mask_array: numpy array (grayscale, 255=wall, 0=not wall)
        color_hex: string like '#87CEEB'
        opacity: float 0.0-1.0 (how strong the color is)

    Returns:
        painted image as numpy array (BGR format)
    """
    # Convert hex color to BGR
    color_hex = color_hex.lstrip('#')
    r, g, b = tuple(int(color_hex[i:i + 2], 16) for i in (0, 2, 4))
    color_bgr = np.array([b, g, r], dtype=np.uint8)

    # Create colored layer (entire image filled with paint color)
    colored_layer = np.full_like(image_array, color_bgr)

    # Normalize mask to 0.0-1.0 range
    mask_normalized = mask_array.astype(float) / 255.0

    # Make mask 3-channel to match image
    if len(mask_normalized.shape) == 2:
        mask_normalized = np.stack([mask_normalized] * 3, axis=-1)

    # Convert images to float for blending
    img_float = image_array.astype(float)
    colored_float = colored_layer.astype(float)

    # Multiply blend (preserves texture and shadows)
    blended = (img_float * colored_float / 255.0) * mask_normalized

    # Mix blended with original based on opacity and mask
    result = img_float * (1 - mask_normalized * opacity) + blended * opacity

    # Convert back to uint8
    result = np.clip(result, 0, 255).astype(np.uint8)

    return result


def pil_to_cv2(pil_image):
    """
    Convert PIL Image to OpenCV numpy array (BGR format).

    Args:
        pil_image: PIL Image object (RGB)
    Returns:
        numpy array (BGR format for OpenCV)
    """
    # Convert PIL (RGB) to numpy array
    numpy_image = np.array(pil_image)

    # Convert RGB to BGR (OpenCV format)
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    return opencv_image


def cv2_to_pil(cv2_image):
    """
    Convert OpenCV numpy array to PIL Image.

    Args:
        cv2_image: numpy array (BGR format from OpenCV)
    Returns:
        PIL Image object (RGB)
    """
    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

    # Convert to PIL Image
    pil_image = Image.fromarray(rgb_image)

    return pil_image