from pathlib import Path

import markdown


class MarkdownToHtml:
    def __init__(self, input_path: Path, output_path: Path) -> None:
        self.input_path = input_path
        self.output_path = output_path

        if not self.input_path.exists():
            return print("input file do not exist")

        self.output_path.parent.mkdir(exist_ok=True, parents=True)

    def run(self):
        with open(self.input_path, "r", encoding="utf-8") as input_file:
            markdown_text = input_file.read()

        html = markdown.markdown(markdown_text)

        with open(self.output_path, "w") as output_file:
            output_file.write(html)
