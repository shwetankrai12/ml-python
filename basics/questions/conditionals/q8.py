password = "shwetank@12"

size = len(password)

if size < 6:
    status = "Weak"
elif size < 10:
    status = "medium"
else:
    status = "strong"

print("Your password is: ",status)