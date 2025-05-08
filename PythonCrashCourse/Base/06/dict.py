favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# 查询某个键值对
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + 
    ".")
# 添加键值对
favorite_languages['john'] = 'php'
#修改键值对
favorite_languages['sarah'] = 'go'
print(favorite_languages)
# 删除
del favorite_languages['john']
print(favorite_languages)

# 遍历字典的典型方式
for name, language in favorite_languages.items():
    print(name.title() + 
        "'s favorite language is " + 
        language.title() + 
        ".")

# 遍历字典的特殊方式, 关键点在于取key和value的不同.
friends = ['sarah', 'phil']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")
# 注意最后一行代码取key值和value值的不同!!!
