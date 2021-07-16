import numpy as np
from PIL import Image

from .layer import Layer, LayerColors
from .utils import Vec3, Files

cache: dict = {}


def recolor(data: np.ndarray, colors: LayerColors):
    r, g, _, a = data.T
    red_mask = (r >= g) & (a > 10)
    green_mask = (g > r) & (a > 10)

    data[...][green_mask.T] = colors.main.unpack()
    data[...][red_mask.T] = colors.accent.unpack()


def resize_img(img: Image, size: Vec3, keep_ratio=True) -> Image:
    if size.x < 0:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        size.x *= -1
    if size.y < 0:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        size.y *= -1

    if keep_ratio:
        ratio = size.x / float(img.size[0])
        h_size = int(float(img.size[1]) * float(ratio))
        return img.resize((size.x, h_size))
    else:
        return img.resize((size.x, size.y))


def rotate_img(img: Image, size: Vec3):
    if size.z:
        img = img.rotate(size.z, expand=True)
        size.x = img.size[0]
        size.y = img.size[1]
    return img


def draw_background(bg_layer: Layer) -> Image:
    """Draw the background layer to image.

    Returns:
        Image: This image object is the root of the drawing process.
    """
    img = Image.open(Files.map_id_to_path(
        bg_layer.mesh_id)).convert('RGBA')
    return draw_layer(img, bg_layer, cache_miss=True)


def draw_foreground(image: Image, bg_size: Vec3, layers: list) -> Image:
    """Draws all the foreground layers on top of the background
    layer.

    Args:
        image (Image): Root image with background layer.
        bg_size (Vec3): Size of the background layer. 
        layers (list[Layer]): List of all of the foreground layers, in order.

    Returns:
        Image: Complete image of the banner.
    """
    for layer in layers:
        img = cache.get(layer.hash)
        miss = False
        if not img:
            img = Image.open(Files.map_id_to_path(
                layer.mesh_id)).convert('RGBA')
            miss = True
        img = draw_layer(img, layer, cache_miss=miss)
        image.paste(img, calc_pos(bg_size, img.size,
                                  layer.pos), mask=img)
    cache.clear()
    return image


def draw_layer(img: Image, layer: Layer, cache_miss: bool) -> Image:
    if cache_miss:
        img = resize_img(img, layer.size, keep_ratio=False)
        cache[layer.hash] = img

    if layer.mirror:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    img = rotate_img(img, layer.size)
    data = np.array(img)
    recolor(data, layer.colors)
    return Image.fromarray(data)


def calc_pos(bg_size: Vec3, src_img_size: list, pos: Vec3):
    X, Y = 0, 1
    offset_x = 764
    offset_y = 764

    real_pos_x = pos.x - offset_x
    real_pos_y = pos.y - offset_y

    center_p_x = int(bg_size.x / 2 - src_img_size[X] / 2)
    center_p_y = int(bg_size.y / 2 - src_img_size[Y] / 2)

    return center_p_x + real_pos_x, center_p_y + real_pos_y
