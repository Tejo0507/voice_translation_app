import sounddevice as sd
import numpy as np

class MicListener:
    def __init__(self, sample_rate=16000, channels=1, chunk_duration_sec=1):
        self.sample_rate = sample_rate
        self.channels = channels
        self.chunk_size = int(sample_rate * chunk_duration_sec)

    def start_listening(self, callback):
        def audio_callback(indata, frames, time, status):
            audio_chunk = indata[:, 0].copy()
            callback(audio_chunk)

        with sd.InputStream(channels=self.channels,
                            

