print ("Welcome to My English Quiz Game!!")
print ("You Need to Answer 15 Questions. Answer by using Past Perfect Tense!")

score = 0
playing = input ("Do you want to play? ")

if playing.lower() !=  "yes" :
    quit ()

print ("Okay! Let's Play :)")

answer = input ("She __________ her Delhi relatives once in 2002 before she moved in with them in 1999. ")
if answer == "had visited" :
    print ("Correct!")
    score +=1
else :
    print ("Incorrect!")

answer = input ("She __________ a bear before she moved to Japan. ")
if answer == "had never seen" :
    print ("Correct!")
    score +=1 
else :
    print ("Incorrect!")

answer = input ("I _________ such a beautiful beach before I went to New York. ")
if answer == "had never seen" :
    print ("Correct!")
    score +=1
else :
    print ("Incorrect!")

answer = input ("We ______ that car for ten years before it broke down. ")
if answer == "had had" :
    print ("Correct!")
    score +=1
else :
    print ("Incorrect!")

answer = input ("They felt bad about selling the house because they ________ it for more than forty years. ")
if answer == "had owned" :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("Kristine ________ to an opera before last night. ")
if answer == ("had never been") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("The poet __________ a romantic poem before he came to the program. ")
if answer == ("had written") :
    print ("Correct! You got +1 Score!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("We _________ an ice-cream before we left the ice-cream parlor. ")
if answer == ("had taken") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("We _________ a movie in that Cineplex before he came. ")
if answer == ("had watched") :
    print ("Correct!")
    score +=1
else :
    print ("Incorrect!")

answer = input ("I ________ to melodious songs before I started the work. ")
if answer == ("had listened") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("I __________ the cricket match on television before you came. ")
if answer == ("had not watched") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("Anthony _________ Ryan before you introduced him to us at the party. ")
if answer == ("had met") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("I ________ asleep before eight o'clock. ")
if answer == ("had fallen") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("The boss _________ it would be a long meeting. ")
if answer == ("had said") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

answer = input ("She wished she ______ her friend. ")
if answer == ("had seen") :
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")

print ("You got " + str(score) + " questions correct")
print ("You got " + str((score / 15) * 100) + " %.")

