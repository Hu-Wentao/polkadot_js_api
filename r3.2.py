import os


def ts_2_dart(file):
    # print("ts2dart# {}".format(file))
    os.system('ts2dart '+file)
    pass


def traverse_directories(root_path):
    """
    遍历路径下所有的 .ts 文件
    """
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.ts') and not file.endswith('.spec.ts'):
                file_path = os.path.join(root, file)
                # print("debug root {}, dirs {}, file {}, file_path {}".format(root, dirs, file, file_path))
                ts_2_dart(file_path)

if __name__ == '__main__':
    # traverse_directories('./packages')
    traverse_directories('/Users/huwentao/_proj/api/packages/rpc_provider/lib/src')


# [12](packages/rpc_provider/lib/src/substrate-connect/index.ts)