#PYTHON FILE OBJECT#

#open()
var = open('file_path',mode='mode', encoding=encoding_type)

    var = open('file_path',mode='r', encoding=encoding_type)

    var = open('file_path',mode='w', encoding=encoding_type)

    var = open('file_path',mode='x', encoding=encoding_type)

    var = open('file_path',mode='a', encoding=encoding_type)

    var = open('file_path',mode='t', encoding=encoding_type)

    var = open('file_path',mode='b', encoding=encoding_type)

    var = open('file_path',mode='rt', encoding=encoding_type)

#close()
try:
    var = open('file_path',mode=mode, encoding=encoding_type)
    #Perform file operation(s)
    var.close()

#write()
var.write('string\n')

#read()
var.read(num_of_chars)

#seek()
var.seek(offset_in_bytes,from=(start,current,end))
    #ex:
    var.seek(0)
    ##Brings file cursor to initial position##

#tell()
var.tell()
##Returns current file position##

#Line-by-line read-through loop:
for line in file:
    print(line,end='\n')
    ##Prints each file line with a line break##

#readline()
var.readline()

#readlines()
var.readlines()
