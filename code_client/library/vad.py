# -*- coding: utf-8 -*-
import webrtcvad
import collections
import sys
import pyaudio

from array import array
from struct import pack
from datetime import datetime
import wave
import time


class vad(object):
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.CHUNK_DURATION_MS = 30  # supports 10, 20 and 30 (ms)
        self.PADDING_DURATION_MS = 1500  # 1 sec jugement
        self.CHUNK_SIZE = int(self.RATE * self.CHUNK_DURATION_MS / 1000)  # chunk to read
        self.CHUNK_BYTES = self.CHUNK_SIZE * 2  # 16bit = 2 bytes, PCM
        self.NUM_PADDING_CHUNKS = int(self.PADDING_DURATION_MS / self.CHUNK_DURATION_MS)
        self.NUM_WINDOW_CHUNKS = int(400 / self.CHUNK_DURATION_MS)  # 400 ms/ 30ms  ge
        self.NUM_WINDOW_CHUNKS_END = self.NUM_WINDOW_CHUNKS * 2
        self.START_OFFSET = int(self.NUM_WINDOW_CHUNKS * self.CHUNK_DURATION_MS * 0.5 * self.RATE)

    def record_to_file(self, path, data, sample_width):
        "Records from the microphone and outputs the resulting data to 'path'"
        # sample_width, data = record()
        data = pack('<' + ('h' * len(data)), *data)
        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(self.RATE)
        wf.writeframes(data)
        wf.close()

    def normalize(self, snd_data):
        "Average the volume out"
        MAXIMUM = 32767  # 16384
        times = float(MAXIMUM) / max(abs(i) for i in snd_data)
        r = array('h')
        for i in snd_data:
            r.append(int(i * times))
        return r

    def Monitor(self):
        vad = webrtcvad.Vad(2)

        pa = pyaudio.PyAudio()
        stream = pa.open(format=self.FORMAT,
                         channels=self.CHANNELS,
                         rate=self.RATE,
                         input=True,
                         start=False,
                         frames_per_buffer=self.CHUNK_SIZE)

        got_a_sentence = False
        leave = False

        while not leave:
            ring_buffer = collections.deque(maxlen=self.NUM_PADDING_CHUNKS)
            triggered = False
            voiced_frames = []
            ring_buffer_flags = [0] * self.NUM_WINDOW_CHUNKS
            ring_buffer_index = 0

            ring_buffer_flags_end = [0] * self.NUM_WINDOW_CHUNKS_END
            ring_buffer_index_end = 0
            raw_data = array('h')
            index = 0
            start_point = 0
            StartTime = time.time()
            print("* recording: ")
            stream.start_stream()

            while not got_a_sentence and not leave:
                chunk = stream.read(self.CHUNK_SIZE, exception_on_overflow=False)
                raw_data.extend(array('h', chunk))
                index += self.CHUNK_SIZE
                active = vad.is_speech(chunk, self.RATE)

                # sys.stdout.write('1' if active else '_')
                ring_buffer_flags[ring_buffer_index] = 1 if active else 0
                ring_buffer_index += 1

                ring_buffer_index %= self.NUM_WINDOW_CHUNKS

                ring_buffer_flags_end[ring_buffer_index_end] = 1 if active else 0
                ring_buffer_index_end += 1
                ring_buffer_index_end %= self.NUM_WINDOW_CHUNKS_END

                # start point detection
                if not triggered:
                    ring_buffer.append(chunk)
                    num_voiced = sum(ring_buffer_flags)
                    if num_voiced > 0.8 * self.NUM_WINDOW_CHUNKS:
                        sys.stdout.write(' Open ')
                        StartTime = time.time()
                        triggered = True
                        start_point = index - self.CHUNK_SIZE * 20  # start point
                        # voiced_frames.extend(ring_buffer)
                        ring_buffer.clear()
                # end point detection
                else:
                    # voiced_frames.append(chunk)
                    ring_buffer.append(chunk)
                    num_unvoiced = self.NUM_WINDOW_CHUNKS_END - sum(ring_buffer_flags_end)
                    if num_unvoiced > 0.90 * self.NUM_WINDOW_CHUNKS_END or (time.time() - StartTime) > 10:
                        sys.stdout.write(' Close ')
                        triggered = False
                        got_a_sentence = True

                sys.stdout.flush()

            sys.stdout.write('\n')

            stream.stop_stream()
            print("* done recording")
            got_a_sentence = False

            # write to file
            raw_data.reverse()
            for index in range(start_point):
                raw_data.pop()
            raw_data.reverse()
            raw_data = self.normalize(raw_data)
            self.record_to_file("./data/record.wav", raw_data, 2)
            leave = True

    def Monitor_new(self):
        vad = webrtcvad.Vad(2)

        pa = pyaudio.PyAudio()
        stream = pa.open(format=self.FORMAT,
                         channels=self.CHANNELS,
                         rate=self.RATE,
                         input=True,
                         start=False,
                         frames_per_buffer=self.CHUNK_SIZE)

        got_a_sentence = False
        leave = False

        while not leave:
            ring_buffer = collections.deque(maxlen=self.NUM_PADDING_CHUNKS)
            triggered = False
            voiced_frames = []
            ring_buffer_flags = [0] * self.NUM_WINDOW_CHUNKS
            ring_buffer_index = 0

            ring_buffer_flags_end = [0] * self.NUM_WINDOW_CHUNKS_END
            ring_buffer_index_end = 0
            raw_data = array('h')
            index = 0
            start_point = 0
            StartTime = time.time()
            print("* recording: ")
            stream.start_stream()

            old_timestamp = time.time()
            old_datetime = datetime.utcfromtimestamp(old_timestamp)

            while not got_a_sentence and not leave:

                new_timestamp = time.time()
                new_datetime = datetime.utcfromtimestamp(new_timestamp)

                diffseconds = (new_datetime - old_datetime).total_seconds()

                if diffseconds > 15:
                    return True

                chunk = stream.read(self.CHUNK_SIZE, exception_on_overflow=False)
                raw_data.extend(array('h', chunk))
                index += self.CHUNK_SIZE
                active = vad.is_speech(chunk, self.RATE)

                # sys.stdout.write('1' if active else '_')
                ring_buffer_flags[ring_buffer_index] = 1 if active else 0
                ring_buffer_index += 1

                ring_buffer_index %= self.NUM_WINDOW_CHUNKS

                ring_buffer_flags_end[ring_buffer_index_end] = 1 if active else 0
                ring_buffer_index_end += 1
                ring_buffer_index_end %= self.NUM_WINDOW_CHUNKS_END

                # start point detection
                if not triggered:
                    ring_buffer.append(chunk)
                    num_voiced = sum(ring_buffer_flags)
                    if num_voiced > 0.8 * self.NUM_WINDOW_CHUNKS:
                        sys.stdout.write(' Open ')
                        StartTime = time.time()
                        triggered = True
                        start_point = index - self.CHUNK_SIZE * 20  # start point
                        # voiced_frames.extend(ring_buffer)
                        ring_buffer.clear()
                # end point detection
                else:
                    # voiced_frames.append(chunk)
                    ring_buffer.append(chunk)
                    num_unvoiced = self.NUM_WINDOW_CHUNKS_END - sum(ring_buffer_flags_end)
                    if num_unvoiced > 0.90 * self.NUM_WINDOW_CHUNKS_END or (time.time() - StartTime) > 10:
                        sys.stdout.write(' Close ')
                        triggered = False
                        got_a_sentence = True

                sys.stdout.flush()

            sys.stdout.write('\n')

            stream.stop_stream()
            print("* done recording")
            got_a_sentence = False

            # write to file
            raw_data.reverse()
            for index in range(start_point):
                raw_data.pop()
            raw_data.reverse()
            raw_data = self.normalize(raw_data)
            self.record_to_file("./data/record.wav", raw_data, 2)
            leave = True

        return False


if __name__ == "__main__":
    pass
