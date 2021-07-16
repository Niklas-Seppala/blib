import json
from os import path, getcwd
from .utils import RGBA, Files


class Index:
    """Index that holds data related to source images."""
    json_data: dict = None

    def load(self):
        """Load the json file to this index.
        NOTE! source data must be specified before calling this method."""
        self.index_path = path.join(getcwd(), Files.index_path)
        with open(self.index_path) as f:
            self.json_data = json.load(f)

    def backgrounds(self):
        return self.json_data['backgrounds']

    def icons(self):
        return self.json_data['icons']

    def colors(self):
        return self.json_data['colors']

    def get_real_color(self, color_id: int) -> RGBA:
        """Maps color id to real RGBA value.

        Args:
            color_id (int): color id
        Returns:
            RGBA: RGBA object.
        """
        color = self.colors()[str(color_id)]['hex']
        result = RGBA.from_hex(color)
        return result

# application index instance
index = Index()
