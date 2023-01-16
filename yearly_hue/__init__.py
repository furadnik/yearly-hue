"""Get hue."""
from datetime import datetime
import colorsys


def _i_to_h(i: float) -> str:
    h = hex(int(i * 255))
    h = "00" + h[2:]
    return h[-2:]


def get_hue(brightness: float = 1.0) -> str:
    """Return a hex representation of a hue."""
    t = datetime.today()
    hue = (int(t.strftime("%j")) - 1 + (t.hour + (t.minute + t.second / 60) / 60) / 24) / 365
    hue = (6 - hue + 0.6)
    while hue > 1:
        hue -= 1
    r, g, b = colorsys.hsv_to_rgb(hue, 1, brightness)
    return "#" + _i_to_h(r) + _i_to_h(g) + _i_to_h(b)
