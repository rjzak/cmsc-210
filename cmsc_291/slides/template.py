from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

from .build import build_directory

def template_dir_path() -> Path:
    return Path(__file__).parent / "templates"


env = Environment(
    loader=FileSystemLoader(str(template_dir_path())),
    autoescape=select_autoescape(['html', 'xml'])
)

def build_index(location: str = "build") -> None:
    with build_directory(location) as build_dir:
        for source in template_dir_path().iterdir():
            if source.suffix == ".html":
                template = env.get_template(source.name)
                with open(build_dir / source.name, "w") as fh:
                    html = template.render()
                    fh.write(html)


