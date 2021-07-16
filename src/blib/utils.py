class RGBA:
    def __init__(self, r=0, g=0, b=0, a=255) -> None:
        self.r, self.g, self.b, self.a = r, g, b, a

    def compare(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b and self.a == other.a

    def unpack(self):
        return self.r, self.g, self.b, self.a

    @classmethod
    def from_hex(cls, hex: str):
        return cls(int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16))


class Vec3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z