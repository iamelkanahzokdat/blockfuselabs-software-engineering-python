'''person = {"name": "Joseph",
          "age": 40,
          "isMarried": True,
          "likes": ["Eating", "sleeping", "making money"],
          "height": 6.7
         }


if "name" in person.keys():
   print(person["name"])
else:
   print("None")

print(person.keys())
print(person.items())
'''



users = { "Dre": {"status": True},
          "Mark": {"status": False},
          "Mimi": {"status": False},
        }

keywords = {
        "Football": "A sport that involves a total of 22 players",
        "Grape": "A fruit that is purple with seeds",
        "Money": "A currency that makes the world go round."
          } 

name = input("Enter your name: \n ")

if name in users:
   if users[name]["status"]:
      keyword = input("Enter your word: \n")
      if keyword in keywords:
         print(f"Meaning:", keywords[keyword])
      else:
         print("word not found")
   else:
      print("user is not a student")
else:
    print("user not found")
 




