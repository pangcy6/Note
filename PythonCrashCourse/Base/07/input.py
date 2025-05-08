name = input("""
If you tell us who you are, we can personalize the message you see.
What's your name? """)

# 凡是涉及用户输入都要做防御性编程的准备
print(f"\nHello, {name.strip().title()}!")
