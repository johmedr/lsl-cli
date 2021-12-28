from .utils import *
from .list import list
from .echo import echo
from .show import show
from .find import find
import argparse
import sys

def main():
	parser = argparse.ArgumentParser()

	subparser = parser.add_subparsers(dest='command')

	list_parser = subparser.add_parser('list')
	list_parser.add_argument('--all', '-a', dest='all', action='store_true')
	list_parser.add_argument('--list', '-l', dest='list', action='store_true')
	list_parser.add_argument('--timeout', dest='timeout', type=float, default=0.05)

	for field in STREAM_INFO_FIELDS:
		list_parser.add_argument(f'--{field}', dest=field, action='store_true', help=f"Display stream {field}")
	
	list_parser.set_defaults(func=list)

	echo_parser = subparser.add_parser('echo', description="Print to screen messages from a stream.")
	echo_parser.add_argument('name', help='Stream name')
	echo_parser.add_argument('--timeout', dest='timeout', type=float, default=0.05)

	echo_parser.set_defaults(func=echo)

	show_parser = subparser.add_parser('show')
	show_parser.add_argument('name', help='Stream name')
	show_parser.add_argument('--timeout', dest='timeout', type=float, default=0.05)

	show_parser.set_defaults(func=show)

	find_parser = subparser.add_parser('find')
	for field in STREAM_INFO_FIELDS:
		find_parser.add_argument(f'--{field}', dest=field, type=str, help=f"Display stream {field}")
	find_parser.add_argument('--timeout', dest='timeout', type=float, default=0.05)
	find_parser.set_defaults(func=find)

	args = parser.parse_args()
	if args.command is None:
		parser.print_help()
	else: 
		res = args.func(args)
		if res is False:
			parser.print_help()

if __name__ == "__main__": 
	main(sys.argv)	