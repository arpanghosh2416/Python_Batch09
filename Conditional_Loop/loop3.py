day = 7

match day:
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")



    

# _ represents default value holder, and its trigger when no match case gets executed, then only case _ gets executed.


day = 4

match day:
    case 4|5|6:
        print("Today is Working Days")
    case 7|8:
        print("Today is Weekends off")
    case _:
        print("Looking forward to the Weekend")




# if statement as checkpoints


month = 6

day = 4

match day:
    case 1|2|3|4|5|6 if month == 6:
        print("Today is Working Days1")
    case _:
        print("Looking forward to the Weekend")
