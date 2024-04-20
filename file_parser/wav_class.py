import os
import numpy as np

class WavFile:

    __header_values = {}

    def make_header(self):
        self.__header_values['riff_chunk_id'] = self.__file_data[0:4].decode("utf-8")
        self.__header_values['riff_chunk_size'] = int.from_bytes(self.__file_data[4:8], byteorder="little")
        self.__header_values['wave_format'] = self.__file_data[8:12].decode("utf-8")
        self.__header_values['fmt_chunk_id'] = self.__file_data[12:16].decode("utf-8")
        self.__header_values['fmt_chunk_size'] = int.from_bytes(self.__file_data[16:20], byteorder="little")
        self.__header_values['audio_format'] = int.from_bytes(self.__file_data[20:22], byteorder="little")
        self.__header_values['num_channels'] = int.from_bytes(self.__file_data[22:24], byteorder="little")
        self.__header_values['sample_rate'] = int.from_bytes(self.__file_data[24:28], byteorder="little")
        self.__header_values['byte_rate'] = int.from_bytes(self.__file_data[28:32], byteorder="little")
        self.__header_values['block_align'] = int.from_bytes(self.__file_data[32:34], byteorder="little")
        self.__header_values['bits_per_sample'] = int.from_bytes(self.__file_data[34:36], byteorder="little")
        self.__header_values['data_chunk_id'] = self.__file_data[36:40].decode("utf-8")
        self.__header_values['data_chunk_size'] = int.from_bytes(self.__file_data[40:44], byteorder="little")

    def __init__(self, file_path):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file_path)

        try:
            with open(filename, "rb") as file:
                self.__file_data = file.read()
        except FileNotFoundError:
            return None

        self.make_header()

    def __repr__(self):
        return str(self.__header_values)
    
    def get_header_value(self, key):

        try:
            result = self.__header_values[key]
        except KeyError:
            result = None

        return result

    def split_to_chunks(self, max_time=1e-3):
        
        sample_rate = self.get_header_value('sample_rate')

        if not sample_rate:
            return []
        
        chunk_size = int(max_time * sample_rate)
        bytes_array = bytearray(self.__file_data)
        chunks = [bytes_array[i:i+chunk_size] for i in range(0, len(bytes_array), chunk_size)]

        return chunks
        
    def get_payload(self):
        return self.__file_data[44:]
    
    def get_header(self):
        return self.__file_data[0:44]