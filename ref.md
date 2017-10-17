# Quick Reference
 - ```tmp.path``` : location of the folder (a string)
 - ```tmp.dirname``` : name of dir (a string)
 - ```tmp.mkdir(dirname)``` : create a new directory inside the temporary directory
 - ```tmp.mkfile(filename)``` : create a new file inside the temporary directory
 - ```tmp.rm(filename)``` : delete a folder or file inside the temporary directory
 - ```tmp.join(path)``` : join given str with the location of the temporary directory using os.path.join()
 - ```tmp.tmpopen(filename,method='a')``` : open a file with the specified method using open() and returns the file for reading or writing
