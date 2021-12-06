# persian caesar and rot16 encrypt and decrypt

## how to install
- if you use windows
    ```cmd
    python -m venv .venv
    .\.venv\Script\activate
    python -m pip install -r requirements.txt
    ```
- if you use linux
    ```bash
    sudo apt install virtualenv
    virtualenv -p py3 .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ```
- if you use macos
    ```bash
    sudo brew install virtualenv
    virtualenv -p py3 ,venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ```
----

## persian_alphabet.py
the persian alphabetic and numeric in this file.

----
## algorithm.py
this file have the `Encrypt` and `Decrypt` class for algorithm caesar and rot16

----
## caesar.py
this file for encrypt and decrypt `caesar` mode
- with text
- with file

the end of program it will saved on `caesar.txt` file

---

## rot16.py
this file for encrypt and decrypt `rot16` mode
- with text
- with file

the end of program it will saved on `rot16.txt` file

----
## caesar-rot16-cli.py

this is a command line app for encrypt and decrypt your text to `caesar` and `rot16` 
### commands

- `--encrypt`, `-e`, `-E` => for encrypt mode
- `--decrypt`, `-d`, `-D` => for decrypt mode
- `--caesar`, `-c`, `-C` => for `caesar` mode
- `--rot16`, `-r16`, `-R16` => for `rot16` mode
- `--text`, `-t`, `-T` => for text you can use it like => `python3 caesar-rot16-cli.py -e -c -t "your text"`
- `--file`, `-f`, `-F` => for file name you can use it like => `python3 caesar-rot16-cli.py -e -c -f filename.txt` file must be txt
