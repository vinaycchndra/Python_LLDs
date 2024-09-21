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

        # Generates encoded text based on the key and frequency map
        self.encode_text()    
    
        # Generate decode key for the encoded text to decode it when required.
        self.create_decode_map()

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
        # We are trying to avoid first converting the input text to directly the strings of 0 and 1 which will cause more memory required compared 
        # to the actual size of the input string as length of huffman coded string of 0 and 1 will be more and will actully require more size.
        # So we mantain a buffer que which waits until the size of encoded string of 0 and 1 is less than 8 as soon as its length reaches >= 8
        # the que pops up the 8 bits string and  the corresponding 8 bit string is converted to the corresponding ascii character integer and saved 
        # saved into the byte array. Thus we are doing it in a chunk by chunk manner.

        # Total bytes required to save the encoded string
        total_bytes = self.get_max_encoded_bytes_required()
        
        # if total bytes are less than 1 in that case the left over encoded string is saved as strings only in non_encoded_text variable 
        if total_bytes>0:
            byte_array = bytearray(total_bytes)
            byte_index = 0

        # Buffer que to mantain the 0 and 1 string of the encoded text for conversion into the byte character.
        encode_que = deque()

        # Encoder loop iterates through the text and converts every character to corresponding huffman code and combinations of 
        # the huffman code is converted into the corresponding byte character.
         
        for char in self.text:
            encode_que.extend(self.encode_map.get(char))
            if encode_que.__len__()>=8:
                while len(encode_que)//8 > 0:
                    binary_string_arr = []
                    for _ in range(8):
                        binary_string_arr.append(encode_que.popleft())

                    # Converting 8 bit string to the corresponding integer value
                    byte_value = int("".join(binary_string_arr), 2)

                # Integer value is now assigned to the byte array
                byte_array[byte_index] = byte_value
                
                # incrementing the byte array index
                byte_index += 1

        # Assigning the byte array to the encoded text        
        self.encoded_text = byte_array

        # Collecting the left over string of 0 and 1 that could not make it to a byte
        if encode_que.__len__()>0:
            self.non_encoded_text = "".join(encode_que)

    def create_decode_map(self):
        # Creating a decoding map from encode map
        self.decode_map = {}
        for key, value in self.encode_map.items():
            self.decode_map["".join(value)] = key

    def get_encoded_text(self):
        return self.encoded_text
    
    def get_decode_key_map(self):
        return self.decode_map
    
    def get_max_encoded_bytes_required(self):
        # Getting the total characters in the encoded text if that were directly saved as strings of 0 and 1.
        total_size = 0
        for key in self.freq_map:
            total_size += self.freq_map.get(key, 0)*len(self.encode_map.get(key, ""))
        
        # Dividing the total count by 8 to get total bytes array allocation initially to directly encode the characters into the byte
        return  total_size//8
        
        