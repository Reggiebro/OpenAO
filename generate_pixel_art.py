#!/usr/bin/env python3
"""Generate original pixel art for Argentum Online (OpenAO).

Creates a 128x128 pixel art of a warrior character in the style of
classic top-down MMORPGs like Argentum Online / Ultima Online.
"""

from PIL import Image, ImageDraw

# Create 128x128 image
WIDTH, HEIGHT = 128, 128
img = Image.new('RGB', (WIDTH, HEIGHT), (34, 139, 34))  # Forest green background
draw = ImageDraw.Draw(img)

# --- Background: grass tiles with subtle variation ---
for y in range(0, HEIGHT, 8):
    for x in range(0, WIDTH, 8):
        # Vary grass color slightly
        if (x + y) % 16 == 0:
            color = (30, 120, 30)
        else:
            color = (34, 139, 34)
        draw.rectangle([x, y, x+7, y+7], fill=color)

# Add some grass detail pixels
for y in range(4, HEIGHT, 8):
    for x in range(4, WIDTH, 8):
        if (x * y) % 3 == 0:
            draw.point((x, y), fill=(50, 160, 50))

# --- Character: Warrior in top-down view ---
# Position character centered
cx, cy = 64, 64  # Center of character

# Shadow (darker ellipse under character)
draw.ellipse([cx-16, cy+20, cx+16, cy+30], fill=(20, 80, 20))

# --- Legs (brown boots) ---
# Left boot
draw.rectangle([cx-10, cy+8, cx-4, cy+22], fill=(101, 67, 33))
draw.rectangle([cx-10, cy+20, cx-4, cy+22], fill=(80, 50, 20))
# Right boot
draw.rectangle([cx+4, cy+8, cx+10, cy+22], fill=(101, 67, 33))
draw.rectangle([cx+4, cy+20, cx+10, cy+22], fill=(80, 50, 20))

# --- Body (chainmail armor - gray) ---
# Torso
draw.rectangle([cx-12, cy-6, cx+12, cy+10], fill=(128, 128, 128))
# Armor shading
draw.rectangle([cx-12, cy-6, cx-8, cy+10], fill=(100, 100, 100))  # Left shadow
draw.rectangle([cx+8, cy-6, cx+12, cy+10], fill=(150, 150, 150))  # Right highlight

# Belt
draw.rectangle([cx-12, cy+6, cx+12, cy+10], fill=(80, 50, 20))
# Belt buckle
draw.rectangle([cx-2, cy+7, cx+2, cy+9], fill=(218, 165, 32))  # Gold

# --- Arms ---
# Left arm (holding shield)
draw.rectangle([cx-18, cy-4, cx-12, cy+8], fill=(128, 128, 128))
draw.rectangle([cx-18, cy-4, cx-12, cy], fill=(100, 100, 100))  # Shoulder shadow
# Left hand (skin)
draw.rectangle([cx-18, cy+6, cx-12, cy+10], fill=(224, 172, 105))

# Right arm (holding sword)
draw.rectangle([cx+12, cy-4, cx+18, cy+8], fill=(128, 128, 128))
draw.rectangle([cx+12, cy-4, cx+18, cy], fill=(100, 100, 100))  # Shoulder shadow
# Right hand (skin)
draw.rectangle([cx+12, cy+6, cx+18, cy+10], fill=(224, 172, 105))

# --- Shield (left side) ---
# Shield body (wooden with metal rim)
shield_x = cx - 28
shield_y = cy - 2
# Shield shape (rounded rectangle)
draw.rectangle([shield_x-2, shield_y-8, shield_x+4, shield_y+12], fill=(139, 90, 43))
# Shield rim
draw.rectangle([shield_x-2, shield_y-8, shield_x+4, shield_y-6], fill=(180, 180, 180))
draw.rectangle([shield_x-2, shield_y+10, shield_x+4, shield_y+12], fill=(180, 180, 180))
draw.rectangle([shield_x-2, shield_y-8, shield_x, shield_y+12], fill=(180, 180, 180))
draw.rectangle([shield_x+2, shield_y-8, shield_x+4, shield_y+12], fill=(180, 180, 180))
# Shield emblem (red cross)
draw.rectangle([shield_x, shield_y-4, shield_x+2, shield_y+8], fill=(200, 30, 30))
draw.rectangle([shield_x-2, shield_y, shield_x+4, shield_y+2], fill=(200, 30, 30))

