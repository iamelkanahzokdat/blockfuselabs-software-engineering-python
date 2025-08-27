#quiz in python

questions = ("1. True + True = ?", "2. True + False = ?", "3. bool + str = ?", "4. integer + float = ?", "5. Dict + Dict = ?")

options = (("A. True", "B. False", "C. Error", "D. 0"),
           ("A. False", "B. TypeError", "C. True", "D. 4"),
           ("A. TypeError", "B. bool", "C. str", "D. int"),
           ("A. int", "B. bool", "C. Float", "D. str"),
           ("A. tuple", "B. dict", "C. list", "D. Error"))

answers = ("A", "C", "A", "C", "D")
guesses = []
score = 0
option_index = 0


for question in questions:
   print(questions)

   for option in options[option_index]:
      print(option)

   guess = input("select option(A,B,C,D)").upper()
   guesses.append(guess)

   if guess == answers[option_index]:
      print("CORRECT")
      score += 1
   else:
      print("INCORRECT")
      print(f"{answers[option_index]} is the correct option!")
