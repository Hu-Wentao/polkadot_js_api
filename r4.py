
# ### 脚本ts->dart: 可以重命名当前路径下所有文件以及子文件夹中所有扩展名为 .ts 的文件为 .dart：
# ```python

import os
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".ts"):
            new_filename = filename.replace(".ts", ".dart")
            os.rename(os.path.join(root, filename),
                      os.path.join(root, new_filename))