# --- Sword (right side, raised) ---
sword_x = cx + 22
sword_y = cy - 12
# Sword blade
draw.rectangle([sword_x-1, sword_y-10, sword_x+1, sword_y+6], fill=(200, 200, 220))
# Sword tip
draw.polygon([(sword_x-1, sword_y-10), (sword_x+1, sword_y-10), (sword_x, sword_y-14)], fill=(220, 220, 240))
# Sword guard
draw.rectangle([sword_x-4, sword_y+6, sword_x+4, sword_y+8], fill=(218, 165, 32))  # Gold
# Sword handle
draw.rectangle([sword_x-1, sword_y+8, sword_x+1, sword_y+12], fill=(80, 50, 20))
# Sword pommel
draw.rectangle([sword_x-2, sword_y+12, sword_x+2, sword_y+14], fill=(218, 165, 32))

# --- Head ---
# Neck
draw.rectangle([cx-4, cy-10, cx+4, cy-6], fill=(224, 172, 105))
# Head (skin)
draw.rectangle([cx-6, cy-20, cx+6, cy-10], fill=(224, 172, 105))
# Face shadow (right side)
draw.rectangle([cx+2, cy-20, cx+6, cy-10], fill=(200, 150, 85))

# --- Helmet ---
# Helmet base (covers top of head)
draw.rectangle([cx-8, cy-24, cx+8, cy-14], fill=(128, 128, 128))
# Helmet shading
draw.rectangle([cx-8, cy-24, cx-4, cy-14], fill=(100, 100, 100))
draw.rectangle([cx+4, cy-24, cx+8, cy-14], fill=(150, 150, 150))
# Helmet nose guard
draw.rectangle([cx-2, cy-20, cx+2, cy-10], fill=(128, 128, 128))
# Helmet top ridge
draw.rectangle([cx-1, cy-26, cx+1, cy-20], fill=(100, 100, 100))

# --- Helmet plume (red) ---
draw.polygon([(cx-1, cy-26), (cx+1, cy-26), (cx, cy-34)], fill=(200, 30, 30))
draw.polygon([(cx-2, cy-26), (cx, cy-26), (cx-1, cy-32)], fill=(180, 20, 20))
draw.polygon([(cx, cy-26), (cx+2, cy-26), (cx+1, cy-32)], fill=(180, 20, 20))

# --- Eyes (barely visible under helmet) ---
draw.point((cx-3, cy-16), fill=(50, 30, 20))
draw.point((cx+3, cy-16), fill=(50, 30, 20))

# --- Decorative elements ---

# Gold coins scattered near feet
coin_positions = [(cx-20, cy+26), (cx-16, cy+28), (cx+18, cy+26), (cx+22, cy+28)]
for pos in coin_positions:
    x, y = pos
    draw.ellipse([x-2, y-2, x+2, y+2], fill=(218, 165, 32))
    draw.point((x-1, y-1), fill=(255, 215, 0))

# Small stones
stone_positions = [(cx-30, cy+10), (cx+30, cy+12)]
for pos in stone_positions:
    x, y = pos
    draw.ellipse([x-2, y-1, x+2, y+2], fill=(150, 150, 150))

# --- Border frame (decorative AO-style) ---
# Top border
for x in range(0, WIDTH, 4):
    draw.rectangle([x, 0, x+3, 2], fill=(139, 90, 43))
# Bottom border
for x in range(0, WIDTH, 4):
    draw.rectangle([x, HEIGHT-2, x+3, HEIGHT], fill=(139, 90, 43))
# Left border
for y in range(0, HEIGHT, 4):
    draw.rectangle([0, y, 2, y+3], fill=(139, 90, 43))
# Right border
for y in range(0, HEIGHT, 4):
    draw.rectangle([WIDTH-2, y, WIDTH, y+3], fill=(139, 90, 43))

# Save the image
output_path = '/home/redman8326/OpenAO/assets/pixel-art/argentum-warrior.png'
img.save(output_path, 'PNG')
print(f"Pixel art saved to: {output_path}")
print(f"Size: {img.size[0]}x{img.size[1]} pixels")