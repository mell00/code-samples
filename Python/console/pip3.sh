#pip3#

$pip3 help

$pip3 search package_name

$pip3 install package_name

$pip3 list

  $pip3 list --outdated

  $pip3 list --o

$pip3 install -U package_name

$pip3 uninstall package_name

$pip3 freeze

  $pip3 freeze > file_name.txt

  $pip3 freeze __local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U

$pip3 cat file_name.txt

$pip3 install -r file_name
