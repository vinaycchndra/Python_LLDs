from heapq import heappop, heappush

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
            self.encode_map[node.key] = "".join(code)
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
        encode_string_text_arr = []
        for char in self.text:
            encode_string_text_arr.append(self.encode_map.get(char))
        self.encoded_text = "".join(encode_string_text_arr)

    def create_decode_map(self):
        # Creating a decoding map from encode map
        self.decode_map = {}
        for key, value in self.encode_map.items():
            self.decode_map[value] = key

    def get_encoded_text(self):
        return self.encoded_text
    
    def get_decode_key_map(self):
        return self.decode_map