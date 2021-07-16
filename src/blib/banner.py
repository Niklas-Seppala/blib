import os
from PIL import Image

from .code import Code
from .draw import resize_img, draw_background, draw_foreground
from .utils import Vec3
from .files import Files

class Banner:
    """[summary]
    """
    def __init__(self, encoded: str):
        self.create(encoded)

    def create(self, encoded: str):
        self.img: Image = None
        self.code = Code(encoded)
        bg_layer = self.code.bg_layer()
        fg_layers = self.code.fg_layers()
        self.img = draw_background(bg_layer)
        self.img = draw_foreground(self.img, bg_layer, fg_layers)

    def recycle(self, encoded: str):
        self.create(encoded)
        return self

    def export(self) -> Image:
        return self.img

    def rescale(self, rate):
        width = int(self.img.size[0] * rate)
        height = int(self.img.size[1] * rate)
        self.resize(width, height, keep_ratio=True)
        return self

    def resize(self, width, height, keep_ratio=True):
        new_dims = Vec3(width, height, 0)
        self.img = resize_img(self.img, new_dims, keep_ratio)
        return self

    def save(self, format: Files.Format, path: str ='', name: str =''):
        if not path:
            path = Files.out_path
        if not name:
            name = self.code.hash
        filename = f'{name}.{Files.Format.str(format)}'

        if format == Files.Format.JPEG:
            self.img = self.img.convert('RGB')

        self.img.save(os.path.join(path, filename),
                      format=Files.Format.str(format))
        return self

    def crop(self, width, height):
        left = self.img.size[0] / 2 - width / 2
        top = self.img.size[1] / 2 - height / 2
        right = left + width
        bottom = top + height
        self.img = self.img.crop((left, top, right, bottom))
        return self
