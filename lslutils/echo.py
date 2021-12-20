import pylsl
import argparse


if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description="Print to screen messages from a stream.")
	parser.add_argument('name', help='Stream name')
	parser.add_argument('--timeout', dest='timeout', nargs=1, type=1)

	args = args.parse_args()

	pylsl.resolve_streams()
	