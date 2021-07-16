from .utils import Vec3, RGBA
from .index import index

def _parse_bool(string: str) -> bool:
    if (string == '1'):
        return True
    elif string == '0':
        return False
    else:
        raise Exception('String boolean value is neither 1 or 0.')


class LayerColors:
    """Data structure to hold layer's colors.
    """
    main: RGBA
    accent: RGBA

    def __init__(self, main_id: int, accent_id: int, stroke_or_bg: bool) -> None:
        self.main = index.get_real_color(main_id)
        if stroke_or_bg:
            self.accent = index.get_real_color(accent_id)
        else:
            self.accent = RGBA(a=0)


class Layer:
    """Data structure to hold parsed layer data.
    """

    SECT_COUNT = 10

    def __init__(self, layer_str: list, z_index: int, is_bg=False) -> None:
        self.mesh_id: int = int(layer_str[0])
        self.size: Vec3 = Vec3(int(layer_str[3]), int(
            layer_str[4]), int(layer_str[9]))
        self.pos: Vec3 = Vec3(int(layer_str[5]), int(layer_str[6]), z_index)
        self.draw_stroke: bool = _parse_bool(layer_str[7])
        self.mirror: bool = _parse_bool(layer_str[8])
        self.colors: LayerColors = LayerColors(
            int(layer_str[1]), int(layer_str[2]), self.draw_stroke or is_bg)
        self.hash = (self.size.x * 0xf1f1f1f1) ^ (self.size.y ^ self.mesh_id)
