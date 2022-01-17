from contextlib import contextmanager
from pathlib import Path
from shutil import copytree, rmtree


def reset_build_dir(location: str = "build"):
    build_dir = Path(__file__).parent.parent.parent / location
    for file in filter(lambda p: p.is_file(), build_dir.glob("*")):
        file.unlink()
    if build_dir.exists():
        rmtree(str(build_dir))


@contextmanager
def build_directory(location: str) -> Path:
    build_dir = Path(__file__).parent.parent.parent / location
    if not build_dir.exists():
        build_dir.mkdir(parents=True)
    yield build_dir


def same_contents(left: Path, right: Path) -> bool:
    if set(pth.name for pth in left.glob("*")) == set(pth.name for pth in right.glob("*")):
        return {p.name: p.stat().st_size for p in left.glob("*")} == {p.name: p.stat().st_size for p in right.glob("*")}
    return False


def static_dir_path() -> Path:
    return Path(__file__).parent / "static_files"


def images_dir_path() -> Path:
    return Path(__file__).parent / "images"


def copy_static_files(location: str = "build"):
    with build_directory(location) as build_dir:
        pairs = (
            (static_dir_path(), build_dir / "dist"),
            (images_dir_path(), build_dir / "images"),
        )
        for src, dest in pairs:
            if not same_contents(src, dest):
                print(f"Copying {src} to {dest}...")
                if dest.exists():
                    rmtree(dest)
                copytree(str(src), str(dest))
