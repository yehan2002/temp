#!/usr/bin/python
# -*- coding: utf-8 -*-

import __main__ as main
import os
import atexit
import tempfile
import shutil
import time

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
temp.tmpopen(filename,method='a') : open a
    file with the specified method using
    open() and returns the file for
    reading or writing
Example:
import tmp
t = tmp.tmp('tmpdir')
f = t.tmpopen('/hello','a')
f.write('hello world')
f.close()
raw_input('press enter to exit the program')
'''
class tmp:
    def __init__(self,path=False):
        if not path:
            idof = str(int(time.time()*1000000))
            idof = idof.replace('\n','')
            current_temp = tempfile.gettempdir()
            self.shutil = shutil
            try:
                name = os.path.split(main.__file__)[1].replace('.py', '')
            except AttributeError:
                name = os.path.split(__file__)[1].replace('.py', '')
            self.dirname = name + str(idof)
            self.path = os.path.join(current_temp, idof )
        else:
            current_temp = tempfile.gettempdir()
            self.shutil = shutil
            self.path = os.path.join(current_temp,path )
            self.dirname = path
        self._mktmpdir()
        atexit.register(self._deldir)
    def delete(self,filename='',join=True):
        if join:
            filename = self.join(filename)
        try:
            shutil.rmtree(filename)
        except OSError:
            os.remove(filename)
    def _mktmpdir(self):
        os.mkdir(self.path)
    def _deldir(self):
        shutil.rmtree(self.path)
    def mkdir(self,name):
        path = os.path.join(self.path,name)
        os.mkdir(path)
        return path
    def mkfile(self,name):
        path = os.path.join(self.path,name)
        open(path,'a').close()
        return path
    def rm(self,filen):
        if filen[0] == os.sep:
            filen = filen[1:]
        path = os.path.join(self.path,filen)
        self.delete(path)
    def join(self,*pathof):
        if type(pathof) == str:
            pathof = [pathof]
        elif type(pathof) == tuple:
            pathof = list(pathof)
        elif type(pathof) == list:
            pass
        else:
            typerecevied = str(type(pathof)).replace("<type '").replace("'>")
            error = (
            'Expected a string or a list or a turple.Recived a' + typerecevied)
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
    def tmpopen(self,file,method='a'):
        pathof = self.join(file)
        return open(pathof,method)
class temp:
    def __init__(self):
        __temp__ = tmp()
        self.path = __temp__.path
        self.dirname  = __temp__.idof
        self.mkdir = __temp__.mkdir
        self.mkfile = __temp__.mkfile
        self.rm = __temp__.rm
        self.join = __temp__.join
        self.tmpopen = __temp__.tmpopen
        del(__temp__)
