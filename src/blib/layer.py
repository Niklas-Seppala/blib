from .vec3 import Vec3
from .rgba import RGBA
from .index import index

class Layer:
    def __init__(self, mesh_id, main_color_id,
                 accent_color_id, pos, size,
                 draw_stroke, mirror):
        self.mesh_id: int = mesh_id
        self.main_color_id: int = main_color_id
        self.accent_color_id: int = accent_color_id
        self.pos: Vec3 = pos
        self.size: Vec3 = size
        self.draw_stroke: bool = draw_stroke
        self.mirror: bool = mirror

    def get_layer_colors(self, is_bg: bool):
        main = index.get_real_color(self.main_color_id)
        accent = None
        if self.draw_stroke or is_bg:
            accent = index.get_real_color(self.accent_color_id)
        else:
            accent = RGBA(a=0)
        return main, accent
