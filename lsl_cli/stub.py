import pylsl
import time
import numpy as np
import threading
import sys
import signal


def stub(args):
    name = args.name
    channel_count = args.channel_count
    rate = args.nominal_srate
    chunk_size = args.chunk_size

    info = pylsl.StreamInfo(name=name, channel_count=channel_count, nominal_srate=rate)
    outlet = pylsl.StreamOutlet(info)

    exit_event = threading.Event()


    def signal_handler(signum, frame):
        exit_event.set()

    def send_data(): 
        while not exit_event.is_set():
            data = np.random.randn(chunk_size, channel_count).tolist()
            outlet.push_chunk(data)
            if rate > 0:
                time.sleep(1./rate)
            elif rate == pylsl.IRREGULAR_RATE:
                time.sleep(np.random.uniform(0.1, 1))    

    signal.signal(signal.SIGINT, signal_handler)
    thread = threading.Thread(target=send_data)
    thread.start()
    thread.join()