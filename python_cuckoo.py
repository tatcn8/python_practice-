# You're making a program for your coworkers that displays a message on their desktop's idle screen. Depending on the time of day, you want to print a different quote.

# You'll create a variable, time, which has an integer value between zero and 23, representing the hour of the day in military time, which is a 24-hour clock.

# Write a conditional statement with Python code that prints exactly one message using the following rules:

# If the time of day is before 9 a.m. --> print the quote 'Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.'

# Otherwise if the time of day is before or exactly 4 p.m. --> print the quote 'Working hard or hardly working?'

# Otherwise, if the time of day is before 8 p.m. --> print the quote 'How did it get so late so soon?'

# Otherwise if the time of day is before 10 p.m. --> print the quote 'A day without sunshine is like, you know, night.'

# Otherwise, for any time 10 p.m. or later --> print the quote 'Burning the midnight oil!'


time = 8

def cuckoo_clock(time):
    if(time <= 9): 
        print("Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day."),
    elif(time <= 16): 
        print("Working hard or hardly working?"),
    elif(time < 20): 
        print("How did it get so late so soon?"),
    elif(time <= 22): 
        print("A day without sunshine is like, you know, night.")

# cuckoo_clock()


# The mighty Tyrannosaurus rex is the king of dinosaurs, and he does whatever he pleases. When he's hungry, he eats. When he's angry, he fights. When he's bored, he roars. When he's tired, he sleeps!

# Write a conditional statement that selects one of the following actions for T-Rex based on his current mood. T-Rex's actions are ordered by precedence:

# If T-Rex is angry, hungry, and bored he will eat the Triceratops.
# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
# Otherwise if T-Rex is tired, he goes to sleep.
# Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
# Otherwise if T-Rex is angry or bored, he roars.
# Otherwise T-Rex gives a toothy smile.

angry = True
bored = True
hungry = False
tired = False


def rex_mood():
    if(bored) and (angry) and (hungry):
        print("Eat Triceratops")
    elif(tired) and (hungry):
        print("Eat iguanadon")
    elif(tired):
        print("sleep")
    elif(angry) and (bored):
        print("fight velociraptor")
    elif(angry) or (bored):
        print("RAWR")
    else:
        print("toothy smile")

# rex_mood()




# You have a list of Disney characters and you want to find out if each of them contain i, o, or u in their names. Loop through each character in the list and print out the following:

# If the name contains a 'u', print out the name plus 'U are so Uniquely U!'
# Otherwise if the name contains an 'i', print out the name plus "I bet you're Impressively Intelligent!"
# Otherwise if the name contains an 'o', print out the name plus 'O My! How Original!'
# Otherwise, print the name plus "Ehh, a's and e's are so ordinary."

disney_characters = ['simba', 'ariel', 'pumba', 'flounder', 'nala', 'ursula', 'scar', 'flotsam', 'timon']

def name_contain(arr):
    for name in arr:
        if("u" in name): 
            print(name + ' U are so Uniquely U!'),
        elif("i" in name):
            print(name + " I bet you are Intelligent"),
        elif("o" in name):
            print(name + " O my, how Original")
        else:
            print(name + " ehh, e's and a's are so ordinary")

# name_contain(disney_characters)




# Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, but it's really old and kind of finicky. It cools the room by three degrees and shuts off, so you have to keep turning it back on until the temperature gets to where you want it to be. Seventy five sounds much more pleasant than 90, so that's what you're shooting for.

# While the temperature is greater than 75 degrees Fahrenheit, print 'The temperature is XX — crank the AC!', and subtract 3 degrees from the temperature.

# Once the temperature is cool enough and the loop is done, print '75. Ahh, that's better.'


temperature = 90

def thermostat(temperature):
    while temperature >= 75:
        print("Temperature is {} --crank the AC!".format(temperature))
        if temperature == 75:
            print("{}....ahh that's better.".format(temperature))
            break
        temperature -= 3



# thermostat(temperature)

