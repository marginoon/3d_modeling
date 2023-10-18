from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

image_width = 800
image_height = 600
image = Image.new("RGB", (image_width, image_height), color="white")
draw = ImageDraw.Draw(image)

is_drawing = False
polygon_points = []

def handle_click(event):
    global is_drawing, polygon_points
    if not is_drawing:
        is_drawing = True
        polygon_points = []
    polygon_points.append((event.x, event.y))

def handle_release(event):
    global is_drawing, draw
    if is_drawing:
        is_drawing = False
        np_image = np.array(image)
        mask = Image.new('L', (image_width, image_height), 0)
        polygon = [(x, y) for x, y in polygon_points]
        ImageDraw.Draw(mask).polygon(polygon, outline=1, fill=1)
        mask_array = np.array(mask)
        np_image[mask_array == 1] = (0, 255, 0)
        updated_image = Image.fromarray(np_image)
        ax.imshow(updated_image)
        fig.canvas.draw()

fig, ax = plt.subplots(figsize=(8, 6))
canvas_width, canvas_height = fig.canvas.get_width_height()
pil_image = Image.new("RGB", (canvas_width, canvas_height), color="white")
pil_draw = ImageDraw.Draw(pil_image)
ax.imshow(pil_image)

fig.canvas.mpl_connect('button_press_event', handle_click)
fig.canvas.mpl_connect('button_release_event', handle_release)

plt.show()
