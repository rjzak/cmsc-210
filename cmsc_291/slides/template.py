from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

from .build import build_directory

def template_dir_path() -> str:
    return str(Path(__file__).parent / "templates")


env = Environment(
    loader=FileSystemLoader(template_dir_path()),
    autoescape=select_autoescape(['html', 'xml'])
)


SOURCES = ("index.html", "calendar.html", "lecture_01.html", "lecture_02.html", "lecture_03.html", "lecture_04.html", "lecture_05.html", "lecture_06.html")

def build_index(location: str = "build") -> None:
    for source in SOURCES:
        template = env.get_template(source)
        with build_directory(location) as build_dir:
            with open(build_dir / source, "w") as fh:
                html = template.render()
                fh.write(html)


