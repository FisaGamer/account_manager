from useraccount import login
from itertools import chain, product

def changestr(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

def bruteforce(username):
  liste = list(changestr("fisagamerFISAGAMER", 5))
  for i in range(len(liste)):
    if login(username, liste[i]):
      return liste[i]