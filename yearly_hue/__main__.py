"""CLI for Yearly Hue."""
from argparse import ArgumentParser

from . import get_hue


def main() -> None:
    """Run the main function."""
    ap = ArgumentParser()
    ap.add_argument("--format", default="{hex}")
    ap.add_argument("brightness", nargs='?', type=float, default=1)
    ap.add_argument("saturation", nargs='?', type=float, default=1)
    args = ap.parse_args()

    print(get_hue(args.brightness, args.saturation, format=args.format))


if __name__ == '__main__':
    main()
