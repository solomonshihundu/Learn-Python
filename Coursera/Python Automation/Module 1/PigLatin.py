def pig_latin(text):
  say = ""
  new_words = []
  # Separate the text into words
  words = text.split()

  for word in words:
    # Create the pig latin word and add it to the list
    first_char = word[0]
    index = word.index(first_char)
    say = word[1:] + first_char + "ay"
    new_words.append(say)
    # Turn the list back into a phrase
  return " ".join(str(x) for x in new_words)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"