import random

words=["deleterious","abdicate","sagacity","aberration","superfluous","jubilation","mundane","orator", "disdain", "brusque", "bombastic", "verbose", "loquacious", "forbearance", "ephemeral", "hackneyed", "florid", "spurious", "transient", "manifesto", "precocious", "rancorous", "querulous", "longevity", "lobbyist", "venerable", "aardvark", ":)"]
goal_word=random.choice(words)
blank_list=[]
for letter in goal_word:
  blank_list+=["_"]

lives=7
while lives >0 and "_" in blank_list:
  print (blank_list)
  print("Lives: " + str(lives))
  guess=input("Guess a letter: ")
  if guess==goal_word:
    break
  elif guess in goal_word:
    print("YAY! Good Job You guessed correctly!")
    index=0
    for letter in goal_word:
      if guess==letter or guess==letter.upper():
        blank_list[index]=letter
      index+=1
  else:
    print("Try again")
    lives-=1

if lives>0:
  print("Yay You Won, you guessed all the letters correctly!.")
  result="successfully"
else:
  print ("You lost! But you can always try again")
  result="unsuccessfully"
print("You {} guessed the word {}!".format(result,goal_word))
