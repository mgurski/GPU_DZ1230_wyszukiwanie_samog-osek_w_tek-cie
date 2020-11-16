import hurry.filesize
import string
import random
from faker import Faker



def generate_text(length: int):
    letters = string.ascii_letters + string.whitespace.replace('\x0b\x0c','')
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def faker_text(size_mb: int):
    fake = Faker()

    #pełne
    #text = fake.text(max_nb_chars = (1024 **2) * size_mb)

    #szybkie (mnożenie 1mb)
    text = fake.text(max_nb_chars = (1024 **2)) * size_mb 
    return text



def load_text_from_file(path: str):
    """Loads a textfile from the given path and returns it"""
    str = open(path, 'r').read()
    return str

def save_text_to_file(text: str, path: str):
    file = open(path, "w")
    file.write(text)
    file.close

def utf8len(s):
    return len(s.encode('utf-8'))

def get_file_size(text):
    """Returns file size in MB"""
    return hurry.filesize.size(utf8len(text))
