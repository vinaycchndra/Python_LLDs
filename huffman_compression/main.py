import random
from file_handler import FileHandler

input_file_path = "./sample.txt"
filhandler = FileHandler(compress = True, input_file_path=input_file_path)
filhandler.process()

output_file_path = "./sample_compressed.bin"

filhandler = FileHandler(compress = False, input_file_path=output_file_path)
filhandler.process()