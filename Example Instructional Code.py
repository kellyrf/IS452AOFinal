# To start, these are comments! Be sure to explain that "hashtags"/pound key is used to make comments in code that doesn't
# run as actual code, and act as a way to  make notes in your code.



# Open workshop with this video as context: https://www.youtube.com/watch?v=o0u4M6vppCI 

# # Before you begin:
# - review this content carefully and make any necessary modifications for yourself and your instructional style.
# - though this guide documents the entire teaching process, be sure to stop for participant questions, ask important questions
#   throughout as you see fit, and modify the story used as you deem fit for your audience.
# - this is meant to be a guide to the workshop, but not an exact script. Take liberties with the story you create, and allow 
#   for student input to guide the workshop, since it is created for their benefit.
# - The code in this is chunked purposefully to be run together. Be sure to comment out anything you don't want to deal with
#   as the lesson progresses.
# - Remember to note throughout that syntax and semantics matter, keep your code as simple as possible (with one idea per line),
#   and errors are your friend.



######################## Openning the Integrated Development Environment (IDE) ########################

# Prompt all to follow along to the steps provided on the main projected screen.
# Open up the program PyCharm Edu.
# On the welcome screen, click Create New Project.
# Name the project in the location as "ChoiceYourOwnAdventure_[LastName]", with participants inserting
# their last name. If participants have same last name, prompt them to add first name as well.



######################## Creating a Program ########################

# After the project loads, have them right click the file with their label under the project bar, select New,
# and select Python file. 
# Have them name the file "CYOAProgram_[LastName]", with same naming instructions.



######################## Printing a String ########################

# To begin a program, you have to type something. All great programers start somewhere, so we're going to start with "Hello".
# In order to see the results of any program, you often need to print your output. Click inside of the type box loaded with the new 
# program.
# Achieve your first line of code with:
print("Hello World")
# Type this exactly. Use double quotes.
# Run the program with the small green triangle. 

# In this statement, the function 'print()' is passing the literal string "Hello World".
# In programming, a sentence that you would see printed out is considered a string, which is a fancy
# way of saying a line of characters.
# A function does exactly as it says - it creates something in code that "functions." It gets SOMETHING done.
# When you run the program, you will get 
"Hello World"

# This also works with single quotes (' ') and triple quotes (""" """), when you print an item as so: 
print ('Hello World')
print ("""Hello 
World""")

# Single quotes are helpful if you need to print an item with quotations in it, like:
print ('Hello, do you need to "emphasize" this word?')

# and triple quotes are helpful if you need to print an item that spans multiple lines, and you want to maintain the new lines:
print ("""Alexander Hamilton
My name is Alexander Hamilton
And there's a million things I haven't done
But just you wait, just you wait""")

# You can use print(<parameter>) function to print a number of things for a program.
# They don't necessarily have to be words, they can be any character you can type out on a keyboard.
# However, whatever you print in the quotes, is exactly what you get out of the quotes. Examples:
print("Gibb3rish")
print("3+2")
# print('you're walking in the woods...&&%$#')

# the last print statement doesn't work, and we got an error - can you tell me why?
# (After answer received) Yes - if we look at the error message, there is a problem with syntax, which means how something
# was typed. The error tells you where you are wrong and why it is wrong. 
# We can see that the apostrophe makes an argument, and the computer is confused for it.
# So we fix it by using double quotes, so that it does not think that the print statement ended halfway through, and 
# we have useless junk in our code.
print("you're walking in the woods...&&%$#")



######################## Variables ########################

# When you have a string, sometimes you need to give it a name to call it back, as you might need it later.
# To do this, you can make the string a variable. Variables are like in math - the variable x represents
# some sort of number in math, and you can make x equal a specific number to get a result you want.
x = 3
print(x)

# You can do the same with a string. If you have a super long string (or short string you need more than once), 
# you can make it equal a variable.
inthewoods = """You’re walking in the woods, there is no one around, and your phone is dead. Out of the corner of your eye 
you spot him. Its:"""

# As you can see, inthewoods is a pretty long string that takes multiple lines, and you don't want to type that out every time
# you want to have it print. 
# You'll see later that it would make the code look really crowded if we stuck in the entire string for the program.
# So, to avoid that struggle, we set it equal to the name 'inthewoods' and pass that through the print() function.
print(inthewoods)

# Notice that it prints the content of inthewoods, but not the variable name "inthewoods". 
# This is because you're essentially plug and chugging - you're plugging in a value for the variable, like plugging in the
# coordinates to find the slope of a line (y=mx+b).
# Python does the work for you, because it already knows that inthewoods equals your string, so it just prints the string 
# you want via the variable.

##### Prompt for questions so far #####



######################## Prompt for input ########################

# Let's start a story where you can make a choice about what happens next.
# We'll make a few variables, and equate them to the strings we want to print.
inthewoods = """You’re walking in the woods, there is no one around, and your phone is dead. Out of the corner of your eye 
you spot him. Its:"""
choiceA = "A. Shia Labeouf"
choiceB = "B. An adorable cat"

