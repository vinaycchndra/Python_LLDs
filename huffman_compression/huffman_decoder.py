from collections import deque

class HuffmanDecoder:
    def __init__(self, encoded_bytes_arr):
        self.encode_ascii_array = deque([byte_ for byte_ in encoded_bytes_arr])
        self.decode_map = {}
        self.decoded_text_arr = []

    def decode(self):
        self.create_decode_map()
        self.restore_file_content()
        return "".join(self.decoded_text_arr)

    def create_decode_map(self):
        x1 = self.encode_ascii_array.popleft()
        x2 = self.encode_ascii_array.popleft()
        len_encode_map = int(format(x1, '08b')+format(x2, '08b'), 2)

        while len_encode_map>0:
            section_arr = [self.encode_ascii_array.popleft()]
            section_length = section_arr[0]
            len_encode_map -= section_length

            for _ in range(section_length-1):
                section_arr.append(self.encode_ascii_array.popleft())

            char, huffman_code = self.decode_map_keys_value_pair(section_arr)
            self.decode_map[huffman_code] = char

    def decode_map_keys_value_pair(self, ascii_arr: list):
        section_len = ascii_arr[0]
        
        # character to replace in place of the huffman code
        key = chr(ascii_arr[1])
        
        # padding into the huffman code for the key 
        padding_count = ascii_arr[2]
        
        # extracting the huffman code 
        huffman_code_arr = []
        
        for ascii_index in range(3, section_len):
            binary_string = format(ascii_arr[ascii_index], '08b')
            huffman_code_arr.append(binary_string)
        
        # Removing the padded extra character
        if padding_count>0:
            huffman_code_arr[-1] = huffman_code_arr[-1][:8-padding_count]
        
        huffman_code = "".join(huffman_code_arr)
        return key, huffman_code
        
    def restore_file_content(self):
        # How much padding is there in the encoded file content we need to check.
        padding_count = self.encode_ascii_array.pop()

        temp_arr = deque()
        temp_code = ""
        decoded_text = []
        
        # Removing the ascii , converting that to binary code and adding the huffman code to character
        # We are skipping the last byte as that may have padding  
        while self.encode_ascii_array.__len__() > 1:
            binary_string_arr = list(format(self.encode_ascii_array.popleft(), '08b'))
            temp_arr.extend(binary_string_arr)

            while temp_arr.__len__() > 0:
                temp_code += temp_arr.popleft()

                if temp_code in self.decode_map:
                    decoded_text.append(self.decode_map.get(temp_code))
                    temp_code = ""

        # Converting into bits the last byte
        temp_arr.extend(list(format(self.encode_ascii_array.popleft(), '08b')))

        # Removing the padded characters from it 
        while padding_count > 0:
            temp_arr.pop()

        # Collecting the final huffman code
        while temp_arr.__len__() > 0:
            temp_code += temp_arr.popleft()

        if len(temp_code) > 0:
            decoded_text.append(self.decode_map.get(temp_code))

        self.decoded_text_arr = decoded_text
            





