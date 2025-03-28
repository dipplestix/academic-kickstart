from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon():
    # Create a 32x32 image with a transparent background
    size = 32
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a circle background
    circle_color = (41, 128, 185)  # A professional blue color
    draw.ellipse([0, 0, size-1, size-1], fill=circle_color)
    
    # Try to use a system font, fallback to default if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    # Draw the text "CM" in white
    text = "CM"
    text_color = (255, 255, 255)  # White
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    draw.text((x, y), text, font=font, fill=text_color)
    
    # Save as PNG in multiple sizes
    image.save('static/images/favicon-32x32.png')
    image.save('static/images/favicon-16x16.png')
    
    # Create a larger version for better visibility
    large_size = 192
    large_image = image.resize((large_size, large_size), Image.Resampling.LANCZOS)
    large_image.save('static/images/favicon-192x192.png')
    
    # Convert to ICO with multiple sizes
    img = Image.open('static/images/favicon-32x32.png')
    img.save('static/favicon.ico', format='ICO', sizes=[(16,16), (32,32)])

if __name__ == '__main__':
    create_favicon() 