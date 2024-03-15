from wav_class import WavFile

w = WavFile('../assets/rickroll.wav')

value = w.get_header_value('stuff')

print(w, value)