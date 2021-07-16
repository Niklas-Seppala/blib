from os import path, getcwd
import json

from .files import Files
from .utils import RGBA

class Index:
    contents: dict = None

    def load(self):
        self.index_path = path.join(getcwd(), Files.index_path)
        with open(self.index_path) as f:
            self.contents = json.load(f)

    def backgrounds(self):
        return self.contents['backgrounds']

    def icons(self):
        return self.contents['icons']

    def colors(self):
        return self.contents['colors']

    def get_real_color(self, color_id: int) -> RGBA:
        color = self.colors()[str(color_id)]['hex']
        result = RGBA.from_hex(color)
        return result

index = Index()