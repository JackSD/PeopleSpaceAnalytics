
from PIL import Image, ImageDraw

image = Image.open("static/plan_view.PNG")
draw = ImageDraw.Draw(image)
x = round(im.size[0]*0.5)
y = round(im.size[1]*0.5)
r=5
draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0,0))
del draw
# write to stdout
image.save("static/plan_view2.PNG")


