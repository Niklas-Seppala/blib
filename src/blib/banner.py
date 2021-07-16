import os
from PIL import Image

from .code import Code
from .draw import resize_img, draw_background, draw_foreground
from .utils import Vec3, Files

class Banner:
    """Banner object that holds the bitmap created from parsed
    banner code.
    """

    def __init__(self, encoded: str):
        """Creates a new Banner object.

        Args:
            encoded (str): Banner code in string form.
        """
        self._create(encoded)

    def recycle(self, encoded: str):
        """Rewrites the object state to match the new banner code.

        Args:
            encoded (str): Banner code in string form.

        Returns:
            Banner: This object.
        """
        self._create(encoded)
        return self

    def export(self) -> Image:
        """Returns a reference to PIL bitmap image object.

        Returns:
            Image: Banner as a PIL bitmap object.
        """
        return self.img

    def rescale(self, rate: float):
        """Rescales the current image.

        Args:
            rate (float): 0.0 - 1.0 f.

        Returns:
            Banner: this object.
        """
        width = int(self.img.size[0] * rate)
        height = int(self.img.size[1] * rate)
        self.resize(width, height, keep_ratio=True)
        return self

    def resize(self, width: int, height: int, keep_ratio=True):
        """Resizes the current banner image.

        Args:
            width (int): New width in pixels.
            height (int): New Height in pixels.
            keep_ratio (bool, optional): Does the new image retain the old
            widht-height ratio. Defaults to True.

        Returns:
            [type]: [description]
        """
        new_dims = Vec3(width, height, 0)
        self.img = resize_img(self.img, new_dims, keep_ratio)
        return self

    def save(self, format: Files.Format, path: str = '', name: str = ''):
        """Save image in specified format to disc.

        Args:
            format (Files.Format): Image format (PNG/JPEG)
            path (str, optional): File path to saved images directory. Defaults to ''.
            name (str, optional): Name of the file. Defaults to ''.

        Returns:
            Banner: This object.
        """
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
        """Crop the banner image.

        Args:
            width (int): Cropped image width in pixels.
            height (int): Cropped image height in pixels.

        Returns:
            Banner: This object.
        """
        left = self.img.size[0] / 2 - width / 2
        top = self.img.size[1] / 2 - height / 2
        right = left + width
        bottom = top + height
        self.img = self.img.crop((left, top, right, bottom))
        return self

    def _create(self, encoded: str):
        """Creates the bitmap image from banner code.

        Args:
            encoded (str): Banner code in string form.
        """
        self.img: Image = None
        self.code = Code(encoded)
        bg_layer = self.code.bg_layer()
        fg_layers = self.code.fg_layers()
        self.img = draw_background(bg_layer)
        self.img = draw_foreground(self.img, bg_layer.size, fg_layers)
