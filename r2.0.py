"""
创建dart项目
"""

# 递归遍历当前目录下所有文件夹及子文件夹，
# 调用find_package_json函数查找是否存在名为package.json的文件。
#   如果找到，则调用execute_dart_command函数在该路径下执行命令。
# ```python
# Flutter 1.22 dart路径
# /Users/huwentao/fvm/versions/1.22.6/bin/dart

import os

def execute_command(path):
    dir = os.path.dirname(path)
    base = os.path.basename(path)
    os.chdir(dir)
    print("path# {}, base# {} ".format(path, base))
    os.system("/Users/huwentao/fvm/versions/1.22.6/bin/dart create " +
              base+" --force -t package-simple")


def find_packages(path):
    """
    Finds all directories containing a package.json file in the specified path.
    :param path: The path to search for package.json files.
    :return: A list of directory paths containing package.json files.
    """
    package_directories = []
    for root, dirs, files in os.walk(path):
        if 'package.json' in files:
            package_directories.append(os.path.abspath(root))
    return package_directories


if __name__ == "__main__":
    dir = './packages'
    for root in find_packages(dir):
        print("root {}".format(root))
        execute_command(root)