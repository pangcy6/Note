# 列表操作练习排序

wishlist = ["大理", "九寨沟", "成都", "拉萨", "喀什"]

print(wishlist)

# 临时排序
print(sorted(wishlist))

print(wishlist)

# 逆序不排列
wishlist.reverse()
print(wishlist)

# 永久排序,不可恢复
wishlist.sort()
print(wishlist)
# 逆序永久排序
wishlist.sort(reverse=True)
print(wishlist)

# 列表长度
print(f"列表 wishlist 的长度为: {len(wishlist)}.")

# 疑问?
print("\n中文排序的根据是什么?\n\t肯定不是读音!\n\t笔画也不是, 那到底依据是什么???")
