dag = input("schrijf een dag van de week:")
a = 2
while a < 3:
    if dag == "mandag":
        print("mandag")
        break
    elif dag == "dinsdag":
        print("mandag", "dinsdag")
        break
    elif dag == "wonesdag":
        print("mandag", "dinsdag", "wonesdag")
        break
    elif dag == "donderdag":
        print("mandag", "dinsdag", "wonesdag", "donderdag")
        break
    elif dag == "vrijdag":
        print("mandag", "dinsdag", "wonesdag", "donderdag", "vrijdag")
        break
    elif dag ==  "zaterdag":
        print("mandag", "dinsdag", "wonesdag", "donderdag", "vrijdag", "zaterdag")
        break
    elif dag == "zondag":
        print("mandag", "dinsdag", "wonesdag", "donderdag", "vrijdag", "zaterdag", "zondag")
        break
    else:
        print("schrif het nog een keer")
        break
      