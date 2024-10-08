import os
from huffman_encoder import HuffmanEncoder
from huffman_decoder import HuffmanDecoder


class FileHandler:
    
    def __init__(self, compress : bool = False, input_file_path: str = None):
        self.compress = compress
        self.input_file_path = input_file_path

    def process(self):

        if self.input_file_path is None:
            raise Exception("No Valid Input File Path Is Provided.")
        
        file_directory = os.path.dirname(self.input_file_path)
        file_name = os.path.basename(self.input_file_path)
        file_name, file_extension =  os.path.splitext(file_name)
    
        if self.compress:
            if file_extension != ".txt":
                raise Exception("Only text files can be compressed, kindly change the file extension to .txt !!!!")
                    
            output_file_path  = os.path.join(file_directory, file_name+"_compressed.bin")
            
            with open(self.input_file_path, 'r') as input_file, open(output_file_path, 'wb') as output_file:
                input_text = input_file.read()
                encoder_obj = HuffmanEncoder(input_text)
                encoder_obj.encode()                       
                encoded_bytes = encoder_obj.get_encoded_bytes()
                output_file.write(encoded_bytes)
        else:
            if '_COMPRESSED' in file_name.upper():
                file_name  = file_name.split('_')[0]

            output_file_path  = os.path.join(file_directory, file_name+".txt")

            with open(self.input_file_path, 'rb') as input_file, open(output_file_path, 'w') as output_file:
                input_text = input_file.read()
                decoder_obj = HuffmanDecoder(input_text)
                decoded_text = decoder_obj.decode()                       
                output_file.write(decoded_text)