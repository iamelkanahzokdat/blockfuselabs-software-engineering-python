contacts = {
       "Dre": "09138890925",
       "Mimi": "08032568018",
       "TK": "043004988494",
       "Julius": "07094950400",
       "Ajor": "09038340300",
       "Bankat": "09048594500",
       "Dimka": "04056785400",
       "Bamshak": "07090960089",
       "Jaz": "0704066705678",
       "Hillary": "080609606500",
}

print(len(contacts), type(contacts))
print(contacts["Mimi"])
print(contacts)





trial = {
     True: "True",
     False: "False",
     4: "One",
     4.0: "One Zero",
     (1,2): "One comma Zero"
}

print(trial)
print(trial[False])



trial = {"scores": (1,2)}
one, two = trial["scores"]
print(one, two)



#contacts.update
#contacts.popitem
#contacts.pop


laptop = {
       "Dorcas": ["a", "z", "c", "d"],
       "Dan": ["a", "b"],
       "Ben": ["X", 8, "r"],
}

laptop["Dorcas"] += "b"
laptop["Dan"] += "Z"
laptop["Ben"] += "D"

print(laptop)


cart = {}

Dan = cart
Dre = cart
Jibrin = cart
print(id(cart))

Dan.update({"milkshake": 1})  
Dre.update({"coca cola": 2})
Jibrin.update({"red bulls": 2}) 

print(cart)

cart.clear()
