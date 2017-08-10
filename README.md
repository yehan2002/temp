# Temp
A simple module used to make a temporary 
folder and delete the folder when the
script exits.The folder is created in the
/tmp directory with a unique folder name.

## Usage:
 - temp.path : location of the folder (a string)
 - temp.dirname : name of dir (a string)

## Example:
```import temp
f = open(temp.path + '/hello','a')
f.write('hello world')
f.close()
raw_input('press enter to exit the program')
```
