### WATCH THE VIDEO TUTORIAL ON MY YOUTUBE CHANNEL
### https://youtu.be/7CujRmC0eWw

import random

password = ""
password_length = int(input("Enter the password length: "))
for i in range(password_length):
	password += chr(random.randint(33,126))
print(password)