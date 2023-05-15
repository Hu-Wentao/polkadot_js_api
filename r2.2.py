import os


def ts_2_dart(folder, file):
    # ts2dart
    os.chdir(folder)
    os.system('ts2dart '+file)
    pass


def traverse_directories(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.js') or file_path.endswith('.ts'):
                ts_2_dart(folder=root, file=file_path)
                # replace_dash_with_underscore(file_path)


if __name__ == '__main__':
    traverse_directories('./packages')
