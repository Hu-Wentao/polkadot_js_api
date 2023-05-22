"""
预处理ts语法特性 (ES2015)
1. 对不支持的关键字进行替换
2. 添加附加类型(针对TupleType), (需要转换为dart后,在dart中全部合并到单个文件内)
3. 全局附加dart扩展 todo
"""

import os
import re


# 1.多行正则匹配替换 (一般是对代码块操作)
multiRegMap = {
    # 0 移除注释
    re.compile(r'/\/\/.*|\/\*[\s\S]*?\*\/|<!--[\s\S]*?-->/g'): "",

    # 1 移除 export default 导出set
    re.compile(r'(export default \{[\s\S\n\r]*?\};)'): "",
    # 1 移除 export default 导出list
    re.compile(r'(export default \[[\s\S\n\r]*?\];)'): "",
    # 1 移除 export *
    re.compile(r'(export \*.+)'): "",
}

# 2.逐行正则替换
singleRegMap = {
    # 1 unknown 替换为 any
    re.compile(r' unknown'): ' any',
    # 2 移除readonly 关键字
    re.compile(r'readonly\s'): '',

    # 2 移除 typeof
    re.compile(r' typeof '): r' ',
    # 2 移除 protected
    re.compile(r' protected '): r' ',
    # 2 移除 void 函数返回值 ##fixme
    re.compile(r'(function.+): void  \{'): r'\1 \{',
    # 2 WeakMap -> Map
    re.compile(r'WeakMap<'): r'Map<',
    # 2 import type *  -> import
    re.compile(r'import type \*  from '): r'import ',
    re.compile(r'import type '): r'import ',
    # import defaults from
    re.compile(r'import defaults from '): r'import ',  # /* export all */
    # 2 NonNullExpression 移除非空变量声明
    re.compile(r' (\w+)!'): r' \1',
    # 2 ArrayBindingPattern 数字匹配模式
    re.compile(r'\[(\w+)\]: (\w+)\[\]'): r'\1: \2',  # 单个元素匹配
    re.compile(r'const \[(\w+), (\w+)\] = (.+);'): r'const aryBudPtn\1\2 = \3; const \1=aryBudPtn\1\2[0]; const \2=aryBudPtn\1\2[1];',
    re.compile(r'const \[, (\w+)\] = (.+);'): r'const aryBudPtn\1 = \2; const \1=aryBudPtn\1[1];',
    # 2 联合类型替换为 any
    re.compile(r'string \| Error'): 'any',
    re.compile(r'string \| number'): 'any',
    re.compile(r' ((Promise<[\w\.]+>)|([\w]+)) \| null'): r' \1',
    re.compile(r' ((Promise<[\w\.]+>)|([\w]+)) \| undefined'): r' \1',
    # 2 AsExpression: 直接移除 ’as Xxx‘
    re.compile(r' as (\w+)'): r' ',  # /* as \1 */
    # 2 class内部的 连续赋值表达式: this.a = this.b = c -> this.a=c; this.b=c;
    re.compile(r'this\.(\w+)\s?=\s?this\.(\w+)\s?=\s?(\w+\.?\w+);'): r'this.\1 = \3; this.\2 = \3;',
    # 2 Record -> Map
    re.compile(r'Record'): 'Map',
    # 3 #符号 -> readonly
    re.compile(r'#(\w+)'): r'readonly_\1',
    # 3 delete运算符
    re.compile(r'delete ([\.\w\$]+)\[([\w\.]+)\];'): r'\1[\2] = undefined;',
    # 手动替换 ===
    # 2 注释掉不支持的‘字面量’
    re.compile(r"  jsonrpc: '2.0'"): "// jsonrpc: '2.0'"
}

# 3.逐行正则替换(同时附加信息在文件尾部)
supportRegTrailMap = {
    # TupleType: 创建特定Tuple类型
    re.compile(r'\[string, any\]'): 'TupleStrAny',
    re.compile(r'\[number, string\]'): 'TupleNumStr',
    re.compile(r'\[number, JsonRpcRequest\]'): "TupleNumJsonRpcReq",
    re.compile(r'\[ResponseCallback, { unsubscribeMethod: string; id: any }\]'): 'TupleRspCallUnsub',
}

# 配合 supportRegeMap使用,key与其value对应; 用于在尾部添加附加类型
supportTrailMap = {
    "TupleStrAny":
    "class TupleStrAny{constructor(public value1: string, public value2: any) {}}",
    "TupleNumStr": "class TupleNumStr{constructor(public value1: number, public value2: string) {}}",
    "TupleNumJsonRpcReq": "class TupleNumJsonRpcReq{constructor(public value1: number, public value2: JsonRpcRequest) {}}",
    "TupleRspCallUnsub":
    "class CallUnsub{constructor(public unsubscribeMethod: string, public id: any) {}}"
    "class TupleRspCallUnsub{constructor(public value1: ResponseCallback, public value2: CallUnsub) {}}",
}


def replace_in_files(path):
    """
    Performs a regular expression replacement on all lines of all .ts files in the specified path.
    :param path: The path to search for .ts files.
    :param regex: The regular expression to search for.
    :param replacement: The replacement string.
    """
    # Walk through the directory tree and process each file
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.ts'):
                file_path = os.path.join(root, file)
                # 读取
                with open(file_path, 'r') as f:
                    content = f.read()
                # 写入
                with open(file_path, 'w') as f:
                    # 1. 多行替换
                    for pattern, replacement in multiRegMap.items():
                        content = re.sub(pattern, replacement, content)

                    # 2. 逐行替换
                    supportTrailLs = set({})
                    # 2.1 正则替换
                    for contentLn in content.splitlines():
                        new_line = contentLn
                        # 1.1 单行正则替换
                        for pattern, replacement in singleRegMap.items():
                            new_line = re.sub(pattern, replacement, new_line)

                        # 1.2 带附加信息的正则替换
                        for pattern, replacement in supportRegTrailMap.items():
                            new_line2 = re.sub(pattern, replacement, new_line)
                            if new_line != new_line2:
                                supportTrailLs.add(
                                    supportTrailMap[replacement])
                            new_line = new_line2
                        # 1.3 写入替换后的行
                        f.write(new_line+'\n')

                    # 2 尾部添加 Support Info
                    if len(supportTrailLs) > 0:
                        f.write('\n// ======Support Info======\n')
                        for supportLn in supportTrailLs:
                            f.write(supportLn)
                            f.write('\n')


if __name__ == '__main__':
    # replace_in_files('./packages')
    replace_in_files(
        "/Users/huwentao/_proj/api/packages/rpc_provider/lib/src")
