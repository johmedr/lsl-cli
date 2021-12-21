import pylsl


def show(args):
	stream_name = args.name

	infos = pylsl.resolve_streams(args.timeout)
	names = [i.name() for i in infos]

	if stream_name not in names: 
		print('Stream not found.')
		return

	stream_info = infos[names.index(stream_name)]

	print(stream_info.as_xml())
