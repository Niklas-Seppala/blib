from os import path, getcwd
from pathlib import Path

class Files:
    in_path = '../img/'
    out_path = './out/'
    index_path = '../img/index.json'

    @classmethod
    def set_out_path(cls, path: str):
        cls.out_path = path
        Path(cls.out_path).mkdir(parents=True, exist_ok=True)

    @classmethod
    def set_in_path(cls, path: str):
        cls.in_path = path
        cls.index_path = path.join(cls.in_path, 'index.json')

    @staticmethod
    def get_img_path_by_id(id: int):
        return path.join(getcwd(), Files.in_path,
                        '{id}.png'.format(id=id))