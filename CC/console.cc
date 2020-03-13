//C++ CONSOLE//

#include <fstream.h>  //library file for reading/writing files
#include <ofstream.h> //library file for writing files
#include <ifstream.h> //library file for reading files

//Create file handle (pointer to the file):
ifstream infile; //handle for reading file
ofstream outfile; //handle for writing file
fstream f; //handle for reading/writing file

//Open file for reading:
void open(const char "file_path_with_file_name" in);
//Open file for writing:
void open(const char "file_path_with_file_name" out);
//Open file at initial position of end of file:
void open(const char "file_path_with_file_name" ate);
//Open file so that every output is appended at the end of the file:
void open(const char "file_path_with_file_name" app);
//Open file so that if it already exists, it is erased:
void open(const char "file_path_with_file_name" trunc);
//Open file in binary mode:
void open(const char "file_path_with_file_name" binary);

//Close file:
f.close()
