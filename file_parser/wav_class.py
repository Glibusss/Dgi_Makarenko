import os
class WavFile:

    __header_values = {}

    def make_header(self):
        self.__header_values['riff_chunk_id'] = self.__header[0:4].decode("utf-8")
        self.__header_values['riff_chunk_size'] = int.from_bytes(self.__header[4:8], byteorder="little")
        self.__header_values['wave_format'] = self.__header[8:12].decode("utf-8")
        self.__header_values['fmt_chunk_id'] = self.__header[12:16].decode("utf-8")
        self.__header_values['fmt_chunk_size'] = int.from_bytes(self.__header[16:20], byteorder="little")
        self.__header_values['audio_format'] = int.from_bytes(self.__header[20:22], byteorder="little")
        self.__header_values['num_channels'] = int.from_bytes(self.__header[22:24], byteorder="little")
        self.__header_values['sample_rate'] = int.from_bytes(self.__header[24:28], byteorder="little")
        self.__header_values['byte_rate'] = int.from_bytes(self.__header[28:32], byteorder="little")
        self.__header_values['block_align'] = int.from_bytes(self.__header[32:34], byteorder="little")
        self.__header_values['bits_per_sample'] = int.from_bytes(self.__header[34:36], byteorder="little")
        self.__header_values['data_chunk_id'] = self.__header[36:40].decode("utf-8")
        self.__header_values['data_chunk_size'] = int.from_bytes(self.__header[40:44], byteorder="little")

    def __init__(self, file_path):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file_path)

        try:
            with open(filename, "rb") as file:
                file_data = file.read()
        except FileNotFoundError:
            return None
        
        self.__header = file_data[:44]
        self.__payload = file_data[44:]

        self.make_header()

    def __repr__(self):
        return str(self.__header_values)
    
    def get_header_value(self, key):
        return self.__header_values[key]
