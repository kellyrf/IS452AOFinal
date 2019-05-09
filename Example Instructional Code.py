# ######################## Printing a String ########################
#
# # In order to see the results of a program, you often need to print your output.
# # This can be achieved by:
#
# print("Hello World")
#
# # In this statement, the function 'print()' is passing the literal string "Hello World".
# # When you run the program, you will get "Hello World"
#
# # You can use print(<parameter>) to print a number of things for a program.
# # In programming, a sentence that you would see printed out is considered a string, which is a fancy
# # way of saying a line of characters.
# # They don't necessarily have to be words, they can be any character you can type out on a keyboard.
# # However, whatever you print in the quotes, is exactly what you get out of the quotes.
#
# #### Example ####
#
# print("Gibb3rish")
# print("3+2")
# print("you're walking in the woods...&&%$#")
#
#
#
#
# ######################## Variables ########################
#
# # When you have a string, sometimes you need to give it a name to call it back, as you might need it later.
# # To do this, you can make the string a variable. Variables are like in math - the variable x represents
# # some sort of number in math, and you can make x equal a specific number to get a result you want.
# x = 3
# print(x)
#
# # You can do the same with a string. If you have a super long string, you can make it equal a variable.
#
# inthewoods = "You’re walking in the woods, there is no one around, and your phone is dead. Out of the corner of your eye you spot him. Its:"
#
# # As you can see, inthewoods is a pretty long string, and you don't want to type that out every time
# # you want to have it print. So, to avoid that struggle, we set it equal to the name 'inthewoods' and
# # pass that through the print() function.
#
# print(inthewoods)
#
# # Notice that it prints the content of inthewoods, but not the term "inthewoods". This is because you're
# # essentially plug and chugging - you're plugging in a value for the variable, like plugging in the
# # coordinates to find the slope of a line (y=mx+b).
# # Python does the work for you, because it already knows that inthewoods equals your string.
#
# ##### Prompt for questions so far #####
#





######################## Prompt for input ########################

# This will be important to our story!
inthewoods = "You’re walking in the woods, there is no one around, and your phone is dead. Out of the corner of your eye you spot him. Its:"
startchoices = "\nA. Shia Labeouf \nB. An adorable cat \nC. Your cousin, Jim"

# When you make a program, you may want information from the person who is using the program.
# For our purposes, we want to get the user prompts to know what kind of story they want.
# In a choose your own adventure story, you have options to make the story yours. Ours won't be as complex as
# the memorable books from childhood or Black Mirror: Bandersnatch, but will give simple prompts to choose
# a different story for each choice.

# To do this, we need to prompt for an input, where the user interacts with the program by inputing content.
print(inthewoods+startchoices)
firstanswer = input("Who is it? Copy the exact name of who you see: ")

print(firstanswer)

# Let's unpack this. 


######################## If/Else Statements ########################



######################## Functions ########################



######################## Running a Program ########################
