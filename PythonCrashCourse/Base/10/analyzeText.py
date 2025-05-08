# 分析文本中大概有多少单词
# split()以空格为分隔符拆分字符串为列表

filename = "txt/programming.txt"

try:
    with open(filename) as obj:
        contents = obj.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # 计算文件大概包含多少个单词
    words = contents.split()
    print(f"The file {filename} has about {len(words)} words.")
