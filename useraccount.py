import hashlib as h

def login(username, password):
  with open("logins.txt", "r") as f:
    for line in f:
      if line.startswith(username + " , "):
        password_encrypted_infile = line.split(" , ")[1]
        result = h.md5(str.encode(password))
        if password_encrypted_infile == str(result.digest()):
          return True
    return False

def change_password(username, password, newpassword):
  with open("logins.txt", "r") as f:
    users = f.read()
    users = users.split("\n")
    for i in range(len(users)):
      if users[i].startswith(username):
        user_data = users[i].split(" , ")
        password_encrypted_infile = user_data[1]
        result = h.md5(str.encode(password))
        if password_encrypted_infile == str(result.digest()):
          result = h.md5(str.encode(newpassword))
          user_data[1] = str(result.digest())
          users[i] = " , ".join(user_data)
          auth = True
          break
      auth = False
  if auth:
    with open("logins.txt", "w") as f:
      for user in users:
        f.write(user + "\n")
      return True
  return False

def add_user(username, password, confirm_password, email):
  with open("logins.txt", "a") as f:
    if password == confirm_password:
      password_encrypted = h.md5(str.encode(password))
      f.write(username + " , " + str(password_encrypted.digest()) + " , " + email + "\n")
      return True
    return False

def user_info(username):
  with open("logins.txt", "r") as f:
    for line in f:
      if line.startswith(username):
        line = line.split(" , ")
    return("Username : {}\nPassword : {}".format(line[0], line[2]))

def remove_user(username):
  with open("logins.txt", "r") as f:
    users = f.read()
    users = users.split("\n")
    for i in range(len(users)):
      if users[i].startswith(username + " , "):
        nthline = i
  if "nthline" in locals():
    with open("logins.txt", "w") as f:
      users.pop(nthline)
      for user in users:
        f.write(user + "\n")
      return True
  else:
    return False