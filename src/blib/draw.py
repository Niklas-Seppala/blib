import numpy as np
from PIL import Image

from .layer import Vec3, Layer
from .rgba import RGBA

banner_icon_cache: dict = {}

def cache_get(asd):
    return banner_icon_cache.get(asd)

def cache_clear():
    banner_icon_cache.clear()

def recolor(data: np.ndarray, main: RGBA, accent: RGBA):
    r, g, _, a = data.T
    red_mask = (r >= g) & (a > 10)
    green_mask = (g > r) & (a > 10)

    data[...][green_mask.T] = main.unpack()
    data[...][red_mask.T] = accent.unpack()


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


def draw_layer(img: Image, layer: Layer, layer_hash,
               was_cache_miss: bool, is_bg=False) -> Image:
    if was_cache_miss:
        img = resize_img(img, layer.size, keep_ratio=False)
        banner_icon_cache[layer_hash] = img

    if layer.mirror:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    img = rotate_img(img, layer.size)

    main_c, accent_c = layer.get_layer_colors(is_bg)
    data = np.array(img)
    recolor(data, main_c, accent_c)
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
