secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_num = int(input())
while user_num:
    print("Ha ha! You're stuck in my loop!")
    user_num = int(input())
    
print("Well done, muggle! You are free now.")
