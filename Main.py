'''
Andrew Habib
25 October 2021
Crossy Road Program
Main Program
'''

# From the tkinter library import the following modules to aid in creating a Graphical User Interface
# These modules enable one to create objects that may be used to formulate enhanced and essential features to create a functioning interface
from tkinter import Tk, PhotoImage, Canvas, messagebox

# Andrew's Crossy Road Game Components library that contains options to create and manipulate a chicken along with a vehicle which are essential objects within the game
from CrossyRoad import Vehicle, Chicken, Direction

# Import a module that adds more options for creating randomizing objects not included in python
import random

# Import pygame to introduce some more options to create a graphical user interface --> Only to be used for any audio related features
import pygame

# Define a function that will be responsible for initializing basic game objects, variables, lists and other components whenever the game starts, during the game when new levels occur, and if the user would like to play again
def initializeObjects():

	# Declare the following variables, lists, and other components as global variables
	# They may be now accessed and manipulated within this function to re-initialize them whenever needed
	global listCarImgs, listCarObjects, listCarObjectSpeedsPixels, myChicken, timerID, numChickenSpacesMoved, speedChickenPixels, timerSpeed, tree_list

	# Re-initialize the following variables and lists 
	# These are the variables and lists that have to be reset in any circumstance including: restarting the game, going to the next level, and beginning the game (Apply in all senarios)
	# These are not all the variables and lists within the program (See main program for detail on each variable and list) - Only the ones that apply to all 3 cases listed above
	numChickenSpacesMoved = 0
	listCarImgs = []
	listCarObjects = []
	listCarObjectSpeedsPixels = []
	tree_list = []
	myChicken = None

	# Test print function
	print(speedChickenPixels, timerSpeed)

	# Declare a 2 Dimensional tuple consisting of the coordinates of each of the tree images within the game - Each tree's x and y positions 
	tree_coords = ((65, 145), (320, 145), (400, 145), (20, 465), (120, 465), (350, 465))

	# Using a counted for loop iterate 9 times (From 1 to 10) and keep track of each iteration number
	for counter in range(1, 10):

		# Append or add every file name storing a car with a specific colour --> Add the west and the east cars ranging from 1 - 10 --> See files
		listCarImgs.append("sprites/car" + str(counter) + "East.png")
		listCarImgs.append("sprites/car" + str(counter) + "West.png")

		# Using a counted for loop execute the code below in 2 iterations
		for iterations in range(2):

			# Append or add to the list of car speeds in pixels a random integer ranging from the variable storing the speed of the chicken within the current level to the that same variable added to 3
			# This list ensures that random cars within the same level will have varying speeds
			listCarObjectSpeedsPixels.append(random.randint(speedChickenPixels, speedChickenPixels + 3))
	
	# Using the random function, shuffle the list of car image files so that each random car has a random colour and direction
	random.shuffle(listCarImgs)

	# Using a counted for loop, iterate through every image car file string value within the list of car image files and keep track of the index number using the enumeration function
	for index, imgCar in enumerate(listCarImgs):

		# Append or add to the list of car objects a new vehicle object using the Crossy Road module created by Andrew Habib and pass the program's canvas object to be able to draw the vehicle in later code
		listCarObjects.append(Vehicle(canvas))	

		# Set the image of the car object at the current index within the list of car objects to the list of car image files created above at the current enumeration index
		listCarObjects[index].set_Image(listCarImgs[index])
		
		# Set the dimensions of the current car object to a width of 80 pixels and a height of 35 pixels
		listCarObjects[index].set_Dimensions((80, 35))

		# Set the X position of current car object to a random integer ranging between 1 and the background image's width in pixels 
		# The background takes up the full screen so to keep the game more interesting, a randomized starting location could make the cars even more randomized and the game more dynamic 
		# Ensures that each car has completely random positions
		listCarObjects[index].setX(random.randint(1, imgBackground.width()))

		# Using the following mathematical algorithm, Set the Y position of current car object to 685 (below the lowest lane) and subtract that value by the current index multiplied by 40
		# This ensures that the car will be placed in its lane in accordance to its position in the overall list so that each car occupies its own lane (each lane is around )
		listCarObjects[index].setY(685 - index * 40)

		# Check if the list of car image files at the current index from the 12th to 16th characters within that string is equivalent to "West" - Car facing west image
		if (listCarImgs[index])[12:16] == "West":
			
			# Set the direction of the current car object to the Left Direction Enum
			listCarObjects[index].set_Direction(Direction.LEFT)

		# If not, check if the list of car image files at the current index from the 12th to 16th characters within that string is equivalent to "East" - Car facing east image
		elif (listCarImgs[index])[12:16] == "East":

			# Set the direction of the current car object to the right direction Enum
			listCarObjects[index].set_Direction(Direction.RIGHT)

	# Using a counted for loop, iterate through the cars within the list of car objects and keep track of the index using the enumeration function
	for index, car in enumerate(listCarObjects):

		# Check if the index is not equivalen to 0, 4, 12 and is less than 16
		# This condition ensures that cars are not placed on grassy lands or non-road areas since the y positions set above do not account for these gaps 
		if index != 0 and index != 4 and index != 12 and index < 16:

			# Get and display onto the canvas the image of the current car object onto the canvas
			car.get_Image()

	# Store in a variable the timer object that will store after how many seconds a function should execute (Handle delaying events within the car timer function)
	# After the amount of time assigned to the timerSpeed variable make call to the function that will handle continuously moving the car in increments
	timerID = canvas.after(timerSpeed, car_timer)
	
	# Assign the chicken variable a new chicken object using the Crossy Road module created by Andrew Habib and pass the program's canvas object to draw the chicken in later code
	myChicken = Chicken(canvas)

	# Set and update the dimensions of the chicken object to 30x35 (30 width and 35 height)
	myChicken.set_Dimensions((30, 35))

	# Set and update the location of the chicken object to the background image width by 685 (below the first lane - default starting position)
	myChicken.set_Location((imgBackground.width() // 2, 685))

	# Get and display onto the canvas the image of the chicken object onto the canvas
	myChicken.get_Image()

	# Using a counted for loop, iterate 6 times while executing the code below
	for i in range(6):

		# Draw onto the canvas an image of each tree object along with their corresponding coordinates based on the tuple declared above
		canvas.create_image(tree_coords[i][0], tree_coords[i][1], image=imgTree, anchor='nw')

# Define a function that will be responsible for keeping the cars moving using a timer and checking for collision
def car_timer():

	# Declare the following variables, lists, and other components as global variables
	# They may be now accessed and manipulated within this function to re-initialize them whenever needed
	global listCarObjectSpeedsPixels, timerSpeed, speedChickenPixels, level, score, soundEffectChickenDeath

	# Using a counted for loop, iterate through the cars within the list of car objects and keep track of the index using the enumeration function
	for index, car in enumerate(listCarObjects):

		# Check if the index is not equivalen to 0, 4, 12 and is less than 16
		# This condition ensures that cars are not placed on grassy lands or non-road areas since the y positions set above do not account for these gaps 
		if index != 0 and index != 4 and index != 12 and index < 16:

			# Move the current car object by the number of pixels in its corresponding index within the list of speeds in pixels --> Varying speeds within 1 level
			listCarObjects[index].move(pixels=listCarObjectSpeedsPixels[index])

			# Check if the current car is going right and its left border is greater than or equal to the background width --> Goes off Screen to the right
			if listCarObjects[index].get_Direction() == Direction.RIGHT and listCarObjects[index].get_left_Border() >= imgBackground.width():

				# Set the current car's X position to 0 pixels take away half of its own width to account for centered anchoring - Car reappears at the left of the screen
				listCarObjects[index].setX(0 - listCarObjects[index].get_Width() // 2)

			# If not, check if the current car is going left and its right border is less than or equal to 0 --> Goes off screen to the left
			elif listCarObjects[index].get_Direction() == Direction.LEFT and listCarObjects[index].get_right_Border() <= 0:

				# Set the current car's X position to the width of background in addition to half of the car's width to account for centered anchoring - Car reappears at the right of the screen
				listCarObjects[index].setX(imgBackground.width() + listCarObjects[index].get_Width() // 2)
			
			# Collision detection --> Checking if the chicken gets run over by a vehicle --> Leave Add and subtract 5 pixels from the borders to ensure a full collision 
			# Check if the right border of the chicken is greater than the left border of the vehicle object at the current index of the list and the left border of the chicken is less than the right border of the current vehicle (Collision along the x axis)
			if myChicken.get_right_Border() > listCarObjects[index].get_left_Border() + 5 and myChicken.get_left_Border() < listCarObjects[index].get_right_Border() - 5:
				# Check if the top border of the chicken is less than the bottom border of the vehicle object at the current index of the list and the bottom border of the chicken is greater than the top border of the current vehicle (Collision along the y axis)
				if myChicken.get_top_Border() < listCarObjects[index].get_bottom_Border() - 5 and myChicken.get_bottom_Border() > listCarObjects[index].get_top_Border() + 5:
					
					# Kill the chicken by updating its image to the image of a dead chicken and assigning its dead value within the class to true
					myChicken.kill_Chicken()

					# Play a pygame mixer sound effect that would compliment the dying of the chicken when it gets run over by a vehicle
					pygame.mixer.Sound.play(soundEffectChickenDeath)

	# Check if the chicken is not dead (Class function determining the state of the chicken) --> Chicken dead is equivalent to true
	if myChicken.isdead() == False:

		# After the amount of time assigned to the timerSpeed variable make call to the function that will handle continuously moving the car in increments
		# The cars must continue moving so the function is called again until the chicken is dead in which case all the cars must stop
		canvas.after(timerSpeed, car_timer)
	
	# If not, check if the chicken is dead (Class function determining the state of the chicken) --> Chicken dead is equivalent to false
	elif myChicken.isdead() == True:
		
		# Cancel the variable storing the timer for the car as the chicken is dead and there is no need for the cars to keep moving
		canvas.after_cancel(timerID)

		# In a variable, store the user's response when they are told that they died and if they would like to play again (Store the boolean value)
		playAgainAskUser = messagebox.askyesno("Game Over", 
			"You died with " + str(score) + " points at level " + str(level) + "!\nWould you like to play again?")

		# Check if the user would like to play again or the variable storing the user's response to play again is equivalent to true
		if playAgainAskUser == True:

			# Re-initialize the score, level, timer, speeds, the chicken's state and call the function that re-initializes all main variables, lists, objects and other components
			# Restore the state of the game as if the user has just entered the game
			score = 0
			level = 1
			timerSpeed = 25
			speedChickenPixels = 1
			myChicken.reset()
			canvas.itemconfig(level_output, text='{:<10s}{:d}'.format('LEVEL:', level))
			canvas.itemconfig(score_output, text='{:<10s}{:d}'.format('SCORE:', score))	
			initializeObjects()

		# If not, check if the user does not want to play again the variable storing their response is equivalent to False
		elif playAgainAskUser == False:

			# Display a messagebox for the user thanking them for playing the game
			messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road!")

			# Terminate the program
			exit()

# Define a function that will handle the events that occur when certain keys on the keyboard are pressed
def performActionOnKeyboardPress(event):

	# Declare the following variables, lists, and other components as global variables
	# They may be now accessed and manipulated within this function to re-initialize them whenever needed
	global score, level, numChickenSpacesMoved, timerID, timerSpeed, speedChickenPixels

	# Check if the key being pressed is the character key "w" or the key being pressed is the "up" key
	if event.char == "w" or event.keysym == "Up":

		# Move the chicken upwards by increment of 40 pixels
		myChicken.move(direction=Direction.UP, pixels=40)

		# Increment the integer variable storing the number of spaces that the chicken moved
		numChickenSpacesMoved = numChickenSpacesMoved + 1
		
		# Check if the number of spaces that the chicken moved is not equivalent to 4, 12 and less than 16 (Chicken does not get points for going on the grassy lands)
		if numChickenSpacesMoved != 4 and numChickenSpacesMoved != 12 and numChickenSpacesMoved < 16:

			# Increment the integer variable storing the score by 1
			score = score + 1
	
	# If not, check if the key being pressed is the character key "d" or the key being pressed is the "down" key
	elif (event.char == "s" or event.keysym == "Down") and myChicken.getY() < 685:

		# Move the chicken downwards by increment of 40 pixels
		myChicken.move(direction=Direction.DOWN, pixels=40)

		# Decrement the integer varible storing the number of spaces that the chicken moved 
		numChickenSpacesMoved = numChickenSpacesMoved - 1

		# Check if the number of spaces that the chicken moved is not equal to 3 and 11 (Chicken does not lose points for getting off grassy lands since they did not gain the points to begin with)
		if numChickenSpacesMoved != 3 and numChickenSpacesMoved != 11:

			# Decrement the integer varible storing the score by 1
			score = score - 1

	# Check if the number of spaces that the chicken moved is greater than or equal to 16 (Reached the top and passed all cars of the level)
	if numChickenSpacesMoved >= 16:

		# Increment the integer varible storing the level by 1 to move onto the next level
		level = level + 1

		# Check if the timer speed is not less than or equal to 2 (Timer has reached near its lowest value)
		if not timerSpeed <= 2:

			# Decrement the timerspeed variable by 8
			timerSpeed = timerSpeed - 8

		# Otherwise, execute the code below
		else:

			# Increment the speed of the chickens in pixels by 1
			speedChickenPixels = speedChickenPixels + 1

		# Make a call to the function that re-initializes the main variables, lists and other components 
		initializeObjects()

		# Cancel the variable storing the timer for the car as the chicken is dead and there is no need for the cars to keep moving
		canvas.after_cancel(timerID)

	# Update and configure the canvas by changing the drawn level and score texts to the updated and formatted level and score based on the current status of the game
	canvas.itemconfig(level_output, text='{:<10s}{:d}'.format('LEVEL:', level))
	canvas.itemconfig(score_output, text='{:<10s}{:d}'.format('SCORE:', score))	

# Define a function that will close the program when the user clicks the close button at the top right of the screen or the exit button
def terminate_program():

    # Prompt the user through a messagebox verifying whether they would like to exit for sure
    # Store the yes or no answer in the following variable
    user_response = messagebox.askyesno("Crossy Road", 
        "Are you sure you want to exit?")

    # If the user's response is "yes", this indicates that the variable is equal to the boolean value of True in which case the code below will execute
    if user_response == True: 

		# Display a messagebox for the user thanking them for playing the game
        messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road!")

		# Terminate the program
        exit()

# Declare two integer variables that will store the user's current level and their current score - First level and score of Zero since they have not played yet
score, level = 0, 1

# Declare an initialize an integer variable that will store the number of spaces that the chicken has moved
numChickenSpacesMoved = 0

# Declare and initialize an integer variable that will store the speed of the cars that the users will have to curcumvent
# This is the first and easiest car speed of the game that will take place at level 1 but the timer will be decremented with every level to increase the gradually increase the difficulty of the game
# First, the timer will decrement to speed up the cars making it harder for users to pass the cars and survive until the timer reaches a number close to 0 in which case the variable below comes into play
timerSpeed = 25

# Declare and initialize an integer variable that will be used in the functions above to handle the speed of the chicken in pixels
# As the levels progress after the timer reaches its lowest point (number close to 0), this variable will be used to increment the number of pixels the cars travel so that the game keeps getting more difficult even if the timer runs out
speedChickenPixels = 1

# Declare and initialize an empty list that will eventually store all of the image file names of the cars so that the program may display them when appropriate
listCarImgs = []

# Declare and initialize an empty list that will eventually store all of the car objects that the user must not hit as they cross the road
listCarObjects = []

# Declare and initialize an empty list that will eventually store all of the randomly generated speeds of the cars on the road within each level
# Although with each level the cars must increase speed, the group of cars within one level should have varying speeds hence the purpose of this list
listCarObjectSpeedsPixels = []

# Declare and intialize an empty list that will store all of the decoration tree objects --> They will have no impact within the game function but will serve as asthetic
tree_list = []

# Declare a variable initialized to None that will store the chicken object that the user must navigate within the game and try to win each level with (User's character)
myChicken = None

# Create a Tk window that will display all objects for the graphical user interface
root = Tk()

# Set the name of the title of the Tk Window on the top left corner to "Crossy Road" (Name of the program)
root.title('Crossy Road')

# Call the function that terminates the program when the top right x button is clicked
root.protocol('WM_DELETE_WINDOW', terminate_program)

# Formulate keybindings for the user to interact with the game chicken by moving it
# The general program will listen for "KEY PRESSES" and will call the following function and conditional statements will be executed depending on the key being pressed
root.bind("<KeyPress>", performActionOnKeyboardPress)

# Initialize the pygame mixer which will be used as a music playing object
pygame.mixer.init()
    
# Load the mp3 audio file in pygame mixer to get the program to recognize the music file we want playing in the background
pygame.mixer.music.load("audio/J.Geco - Chicken Song.mp3")
    
# Play the loaded mp3 audio file indefinitely (Will not stop playing unless instructed to do so later in the program)
pygame.mixer.music.play(-1)

# Declare a variable to store the sound effect for the chicken dying when getting run over by the car
soundEffectChickenDeath = pygame.mixer.Sound("audio/You are dead sound effect.wav")

# Create a PhotoImage object that contains the image file of the main screen background image
imgBackground = PhotoImage(file='sprites/main_screen_final.png')

# Create a PhotoImage object that contains the image file of the tree images
imgTree = PhotoImage(file='sprites/tree.png')

# Set the size and location of the Tk window using the contants declared above and formatting techniques
# The following properties ensure that the window is centered based on the dimensions of itself and the user's screen 
root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2,
	root.winfo_screenheight() // 2 - imgBackground.height() // 2))

# Test print function
print(imgBackground.width(), imgBackground.height())
# Create a canvas object that will enable the programmer to add components on to the interface and draw other objects - Replicate the dimensions of the background image (imgBackground)
canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
# Output the canvas
canvas.pack()

# Create an image by drawing an image a stored image file of the variable storing the background image for the game and set its positional properties
canvas.create_image(0, 0, image=imgBackground, anchor='nw')

# Store in variable text that has been drawn onto the canvas at the bottom right corner depicting the score and the current level of the user as they play and set the positional and asthetic properties of these formatted statistical displays
score_output = canvas.create_text(canvas.winfo_reqwidth() - 160, canvas.winfo_reqheight() - 40, text='{:<10s}{:d}'.format('SCORE:', score), font=('Britannic Bold', 18), fill='#565656', anchor='w')
level_output = canvas.create_text(20, canvas.winfo_reqheight() - 40, text='{:<10s}{:d}'.format('LEVEL:', level), font=('Britannic Bold', 18), fill='#565656', anchor='w')

# Make a call to the function that will initialize all game variables, lists, objects and all other necessary components required to commence a fresh new game 
initializeObjects()

# Main loop will listen for events triggered by the user and keep the program running
root.mainloop()