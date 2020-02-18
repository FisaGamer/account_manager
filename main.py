import useraccount as ua
import custommenu as cm
import getpass4 as g
import bruteforce as b

keepgoing = True

"""while keepgoing:
  user = input("Username:\n")
  pwd = g.getpass("Password\n", "*", False)
  if ua.login(user, pwd) == True:
    print("Succesfully logged into your account")
    print(ua.change_password("Fisa", "FisaGamer", "FisaG"))
  else:
    print("Unsuccessful login")
  keepgoing = False"""
  
print(b.bruteforce("Fisa"))
