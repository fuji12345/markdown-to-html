import argparse
from pathlib import Path

import command


def main(args):
    if hasattr(command, args.command):
        command_name = getattr(command, args.command)(args.input_path, args.output_path)
        command_name.run()
    else:
        return print("Command not found")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--command", default="MarkdownToHtml", type=str)
    parser.add_argument("--input-path", default=Path("input/sample_input.md"), type=Path)
    parser.add_argument("--output-path", default=Path("output/sample_output.html"), type=Path)
    args = parser.parse_args()

    main(args)
