#OS MODULE#

import os

#Return list of attributes and methods of an object:
dir(object_name[index_value])

#Return current working directory of a process:
os.getcwd()

#Navigate to a file path:
os.chdir("filepath_excluding_module_os")
print(os.chdir())
##Prints 'filepath/module_os'##

#Return list of files and folders contained within current or specified directory:
os.listdir("optional_filepath_excluding_module_os")

#Create a new directory (that does not share a name with an existing directory):
os.mkdir("new_directory_name")

#Create new filepath consisting of a parent directory, and one or more subdirectories:
os.mkdirs("parent_directory/child_directory/grandchild_directory",directory_mode)

#Delete an existing directory:
os.rmdir("directory_name")

#Delete an existing filepath consisting of a parent directory, and one or more subdirectories:
os.removedirs("parent_directory/child_directory/grandchild_directory",directory_mode)

#Rename specified file or folder:
os.rename("current_name","new_name")

#Retrieve status information of specified file or folder:
os.stat(file_or_folder)

#Retrieve particular attribute of status information of specified file or folder:
os.stat(file_or_folder).os_stat_attribute

#Return a tuple containing directory path, directory names, and file names:
for (root,dirs,files) in os.walk(name.topdownbottomup=true):
    print(root)
    print(dirs)
    print(files)
    print()

#Reassign value of environmental variable to "environ_variable_value":
os.environ(["environ_variable_name"]) = "environ_variable_value"

#Retrieve value paired to specified environmental variable:
os.environ(["environ_variable_name"])

#Return a dictionary containing environmental variable:value pairs:
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
