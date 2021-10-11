import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of Cylinder')
parser.add_argument("-r", '--radius', type=int, metavar='', required=True, help='Radius of cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help="Height of a Cylinder")

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true',  help='print_verbose')
args = parser.parse_args()


def cyl_vol(radius, height):
    vol = math.pi * (radius**2) * height
    return vol


if __name__ == '__main__':
    # print(cyl_vol(2,4))
    volume = cyl_vol(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(f"Volume of cylinder with radius: {args.radius} and height: {args.height} is:{volume}")
    else:
        print(f"Volume is {volume}")
