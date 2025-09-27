import simpleaudio as sa

class AudioPlayer:
    @staticmethod
    def play_audio(file_path):
        wave_obj = sa.WaveObject.from_wave_file(file_path)
