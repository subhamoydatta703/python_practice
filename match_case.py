# same as switch case in c or java
x = 2

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:  #case _: means the “default case”
        print("Something else")
