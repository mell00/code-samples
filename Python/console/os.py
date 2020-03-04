#OS MODULE#

import os

#Return list of attributes and methods of an object:
dir(object_name[index_value])

os.getcwd()

os.chdir("filepath_excluding_module_os")
print(os.chdir())
##Prints 'filepath/module_os'##

os.listdir("optional_filepath_excluding_module_os")

os.mkdir("new_directory_name")

os.mkdirs("parent_directory/child_directory/grandchild_directory",directory_mode)

os.rmdir("directory_name")

os.removedirs("parent_directory/child_directory/grandchild_directory",directory_mode)

os.rename("current_name","new_name")

os.stat(file_or_folder)

os.stat(file_or_folder).os_stat_attribute

for (root,dirs,files) in os.walk(name.topdownbottomup=true):
    print(root)
    print(dirs)
    print(files)
    print()

os.environ(["environ_variable_name"]) = "environ_variable_value"

os.environ(["environ_variable_name"])

os.environ.get("environ_variable_name")

#Retrieve file name from given path, excluding the file path name:
var = os.path.basename("file_path")
print(var)
##Prints "file_name"##

#Retrieve directory name from given file path, excluding the file path name:
var2 = os.path.dirname("directory_file_path")
print(var2)
##Prints "directory_name"##

#Determines whether specified file path is absolute or not:
var3 = os.path.isabs("file_path")
print(var3)
##Prints boolean value##

#Determines whether specified file path is an existing directory or not:
var4 = os.path.isdir("file_path")
print(var4)
##Prints boolean value##

#Convert file path into "normalized"/lowercase characters; in Windows, forward slashes become backward slashes
var5 = os.path.normcase("file_path")
print(var5)
##Prints lowercase file_path##

#Print file path without redundant separators and up-level references; in Windows, forward slashes become backward slashes
var6 = os.path.normpath("file_path")
print(var6)
##Prints file_path without redundant separators and/or up-level references##

#Access tuple of directory name(s) and file name(s) of a given file path in individual strings:
os.path.split("file_path")
##Returns "parent_directory", "file_name"##

#Find whether a given file path name exists or not:
os.path.exists("file_path")
##Returns boolean value##

#Find whether a given file exists or not:
os.path.isfile("file_path")
##Returns boolean value##
