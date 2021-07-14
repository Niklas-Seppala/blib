from os import path, getcwd
import json

from blib.files import Files
from blib.rgba import RGBA

class Index:
    content: dict = None

    def load(self):
        self.index_path = path.join(getcwd(), Files.index_path)
        with open(self.index_path) as f:
            self.content = json.load(f)

    def backgrounds(self):
        return self.content['backgrounds']

    def icons(self):
        return self.content['icons']

    def colors(self):
        return self.content['colors']

    def get_real_color(self, color_id: int) -> RGBA:
        color = self.colors()[str(color_id)]['hex']
        result = RGBA.from_hex(color)
        return result

index = Index()