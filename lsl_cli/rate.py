import pylsl
import numpy as np
import time
from .utils import suppress_stdout_stderr

MAX_BUFFER_SIZE = 100_000

def rate(args): 
    name = args.name
    if args.count != -1:
        count = max(args.count, 5)
    else:
        count = -1

    with suppress_stdout_stderr():
        infos = pylsl.resolve_byprop("name", name, timeout=args.timeout)
    
    if len(infos) == 0:
        print("Cannot find outlet.")
        return 0

    info = infos[0]
    rate = info.nominal_srate()

    print(f'Announced rate for stream "{name}": {rate if rate > 0 else "IRREGULAR_RATE"}')

    # inlet = silent_output(
    with suppress_stdout_stderr():
        inlet = pylsl.StreamInlet(info)


    tstamp_ivals = []
    time_ivals = []
    last_tstamp = None
    last_tnow = None
    # i = 0


    while len(tstamp_ivals) < count or count == -1:
        try:
            res = inlet.pull_sample(0)
            if res[0] is None:
                continue
            else: 
                tnow = time.perf_counter()
                tstamp = res[1]
                if last_tstamp is None: 
                    last_tstamp = tstamp
                    last_tnow = tnow
                else: 
                    tstamp_ivals.append(tstamp - last_tstamp)
                    last_tstamp = tstamp

                    time_ivals.append(tnow - last_tnow)
                    last_tnow = tnow

                    if len(tstamp_ivals) > MAX_BUFFER_SIZE:
                        tstamp_ivals = tstamp_ivals[-MAX_BUFFER_SIZE:]
                    if len(tstamp_ivals) > MAX_BUFFER_SIZE:
                        time_ivals = time_ivals[-MAX_BUFFER_SIZE:]

                    if count == -1:
                        arrival_rate = 1./np.mean(time_ivals)
                        tstamp_rate = 1. / np.mean(tstamp_ivals)
                        print(f"Timestamp rate:  {tstamp_rate:.3f}Hz - Arrival rate: {arrival_rate:.3f}Hz", end="\r")

        except KeyboardInterrupt:
            break

    arrival_rate = 1./np.mean(time_ivals)
    tstamp_rate = 1. / np.mean(tstamp_ivals)
    print(f"Timestamp rate:  {tstamp_rate:.3f}Hz - Arrival rate: {arrival_rate:.3f}Hz")