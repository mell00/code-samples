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

##PATHS:
var = os.path(bytes_or_"string_objects")
##Prints an object of the same type (if path or file name is returned)##

    ##FORMAT CONVENTIONS FOR OS PATHS:
    os.path #by default, will always be the path module suitable for the OS that Python currently runs on; suitable for local paths
    os.posixpath #sets UNIX-style paths
    os.ntpath #sets Windows paths

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

    #Print longest common sub_path_name of each path name in path_sequence:
    path_sequence = ["file_path1","file_path2","file_path3"]
    var = os.path.commonpath(path_sequence)
    print(var)
    ##Prints "sub_path_name"##

    #Print longest path_prefix (taken character-by-character) shared by all path names in path_sequence:
    path_sequence = ["file_path1","file_path2","file_path3"]
    var = os.path.commonprefix(path_sequence)
    print(var)
    ##Prints "path_prefix"##

    #Return "file_path" with initial "~user" component replaced by the user's home directory:
    path = "~user/file_path"
    os.path.expanduser(path)
    ##Returns "home path/file_path"##

    #
    path = "~user/file_path"
    os.path.expandvars(path)

    #
    path = "~user/file_path"
    os.path.getatime(path)

    #
    path = "~user/file_path"
    os.path.getmtime(path)

    #
    path = "~user/file_path"
    os.path.getctime(path)

    #
    path = "~user/file_path"
    os.path.getsize(path)

    #
    path = "~user/file_path"
    os.path.islink(path)

    #
    path = "~user/file_path"
    os.path.ismount(path)

    #
    path = "~user/file_path"
    os.path.join(path,*other_paths)

    #
    path = "~user/file_path"
    os.path.realpath(path)

    #
    path = "~user/file_path"
    os.path.relpath(path,start=os.curdir)

    #
    path1 = "~user/file_path1"
    path2 = "~user/file_path2"
    os.path.samefile(path1,path2)

    #
    path = "~user/file_path"
    fp1 =
    fp2 =
    os.path.sameopenfile(fp1,fp2)

    #
    path = "~user/file_path"
    stat1 =
    stat2 =
    os.path.samestat(stat1,stat2)

    #
    path = "~user/file_path"
    os.path.splitdrive(path)

    #
    path = "~user/file_path"
    os.path.splittext(path)

    #
    path = "~user/file_path"
    os.path.supports_unicode_filenames
