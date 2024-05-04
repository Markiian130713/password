import random

text = 'qwertyuioplkjhgfdsazxcvbnm0123456789'
password = ''
for i in range(16):
    password += random.choice(text)
print(password)