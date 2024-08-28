"""Color dataclass."""
import colorsys
from dataclasses import dataclass


def _f_to_h(i: int) -> str:
    h = hex(i)
    h = "00" + h[2:]
    return h[-2:]


@dataclass
class Color:
    """Represent a color object."""

    hue: float
    saturation: float
    value: float

    @property
    def hex(self) -> str:
        """Return color as hex."""
        r, g, b = self.rgb
        return "#" + _f_to_h(r) + _f_to_h(g) + _f_to_h(b)

    @property
    def rgb(self) -> tuple[int, int, int]:
        """Return color as (R,G,B) integers in range 0-255."""
        r, g, b = colorsys.hsv_to_rgb(self.hue, self.saturation, self.value)
        return int(r * 255), int(g * 255), int(b * 255)
