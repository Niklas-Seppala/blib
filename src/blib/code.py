from .layer import Layer
from hashlib import md5

class Code:
    """Object that contains the parsed layers
    of the banner code."""

    layers: list = []
    layer_count = 0  # Acts also as a z-index for layer during parsing.
    hash: str

    def __init__(self, encoded: str):
        sections, count = self._split_to_sections(encoded)
        # Banner layer must have atleast 10 sections.
        if count % 10 != 0:
            raise ValueError('Invalid banner code.')
        layers = self._divide_to_layers(sections, count)
        self._parse_layers(layers)
        self._hash_banner_code(encoded)

    def bg_layer(self) -> Layer:
        """
        Returns:
            Layer: Background layer.
        """
        return self.layers[0]

    def fg_layers(self) -> list:
        """
        Returns:
            list[Layer]: List of the foreground layers.
        """
        return self.layers[1:]

    def _divide_to_layers(self, code: list, count: int):
        for i in range(0, count, Layer.SECT_COUNT):
            yield code[i:i + Layer.SECT_COUNT]

    def _hash_banner_code(self, encoded: str):
        self.hash = md5(encoded.encode('utf-8')).hexdigest()

    def _parse_layers(self, layers):
        self._create_layer(next(layers), is_bg=True)
        for layer in layers:
            try:
                self._create_layer(layer)
            except:
                raise ValueError(
                    f'Parse error occured on layer {self.layer_count}.')

    def _split_to_sections(self, encoded: str) -> tuple:
        sections = encoded.split('.')
        count = len(sections)
        return sections, count

    def _create_layer(self, layer, is_bg=False):
        self.layers.append(Layer(layer, self.layer_count, is_bg))
        self.layer_count += 1
