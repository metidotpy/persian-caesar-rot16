import argparse
import os
from termcolor2 import colored
from string import Template
from algorithm import Encrypt, Decrypt

encrypt = Encrypt()
decrypt = Decrypt()

parser = argparse.ArgumentParser(
    prog='caesar',
    usage='%(prog)s [options]',
    description="Caesar is a command line app for your encrypt and decrypt persian words",
    epilog=colored("writed by metidotpy", 'yellow'),
)

parser.add_argument(
    '--encrypt',
    '-e',
    '-E',
    action='store_true',
    help="encrypt your text.",
)

parser.add_argument(
    '--decrypt',
    '-d',
    '-D',
    action='store_true',
    help="decrypt your text.",
)

parser.add_argument(
    '--caesar',
    '-c',
    '-C',
    action='store_true',
    help="caesar mode.",
)

parser.add_argument(
    '--rot16',
    '-r16',
    '-R16',
    action='store_true',
    help="rot16 mode.",
)

parser.add_argument(
    '--text',
    '-t',
    '-T',
    type=str,
    help="enter your text here.",
)

parser.add_argument(
    '--file',
    '-f',
    '-F',
    type=str,
    help="enter your file name here."
)

arguments = parser.parse_args()

if arguments.encrypt and arguments.caesar and arguments.text:
    try:
        text = arguments.text
        encrypted_text = encrypt.caesar(text)
        with open('caesar.txt', 'a+') as file:
            file.write(Template("متن اصلی شما: $text\nمتن رمز شده ی شما: $encrypt\n---------------------\n").substitute(text=text, encrypt=encrypted_text))
        print(colored(encrypted_text, 'yellow'))
    except Exception as err:
            print(colored(err, 'red'))

elif arguments.encrypt and arguments.caesar and arguments.file:
    file = arguments.file
    if file.endswith(".txt"):
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_encrypt:
                    text = file_encrypt.read()
                    encrypted_text = encrypt.caesar(text)
                with open('caesar.txt', 'a+') as file_write:
                    file_write.write(Template("متن اصلی شما: $text\nمتن رمز شده ی شما: $encrypt\n---------------------\n").substitute(text=text, encrypt=encrypted_text))
                print(colored(encrypted_text, 'yellow'))
                print(colored('saved on caesar.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))
            
    else:
        file = f"{file}.txt"
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_encrypt:
                    text = file_encrypt.read()
                    encrypted_text = encrypt.caesar(text)
                with open('caesar.txt', 'a+') as file_write:
                    file_write.write(Template("متن اصلی شما: $text\nمتن رمز شده ی شما: $encrypt\n---------------------\n").substitute(text=text, encrypt=encrypted_text))
                print(colored(encrypted_text, 'yellow'))
                print(colored('saved on caesar.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))
elif arguments.encrypt and arguments.rot16 and arguments.text:
    try:
        text = arguments.text
        encrypted_text = encrypt.rot16(text)
        with open('rot16.txt', 'a+') as file:
            file.write(Template("متن اصلی شما: $text\nمتن رمز شده ی شما: $encrypt\n---------------------\n").substitute(text=text, encrypt=encrypted_text))
        print(colored(encrypted_text, 'yellow'))
    except Exception as err:
            print(colored(err, 'red'))
elif arguments.encrypt and arguments.rot16 and arguments.file:
    file = arguments.file
    if file.endswith(".txt"):
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_encrypt:
                    text = file_encrypt.read()
                    encrypted_text = encrypt.rot16(text)
                with open('rot16.txt', 'a+') as file_write:
                    file_write.write(Template("متن اصلی شما: $text\nمتن رمز شده ی شما: $encrypt\n---------------------\n").substitute(text=text, encrypt=encrypted_text))
                print(colored(encrypted_text, 'yellow'))
                print(colored('saved on rot16.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))
            
    else:
        file = f"{file}.txt"
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_encrypt:
                    text = file_encrypt.read()
                    encrypted_text = encrypt.rot16(text)
                with open('rot16.txt', 'a+') as file_write:
                    file_write.write(Template("متن اصلی شما: $text\nمتن رمز شده ی شما: $encrypt\n---------------------\n").substitute(text=text, encrypt=encrypted_text))
                print(colored(encrypted_text, 'yellow'))
                print(colored('saved on rot16.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))
elif arguments.decrypt and arguments.caesar and arguments.text:
    try:
        text = arguments.text
        decrypted_text = decrypt.caesar(text)
        with open('caesar.txt', 'a+') as file:
            file.write(Template("متن رمز شده ی شما: $text\nمتن اصلی شما: $decrypt\n---------------------\n").substitute(text=text, decrypt=decrypted_text))
        print(colored(decrypted_text, 'yellow'))
    except Exception as err:
        print(colored(err, 'red'))
elif arguments.decrypt and arguments.caesar and arguments.file:
    file = arguments.file
    if file.endswith(".txt"):
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_decrypt:
                    text = file_decrypt.read()
                    decrypted_text = decrypt.caesar(text)
                with open('caesar.txt', 'a+') as file_write:
                    file_write.write(Template("متن رمز شده ی شما: $text\nمتن اصلی شما: $decrypt\n---------------------\n").substitute(text=text, decrypt=decrypted_text))
                print(colored(decrypted_text, 'yellow'))
                print(colored('saved on caesar.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))
            
    else:
        file = f"{file}.txt"
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_decrypt:
                    text = file_decrypt.read()
                    decrypted_text = decrypt.caesar(text)
                with open('caesar.txt', 'a+') as file_write:
                    file_write.write(Template("متن رمز شده ی شما: $text\nمتن اصلی شما: $decrypt\n---------------------\n").substitute(text=text, decrypt=decrypted_text))
                print(colored(decrypted_text, 'yellow'))
                print(colored('saved on caesar.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))    
elif arguments.decrypt and arguments.rot16 and arguments.text:
    try:
        text = arguments.text
        decrypted_text = decrypt.rot16(text)
        with open('rot16.txt', 'a+') as file:
            file.write(Template("متن رمز شده ی شما: $text\nمتن اصلی شما: $decrypt\n---------------------\n").substitute(text=text, decrypt=decrypted_text))
        print(colored(decrypted_text, 'yellow'))
    except Exception as err:
        print(colored(err, 'red'))
elif arguments.decrypt and arguments.rot16 and arguments.file:
    file = arguments.file
    if file.endswith(".txt"):
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_decrypt:
                    text = file_decrypt.read()
                    decrypted_text = decrypt.rot16(text)
                with open('rot16.txt', 'a+') as file_write:
                    file_write.write(Template("متن رمز شده ی شما: $text\nمتن اصلی شما: $decrypt\n---------------------\n").substitute(text=text, decrypt=decrypted_text))
                print(colored(decrypted_text, 'yellow'))
                print(colored('saved on rot16.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))
            
    else:
        file = f"{file}.txt"
        try:
            if os.path.isfile(file):
                with open(file, 'r') as file_decrypt:
                    text = file_decrypt.read()
                    decrypted_text = decrypt.rot16(text)
                with open('rot16.txt', 'a+') as file_write:
                    file_write.write(Template("متن رمز شده ی شما: $text\nمتن اصلی شما: $decrypt\n---------------------\n").substitute(text=text, decrypt=decrypted_text))
                print(colored(decrypted_text, 'yellow'))
                print(colored('saved on rot16.txt file', 'blue'))
            else:
                print(colored("File Not Found", 'red'))
                exit()
        except Exception as err:
            print(colored(err, 'red'))
