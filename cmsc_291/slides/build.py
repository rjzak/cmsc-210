from contextlib import contextmanager
from pathlib import Path
from shutil import copytree, rmtree

def reset_build_dir():
    rmtree(str(Path(__file__).parent.parent.parent / "build"))


@contextmanager
def build_directory():
    build_dir = Path(__file__).parent.parent.parent / "build"
    if not build_dir.exists():
        build_dir.mkdir(parents=True)
    yield build_dir

def static_dir_path() -> str:
    return str(Path(__file__).parent / "static_files")

def images_dir_path() -> str:
    return str(Path(__file__).parent / "images")

def copy_static_files() -> None:   
    with build_directory() as build_dir:
        pairs = ((static_dir_path(), str(build_dir / "dist")), 
                 (images_dir_path(), str(build_dir / "images")))
        for src, dest in pairs:
            copytree(src, dest)

