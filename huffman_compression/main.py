import random
from huffman_encoder import HuffmanEncoder
from huffman_decoder import HuffmanDecoder

input_text = []
for i in range(100, 120):
    count_char  = random.randint(400000, 550000)
    input_text.append(chr(i)*count_char)
input_text = "".join(input_text)
input_text = ''.join(random.sample(input_text,len(input_text)))

encoder = HuffmanEncoder(input_text)

# Calls encoder
encoder.encode()
encode_input_text = encoder.get_encoded_bytes()
decode_map = encoder.get_decode_key_map()

# Calls decoder
obj = HuffmanDecoder(encoder.get_encoded_bytes())
output_text = obj.decode()

# Compression ratio
print("compression ratio:::", len(encode_input_text)/len(input_text))