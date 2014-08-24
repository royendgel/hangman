import random
print "welcome to hangman"


words = [
    "dein",
    "kanga",
    "skol",
    "kenia",
    "aisha",
    "shanty",
    "misha",
]

word = random.choice(words)
wordn = word
pword = ''

print "bo tin ku skohe un palabra di %s letter" %(len(word))
score = 0
end = False
while end is not True:
  print "Bo Score ta : %s \n" %(score)
  letter = raw_input("hinka un letter >")
  if letter.lower() in word.lower():
    word = word.strip(letter)
    pword = pword + letter
    score = score + 10
    if len(word) == 0:
      print "YESSSSS BA GANA E PALABRA KOREKTO TA %s" %(wordn.upper())
      end = True
    print "Hopi Bon"
  elif letter in pword:
    print "Bo tek e letter aki kaba !!!"
  else:
    score = score - 5
    print "purba atrobe, e no ta bon"
