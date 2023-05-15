# ### 脚本#/src->/lib/src:
# 可能不必要
# ```python
import os
import shutil

# 获取当前工作目录
current_dir = os.getcwd()

# 遍历当前目录以及子目录
def move_src_to_lib(str:root='./packages'):
    for root, dirs, files in os.walk(current_dir):
        # 如果当前目录下存在 package.json 文件
        if 'package.json' in files:
            # 获取 src 文件夹的路径
            src_path = os.path.join(root, 'src')
            # 获取 lib 文件夹的路径
            lib_path = os.path.join(root, 'lib', 'src')
            # 如果 lib 文件夹已经存在，则删除其中所有内容
            if os.path.exists(lib_path):
                shutil.rmtree(lib_path)
            # 将 src 文件夹移动到 lib 文件夹中
            shutil.move(src_path, lib_path)

if __name__ == '__main__':
    move_src_to_lib()