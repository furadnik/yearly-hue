"""Get hue."""
import colorsys
from datetime import datetime

__version__ = '1.2.0'


def _f_to_h(i: float) -> str:
    h = hex(int(i * 255))
    h = "00" + h[2:]
    return h[-2:]


def _f_to_i(f: float) -> int:
    return int(f * 255)


def get_hue(brightness: float = 1.0, saturation: float = 1.0, format: str = "{hex}") -> str:
    """Return a hex representation of a hue."""
    t = datetime.today()
    hue = (int(t.strftime("%j")) - 1 + (t.hour + (t.minute + t.second / 60) / 60) / 24) / 365
    hue = (6 - hue + 0.6)
    while hue > 1:
        hue -= 1
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, brightness)
    hex = "#" + _f_to_h(r) + _f_to_h(g) + _f_to_h(b)
    return format.format(r=_f_to_i(r), g=_f_to_i(g), b=_f_to_i(b), hex=hex)


if __name__ == "__main__":
    print(get_hue())
