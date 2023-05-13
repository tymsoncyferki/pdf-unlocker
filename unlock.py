import pikepdf
import glob
import os
from config import pdf_passwords, absolute_path
import argparse


def unlock():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--current", help="Use current directory instead of absolute path", action="store_true")
    args = parser.parse_args()
    if args.current or not absolute_path:
        print("Using current directory")
        cwd = os.getcwd()
    else:
        print("Using absolute path")
        cwd = absolute_path
    for file in glob.glob(cwd + '\\*.pdf'):
        print(file)
        unlocked = False
        try:
            pdf = pikepdf.open(file)
            print("PDF do not have a password")
            continue
        except (PermissionError, Exception):
            pass
        for password in pdf_passwords:
            try:
                pdf = pikepdf.open(file, password=password, allow_overwriting_input=True)
                unlocked = True
                break
            except (PermissionError, Exception):
                continue
        if not unlocked:
            print('Cannot unlock pdf')
            continue
        pdf.save(file)
        print('File unlocked succesfully')


if __name__ == '__main__':
    unlock()

