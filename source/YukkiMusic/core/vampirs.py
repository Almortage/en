"""
By vambir
"""

n = "\n\n"
w = " "

bold = lambda x: f"**{x}:** "
bold_ul = lambda x: f"**--{x}:**-- "

mono = lambda x: f"`{x}`{n}"


def vampir(
        title: str,
        vambir: dict,
        indent: int = 2,
        underline: bool = False,
) -> str:
    text = (bold_ul(title) + n) if underline else bold(title) + n

    for key, value in vambir.items():
        text += (
                indent * w
                + bold(key)
                + ((value[0] + n) if isinstance(value, list) else mono(value))
        )
    return text
