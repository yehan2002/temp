# Getting started
## Simple Usage

If you have installed tmp, you can start using it from Python like this.
``` python
import tmp
t = tmp.tmp('tmpdir')
f = t.tmpopen('/hello','a')
f.write('hello world')
f.close()
raw_input('press enter to exit the program')
``` 
The above script can be saved into a file (eg:- tmptest.py), then it can be run like this:

``` 
python tmptest.py
 ```
 
The above command will run ask you to press enter to continue.
Do not press enter,yet.
instead open your tmp directory(/tmp in most linux distros).
You should notice a directory called tmpdir there containing a text file called hello.

Now press enter and reopen the tmp directory. 'tmpdir' should have vanished !!

## Example explained

Calling the  ```tmp()`` class creates a temporary directory in the current 
Operating systems default location with the given name or a random name.

The ```tmpopen()``` function opens a file in the tmpdirectory with given path and name.
The method for opening the file is the second arg.It is not required.If no method is given
the file is opened with the 'a' method.

