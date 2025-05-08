# 检验字典几种遍历方式

languages = {
    "tom": "c",
    "jerry": "rust",
    "alice": "java",
    "ellie": "python",
    "bruse": "php",
}

# key/value双遍历
for name, language in languages.items():
    print(f"{name.title()} loves {language.title()}")

# key单遍历
for name in languages.keys():
    print(name.title())

# value单遍历
for lan in languages.values():
    print(lan.title())

"""
总结:
    双遍历:     dictName.items()
    key遍历:    dictName.keys()
    value遍历:  dictName.values()
"""
