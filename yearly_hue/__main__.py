"""CLI for Yearly Hue."""
from . import get_hue
from argparse import ArgumentParser


ap = ArgumentParser()
ap.add_argument("brightness", nargs='?', type=float, default=1)
ap.add_argument("saturation", nargs='?', type=float, default=1)
args = ap.parse_args()

print(get_hue(args.brightness, args.saturation))
