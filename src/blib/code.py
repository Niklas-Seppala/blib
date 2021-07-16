from typing import Generator, List
from .layer import Layer
from hashlib import md5


def _divide_to_layers(code: list[str], count: int, chunk_count: int):
    for i in range(0, count, chunk_count):
        yield code[i:i + chunk_count]

class Code:
    layers: list[Layer] = []
    layer_count = 0  # Acts also as a z-index for layer during parsing.
    hash: str

    def __init__(self, encoded: str):
        sections, c = self._split_to_sections(encoded)
        # Banner layer must have atleast 10 sections.
        if c % 10 != 0:
            raise ValueError('Invalid banner code.')
        layers = _divide_to_layers(sections, c, Layer.SECT_COUNT)
        self._parse_layers(layers)
        self._hash_banner_code(encoded)

    def bg_layer(self) -> Layer:
        return self.layers[0]

    def fg_layers(self) -> list[Layer]:
        return self.layers[1:]

    def _divide_to_layers(self, code: list[str], count: int, chunk_size: int):
        for i in range(0, count, chunk_size):
            yield code[i:i + chunk_size]

    def _hash_banner_code(self, encoded: str):
        self.hash = md5(encoded.encode('utf-8')).hexdigest()

    def _parse_layers(self, layers: Generator[List[str], None, None]):
        self._create_layer(next(layers), is_bg=True)
        for layer in layers:
            try:
                self._create_layer(layer)
            except:
                raise ValueError(
                    f'Parse error occured on layer {self.layer_count}.')

    def _split_to_sections(self, encoded: str):
        sections = encoded.split('.')
        count = len(sections)
        return sections, count

    def _create_layer(self, layer, is_bg=False):
        self.layers.append(Layer(layer, self.layer_count, is_bg))
        self.layer_count += 1
