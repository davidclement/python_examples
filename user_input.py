
#----------------------------------------
# standard get input
#----------------------------------------
input = raw_input("question? ")

#----------------------------------------
# read in password
#----------------------------------------
from getpass import getpass
password = getpass()         # default prompt
password = getpass("pwd: ")  # custom prompt



#----------------------------------------
# a class for yes/no choices
#----------------------------------------
class YesNoChoice:
  '''
  note that self.yes and self.no will cause
  attribute error prior to the answer being
  successfully chosen.  This enforces that
  these can only be tested after self.parseChoice
  is successfully run.  Test for that with boolean
  self.chosen
  '''
  def __init__(self):
    self.chosen = False
  def parseChoice(self,choice):
    if choice.lower() in ['y','yes','yep','yeah']:
      self.chosen = True
      self.yes = True
      self.no = False
    elif choice.lower() in ['n','no','nope']:
      self.chosen = True
      self.yes = False
      self.no = True