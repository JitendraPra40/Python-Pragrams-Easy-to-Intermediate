def emailslicer(email):
    username, domain = email.split("@")
    return username, domain
email = input("Enter your email address: ")
print(emailslicer(email))
