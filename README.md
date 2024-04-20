# ДГИ Макаренко 

## Парсер .wav файла WavClass

Вход:
Относительный путь к файлу формата **.wav**

Вывод в консоль:
Dictionary в строковом представлении формата _Поле заголовка_:_Значение_

Для получения конкретного поля следует воспользоваться методом **get_header_value**

```
from wav_class import WavFile

w = WavFile('../assets/rickroll.wav')

value = w.get_header_value('riff_chunk_id')

print(value)
#Вывод в консоль: Riff
```

Возможные значения, передаваемые в **get_header_value**:
* riff_chunk_id
* riff_chunk_size
* wave_format
* fmt_chunk_id
* fmt_chunk_size
* audio_format
* num_channels
* sample_rate
* byte_rate
* block_align
* bits_per_sample
* data_chunk_id
* data_chunk_size

**split_to_chunks** разбивает на массив чанков

Параметры: max_time: float - размер одного чанка во времени. Значение по умолчанию 1 мс