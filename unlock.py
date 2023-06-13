import pikepdf
import glob
import os
from config import pdf_passwords, absolute_path
import argparse


def get_directory(arg, path):
    """ Gets working directory """
    if arg or not path:
        print("Using current directory")
        return os.getcwd()
    else:
        print("Using absolute path")
        return absolute_path


def is_encrypted(file):
    """ Checks if pdf is encrypted """
    try:
        pdf = pikepdf.open(file)
        print("PDF does not have a password")
        return False
    except (PermissionError, pikepdf.PasswordError):
        return True


def unlock(file, passwords):
    """ Tries unlocking pdf with given list of passwords """
    unlocked = False
    for password in passwords:
        try:
            pdf = pikepdf.open(file, password=password, allow_overwriting_input=True)
            unlocked = True
            return unlocked, pdf
        except (PermissionError, pikepdf.PasswordError):
            continue
    return unlocked, None


def main():
    # Get argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--current", help="Use current directory instead of absolute path", action="store_true")
    args = parser.parse_args()

    # Get directory
    cwd = get_directory(args.current, absolute_path)

    # Iterate over pdf files
    for file in glob.glob(cwd + '\\*.pdf'):
        print(file)
        if not is_encrypted(file):
            continue

        unlocked, pdf = unlock(file, pdf_passwords)

        if not unlocked:
            print('Cannot unlock pdf')
            continue

        pdf.save(file)
        print('File unlocked succesfully')


if __name__ == '__main__':
    main()

