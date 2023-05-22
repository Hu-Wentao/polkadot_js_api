# ### 脚本#/src->/lib/src:
# 可能不必要
# ```python
import os
import shutil

# 获取当前工作目录
current_dir = os.getcwd()


def find_packages(path):
    """
    从2.0复制得到; 用于查询路径下所有包含package.json的文件夹;返回绝对路径list[str];
    Finds all directories containing a package.json file in the specified path.
    :param path: The path to search for package.json files.
    :return: A list of directory paths containing package.json files.
    """
    package_directories = []
    for root, dirs, files in os.walk(path):
        if 'package.json' in files:
            package_directories.append(os.path.abspath(root))
    return package_directories

# 遍历当前目录以及子目录


def move_src_to_lib(root: str = './packages'):
    # 获取 src 文件夹的路径
    src_path = os.path.join(root, 'src')
    if not os.path.exists(src_path):
        return
    # 获取 lib 文件夹的路径
    lib_path = os.path.join(root, 'lib', 'src')
    # 如果 lib 文件夹已经存在，则删除其中所有内容
    if os.path.exists(lib_path):
        shutil.rmtree(lib_path)
    # 将 src 文件夹移动到 lib 文件夹中
    shutil.move(src_path, lib_path)


if __name__ == '__main__':
    path = './packages'
    for root in find_packages(path):
        print("root {}".format(root))
        move_src_to_lib(root=root)
