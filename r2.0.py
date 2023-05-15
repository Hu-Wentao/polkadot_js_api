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


def find_package_json(path):
    for root, dirs, files in os.walk(path):
        if "package.json" in files:
            return root
    return None


def execute_command(path, cmd):
    os.chdir(path)
    os.system(cmd)
    # os.system("/Users/huwentao/fvm/versions/1.22.6/bin/dart create . package --force")


if __name__ == "__main__":
    # dir = os.getcwd()
    dir = './packages'
    cmd = "/Users/huwentao/fvm/versions/1.22.6/bin/dart create . package --force"
    for root, dirs, files in os.walk(dir):
        package_dir = find_package_json(root)
        if package_dir:
            execute_command(package_dir, cmd=cmd)
