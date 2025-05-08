# 模拟网站新用户注册
current_users = ['admin', 'alice', 'john', 'bob', 'elliot', 'jack']
new_users = ['Ted', 'JOHN', 'webbo']

for new_user in new_users:
	if new_user.lower() not in current_users:
		current_users.append(new_user.lower())
		print(f"Welcom {new_user.title()}.")
	else:
		print(f"Sorry {new_user}, you need to choose a new username.")

#print(current_users)
