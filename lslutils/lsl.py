from .resolve import resolve
from .utils import *
import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	subparser = parser.add_subparsers(dest='arg_type')

	resolve_parser = subparser.add_parser('resolve')
	resolve_parser.add_argument('--timeout', dest='timeout', type=float, default=0.05)
	resolve_parser.add_argument('--all', '-a', dest='all', action='store_true')
	resolve_parser.add_argument('--list', '-l', dest='list', action='store_true')
	for field in STREAM_INFO_FIELDS:
		resolve_parser.add_argument(f'--{field}', dest=field, action='store_true', help=f"Display stream {field}")
	resolve_parser.set_defaults(func=resolve)

	args = parser.parse_args()
	if args.arg_type is None:
		print(parser.print_help())

	else: 
		args.func(args)


if __name__ == "__main__": 
	main(sys.argv)	