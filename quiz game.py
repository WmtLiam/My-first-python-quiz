print("hello and welcome to my quiz")


playing = input("Do you want to play it?" )

if playing != "yes":
    quit()

print("oh ok then join me IN THIS ADVENTURE and remember NO CAPS or else you will be booted!")

anwser = input("what does tdlr stand for? ")

if anwser == "tldr":
    print("correct now remember if you get things wrong you will get booted by the game now")
else:
    print("bye bye")
    quit()

anwser = input("What are the digits of Pi? ")

if anwser == "3.14":
    print("good job only 2/5 to go")
else:
    print("bye bye")
    quit()

anwser = input("When was ww2 started? ")

if anwser == "1939":
    print("good job only 3/5 to go")
else:
    print("bye bye")
    quit()

anwser = input("are you happy? ")

if anwser == "yes":
    print("thanks happy for your feedback")
else:
    print("screw you")
    quit()

anwser = input("what is 2+2? ")

if anwser == "fish":
    print("Nice 5/5 good job and see you next time you will be booted from this game")
    quit()
    
else:
    print("YOU FAIL ON THE LAST ONE WHAT YOU IDIOT")
    quit()
