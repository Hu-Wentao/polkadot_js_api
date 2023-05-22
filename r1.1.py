import os
import shutil
"""
重命名包名 - _
"""
def rename_folder(root: str = './packages'):
    for root, dirs, files in os.walk(root):
        for file in files:
            old_path = os.path.join(root, file)
            new_file = file.replace('-', '_')
            new_path = os.path.join(root, new_file)
            os.rename(old_path, new_path)

        for dir in dirs:
            old_path = os.path.join(root, dir)
            new_dir = dir.replace('-', '_')
            new_path = os.path.join(root, new_dir)
            if old_path == new_path:
                continue
            # 将old_pRath替换new_path
            if os.path.exists(new_path):
                shutil.rmtree(new_path)
            # os.removedirs(new_path)
            os.replace(old_path, new_path,)
            
            


if __name__ == '__main__':
    rename_folder()
