from .vec3 import Vec3
from .layer import Layer

class BannerParser:
    @staticmethod
    def parse_bool(string: str) -> bool:
        if (string == '1'):
            return True
        elif string == '0':
            return False
        else:
            raise Exception('String boolean value is neither 1 or 0.')

    @staticmethod
    def parse_layer(splitted: list, layers: list, iter_num) -> None:
        mesh_id = int(splitted.pop(0))
        main_color_id = int(splitted.pop(0))
        accent_color_id = int(splitted.pop(0))

        size = Vec3(int(splitted.pop(0)), int(splitted.pop(0)), 0)
        position = Vec3(int(splitted.pop(0)), int(splitted.pop(0)), iter_num)

        draw_stroke = BannerParser.parse_bool(splitted.pop(0))
        mirror = BannerParser.parse_bool(splitted.pop(0))

        rotation = int(splitted.pop(0))
        size.z = rotation

        result = Layer(mesh_id, main_color_id, accent_color_id,
                    position, size, draw_stroke, mirror)
        layers.append(result)

    @staticmethod
    def parse(encoded_banner: str) -> list:
        layers = []
        splitted: list[str] = encoded_banner.split('.')
        n = 0
        try:
            while splitted:
                BannerParser.parse_layer(splitted, layers, n)
                n += 1
        except Exception as e:
            print(f'Parse error on layer {n}', e)
            return []
        return layers