# When you make a program, you may want information from the person who is using the program, like this story.
# For our purposes, we want to get the user prompts to know what kind of story they want - a weird or innocent one.
# In a choose your own adventure story, you have options to make the story yours. 
# Ours won't be as complex as the memorable books from childhood or Black Mirror: Bandersnatch, but will give simple prompts to choose
# a different story for each choice.
# To do this, we need to prompt for an input, where the user interacts with the program by inputing content.
print(inthewoods)
print(choiceA)
print(choiceB)
			
# That was a lot of typing, and there might be any easier way to do that, which we'll get to later.
firstanswer = input("Who is it? Type choiceA or choiceB ")
			
# the input function allows for a user to answer whatever prompt is in the input with some sort of typing, and the 
# program will respond based on what is typed by running the input somehow.
# We're prompting the user here to type in the exact terms, so that the program will recognize that we need one of those 
# answers.
# Later, we'll talk about how to use that answer to move to the next prompt. 
print(firstanswer)

# Let's unpack this. 
# We first printed all of our variables that we need for the story to start, along with the options. 
# However, it seems like there might be an easier way to do this.
# We also have an input option, but users have to type out the whole choice in order to prompt the program. 
# How can we clean this up to make it easier to move forward?
# Let's try keeping most of it under one variable. 
inthewoods = """You’re walking in the woods, there is no one around, and your phone is dead. Out of the corner of your eye 
you spot him. Its:
A. Shia Labeouf
B. An adorable cat"""

# We use the triple quotes so that it will hold the format of printing a new line each time we do. 
# This is where the variable comes in handy, because again, we don't want to make the code crowded.
# This is also helpful because like earlier, we use a colon, and need to make sure that doesn't effect our code
print(inthewoods)     
answer0 = input("Your choice (a/b): ")      
      
# Now, what do we do with that input? We have somewhere to start the story.      
# # Break for lunch and questions      

	   
	   
######################## If/Else Statements ########################

# You may have talked about in math using if statements. 
# Whether you did or did not doesn't provide much advantage, so no worries to those who didn't.
# An if statement provides a way of having options in a program, where whatever input is received may then lead the program 
# to make certain choices so as to continue in a specific direction. 

# Take this example:
input("type a whole number above 0: ")
if x == 2: # we are asking a question about a variable, known as x.
	print ("yes, it is 2!") # if the answer matches, then the output is the printed string
else: # if it does not fit,
	print ("that is not 2") #then the output says so

# Here, we have code that splits off in two directions. If the data lines up one way, it runs that part of the code only.
# If it doesn't, it runs the other part only. 
# This is super helpful if we need to make different choices, or tell a story that can change based on what the user says!
# you can ask different questions with your if statement, and extend it out with more ifs. 
# Once its done, if you need to wrap up the choices the code can make, use an else - if the user gives anything else, the else
# catches it and can say "that doesn't match any of the if statements, so we can't run that. Try again."
# This isn't the only way you can use if/else statements, but it will be how we introduce it in this workshop.

# Now let's see our story continue:
Meow1 = """The adorable cat walks up to you and sits on a large leaf. The cat gives you an inquisitive look, and meows. You:
A. kneel and reach out cautiously for the cat to sniff you
B. step back, because you are intensely allergic to cats""" 

Shia1 = """He's following you, about thirty feet back. He get's down on all fours and breaks into a 
sprint. He's gaining on you. You try to go back to the parking lot and find your car, but you're all turned
around. You:
A. Run for your life
B. Decide to fight back"""

