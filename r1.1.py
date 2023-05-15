"""
替换import中的-为_

这段 Python 脚本会遍历当前路径下的所有文件夹以及子文件夹中的文件，
对所有以 "@polkadot/" 开头的字符串中的 "-" 进行替换，将其替换为 "_"。具体实现使用了正则表达式。
"""

import os
import re


def replace_hyphen_in_imports(code: str) -> str:
    def replacer(match):
        return match.group(0).replace('-', '_')

    return re.sub(r"(import\s+.*?'.*?-.*?';)", replacer, code)

# s = "import { MockProvider } from '@polkadot/rpc-provider/mock-a/dawf';"
# print(replace_hyphen_in_imports(s))


def replace_string_in_ts(root_path):
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            print('process# '+filepath)
            if filepath.endswith('.js') or filepath.endswith('.ts'):
                with open(filepath, 'r') as f:
                    content = f.read()

                content = replace_hyphen_in_imports(code=content)
                with open(filepath, 'w') as f:
                    f.write(content)


if __name__ == '__main__':
    root_path = './packages'  # 当前路径
    replace_string_in_ts(root_path)

