"""Get the minimum color satisfying the contrast."""
from enum import Enum

from .color import Color


class ContrastStandard(Enum):
    """Contrast standard with minimum values for contrast."""

    AA = "AA"
    AAA = "AAA"
    NONE = "NONE"


WHITE_MIN_CONTRAST = {
    ContrastStandard.AA: 4.5,
    ContrastStandard.AAA: 7,
    ContrastStandard.NONE: 0,
}


RED_LUM = 0.2126
GREEN_LUM = 0.7152
BLUE_LUM = 0.0722


def get_luminance(color: Color):
    """Get the luminance of `color`."""
    ired, igreen, iblue = color.rgb

    red = ired / 255
    green = igreen / 255
    blue = iblue / 255

    red = red / 12.92 if red <= 0.04045 else ((red + 0.055) / 1.055) ** 2.4
    green = green / 12.92 if green <= 0.04045 else ((green + 0.055) / 1.055) ** 2.4
    blue = blue / 12.92 if blue <= 0.04045 else ((blue + 0.055) / 1.055) ** 2.4

    return red * RED_LUM + green * GREEN_LUM + blue * BLUE_LUM


def get_white_contrast(color: Color) -> float:
    """Get the contrast of `color` against white."""
    return 1 / (get_luminance(color))


def get_min_contrast_to_white(color: Color, contrast: ContrastStandard) -> Color:
    """Return color with maximum brightness, such that text contrast against white background is at least `contrast`."""
    if contrast == ContrastStandard.NONE:
        return color

    brightness = 0.5
    for i in range(2, 16):
        new_color = Color(color.hue, color.saturation, brightness)
        print(brightness, get_white_contrast(new_color), new_color)
        if get_white_contrast(new_color) >= WHITE_MIN_CONTRAST[contrast]:
            brightness += 2**(-i)
        else:
            brightness -= 2**(-i)

    return Color(color.hue, color.saturation, min(brightness, color.value))