print(inthewoods)     
answer0 = (input("Your choice (a/b): ")  

if answer0 == "a": 
# here, you are starting with the if statement - if the answer by the user is an a, being if answer0 == a, then the following 
# occurs:
	print(Shia1) # good thing we're avoiding a whole chunk of string right here! It would look gross.
	answershia1 = input("What do you do? (a/b): ")
elif answer0 == "b":
# elif is just a fancy way of saying "else/if" because we don't just want to say "else" here, because we have another parameter
# we want to ask about.
	print(Meow1)
	answermeow1 = input("what do you do? (a/b): ")

	   
# To make the next step, the information has to be within the if statement, per an indent. This is so the code knows that 
# everything whatever follows the statements in the indent, has to run first before moving on to the next step.	   
# Prompt for questions so far

	   
	   
######################## Functions ########################
# When writing a program, sometimes appearance does matter for your work. 
# Not only does it help you visually, but it can also make it easier to spot errors in your code, or rework certain items. 	   
# If we were to continue with the code, we would have indent after indent of code, like:
if <variable> == <variable>:
	print(<string>)
	answerstring = input("word things: ")
	if <variable> == <variable>:
		print(<string>)
	   	answerstring = input("word things: ")
	   	if <variable> == <variable>:
	   		print(<string>)
	   		answerstring = input("word things: ")
if <variable> == <variable>:
	print(<string>)
	answerstring = input("word things: ")
	if <variable> == <variable>:
		print(<string>)
	   	answerstring = input("word things: ")
	   	if <variable> == <variable>:
			print(<string>)
	   		answerstring = input("word things: ")

# While we can follow this pretty easily, if we want a longer story for each option, it's going to get crowded. 
# We can avoid this by creating a function! Like print() or input(), we can make our own function that runs certain steps 
# when we call it. The earlier this is introduced, the easier it is to set up a clean program to run.
# Since there is more than one story line, we may want to set up a function for each story.
# Where do you think we should start?

def ShiaStory(): 
	# Under here, we can put all of the strings we need for the story, and the code it will use. 	   
	# def <func>() means we are 'defining' a function, which we do by giving it code to follow through. 
	# I would recommend mapping out the stories with the variables used to keep track. The code will help track, but you
	# don't want to miss an input choice if you change the story.
	# Please note that the following story has some gore and violence. Note your audience and use discression.
	Shia1 = """He's following you, about thirty feet back. He get's down on all fours and breaks into a 
	sprint. He's gaining on you. You try to go back to the parking lot and find your car, but you're all turned
	around. You:
	A. Run for your life
	B. Decide to fight back"""

	Shia1A = """You spot a small cottage with a light on, and suddenly have hope. You begin creeping through
	the underbrush but your leg! Ah! It's caught in a bear trap!
	A. Attempt to gnaw your leg off
	B. Drag the trap with you towards the cottage"""

	Shia1B = """He's brandishing a knife, but you have a sword on you. The battle begins. He parries to the left, and
	dodges your swipes. You counter to the right and stab him in the kidney. You:
	A. Run after stabbing him in the kidney
	B. Ask him "Shia, why me?" """
	   
	Shia1AA = """You have gnawed your leg off successfully, but now blood is oozing from your stump leg. You quietly fight
	the pain as you find your way back to your car, not trusting the cottage. You unlock it and climb in, grabbing the 
	sweater from your passenger seat to make a tourniquet to stop the bleeding. You're lightheaded. You:
	A. turn your car on and plug your phone in
	B. turn your car on and try to drive away"""
	
	Shia1AB = """You make it to the cottage and see Shia sitting inside, sharpening an axe. You sneak up behind him, but he
	hears the clatter of the bear trap just as you get your hands around his neck. Shia surprise! He tries to turn to you, but 
	you can do Jis Jitsu and bodyslam him down, knocking him out. You:
	A. Tie him up and go plug your phone in to the wall socket with the charger you conveniently have in your pocket
	B. Take the axe and finish him"""
	
	Shia1BA = """You note the positioning of the stars and recall that your car was parked in the south parking lot.
	You run through the woods, and make it back to your car, jump in, and drive away. You can't believe that happened, and
	as you hit the gas, you suddenly drive off a cliff, and wake up."""
	
	Shia1BB = """Shia says "its because you've grown too powerful", and he's right. You use your powers to fly off,
	leaving him to the woods. You return to your home by flight, knowing this is not the last time you will see Shia
	Labeouf."""	   
	
	Shia1AAA = """Unsure if Shia chased after you, you quickly dial 911. You state your emergency, and the police arrive
	minutes later, because they've been after Shia Labeouf for quite some time. They swat the woods, but he's nowhere to be found.
	Will this be the last of Shia Labeouf? You do not know."""
	
	Shia1AAB = """As you drive off, you can't shake the feeling that you're being followed. You look in your rearview mirror,
	and you see Shia jogging after you, but watch as he drops to all fours again and bounds towards your vehicle. As you look 
	back to the road and accelerate, the idea comes to you to reverse. You quickly hit your brakes and reverse, and Shia
	is taken by surprise, flattened by your vehicle. You have defeated Shia Labeouf."""
	
	Shia1ABA = """You boot up your phone and begin an Instagram live stream for your thousands of followers, revealing
	that you have captured Shia Labeouf and his tyranny is over. You get several comments and likes, and the authorities
	use your video to pin your location and take away Shia Labeouf. As he awakens, he is dragged off, but he's staring
	back at you, smiling. Is it over? You don't know."""   
	
	Shia1ABB = """You have just decapitated Shia Labeouf. His head topples to the floor, expressionless. You fall to your
	knees and catch your breath. You're finally safe from Shia Labeouf."""
	
	whatdo = "what do you do? (a/b): "
	   
	print (Shia1)
	answer0 = input(whatdo)
	if answer0 == "a":
		print(Shia1A)
		answer1 = input(whatdo)
		if answer1 == "a":
			print(Shia1AA)
			answer1A = input(whatdo)
			if answer1A == "a":
				print(Shia1AAA)
			elif answer1A == "b":
				print(Shia1AAB)
		elif answer1 =="b":
			print(Shia1AB)
			answer1B = input(whatdo)
			if answer1B == "a":
				print(Shia1ABA)
			elif answer1B == "b":
				print(Shia1ABB)
	elif answer0 == "b":
		print(Shia1B)
		answer2 = input(whatdo)
		if answer2 == "a":
			print(Shia1BA)
		elif answer2 == "b":
			print(Shia1BB)
	else:
		print("You may have answered in a way the story didn't understand. Run again.")
	   

def MeowStory():
######################## Running a Program ########################
