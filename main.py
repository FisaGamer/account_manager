import useraccount as ua
import custommenu as cm
import getpass4 as g

keepgoing = True

while keepgoing:
  user = input("Username:\n")
  pwd = g.getpass("Password\n", "*", False)
  if ua.login(user, pwd) == True:
    print("Succesfully logged into your account")
    cm.menu()
  else:
    print("Unsuccessful login")
  keepgoing = False
