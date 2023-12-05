import os
import re

def main():
    file_path = input("Укажиет путь к компилироваемому файлу \n")
    with open(file_path, 'r') as f:
        code = [line.strip() for line in f]
        for code_line in code:
            # print(code_line)
            m = re.search("=", code_line)
            if m is not None:
                print(f"{str(m)} \n")


if __name__ == '__main__':
    main()
    