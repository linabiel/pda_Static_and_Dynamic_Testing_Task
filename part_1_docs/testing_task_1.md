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

# value is not defined anywhere. Python will throw an error. should add value as a parameter, unless it is defined in the class Card
  def check_for_ace(self, card):
    # wrong syntax for a comparison operator: should be ==. python will throw an indentation error
    if card.value = 1:
      return True
  # semicolon is mising after else, python will throw an indentation error
    else
      return False
   

  # spelling mistake - dif should be def, python won't recognise the word and won't run the function
  # missing comma after card1
  dif highest_card(self, card1 card2):
  # the whole if statemnet needs to be indented
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# value is not defined anywhere. Python will throw an error. should add value as a parameter, unless it is defined in the class Card
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
