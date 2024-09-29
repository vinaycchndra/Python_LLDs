import random
from huffman_encoder import HuffmanEncoder
from huffman_decoder import HuffmanDecoder

input_text = "a"*110 +"b"*105+"c"*102+"d"*113+"e"*150+"f"*114+"g"*49+'q'*105
input_text = ''.join(random.sample(input_text,len(input_text)))
print(input_text)
# freq_map = {"a": 5, "b": 5, "c": 12, "d": 13, "e": 16, "f": 45}
encoder = HuffmanEncoder(input_text)

# Calls encoder
encoder.encode()
print("encoder_decoded_map", encoder.decode_map)
encode_input_text = encoder.get_encoded_bytes()
decode_map = encoder.get_decode_key_map()

print(len(input_text))
print(len(encode_input_text))
obj = HuffmanDecoder(encoder.get_encoded_bytes())
print(obj.decode())