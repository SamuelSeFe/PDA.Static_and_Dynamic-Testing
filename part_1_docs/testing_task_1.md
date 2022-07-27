### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# the card.value should have be " == 1: " rather than " = 1: "
# the 'else' should have a colon afterwards, " else: "
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
# 'dif' should be spelled with " def " instead
# there should be a comma after 'card1' --> " card1, "
# the 'return card' should be " return card1 "
# both the 'if' and 'else' statements should be indented


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
# 'total' just after the function declaration is not assigned to any value so it will not do anything
# because 'total' is not assigned a value the line 'total += card.value' will not do anything
# the whole function needs to be indented by one space
# 'return' needs to be un-indented, meaning it should not be inside the 'for' loop
# last line has the wrong syntax for concatenation as you cannot concatenate a string and an integer

```
