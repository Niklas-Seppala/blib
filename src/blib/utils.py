from os import path, getcwd
from pathlib import Path


class RGBA:
    def __init__(self, r=0, g=0, b=0, a=255) -> None:
        self.r, self.g, self.b, self.a = r, g, b, a

    def equals(self, other) -> bool:
        """Executes comparison bwtween self and other RGBA object.

        Args:
            other (RGBA): Target of the comparison.
        Returns:
            bool: True if other equals this.
        """
        return self.r == other.r and self.g == other.g and self.b == other.b and self.a == other.a

    def unpack(self) -> tuple:
        """Unpacks the rgba values to tuple.

        Returns:
            tuple: RGBA values in order, as a tuple.
        """
        return self.r, self.g, self.b, self.a

    @classmethod
    def from_hex(cls, hex: str):
        """Creates a RGBA object from hexadecimal presentation.

        Args:
            hex (str): RGBA values in hexadecimal string.
        Returns:
            RGBA: new RGBA object.
        """
        return cls(int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16))


class Vec3:
    """Vector with X, Y and Z values."""

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

class Files:
    """Class to store the runtime data related to file operations."""
    in_path: str = None
    out_path: str = None
    index_path: str = None

    @classmethod
    def set_out_path(cls, path: str):
        """Set the output directory path for the application.
        If the directory does'n exist, it will get created.

        Args:
            path (str): Relative path to output directory.
        """
        cls.out_path = path
        Path(cls.out_path).mkdir(parents=True, exist_ok=True)

    @classmethod
    def set_in_path(cls, path: str):
        """Set the source image path for the application.

        Args:
            path (str): Relative path to dir containing
            the source images.
        """
        cls.in_path = path
        cls.index_path = f'{path}index.json'

    @staticmethod
    def map_id_to_path(id: int):
        """Get the absolute path to source image by it's id.

        Args:
            id (int): Source image id.
        Returns:
            str: Source image path for specified id.
        """
        return path.join(getcwd(), Files.in_path,
                         '{id}.png'.format(id=id))

    class Format:
        """Image file format enum."""
        JPEG = 1
        PNG = 2
        str_map = {
            1: 'JPEG',
            2: 'PNG'
        }

        @classmethod
        def str(cls, format: int) -> str:
            """Maps enum to string presentation.

            Args:
                format (int): Image file format enum.
            Raises:
                ValueError: On unknown integer value.
            Returns:
                str: String presentation of the supplied enum.
            """
            result: str = cls.str_map.get(format)
            if not result:
                raise ValueError('Unknown image format.')
            else:
                return result
