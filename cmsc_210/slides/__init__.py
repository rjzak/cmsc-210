import logging

from .build import copy_static_files, reset_build_dir
from .template import build_index

logger = logging.getLogger("cmsc-210")


def build(location: str = "build"):
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")
    reset_build_dir(location)
    logger.info("Copying static files...")
    copy_static_files(location)
    logger.info("Rendering templates...")
    build_index(location)


if __name__ == "__main__":
    build()
