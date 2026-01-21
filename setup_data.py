# setup_data.py
from paint_app.models import PaintBrand, PaintProduct

print("Creating paint brands...")

# Create Brands
brands_data = [
    {'name': 'Dulux', 'description': 'Premium quality paints'},
    {'name': 'Nippon', 'description': 'Japanese paint technology'},
    {'name': 'Berger', 'description': 'Trusted for generations'},
    {'name': 'Asian Paints', 'description': 'India\'s leading paint brand'},
    {'name': 'Nerolac', 'description': 'Beautiful homes made easy'},
]

brands = {}
for brand_data in brands_data:
    brand, created = PaintBrand.objects.get_or_create(
        name=brand_data['name'],
        defaults={'description': brand_data['description']}
    )
    brands[brand.name] = brand
    if created:
        print(f"✓ Created brand: {brand.name}")
    else:
        print(f"  Brand already exists: {brand.name}")

print("\nCreating paint products...")

# Create Products
products_data = [
    # Dulux Products
    {'brand': 'Dulux', 'name': 'Premium White', 'color_name': 'Pure White', 'color_code': '#FFFFFF',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [250, 900, 2100, 4000]},
    {'brand': 'Dulux', 'name': 'Sky Blue', 'color_name': 'Ocean Blue', 'color_code': '#87CEEB',
     'finish': 'glossy', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [280, 1000, 2300, 4400]},

    # Nippon Products
    {'brand': 'Nippon', 'name': 'Classic Cream', 'color_name': 'Ivory Cream', 'color_code': '#FFFDD0',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [270, 950, 2200, 4200]},
    {'brand': 'Nippon', 'name': 'Rose Pink', 'color_name': 'Blush Pink', 'color_code': '#FFB6C1',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [290, 1050, 2400]},

    # Berger Products
    {'brand': 'Berger', 'name': 'Forest Green', 'color_name': 'Emerald Green', 'color_code': '#228B22',
     'finish': 'semi_glossy', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [260, 920, 2150, 4100]},
    {'brand': 'Berger', 'name': 'Royal Purple', 'color_name': 'Deep Purple', 'color_code': '#663399',
     'finish': 'glossy', 'sizes': ['1L', '4L', '10L'], 'prices': [300, 1100, 2500]},

    # Asian Paints Products
    {'brand': 'Asian Paints', 'name': 'Sunset Orange', 'color_name': 'Tangerine', 'color_code': '#FF8C00',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [265, 940, 2180, 4150]},
    {'brand': 'Asian Paints', 'name': 'Charcoal Grey', 'color_name': 'Stone Grey', 'color_code': '#696969',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L'], 'prices': [275, 980, 2250]},

    # Nerolac Products
    {'brand': 'Nerolac', 'name': 'Lemon Yellow', 'color_name': 'Sunshine Yellow', 'color_code': '#FFFF00',
     'finish': 'glossy', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [255, 910, 2130, 4050]},
    {'brand': 'Nerolac', 'name': 'Mint Green', 'color_name': 'Fresh Mint', 'color_code': '#98FF98',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [260, 930, 2170]},

    # More colors for wall preview
    {'brand': 'Dulux', 'name': 'Ruby Red', 'color_name': 'Crimson Red', 'color_code': '#DC143C',
     'finish': 'glossy', 'sizes': ['1L', '4L', '10L'], 'prices': [290, 1050, 2400]},
    {'brand': 'Nippon', 'name': 'Navy Blue', 'color_name': 'Deep Navy', 'color_code': '#000080',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [280, 1000, 2300]},
    {'brand': 'Berger', 'name': 'Peach', 'color_name': 'Soft Peach', 'color_code': '#FFDAB9',
     'finish': 'satin', 'sizes': ['1L', '4L'], 'prices': [270, 950]},
    {'brand': 'Asian Paints', 'name': 'Lavender', 'color_name': 'Light Lavender', 'color_code': '#E6E6FA',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [265, 940, 2180]},
]

product_count = 0
for product_data in products_data:
    brand = brands[product_data['brand']]
    for i, size in enumerate(product_data['sizes']):
        product, created = PaintProduct.objects.get_or_create(
            brand=brand,
            name=product_data['name'],
            color_name=product_data['color_name'],
            size=size,
            defaults={
                'color_code': product_data['color_code'],
                'finish': product_data['finish'],
                'price': product_data['prices'][i],
                'coverage_per_litre': 10.0,
                'stock': 50
            }
        )
        if created:
            product_count += 1

print(f"\n✓ Created {product_count} products successfully!")
print(f"✓ Total products in database: {PaintProduct.objects.count()}")
print(f"✓ Products with stock: {PaintProduct.objects.filter(stock__gt=0).count()}")
print("\nSetup completed! You can now use the wall preview feature.")