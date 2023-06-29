import re
import sys
from pathlib import Path


def get_text(s: str) -> str:
    s = re.sub(r"%(.*?)\n", r"", s)

    s = re.sub(r"\\\\", r"", s)

    s = re.sub(r"\\url{(.*?)}", r"", s)

    s = re.sub(r"\\textit{(.*?)}", r"\1", s)

    s = re.sub(r"``", r'"', s)
    s = re.sub(r"''", r'"', s)

    s = re.sub(r"(in|by) \\cite{.*?}", r"", s)
    s = re.sub(r"\\cite{.*?}", r"", s)
    s = re.sub(r"\\citep{.*?}", r"", s)
    s = re.sub(r"\\citet{.*?}", r"John", s)

    s = re.sub(r"\\label{.*?}", r"", s)

    s = re.sub(r"\\textasciitilde", r"~", s)
    s = re.sub(r"~", r"", s)

    s = re.sub(r"\\footnote{(.*)}", r"\n\1", s)
    s = re.sub(r"\\autoref{.*?}", r"Fig 1", s)

    s = re.sub(r"\\section{(.*?)}", r"\1", s)
    s = re.sub(r"\\subsection{(.*?)}", r"\1", s)
    s = re.sub(r"\\subsubsection{(.*?)}", r"\1", s)
    s = re.sub(r"\\paragraph{(.*?)}", r"\1", s)

    s = re.sub(r"\\renewcommand.*?\n", r"", s)

    s = re.sub(r"(satisfies|satisfy) \$.*?\$", r"\1 the condition", s)
    s = re.sub(r": \$.*?\$", r"", s)
    s = re.sub(r", (i\.e\.|e\.g\.), \$.*?\$,?", r"", s)
    s = re.sub(r"\$.*?\$ (denotes|denote)", r"X \1", s)
    s = re.sub(r"(as|by|with|in|on) \$.*?\$", r"\1 X", s)
    s = re.sub(r"(is|are) \$.*?\$", r"\1 X", s)
    s = re.sub(r"(where|,|, and) \$.*?\$ (is|are)", r"\1 the variable X \2", s)
    s = re.sub(r"\$.*?\$", r"Y", s)

    s = re.sub(r":\n", r".", s)
    s = re.sub(r"\n[\s]*?(where)", r"\nX is Y, \1", s)
    s = re.sub(r"\n[\s]*?(since)", r"\nX is Y \1", s)

    s = re.sub(r"(\\begin{align\*?})([\s\S]*?)(\\end{align\*?})", r"", s)
    s = re.sub(r"(\\begin{align\*?})([\s\S]*?)(\\end{align\*?})", r"", s)

    s = re.sub(
        r"\\begin{(figure|table)[\*]?}([\s\S]*?)\\caption{(.*?)}([\s\S]*?)\\end{(figure|table)[\*]?}",
        r"\3",
        s,
    )
    s = re.sub(r"(\\begin{CJK}{.*?}{.*?})(.*?)(\\end{CJK})", r"\2", s)

    s = re.sub(r"(\\begin{.*?})", r"", s)
    s = re.sub(r"(\\end{.*?})", r"", s)

    s = re.sub(r"\\item", r"-", s)

    return s


def clean_texfile(input_file: Path, output_file: Path):
    with input_file.open(mode="r") as f:
        s: str = "\n".join(f.readlines())

        cleaned_s: str = get_text(s)

    with output_file.open(mode="w") as g:
        g.write(cleaned_s)


if __name__ == "__main__":
    args: list[str] = sys.argv[1:]

    if len(args) == 2:
        input_file: Path = Path(args[0])
        output_file: Path = Path(args[1])
    else:
        input_file: Path = Path("./input.tex")
        output_file: Path = Path("./output.txt")

    clean_texfile(input_file=input_file, output_file=output_file)
