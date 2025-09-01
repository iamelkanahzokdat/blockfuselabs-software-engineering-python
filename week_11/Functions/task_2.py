def myCustomPrint(*args):
    print(*args, "\n", args)   


myCustomPrint("Hello World")
print("Hello World")


def specifyTodoList(**kwargs):
   for todo, value in kwargs.items():
      print(f"{todo} '--->', {value}")    
      #print(kwargs, "\n", *kwargs)


specifyTodoList(code = "learn python", lunch = "rice and beans", sleep = "8 hours")