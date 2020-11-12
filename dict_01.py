my_dict = {"собака":"dog",     "кот":"cat",
           "лиса":"fox",
"медведь":"bear",
           "слон":"elefant",
"слон":"ele",
           "слон":"elefa",
           "кенгуру":"kenguru",}


while (1):

 print("введите слово:")
 word = input()

 if word == "стоп":
     break

 if word in my_dict:
    print( my_dict[word] )
    print("")
 else:
    print("слово не найдено")
    print("")





