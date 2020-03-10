from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
import time
import datetime

serial = spi(device=0, port=0)
device = ssd1309(serial)

def primitives(device, draw):
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 2
    shape_width = 20
    top = padding
    bottom = device.height - padding - 1
    # Move left to right keeping track of the current x position for drawing shapes.
    x = padding
    # Draw an ellipse.
    draw.ellipse((x, top, x + shape_width, bottom), outline="red", fill="black")
    x += shape_width + padding
    # Draw a rectangle.
    draw.rectangle((x, top, x + shape_width, bottom), outline="blue", fill="black")
    x += shape_width + padding
    # Draw a triangle.
    draw.polygon([(x, bottom), (x + shape_width / 2, top), (x + shape_width, bottom)], outline="green", fill="black")
    x += shape_width + padding
    # Draw an X.
    draw.line((x, bottom, x + shape_width, top), fill="yellow")
    draw.line((x, top, x + shape_width, bottom), fill="yellow")
    x += shape_width + padding
    # Write two lines of text.
    size = draw.textsize('World!')
    x = device.width - padding - size[0]
    draw.rectangle((x, top + 4, x + size[0], top + size[1]), fill="black")
    draw.rectangle((x, top + 16, x + size[0], top + 16 + size[1]), fill="black")
    draw.text((device.width - padding - size[0], top + 4), 'Hello', fill="cyan")
    draw.text((device.width - padding - size[0], top + 16), 'World!', fill="purple")
    # Draw a rectangle of the same size of screen
    draw.rectangle(device.bounding_box, outline="white")


time.sleep(2)
x = 0
while True:
    with canvas(device) as draw:
        now = datetime.datetime.now()
        musictitle = "This Very Long Music Title Circling in the screen"
        if x <= 128:
            draw.text((x, 0), str(now.date()), fill="white")
            --draw.text((48-x, 11), musictitle, fill="white")
        if x > 128:
                x = 0
        draw.text((10, 20), str(now.time()), fill="white")
        x += 1
        print(x)
        time.sleep(0.1)
