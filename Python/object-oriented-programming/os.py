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

var = os.path.basename("file_path")
print(var)
##Prints "file_name"##

var2 = os.path.dirname("directory_file_path")
print(var2)
##Prints "directory_name"##

var3 = os.path.isabs("file_path")
print(var3)
##Prints boolean value##

var4 = os.path.isdir("file_path")
print(var4)
##Prints boolean value##

var5 = os.path.normcase("file_path")
print(var5)
##Prints lowercase file_path##

var6 = os.path.normpath("file_path")
print(var6)
##Prints file_path without redundant separators and/or up-level references##

os.path.split("file_path")
