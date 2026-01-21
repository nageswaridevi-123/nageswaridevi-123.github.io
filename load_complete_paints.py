# load_complete_paints.py

from paint_app.models import PaintBrand, PaintProduct

print("=" * 80)
print("LOADING COMPLETE PAINT CATALOG")
print("=" * 80)

# Clear existing data (optional - comment out if you want to keep existing)
# PaintProduct.objects.all().delete()
# PaintBrand.objects.all().delete()

# ============================================================================
# CREATE BRANDS
# ============================================================================

brands_data = [
    {'name': 'Dulux', 'description': 'Premium quality paints from AkzoNobel'},
    {'name': 'Asian Paints', 'description': 'India\'s leading paint brand'},
    {'name': 'Nerolac', 'description': 'Kansai Nerolac - Beautiful homes made easy'},
    {'name': 'Nippon Paint', 'description': 'Japanese paint technology'},
    {'name': 'Berger Paints', 'description': 'Trusted for generations'},
]

brands = {}
for brand_data in brands_data:
    brand, created = PaintBrand.objects.get_or_create(
        name=brand_data['name'],
        defaults={'description': brand_data['description']}
    )
    brands[brand.name] = brand
    print(f"{'✓ Created' if created else '  Exists'}: {brand.name}")

# ============================================================================
# DULUX PRODUCTS
# ============================================================================

print("\n" + "=" * 80)
print("ADDING DULUX PRODUCTS")
print("=" * 80)

