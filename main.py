from PIL import Image, ImageDraw, ImageFont

CARD_NUMBER = "0000 0000 0000 0000"
BANK_NAME = "YOUR BANK"
CVV = "CVV: 111"
EXPIRY = "11/35"
CARD_HOLDER = "CARDHOLDER NAME"

PRIMARY_COLOR = "#1E3A8A"
SECONDARY_COLOR = "#1F2937"
TEXT_GRAY = "#6B7280"
BACKGROUND_GRAY = "#E5E7EB"
WHITE = "#FFFFFF"


def generate_card():
    width, height = 850, 540
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)

    for y in range(height):
        alpha = y / height
        r = int(255 - (20 * alpha))
        g = int(255 - (20 * alpha))
        b = int(255 - (20 * alpha))
        draw.line((0, y, width, y), fill=(r, g, b))

    try:
        title_font = ImageFont.truetype("arialbd.ttf", 42)
        number_font = ImageFont.truetype("ocra.ttf", 58)
        text_font = ImageFont.truetype("arial.ttf", 32)
    except:
        title_font = ImageFont.load_default(size=36)
        number_font = ImageFont.load_default(size=48)
        text_font = ImageFont.load_default(size=28)

    draw.text((50, 40), BANK_NAME, font=title_font, fill=PRIMARY_COLOR)

    draw.rounded_rectangle((50, 120, 110, 180), radius=12, fill=BACKGROUND_GRAY)
    for i in range(4):
        draw.rectangle(
            (55 + i * 15, 125, 65 + i * 15, 175),
            fill=PRIMARY_COLOR if i % 2 == 0 else WHITE,
        )

    bbox = draw.textbbox((0, 0), CARD_NUMBER, font=number_font)
    x = (width - (bbox[2] - bbox[0])) // 2
    draw.text((x, 240), CARD_NUMBER, font=number_font, fill=SECONDARY_COLOR)

    draw.rounded_rectangle((680, 40, 820, 130), radius=15, fill=PRIMARY_COLOR)
    draw.text((700, 60), "MIR", font=title_font, fill=WHITE)

    draw.text((50, 350), "VALID THRU", font=text_font, fill=TEXT_GRAY)
    draw.text((50, 390), EXPIRY, font=text_font, fill=SECONDARY_COLOR)
    draw.text((50, 450), CARD_HOLDER, font=text_font, fill=SECONDARY_COLOR)

    draw.text((700, 450), CVV, font=text_font, fill=TEXT_GRAY)

    draw.line((50, 320, 800, 320), fill=BACKGROUND_GRAY, width=2)

    draw.rectangle([(0, 0), (width - 1, height - 1)], outline="black", width=1)

    img.save("card.png", quality=100)
    img.show()


if __name__ == "__main__":
    generate_card()
