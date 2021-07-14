from blib.banner import Banner
from blib.files import Files
from blib.index import index


def init(out='', src=''):
    if out:
        Files.set_out_path(out)
    if src:
        Files.set_in_path(src)

    index.load()