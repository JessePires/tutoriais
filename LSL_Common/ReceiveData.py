"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream
from time import time


def main():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EOG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    start_t = time()
    count = 0

    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        # print(timestamp, sample)
        count += 1 

        if (time() - start_t) >= 1: 
            print(f'COUNT: {count}')
            start_t = time()
            count = 0

if __name__ == '__main__':
    main()
