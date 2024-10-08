from heapq import heappop, heappush
from collections import deque

class HuffmanEncoder: 
    class Node: 
        def __init__(self, frequency: int):
            self.left  = None
            self.right = None
            self.frequency = frequency
            self.key = None
        
        def __repr__(self) -> str:
            return str(self.frequency)

        def __lt__(self, next):
            return self.frequency<next.frequency
    
    def __init__(self, text: str):
        self.freq_map = {}
        self.text = text
        self.heap = []
        self.huffman_tree = None
        self.encode_map = {}
        self.encoded_text = None
        self.non_encoded_text = None
        self.decode_map = {}

    def encode(self): 
        # Count the frequency of the text 
        self.countFreq()

        # Creating the heap of the nodes
        self.createHeap()
               
        # Creating the huffman tree from the heap of nodes using greedy algorithm of choosing the lowest two frequencies
        self.createHuffmanTree()

        # Generating the code for the characters in the text and saving them in the encode_map
        self.recursively_encode(self.huffman_tree)

        # Generate decode key for the encoded text to decode it when required.
        self.create_decode_map()

        # Generates encoded text based on the key and frequency map
        self.encode_text()    
    
        

    def countFreq(self):
        for char in self.text:
            self.freq_map[char] = self.freq_map.get(char, 0)+1
        
    def createHeap(self):
        # Creating the heap of the nodes which will be later used to create the huffman tree. 
        for key, value in self.freq_map.items():
            node = self.Node(value)
            node.key = key
            heappush(self.heap, node)
    
    
    def createHuffmanTree(self):
        # Here in below we are merging the multiple nodes in every step 
        # by selecting two minimum nodes and creating new nodes with frequency being the sum 
        # of the two minumum frequency nodes popped from the heap.
        
        while len(self.heap)>1:
            node1 = heappop(self.heap)
            node2 = heappop(self.heap)

            # Creating the new node with the sum of two minimum frequencies.
            new_node = self.Node(node1.frequency+node2.frequency)
            new_node.left = node1
            new_node.right = node2

            # Pushing this new tree back into the heap
            heappush(self.heap, new_node)
        
        # Popping the single node to the huffman tree.
        self.huffman_tree = self.heap.pop()

    def recursively_encode(self, node, code = []):
        # Creating the code by traversing the huffman tree.
        if node.left is None and node.right is None:
            if len(code) == 0:
                code.append("0")
            self.encode_map[node.key] = code.copy()
            return 
        
        # Traversing left portion of the tree to generate the code value for the character in the text
        code.append("0")
        self.recursively_encode(node.left, code)
        code.pop()

        # Traversing right portion of the tree to generate the code value for the character in the text
        code.append("1")
        self.recursively_encode(node.right, code)
        code.pop()

    def encode_text(self):
        # First we are encoding the decode_map. later we encode the text and merge them to form a byte array
        self.encoded_text = bytes(self.encode_decode_map()+self.encode_content_text()) 

    def encode_content_text(self):
        # We are trying to avoid first converting the input text to directly the strings of 0 and 1 which will cause more memory required compared 
        # to the actual size of the input string as length of huffman coded string of 0 and 1 will be more and will actully require more size.
        # So we mantain a buffer que which waits until the size of encoded string of 0 and 1 is less than 8 as soon as its length reaches >= 8
        # the que pops up the 8 bits string and  the corresponding 8 bit string is converted to the corresponding ascii character integer and saved 
        # saved into the byte array. Thus we are doing it in a chunk by chunk manner.

        # Total bytes required to save the encoded string
        padding_count = self.get_padding_character_required()
        
        # initialising the byte array list
        byte_array = list()        

        # Buffer que to mantain the 0 and 1 string of the encoded text for conversion into the byte character.
        encode_que = deque()

        # Encoder loop iterates through the text and converts every character  
        for char in self.text:
            encode_que.extend(self.encode_map.get(char))
            while len(encode_que)//8 > 0:
                binary_string_arr = []
                for _ in range(8):
                    binary_string_arr.append(encode_que.popleft())

                # Converting 8 bit string to the corresponding integer value
                byte_value = int("".join(binary_string_arr), 2)

                # Integer value is now appended byte array
                byte_array.append(byte_value)
                
        # We are using the padding of '0' to complete the output to whole number bytes
        for _ in range(padding_count):
            encode_que.append('0')

        if len(encode_que)>0:
            byte_value = int("".join(encode_que), 2)
            byte_array.append(byte_value)
        
        # saving the padding count of bits of '0' to decode the encoded text
        byte_array.append(padding_count)

        # Assigning the byte array to the encoded text        
        return byte_array

    def create_decode_map(self):
        # Creating a decoding map from encode map
        self.decode_map = {}
        for key, value in self.encode_map.items():
            self.decode_map["".join(value)] = key

    # This function is encoding the decode map, the out put of this function will be appended at the begining 
    # of the encoded bin file which will be used by huffman decoder class to decompress the file content. 
    def encode_decode_map(self):
        if self.decode_map.__len__() == 0:
            return 
        
        que = deque()
        for huffman_code, char in self.decode_map.items():
            que.extend(self.encode_map_keys_value_pairs(char, huffman_code))
        header_length_string = format(len(que), '016b')

        # Now we are saving the total length of the decode map in 16 bit number 
        # as the maximum length of the decode map may get more than a number that can be
        # represented by 8 bit integer 

        # so after reading the first two bytes of the encoded binary one will be able to know how many
        # next bytes actually represent the encoding map which can be used to decompress the enoded file.
        que.appendleft(int(header_length_string[8:],2))
        que.appendleft(int(header_length_string[:8],2))
        
        return list(que)


    # This method is the sub function in encoding the decode_map which will be used as keys while decompressing the file and reconvering the original file 
    def encode_map_keys_value_pairs(self, decode_key: str, encoded_key: str):
        section_que = deque()
        decode_key = ord(decode_key)
        encoded_key = list(encoded_key)
        key_pad = key_pad = (8-len(encoded_key)%8)%8
        
        # The first character of the section que will the asccii 
        # value of the decode key for example in decode_map
        # {"a": "010110"}----> "a" is the decode key and the "010110" is the huffman code
        section_que.append(decode_key)
        
        # The second character is the padding count in the huffman code to make it multiple of the 8 
        # the padding count is useful while decoding the individual character key and corresponding huffamn code 
        section_que.append(key_pad)
        
        # padding the huffman code with the zeros 
        for _ in range(key_pad):
            encoded_key.append('0')

        # converting the huffman code with padding into combination of ascii values
        temp_arr = []
        for char in encoded_key:
            temp_arr.append(char)
            
            if len(temp_arr) == 8:
                section_que.append(int("".join(temp_arr), 2))
                temp_arr = []

        # To know overall section length of the key and value pair along with the padding count byte, key byte, huffman code(with padding) bytes 
        section_que.appendleft(len(section_que)+1)
        return list(section_que)

    def get_encoded_bytes(self):
        return self.encoded_text
    
    def get_decode_key_map(self):
        return self.decode_map
    
    def get_padding_character_required(self):
        # Getting the total characters in the encoded text if that were directly saved as strings of 0 and 1.
        # This is required to preallocate the bytes array so that dynamic memory allocation for the bytes_array 
        # can be avoided.
        total_size = 0
        for key in self.freq_map:
            total_size += self.freq_map.get(key, 0)*len(self.encode_map.get(key, ""))
        
        # Dividing the total count by 8 to get total bytes array allocation initially to directly encode the characters into the byte
        padding_count = (8-total_size%8)%8
        return  padding_count
    