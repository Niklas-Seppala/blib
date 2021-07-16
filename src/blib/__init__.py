from .banner import Banner
from .utils import Files
from .index import index



def blib_init(out='', src=''):
    if out:
        Files.set_out_path(out)
    if src:
        Files.set_in_path(src)
    index.load()