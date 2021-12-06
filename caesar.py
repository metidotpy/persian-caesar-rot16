import os
from algorithm import Encrypt, Decrypt
from termcolor2 import colored
from pyfiglet import figlet_format
from string import Template

print(figlet_format("WELCOME TO PERSIAN CAESAR ENCRYPT AND DECRYPT"))

file_or_text = input(colored("file or text? ", "yellow")).lower()
encrypt_or_decrypt = input(colored("encrypt or decrypt? ", "cyan")).lower()

encrypt = Encrypt()
decrypt = Decrypt()

if file_or_text == 'text' and encrypt_or_decrypt == 'encrypt':
    try:
        text = input(colored("Enter Your Text (Persian): ", "green"))
        encrypted_text = encrypt.caesar(text)
        with open('caesar.txt', 'a+') as file:
            file.write(Template("متن اصلی شما: $text\nمتن رمز شده ی شما: $encrypt\n---------------------\n").substitute(text=text, encrypt=encrypted_text))
        print(colored(encrypted_text, 'yellow'))
    except Exception as err:
            print(colored(err, 'red'))

elif file_or_text == 'text' and encrypt_or_decrypt == 'decrypt':
    try:
        text = input(colored("Enter Your Text (Persian): ", "green"))
        decrypted_text = decrypt.caesar(text)
        with open('caesar.txt', 'a+') as file:
            file.write(Template("متن رمز شده ی شما: $text\nمتن اصلی شما: $decrypt\n---------------------\n").substitute(text=text, decrypt=decrypted_text))
        print(colored(decrypted_text, 'yellow'))
    except Exception as err:
            print(colored(err, 'red'))

elif file_or_text == 'file' and encrypt_or_decrypt == 'encrypt':
    file = input(colored("Enter Your File Name (must be a txt file): ", 'cyan'))
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

elif file_or_text == 'file' and encrypt_or_decrypt == 'decrypt':
    file = input(colored("Enter Your File Name (must be a txt file): ", 'cyan'))
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
else:
    print(colored("Bad Argument!", 'red'))