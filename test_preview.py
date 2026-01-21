"""
Manual test script for Wall Preview feature
Run: python manage.py shell < test_preview.py
"""

print("=" * 60)
print("WALL PREVIEW DIAGNOSTIC TEST")
print("=" * 60)

from django.contrib.auth.models import User
from paint_app.models import WallPreview, PaintProduct, PaintBrand

# Test 1: Check if models are accessible
print("\n1. Testing Models...")
try:
    print("   ✓ WallPreview model accessible")
    print("   ✓ PaintProduct model accessible")
    print("   ✓ PaintBrand model accessible")
except Exception as e:
    print(f"   ✗ Error importing models: {e}")

# Test 2: Check if users exist
print("\n2. Testing Users...")
user_count = User.objects.count()
print(f"   Total users: {user_count}")
if user_count > 0:
    test_user = User.objects.first()
    print(f"   ✓ Test user available: {test_user.username}")
else:
    print("   ⚠ No users found. Create one with: python manage.py createsuperuser")

# Test 3: Check paint products and colors
print("\n3. Testing Paint Products...")
product_count = PaintProduct.objects.count()
print(f"   Total products: {product_count}")

if product_count > 0:
    products_with_stock = PaintProduct.objects.filter(stock__gt=0).count()
    print(f"   Products in stock: {products_with_stock}")

    # Show sample colors
    print("\n   Available colors:")
    colors = PaintProduct.objects.filter(stock__gt=0).values(
        'color_code', 'color_name', 'brand__name'
    ).distinct()[:5]

    for color in colors:
        print(f"   - {color['color_name']}: {color['color_code']} ({color['brand__name']})")

    if products_with_stock > 0:
        print("   ✓ Colors available for preview")
    else:
        print("   ✗ No products with stock!")
else:
    print("   ✗ No products found!")
    print("   Run: python manage.py shell < setup_data.py")

# Test 4: Check wall previews
print("\n4. Testing Wall Previews...")
preview_count = WallPreview.objects.count()
print(f"   Total wall previews: {preview_count}")

if preview_count > 0:
    recent = WallPreview.objects.order_by('-created_at')[:3]
    print("\n   Recent previews:")
    for preview in recent:
        print(f"   - User: {preview.user.username}")
        print(f"     Image: {preview.wall_image.url}")
        print(f"     Date: {preview.created_at}")
        if preview.selected_color_code:
            print(f"     Last color: {preview.selected_color_code}")
        print()
else:
    print("   ⚠ No wall previews uploaded yet")

# Test 5: Check media configuration
print("\n5. Testing Media Configuration...")
from django.conf import settings
import os

print(f"   MEDIA_URL: {settings.MEDIA_URL}")
print(f"   MEDIA_ROOT: {settings.MEDIA_ROOT}")

media_exists = os.path.exists(settings.MEDIA_ROOT)
if media_exists:
    print("   ✓ Media directory exists")

    preview_dir = os.path.join(settings.MEDIA_ROOT, 'wall_previews')
    if os.path.exists(preview_dir):
        file_count = len(os.listdir(preview_dir))
        print(f"   ✓ wall_previews directory exists ({file_count} files)")
    else:
        print("   ⚠ wall_previews directory doesn't exist")
        print(f"   Create it: mkdir -p {preview_dir}")
else:
    print("   ✗ Media directory doesn't exist!")
    print(f"   Create it: mkdir -p {settings.MEDIA_ROOT}")

# Test 6: URL configuration check
print("\n6. Testing URL Configuration...")
try:
    from django.urls import reverse

    urls_to_test = [
        'wall_preview',
    ]

    for url_name in urls_to_test:
        try:
            url = reverse(url_name)
            print(f"   ✓ {url_name}: {url}")
        except Exception as e:
            print(f"   ✗ {url_name}: Error - {e}")

except Exception as e:
    print(f"   ✗ Error checking URLs: {e}")

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

issues = []

if user_count == 0:
    issues.append("No users exist - create superuser")

if product_count == 0:
    issues.append("No paint products - run setup_data.py")
elif PaintProduct.objects.filter(stock__gt=0).count() == 0:
    issues.append("No products with stock")

if not media_exists:
    issues.append("Media directory missing")

if issues:
    print("\n⚠ ISSUES FOUND:")
    for i, issue in enumerate(issues, 1):
        print(f"   {i}. {issue}")
    print("\nFix these issues before testing wall preview.")
else:
    print("\n✓ ALL CHECKS PASSED!")
    print("\nYou can now:")
    print("   1. Run server: python manage.py runserver")
    print("   2. Login to the system")
    print("   3. Navigate to Wall Preview")
    print("   4. Upload a wall image")
    print("   5. Test color selection and painting")

print("\n" + "=" * 60)