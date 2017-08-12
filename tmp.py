#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import __main__ as main
import os
import atexit

'''
A simple module used to make a temporary
folder and delete the folder when the
script exits.The folder is created in the
/tmp directory with a unique folder name.

temp.path : location of the folder (a string)
temp.dirname : name of dir (a string)
temp.mkdir(dirname) : create a new directory
        inside the temporary directory
temp.mkfile(filename) : create a new file
        inside the temporary directory
temp.rm(filename) : delete a folder or
        file inside the temporary directory
temp.join(path) : join given str or list
    or tuple with the location of the
    temporary directory using
    os.path.join()
temp.open(filename,method='a') : open a
    file with the specified method using
    open() and returns the file for
    reading or writing
Example:
import temp
f = temp.open('/hello','a')
f.write('hello world')
f.close()
raw_input('press enter to exit the program')
'''
class __tempfile__:
    def __init__(self):
        idof = subprocess.check_output(['date', '+%s%N'])
        idof = idof.replace('\n','')
        try:
            name = os.path.split(main.__file__)[1].replace('.py', '')
        except AttributeError:
            name = os.path.split(__file__)[1].replace('.py', '')
        self.idof = name + str(idof)
        self.path = os.path.join('/tmp', self.idof )
    def mktmpdir(self):
        os.mkdir(self.path)
    def deldir(self):
        os.system('rm -r ' + self.path)
    def mkdir(self,name):
        path = os.path.join(self.path,name)
        os.mkdir(path)
        return path
    def mkfile(self,name):
        path = os.path.join(self.path,name)
        open(path,'a').close()
        return path
    def delit(self,file):
        path = os.path.join(self.path,file)
        os.system('rm -r -f ' + path)
    def pathcreate(self,pathof):
        if type(pathof) == str:
            pathof = [pathof]
        elif type(pathof) == tuple:
            pathof = list(pathof)
        elif type(pathof) == list:
            pass
        else:
            error = ('Expected a string or a list or a turple.Recived a' +
            str(type(pathof)).replace("<type '").replace("'>"))
            raise TypeError(error)
        pathof2 = []
        for item in pathof:
            if item[0] == '/':
                pathof2.append(item[1:])
            else:
                pathof2.append(item)
        pathof = pathof2
        base = [self.path]
        base.extend(pathof)
        exec("base = os.path.join"+str(tuple(base)))
        return base
    def openfile(self,file,method='a'):
        pathof = self.pathcreate(file)
        return open(pathof,method)
__temp__ = __tempfile__()
atexit.register(__temp__.deldir)
__temp__.mktmpdir()
path = __temp__.path
dirname  = __temp__.idof
mkdir = __temp__.mkdir
mkfile = __temp__.mkfile
rm = __temp__.delit
join = __temp__.pathcreate
open = __temp__.openfile
del(__temp__)
