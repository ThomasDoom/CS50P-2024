from validators import email

if email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")
