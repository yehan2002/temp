# Tmp
A simple module used to make a temporary 
folder and delete the folder when the
script exits.The folder is created in the
/tmp directory with a unique folder name.
##### Currently only works on linux

## Usage:
 - tmp.path : location of the folder (a string)
 - tmp.dirname : name of dir (a string)
 - tmp.mkdir(dirname) : create a new directory inside the temporary directory
 - tmp.mkfile(filename) : create a new file inside the temporary directory
 - tmp.rm(filename) : delete a folder or file inside the temporary directory
 - tmp.join(path) : join given str with the location of the temporary directory using os.path.join()
 - tmp.open(filename,method='a') : open a file with the specified method using open() and returns the file for reading or writing

## Example:
```python
import tmp
f = tmp.open('/hello','a')
f.write('hello world')
f.close()
raw_input('press enter to exit the program')
```
## Download
  <a href="https://github.com/yehan2002/tmp/releases" class="btn" style='background-color:#15915F;text-align:center;margin-left:40%;margin-right:40%;'>Download now</a>
