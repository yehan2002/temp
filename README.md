# Temp
A simple module used to make a temporary 
folder and delete the folder when the
script exits.The folder is created in the
/tmp directory with a unique folder name.
##### Currently only works on linux

## Usage:
 - temp.path : location of the folder (a string)
 - temp.dirname : name of dir (a string)
 - temp.mkdir(dirname) : create a new directory inside the temporary directory
 - temp.mkfile(filename) : create a new file inside the temporary directory
 - temp.rm(filename) : delete a folder or file inside the temporary directory
 - temp.join(path) : join given str or list or tuple with the location of the temporary directory using os.path.join()
 - temp.open(filename,method='a') : open a file with the specified method using open() and returns the file for reading or writing

## Example:
```python import temp
f = temp.open('/hello','a')
f.write('hello world')
f.close()
raw_input('press enter to exit the program')
```
## Todo
- [x] Add intro to the module
- [ ] Cross platform support
