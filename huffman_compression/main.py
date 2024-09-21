import random
from huffman_encoder import HuffmanEncoder

input_text = "a"*5+"b"*5+"c"*12+"d"*13+"e"*16+"f"*45+"g"*45
input_text = ''.join(random.sample(input_text,len(input_text)))

# freq_map = {"a": 5, "b": 5, "c": 12, "d": 13, "e": 16, "f": 45}
encoder = HuffmanEncoder(input_text)

# Calls encoder
encoder.encode()

encode_input_text = encoder.get_encoded_text()
decode_map = encoder.get_decode_key_map()

print(encode_input_text)

word = ""
decoded_text_arr = []
for char in encode_input_text:
    word += char
    if word in decode_map:
        decoded_text_arr.append(decode_map.get(word))
        word = ""

decoded_text = "".join(decoded_text_arr)

print("Decoded text is over here:    ", decoded_text)
print("Input   text is over here:    ", input_text)


