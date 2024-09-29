import random
from huffman_encoder import HuffmanEncoder

input_text = "a"*1000 +"b"*1500+"c"*1000+"d"*1300+"e"*1500+"f"*1450+"g"*4500+'q'*1000
input_text = ''.join(random.sample(input_text,len(input_text)))
print(input_text)
# freq_map = {"a": 5, "b": 5, "c": 12, "d": 13, "e": 16, "f": 45}
encoder = HuffmanEncoder(input_text)

# Calls encoder
encoder.encode()

encode_input_text = encoder.get_encoded_bytes()
decode_map = encoder.get_decode_key_map()

print(len(input_text))
print(len(encode_input_text))
print(len(encode_input_text)/len(input_text)*100)