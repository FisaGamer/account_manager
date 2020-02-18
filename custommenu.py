import useraccount as ua
from cursesmenu import *
from cursesmenu.items import *


def launchmenu():
  menu = CursesMenu("Member manager", "Choose an option")
  add_user = FunctionItem("Add a user", input, ["What's the new account username?\n"])
  menu.append_item(add_user)
  menu.show()


def menu():
  try:
    launchmenu()
  except:
    return False


#curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
#os.system('clear')
