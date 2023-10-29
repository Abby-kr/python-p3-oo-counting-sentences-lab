#!/usr/bin/env python3
import re

class MyString:
    def __init__(self,value = "" ):
      self._value = value

    def get_value(self):
      return self._value
  
    def set_value(self,item):
      if isinstance(item, str):
          self._value = item
      else:
          print("The value must be a string.")

    value = property(get_value, set_value )

    def is_sentence(self):
       x = self.value
       y = x.rfind(".")
       if y == (len(self.value) - 1):
          return True
       else:
          return False

    def is_question(self):
       x = self.value
       y = x.rfind("?")
       if y == (len(self.value) - 1):
          return True
       else:
          return False 

    def is_exclamation(self):
       x = self.value
       y = x.rfind("!")
       if y == (len(self.value) - 1):
          return True
       else:
          return False 
      
    def count_sentences(self):
      delimiters = r'[.!?]+[ ]*'
      sentences = re.findall(delimiters, self.value)

      return len(sentences)
