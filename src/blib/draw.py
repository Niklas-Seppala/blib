import numpy as np
from PIL import Image

from .files import Files
from .layer import Layer, LayerColors
from .utils import RGBA, Vec3

banner_icon_cache: dict = {}

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
    img = Image.open(Files.get_img_path_by_id(
        bg_layer.mesh_id)).convert('RGBA')
    result = draw_layer(img, bg_layer, cache_miss=True)
    return result

def draw_foreground(image: Image, bg_layer, layers: list[Layer]) -> Image:
    for layer in layers:
        img = banner_icon_cache.get(layer.hash)
        cache_miss = False
        if not img:
            img = Image.open(Files.get_img_path_by_id(
                layer.mesh_id)).convert('RGBA')
            cache_miss = True
        img = draw_layer(img, layer, cache_miss=cache_miss)
        image.paste(img, calc_pos(bg_layer.size, img.size,
                                        layer.pos), mask=img)
    banner_icon_cache.clear()
    return image

def draw_layer(img: Image, layer: Layer, cache_miss: bool) -> Image:
    if cache_miss:
        img = resize_img(img, layer.size, keep_ratio=False)
        banner_icon_cache[layer.hash] = img

    if layer.mirror:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    img = rotate_img(img, layer.size)
    data = np.array(img)
    recolor(data, layer.colors)
    return Image.fromarray(data)


def calc_pos(bg_size: Vec3, img_size: list, pos: Vec3):
    x_index, y_index = 0, 1
    offset_x = 764
    offset_y = 764

    real_pos_x = pos.x - offset_x
    real_pos_y = pos.y - offset_y

    center_p_x = int(bg_size.x / 2 - img_size[x_index] / 2)
    center_p_y = int(bg_size.y / 2 - img_size[y_index] / 2)

    return center_p_x + real_pos_x, center_p_y + real_pos_y
