import logging

from .build import copy_static_files, reset_build_dir
from .template import build_index

logger = logging.getLogger("cmsc_291")

def build():
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")
    reset_build_dir()
    logger.info("Copying static files...") 
    copy_static_files()
    logger.info("Rendering templates...") 
    build_index()


if __name__ == "__main__":
    build()