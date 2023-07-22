#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value= value

  @property
  def value(self, value):
    return self._value

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value= new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value.endswith(".")
  def is_question(self):
    return self._value.endswith("?")
  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
      # replace_questionmark= self._value.replace("?",".")
      # replace_ex=replace_questionmark.replace("!",".")
      # split_value=replace_ex.split(".")
      # no_empty_string=" ".join(split_value).split()
      # return len(no_empty_string)
    value=self._value
    for punc in ["!","?"] :
      value=value.replace(punc,".")
      print(value)
    sentences=[s for s in value.split(".") if s]
    return len(sentences)


  