dulux_products = [
    # MATTE FINISH
    {'name': 'Velvet Touch', 'color_name': 'Pure White', 'color_code': '#FFFFFF',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [280, 1050, 2400, 4500]},
    {'name': 'Velvet Touch', 'color_name': 'Ivory', 'color_code': '#FFFFF0',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [280, 1050, 2400]},
    {'name': 'Diamond Matt', 'color_name': 'Cool Grey', 'color_code': '#8C92AC',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [320, 1200, 2750, 5200]},
    {'name': 'EasyCare Matt', 'color_name': 'Warm Beige', 'color_code': '#F5F5DC',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [290, 1080, 2480]},

    # SATIN FINISH
    {'name': 'Dulux Silk', 'color_name': 'Sky Blue', 'color_code': '#87CEEB',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L'], 'prices': [300, 1120, 2580]},
    {'name': 'Diamond Eggshell', 'color_name': 'Soft Pink', 'color_code': '#FFB6C1',
     'finish': 'satin', 'sizes': ['1L', '4L'], 'prices': [330, 1240]},
    {'name': 'Satinwood', 'color_name': 'Mint Green', 'color_code': '#98FF98',
     'finish': 'satin', 'sizes': ['1L', '4L'], 'prices': [310, 1160]},

    # SEMI-GLOSS
    {'name': 'Quick Dry Satinwood', 'color_name': 'Classic White', 'color_code': '#FAFAFA',
     'finish': 'semi_glossy', 'sizes': ['1L', '4L'], 'prices': [340, 1280]},
    {'name': 'Trade Satinwood', 'color_name': 'Pearl Grey', 'color_code': '#D3D3D3',
     'finish': 'semi_glossy', 'sizes': ['1L', '4L', '10L'], 'prices': [350, 1320, 3050]},

    # GLOSSY
    {'name': 'Dulux Gloss', 'color_name': 'Brilliant White', 'color_code': '#FFFFFF',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [360, 1360]},
    {'name': 'Quick Dry Gloss', 'color_name': 'Racing Green', 'color_code': '#228B22',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [370, 1400]},
]

# ============================================================================
# ASIAN PAINTS PRODUCTS
# ============================================================================

print("\nADDING ASIAN PAINTS PRODUCTS")

asian_paints_products = [
    # MATTE FINISH
    {'name': 'Royale Matt', 'color_name': 'Snow White', 'color_code': '#FFFAFA',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [270, 1020, 2350, 4450]},
    {'name': 'Royale Matt', 'color_name': 'Desert Sand', 'color_code': '#EDC9AF',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [270, 1020, 2350]},
    {'name': 'Apcolite Premium', 'color_name': 'Ocean Blue', 'color_code': '#4682B4',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [250, 940, 2150]},
    {'name': 'Tractor Emulsion', 'color_name': 'Lemon Yellow', 'color_code': '#FFFF00',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [180, 680, 1560, 2950]},

    # SATIN FINISH
    {'name': 'Royale Shyne', 'color_name': 'Pearl White', 'color_code': '#F8F8FF',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L'], 'prices': [290, 1090, 2510]},
    {'name': 'Royale Luxury', 'color_name': 'Rose Pink', 'color_code': '#FF69B4',
     'finish': 'satin', 'sizes': ['1L', '4L'], 'prices': [310, 1170]},
    {'name': 'Tractor Shyne', 'color_name': 'Turquoise', 'color_code': '#40E0D0',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L'], 'prices': [200, 750, 1720]},

    # SEMI-GLOSS
    {'name': 'Apcolite Advanced', 'color_name': 'Cream', 'color_code': '#FFFDD0',
     'finish': 'semi_glossy', 'sizes': ['1L', '4L'], 'prices': [320, 1200]},

    # GLOSSY
    {'name': 'Apcolite Enamel', 'color_name': 'Cherry Red', 'color_code': '#DC143C',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [350, 1320]},
    {'name': 'Enamelac', 'color_name': 'Royal Blue', 'color_code': '#000080',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [340, 1280]},
]

# ============================================================================
# NEROLAC PRODUCTS
# ============================================================================

print("ADDING NEROLAC PRODUCTS")

nerolac_products = [
    # MATTE FINISH
    {'name': 'Beauty Gold', 'color_name': 'Pristine White', 'color_code': '#FFFFFF',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [260, 980, 2250, 4250]},
    {'name': 'Impressions', 'color_name': 'Olive Green', 'color_code': '#808000',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [280, 1050, 2420]},
    {'name': 'Excel Total', 'color_name': 'Light Grey', 'color_code': '#D3D3D3',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [170, 640, 1470, 2780]},

    # SATIN FINISH
    {'name': 'Beauty Salon Finish', 'color_name': 'Peach', 'color_code': '#FFDAB9',
     'finish': 'satin', 'sizes': ['1L', '4L'], 'prices': [280, 1050]},
    {'name': 'Impressions Luxury', 'color_name': 'Lavender', 'color_code': '#E6E6FA',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L'], 'prices': [300, 1130, 2600]},

    # SEMI-GLOSS
    {'name': 'Nerolac IQ', 'color_name': 'Steel Blue', 'color_code': '#4682B4',
     'finish': 'semi_glossy', 'sizes': ['1L', '4L'], 'prices': [310, 1170]},

    # GLOSSY
    {'name': 'Beauty Enamel', 'color_name': 'Fire Red', 'color_code': '#FF0000',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [340, 1280]},
    {'name': 'Syntex', 'color_name': 'Jet Black', 'color_code': '#000000',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [330, 1240]},
]

# ============================================================================
# NIPPON PAINT PRODUCTS
# ============================================================================

print("ADDING NIPPON PAINT PRODUCTS")

nippon_products = [
    # MATTE FINISH
    {'name': 'Odour-less Premium', 'color_name': 'Arctic White', 'color_code': '#F0F8FF',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [290, 1090, 2510]},
    {'name': 'Vinilex Fresh', 'color_name': 'Sage Green', 'color_code': '#9DC183',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [270, 1020, 2350]},
    {'name': 'Matex', 'color_name': 'Sand Beige', 'color_code': '#F4A460',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [180, 680, 1560, 2950]},

    # SATIN FINISH
    {'name': 'Vinilex 5000', 'color_name': 'Coral', 'color_code': '#FF7F50',
     'finish': 'satin', 'sizes': ['1L', '4L'], 'prices': [300, 1130]},
    {'name': 'Silk Touch', 'color_name': 'Dusty Rose', 'color_code': '#DCAE96',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L'], 'prices': [280, 1050, 2420]},

    # SEMI-GLOSS
    {'name': '3-in-1 Medifresh', 'color_name': 'Clinical White', 'color_code': '#FAFAFA',
     'finish': 'semi_glossy', 'sizes': ['1L', '4L'], 'prices': [320, 1200]},

    # GLOSSY
    {'name': 'Hi-Gloss Enamel', 'color_name': 'Sunset Orange', 'color_code': '#FF8C00',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [350, 1320]},
    {'name': 'Quick Dry Enamel', 'color_name': 'Emerald Green', 'color_code': '#50C878',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [360, 1360]},
]

# ============================================================================
# BERGER PAINTS PRODUCTS
# ============================================================================

print("ADDING BERGER PAINTS PRODUCTS")

berger_products = [
    # MATTE FINISH
    {'name': 'Silk Luxury', 'color_name': 'Cloud White', 'color_code': '#F5F5F5',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [280, 1050, 2420, 4580]},
    {'name': 'Easy Clean Fresh', 'color_name': 'Lilac', 'color_code': '#C8A2C8',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L'], 'prices': [270, 1020, 2350]},
    {'name': 'Magicote', 'color_name': 'Warm Yellow', 'color_code': '#FFDB58',
     'finish': 'matte', 'sizes': ['1L', '4L', '10L', '20L'], 'prices': [170, 640, 1470, 2780]},

    # SATIN FINISH
    {'name': 'Silk Glamour', 'color_name': 'Mauve', 'color_code': '#E0B0FF',
     'finish': 'satin', 'sizes': ['1L', '4L'], 'prices': [290, 1090]},
    {'name': 'Easy Clean', 'color_name': 'Aqua Blue', 'color_code': '#00FFFF',
     'finish': 'satin', 'sizes': ['1L', '4L', '10L'], 'prices': [280, 1050, 2420]},

    # SEMI-GLOSS
    {'name': 'Luxol Hi-Gloss', 'color_name': 'Champagne', 'color_code': '#F7E7CE',
     'finish': 'semi_glossy', 'sizes': ['1L', '4L'], 'prices': [330, 1240]},

    # GLOSSY
    {'name': 'Luxol', 'color_name': 'Deep Red', 'color_code': '#8B0000',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [340, 1280]},
    {'name': 'Robbialac Enamel', 'color_name': 'Chocolate Brown', 'color_code': '#8B4513',
     'finish': 'glossy', 'sizes': ['1L', '4L'], 'prices': [360, 1360]},
]

# ============================================================================
# ADD ALL PRODUCTS TO DATABASE
# ============================================================================

all_products = [
    ('Dulux', dulux_products),
    ('Asian Paints', asian_paints_products),
    ('Nerolac', nerolac_products),
    ('Nippon Paint', nippon_products),
    ('Berger Paints', berger_products),
]

total_created = 0

for brand_name, products in all_products:
    brand = brands[brand_name]
    print(f"\nProcessing {brand_name}...")

    for product_data in products:
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
                total_created += 1

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"✓ Total Brands: {PaintBrand.objects.count()}")
print(f"✓ Total Products: {PaintProduct.objects.count()}")
print(f"✓ New Products Added: {total_created}")
print(f"✓ Products in Stock: {PaintProduct.objects.filter(stock__gt=0).count()}")

# Show color breakdown
print("\n" + "=" * 80)
print("COLOR BREAKDOWN BY BRAND")
print("=" * 80)
for brand_name in brands.keys():
    brand = brands[brand_name]
    count = PaintProduct.objects.filter(brand=brand).count()
    print(f"{brand_name}: {count} products")

print("\n✓ COMPLETE! All paint products loaded successfully!")
print("=" * 80)