
class WavFile:
    def make_header(self):
        self.riff_chunk_id = self.header[0:4].decode("utf-8")
        self.riff_chunk_size = int.from_bytes(self.header[4:8], byteorder="little")
        self.wave_format = self.header[8:12].decode("utf-8")
        self.fmt_chunk_id = self.header[12:16].decode("utf-8")
        self.fmt_chunk_size = int.from_bytes(self.header[16:20], byteorder="little")
        self.audio_format = int.from_bytes(self.header[20:22], byteorder="little")
        self.num_channels = int.from_bytes(self.header[22:24], byteorder="little")
        self.sample_rate = int.from_bytes(self.header[24:28], byteorder="little")
        self.byte_rate = int.from_bytes(self.header[28:32], byteorder="little")
        self.block_align = int.from_bytes(self.header[32:34], byteorder="little")
        self.bits_per_sample = int.from_bytes(self.header[34:36], byteorder="little")
        self.data_chunk_id = self.header[36:40].decode("utf-8")
        self.data_chunk_size = int.from_bytes(self.header[40:44], byteorder="little")

    def __init__(self, file_data):
        self.header = file_data[:44]
        self.make_header()
        self.payload = file_data[44:]

    def print_header(self):
        header_str = self.header.decode('utf-8')
        print("Header:", header_str)
