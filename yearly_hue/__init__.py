"""Get hue."""
from datetime import datetime

from .color import Color
from .contrast import ContrastStandard, get_min_contrast_to_white

__version__ = '1.3.2'


def _f_to_h(i: float) -> str:
    h = hex(int(i * 255))
    h = "00" + h[2:]
    return h[-2:]


def _f_to_i(f: float) -> int:
    return int(f * 255)


def get_hue_from_dt() -> float:
    """Get hue based on the current datetime."""
    t = datetime.today()
    hue = (int(t.strftime("%j")) - 1 + (t.hour + (t.minute + t.second / 60) / 60) / 24) / 365
    hue = (6 - hue + 0.6)
    while hue > 1:
        hue -= 1
    return hue


def get_hue(brightness: float = 1.0, saturation: float = 1.0, format: str = "{hex}",
            min_contrast: ContrastStandard = ContrastStandard.NONE) -> str:
    """Return a hex representation of a hue."""
    hue = get_hue_from_dt()
    c = Color(hue, saturation, brightness)
    c = get_min_contrast_to_white(c, min_contrast)

    r, g, b = c.rgb
    hex = c.hex
    return format.format(r=r, g=g, b=b, hex=hex)


if __name__ == "__main__":
    print(get_hue())
