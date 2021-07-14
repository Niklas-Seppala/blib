import os
from hashlib import md5
from PIL import Image

from blib.draw import calc_pos, draw_layer, resize_img, cache_get, cache_clear
from blib.vec3 import Vec3

from .files import Files
from .parser import BannerParser

class Banner:
    @staticmethod
    def create_hash(size: Vec3, id):
        return (size.x * 0xf1f1f1f1) ^ (size.y ^ id)

    def __init__(self, encoded: str):
        self.img: Image = None
        self.layers: list = BannerParser.parse(encoded)
        self.code_hash = md5(encoded.encode('utf-8')).hexdigest()
        self.name = ''

    def export(self) -> Image:
        return self.img

    def rescale(self, rate):
        new_x = int(self.img.size[0] * rate)
        new_y = int(self.img.size[1] * rate)
        self.resize(new_x, new_y, keep_ratio=True)
        return self

    def resize(self, new_width, new_height, keep_ratio=True):
        self.img = resize_img(self.img, Vec3(
            new_width, new_height, 0), keep_ratio)
        return self

    def save(self, path='', name='', format='PNG'):
        if not path:
            path = Files.out_path
        if not name:
            name = self.code_hash
        fname = '{name}.{format}'.format(name=name, format=format)
        self.name = fname

        if format == 'JPEG':
            self.img = self.img.convert('RGB')

        self.img.save(os.path.join(path, fname),
                      format=format)
        return self

    def crop(self, width, height):
        left = self.img.size[0] / 2 - width / 2
        top = self.img.size[1] / 2 - height / 2
        right = left + width
        bottom = top + height
        self.img = self.img.crop((left, top, right, bottom))
        return self

    def draw(self):
        bg_layer = self.layers[0]
        bg_img = Image.open(Files.get_img_path_by_id(bg_layer.mesh_id)).convert('RGBA')
        result_img = draw_layer(
            bg_img, bg_layer, layer_hash=None, was_cache_miss=True, is_bg=True)
        for layer in self.layers[1:]:
            layer_hash = self.create_hash(layer.size, layer.mesh_id)
            img = cache_get(layer_hash)
            cache_miss = False
            if not img:
                img = Image.open(Files.get_img_path_by_id(layer.mesh_id)).convert('RGBA')
                cache_miss = True
            img = draw_layer(img, layer, layer_hash, cache_miss)
            result_img.paste(img, calc_pos(bg_layer.size, img.size,
                                            layer.pos), mask=img)

        cache_clear()
        self.img = result_img
        return self
