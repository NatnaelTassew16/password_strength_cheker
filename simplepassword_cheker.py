print("""---------------------------------------------
	             PASSWORD CREATION PAGE
	        ----------------------------------------------
	""")
#asking for user to enter there passowrd
password = input("Please inter your password on the box: ")
#cheking for password length
if len(password) < 8:
	print("your password is too short")
#cheking how many alphabet does they use in ther password at list 3
aphabetchecker = sum(1 for apha in password if apha.isalpha())
if aphabetchecker < 2:
	print("please use morethan 2 alphabet on your password")
#chekig how many digit does they use in thire passowrd at list 4
isdigit = sum(1 for digit in password if digit.isdigit())
if isdigit < 3:
	print("please use morethan 3 number on your password ") 
#cheking how many special character does they use in there password at lsit 3
special_char = sum(1 for char in password if not char.isalnum() and not char.isspace())
if special_char < 2:
	print("please use at least one more characher")
#running the final out put if they write correctly 
else:
	print("YOUR PASSWORD IS TOO STRONG : ",password.replace(" ","-"))
	print("working")
