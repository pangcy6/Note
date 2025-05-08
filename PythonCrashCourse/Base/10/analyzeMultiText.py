# 多文件文本单词数统计

def count_words(file):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file) as obj:
            contents = obj.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file} does not exist.")
    else:
        # 计算文件大概包含多少个单词
        words = contents.split()
        print(f"The file {file} has about {len(words)} words.")


files = ['txt/guestList.txt', 'txt/pi.tt', 'txt/programming.txt']
for file in files:
    count_words(file)
