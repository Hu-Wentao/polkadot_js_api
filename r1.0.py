import os
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
            # 将old_path替换new_path
            os.replace(old_path, new_path,)
            
            


if __name__ == '__main__':
    rename_folder()
