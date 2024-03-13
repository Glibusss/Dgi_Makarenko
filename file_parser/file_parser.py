from wav_class import WavFile
import os

def read_binary_file(file_path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, file_path)
    try:
        with open(filename, "rb") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return None


