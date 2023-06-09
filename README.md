# pdf-unlocker
This little project was created to unlock pdf files from statistics course. Of course it can be used for any encrypted pdf files - you just have to edit config file.

## Usage

Specify absolute path in config.py or use -c option to use current working directory.
To use this app for other files just replace passwords in config.py.

PikePDF is required
```
pip install -r requirements.txt
```
In console run
```
python unlock.py
```
If you want to use current working directory run
```
python unlock.py -c
```
