import pikepdf
import os
import glob


def unlock():
    cwd = os.getcwd()
    pdf_pass = 'statystyka_nas_przenika'
    pdf_pass2 = 'urocze_zadanka'
    for file in glob.glob(cwd + '\\*.pdf'):
        print(file)
        try:
            pdf = pikepdf.open(file, password=pdf_pass, allow_overwriting_input=True)
        except (PermissionError, Exception):
            try:
                pdf = pikepdf.open(file, password=pdf_pass2, allow_overwriting_input=True)
            except (PermissionError, Exception):
                print('cannot unlock pdf')
                continue
        print('Processing')
        pdf.save(file)
        print('Files unlocked succesfully')


if __name__ == '__main__':
    unlock()

