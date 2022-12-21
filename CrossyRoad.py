'''
Andrew Habib
25 October 2021
Crossy Road
Crossy Road Classes
'''

# From the tkinter library import the following modules to aid in creating a Graphical User Interface
# These modules enable one to create objects that may be used to formulate enhanced and essential features to create a functioning interface
# Only Import PhotoImage to aid in creating image objects that may be manipulated for visual aid for the user
from tkinter import PhotoImage, Canvas

# From the PIL library, import Image and ImageTk for more options related to manipulating imagery
# Contains greater facilities that are not included in PhotoImage to help adjust image dimensions
from PIL import Image, ImageTk

# Import options for enumerations to enable symbolic meaningful constants
from enum import Enum

# From the tkinter library import the following modules to aid in creating a Graphical User Interface
# These modules enable one to create objects that may be used to formulate enhanced and essential features to create a functioning interface
from tkinter import Canvas

# Create a class that makes assigning directions more intuitive
class Direction(Enum):
    """Direction class with enumerations

    Args:
        Enum (Enum): Options enabling symbolic names to represent unique constant Values
    """

    # Assign the UP constant value to 0 resembling moving upwards
    UP = 0
    # Assign the DOWN constant value to 1 resembling moving downwards
    DOWN = 1
    # Assign the LEFT constant value to 2 resembling moving left
    LEFT = 2
    # Assign the RIGHT constant value to 3 resembling moving right
    RIGHT = 3

# Create a class for the vehicle
class Vehicle:

    def __init__(self, canvas):
        """Creates a Vehicle object (constructor) with the specified canvas 


        Args:
            canvas (Canvas): The Graphical User Interface Canvas
        """
        # Declare a private class variable that will store the canvas that the user passes as a parameter into the constructor
        self.__canvas = canvas
        # Declare and initialize a private class variable that will store the loaded image of the car - This is the variable that may handle dimension alterations
        # Initialized to the first car facing east
        self.__loadedCarImg = Image.open('sprites/car1East.png')
        # Declare a private class variable that uses the processed image to create a PhotoImage object that could be displayed to the user when needed
        self.__imgCar = ImageTk.PhotoImage(self.__loadedCarImg)
        # Declare a private class variable that stores the x position of the vehicle defaulted to 0 pixels
        self.__xpos = 0
        # Declare a private class variable that stores the y position of the vehicle defaulted to 0 pixels
        self.__ypos = 0
        # Declare a private class variable that stores the width of the image retrieved above (vehicle image)
        self.__width = self.__loadedCarImg.size[0]
        # Declare a private class variable that stores the height of the image retrieved above (vehicle image)
        self.__height = self.__loadedCarImg.size[1]
        # Declare a private class variable that stores the direction of the vehicle using the Enum class created above
        self.__direction = Direction.RIGHT
        # Declare and initialize a private class variable that will store the created image that will be placed on the canvas - initialized to None
        self.__imgOutputCar = None

    def get_Height(self):
        """Returns the height of the Vehicle

        Returns:
            int: The height of the vehicle
        """
        return self.__height

    def get_Image(self):
        """Draws the car image on a user's canvas while setting its positional properties and stores it within a variable
        Returns the image of the vehicle
        """
        self.__imgOutputCar = self.__canvas.create_image(self.__xpos, self.__ypos, image=self.__imgCar, anchor='n')

    def get_Direction(self):
        """Returns the direction of the vehicle

        Returns:
            Direction: The direction of the vehicle
        """
        return self.__direction

    def get_Location(self):
        """Returns the X and Y positions of the vehicle

        Returns:
            tuple: The X and Y positions of the vehicle
        """
        return (self.__xpos, self.__ypos)
    
    def get_Width(self):
        """Returns the width of the vehicle

        Returns:
            int: The width of the vehicle
        """
        return self.__width

    def get_Height(self):
        """Returns the height of the vehicle

        Returns:
            int: The height of the vehicle
        """
        return self.__height

    def get_Dimensions(self):
        """Returns the dimensions of the vehicle

        Returns:
            tuple: The dimensions of the vehicle
        """
        return (self.__width, self.__height)

    def getX(self):
        """Returns the X position of the vehicle

        Returns:
            int: The X position of the vehicle
        """
        return self.__xpos

    def getY(self):
        """Returns the Y position of the vehicle

        Returns:
            int: The Y position of the vehicle
        """
        return self.__ypos

    def get_left_Border(self):
        """Returns the X position of the left side of the vehicle image (Left Border)

        Returns:
            int: The X position of the left side of the vehicle image (Left Border)
        """
        return self.__canvas.bbox(self.__imgOutputCar)[0]

    def get_right_Border(self):
        """Returns the X position of the right side of the vehicle image (Right Border)

        Returns:
            int: The X position of the right side of the vehicle image (Right Border)
        """
        return self.__canvas.bbox(self.__imgOutputCar)[2]      
    
    def get_top_Border(self):
        """Returns the Y position of the top side of the vehicle image (Top Border)

        Returns:
            int: The Y position of the top side of the vehicle image (Top Border)
        """
        return self.__canvas.bbox(self.__imgOutputCar)[1]
    
    def get_bottom_Border(self):
        """Returns the Y position of the bottom side of the vehicle image (Bottom Border)

        Returns:
            int: The Y position of the bottom side of the vehicle image (Bottom Border)
        """
        return self.__canvas.bbox(self.__imgOutputCar)[3]

    def set_Image(self, img="sprites/car1East.png", direction=Direction.RIGHT):
        """Sets the image of the vehicle along with the default direction

        Args:
            img (str, optional): The image of the vehicle. Defaults to "sprites/car1East.png".
            direction (Direction, optional): The direction of the vehicle. Defaults to Direction.RIGHT.
        """
        # Assign the string containing the image file that must be loaded to the private class variable that will take in loaded images
        self.__loadedCarImg = Image.open(img)
        # Update the PhotoImage object that will contain the image to be displayed with the new loaded image
        self.__imgCar = ImageTk.PhotoImage(self.__loadedCarImg)
        # Update and configure the canvas with the new car image
        self.__canvas.itemconfig(self.__imgOutputCar, image=self.__imgCar)
        # Set the direction of the car to the direction parameter passed
        self.__direction = direction

    def set_Width(self, width):
        """Sets the width of the vehicle and updates the canvas with the vehicle's new dimensions

        Args:
            width (int): The width of the vehicle
        """
        self.__width = width
        # Resize loaded car image with the new dimensions set by the user (width)
        self.__loadedCarImg = self.__loadedCarImg.resize((self.__width, self.__height), Image.ANTIALIAS)
        # Update the PhotoImage object that will contain the image to be displayed with the newly sized loaded image
        self.__imgCar = ImageTk.PhotoImage(self.__loadedCarImg)
        # Update and configure the canvas with the newly sized car image
        self.__canvas.itemconfig(self.__imgOutputCar, image=self.__imgCar)

    def set_Height(self, height):
        """Sets the height of the vehicle and updates the canvas with the vehicle's new dimensions

        Args:
            height (int): The height of the vehicle
        """
        self.__height = height
        # Resize loaded car image with the new dimensions set by the user (height)
        self.__loadedCarImg = self.__loadedCarImg.resize((self.__width, self.__height), Image.ANTIALIAS)
        # Update the PhotoImage object that will contain the image to be displayed with the newly sized loaded image
        self.__imgCar = ImageTk.PhotoImage(self.__loadedCarImg)
        # Update and configure the canvas with the newly sized car image
        self.__canvas.itemconfig(self.__imgOutputCar, image=self.__imgCar)

    def set_Dimensions(self, dimensions):
        """Sets the dimensions (width and height) of the vehicle and updates the canvas with the vehicle's new dimensions

        Args:
            dimensions (tuple): The dimensions (width and height) of the vehicle
        """
        self.__width = dimensions[0]
        self.__height = dimensions[1]
        # Resize loaded car image with the new dimensions set by the user
        self.__loadedCarImg = self.__loadedCarImg.resize((self.__width, self.__height), Image.ANTIALIAS)
        # Update the PhotoImage object that will contain the image to be displayed with the newly sized loaded image
        self.__imgCar = ImageTk.PhotoImage(self.__loadedCarImg)
        # Update and configure the canvas with the newly sized car image
        self.__canvas.itemconfig(self.__imgOutputCar, image=self.__imgCar)

    def set_Location(self, location):
        """Sets the location (X and Y positions) of the vehicle and updates the canvas with the vehicle's new location

        Args:
            location (tuple): The location (X and Y positions) of the vehicle
        """
        self.__xpos = location[0]
        self.__ypos = location[1]
        # Check if the output car image storing the canvas drawn image is equivalent to none --> An image has actually been drawn
        if self.__imgOutputCar != None:
            # Update the vehicle with its new location with the newly set x and y positions
            self.__canvas.coords(self.__imgOutputCar, self.__xpos, self.__ypos)

    def setX(self, x):
        """Sets the X position of the vehicle and updates the canvas with the vehicle's new location

        Args:
            x (int): The X position of the vehicle
        """
        self.__xpos = x
        # Check if the output car image storing the canvas drawn image is equivalent to none --> An image has actually been drawn
        if self.__imgOutputCar != None:
            # Update the vehicle with its new location with the newly set x and y positions
            self.__canvas.coords(self.__imgOutputCar, self.__xpos, self.__ypos)
    
    def setY(self, y):
        """Sets the Y position of the vehicle and updates the canvas with the vehicle's new location

        Args:
            y (int): The Y position of the vehicle
        """
        self.__ypos = y

        # Check if the output car image storing the canvas drawn image is equivalent to none --> An image has actually been drawn
        if self.__imgOutputCar != None:
            # Update the vehicle with its new location with the newly set x and y positions
            self.__canvas.coords(self.__imgOutputCar, self.__xpos, self.__ypos)

    def set_Direction(self, direction):
        """Sets the direction of vehicle

        Args:
            direction (Direction): The direction of the vehicle
        """
        self.__direction = direction

    def move(self, pixels):
        """Moves the vehicle by a certain number of pixels

        Args:
            pixels (int): Number of pixels that the vehicle will move
        """
        self.__carSpeed = pixels
        # Check if the current direction is equivalent to right
        if self.__direction == Direction.RIGHT:
            # Increment the x position by the car speed set by the user above
            self.__xpos = self.__xpos + self.__carSpeed
        
        # If not, check if the current direction is equivalent to left
        elif self.__direction == Direction.LEFT:
            # Decrement the x position by the car speed set by the user above
            self.__xpos = self.__xpos - self.__carSpeed

        # If not, check if the current direction is equivalent to up
        elif self.__direction == Direction.UP:
            # Increment the y position by the car speed set by the user above
            self.__ypos = self.__ypos + self.__carSpeed 
        
        # If not, check if the current direction is equivalent to down
        elif self.__direction == Direction.DOWN:
            # Decrement the y position by the car speed set by the user above
            self.__ypos = self.__ypos - self.__carSpeed

        # Update the vehicle with its new location with the newly set x and y positions 
        self.__canvas.coords(self.__imgOutputCar, self.__xpos, self.__ypos)

class Chicken:
    def __init__(self, canvas):
        """Creates a Chicken object (constructor) with the specified canva

        Args:
            canvas (Canvas): The Graphical User Interface Canvas
        """
        # Declare a private class variable that will store the canvas that the user passes as a parameter into the constructor
        self.__canvas = canvas
        # Declare and initialize a private class variable that will store the loaded image of the chicken
        self.__loadedChickenImg = Image.open('sprites/chicken.png')
        # Declare a private class variable that uses the processed image to create a PhotoImage object that could be displayed to the user when needed
        self.__imgChicken = ImageTk.PhotoImage(self.__loadedChickenImg)
        # Declare and initialize a private class variable that will store the loaded image of the dead chicken 
        self.__loadedDeadImg = Image.open('sprites/dead_chicken.png')
        # Declare a private class variable that uses the processed image to create a PhotoImage object that could be displayed to the user when needed
        self.__imgDead = ImageTk.PhotoImage(self.__loadedDeadImg)
        # Declare and initialize a private class variable that will store the loaded image of the chicken (either alive or dead depending on the chicken's current state set)
        # Currently alive
        self.__loadedCurrentImg = self.__loadedChickenImg
        # Declare a private class variable that uses the processed image to create a PhotoImage object that could be displayed to the user when needed
        self.__imgCurrent = self.__imgChicken
        # Declare a private class variable that stores the width of the image retrieved above (current chicken image)
        self.__width = self.__loadedCurrentImg.size[0]
        # Declare a private class variable that stores the height of the image retrieved above (current chicken image)
        self.__height = self.__loadedChickenImg.size[1]
        # Declare a private class variable that stores the x position of the chicken defaulted to 0 pixels
        self.__xpos = 0
        # Declare a private class variable that stores the y position of the chicken defaulted to 0 pixels
        self.__ypos = 0
        # Declare and initialize a private class variable that stores the state of the chicken (dead or alive boolean)
        self.__dead = False
        # Declare and initialize a private class variable that stores the current image drawn onto the canvas - Initialized to None until image is retrieved
        self.__currentImgOutput = None
        
    def get_Width(self):
        """Returns the width of the Chicken

        Returns:
            int: The width of the Chicken
        """
        return self.__width

    def get_Height(self):
        """Returns the height of the Chicken

        Returns:
            int: The height of the Chicken
        """
        return self.__height

    def get_Image(self):
        """Draws the chicken image on a user's canvas while setting its positional properties and stores it within a variable
        Returns the Image of the Chicken
        """
        self.__currentImgOutput = self.__canvas.create_image(self.__xpos, self.__ypos, image=self.__imgCurrent, anchor='n')

    def get_Location(self):
        """Returns the location of the chicken (X and Y positions)

        Returns:
            tuple: The location of the Chicken (X and Y positions)
        """
        return (self.__xpos, self.__ypos)

    def getX(self):
        """Returns the X position of the chicken (X position)

        Returns:
            int: The X position of the chicken (X position)
        """
        return self.__xpos

    def getY(self):
        """Returns the Y position of the chicken (Y position)

        Returns:
            int: The Y position of the chicken (Y position)
        """
        return self.__ypos

    def get_left_Border(self):
        """Returns the X position of the left side of the chicken image (Left Border) 

        Returns:
            int: The X position of the left side of the chicken image (Left Border) 
        """
        return self.__canvas.bbox(self.__currentImgOutput)[0]

    def get_right_Border(self):
        """Returns the X position of the right side of the chicken image (Right Border)

        Returns:
            int: The X position of the right side of the chicken image (Right Border)
        """
        return self.__canvas.bbox(self.__currentImgOutput)[2]      
    
    def get_top_Border(self):
        """Returns the Y position of the top side of the chicken image (Top Border)

        Returns:
            int: The Y position of the top side of the chicken image (Top Border)
        """
        return self.__canvas.bbox(self.__currentImgOutput)[1]
    
    def get_bottom_Border(self):
        """Returns the Y position of the bottom side of the chicken image (Bottom Border)

        Returns:
            int: The Y position of the bottom side of the chicken image (Bottom Border)
        """
        return self.__canvas.bbox(self.__currentImgOutput)[3]

    def set_Width(self, width):
        """Sets the width of the chicken and updates the canvas with the chicken's new dimensions

        Args:
            width (int): The width of the chicken
        """
        self.__width = width
        # Resize loaded current chicken image with the new dimensions set by the user (width)
        self.__loadedCurrentImg = self.__loadedCurrentImg.resize((self.__width, self.__height), Image.ANTIALIAS)
        # Update the PhotoImage object that will contain the image to be displayed with the newly sized loaded image
        self.__imgCurrent = ImageTk.PhotoImage(self.__loadedCurrentImg)
        # Update and configure the canvas with the newly sized car image
        self.__canvas.itemconfig(self.__currentImgOutput, image=self.__imgCurrent)

    def set_Height(self, height):
        """Sets the height of the chicken and updates the canvas with the chicken's new dimensions.

        Args:
            height (int): The height of the chicken
        """
        self.__height = height
        # Resize loaded car image with the new dimensions set by the user (height)
        self.__loadedCurrentImg = self.__loadedCurrentImg.resize((self.__width, self.__height), Image.ANTIALIAS)
        # Update the PhotoImage object that will contain the image to be displayed with the newly sized loaded image
        self.__imgCurrent = ImageTk.PhotoImage(self.__loadedCurrentImg)
        # Update and configure the canvas with the newly sized car image
        self.__canvas.itemconfig(self.__currentImgOutput, image=self.__imgCurrent)

    def set_Dimensions(self, dimensions):
        """Sets the dimensions (width and height) of the chicken and updates the canvas with the chicken's new dimensions

        Args:
            dimensions (tuple): The dimensions (width and height) of the chicken
        """
        self.__width = dimensions[0]
        self.__height = dimensions[1]
        # Resize loaded car image with the new dimensions set by the user
        self.__loadedCurrentImg = self.__loadedCurrentImg.resize((self.__width, self.__height), Image.ANTIALIAS)
        # Update the PhotoImage object that will contain the image to be displayed with the newly sized loaded image
        self.__imgCurrent = ImageTk.PhotoImage(self.__loadedCurrentImg)
        # Update and configure the canvas with the newly sized car image
        self.__canvas.itemconfig(self.__currentImgOutput, image=self.__imgCurrent)

    def setX(self, x):
        """Sets the X position of the chicken and updates the canvas with the chicken's new location

        Args:
            x (int): The X position of the chicken
        """
        self.__xpos = x
        # Check if the output current chicken image storing the canvas drawn image is equivalent to none --> An image has actually been drawn
        if self.__currentImgOutput != None:
            self.__canvas.coords(self.__currentImgOutput, self.__xpos, self.__ypos)
    
    def setY(self, y):
        """Sets the Y position of the chicken and updates the canvas with the chicken's new location

        Args:
            y (int): The Y position of the chicken
        """
        self.__ypos = y
        # Check if the output current chicken image storing the canvas drawn image is equivalent to none --> An image has actually been drawn
        if self.__currentImgOutput != None:
            self.__canvas.coords(self.__currentImgOutput, self.__xpos, self.__ypos)

    def set_Location(self, location):
        """Sets the location (X and Y positions) of the chicken and updates the canvas with the chicken's new location

        Args:
            location (tuple): The location (X and Y positions) of the chicken
        """
        self.__xpos = location[0]
        self.__ypos = location[1]
        # Check if the output current chicken image storing the canvas drawn image is equivalent to none --> An image has actually been drawn
        if self.__currentImgOutput != None:
            self.__canvas.coords(self.__currentImgOutput, self.__xpos, self.__ypos)
    
    

    def move(self, direction=Direction.UP, pixels=1):
        """Moves the chicken by a specified number of pixels and in a specified direction

        Args:
            direction (Direction, optional): The direction of the chicken. Defaults to Direction.UP.
            pixels (int, optional): The number of pixels the chicken will move. Defaults to 1.
        """
        # Check if the direction passed by the user is equivalent to up
        if direction == Direction.UP:
            # Decrement the y position by the number of pixels passed 
            self.__ypos = self.__ypos - pixels

        # If not, check if the direction passed by the user is equivalent to down
        elif direction == Direction.DOWN:
            # Increment the y position by the number of pixels passed 
            self.__ypos = self.__ypos + pixels
        
        # If not, check if the direction passed by the user is equivalent to left
        elif direction == Direction.LEFT:
            # Decrement the x position by the number of pixels passed
            self.__xpos = self.__xpos - pixels

        # If not, check if the direction passed by the user is equivalent to right
        elif direction == Direction.RIGHT:
            # Increment the x position by the number of pixels passed
            self.__xpos = self.__xpos + pixels
        
        # Update the chicken with the the newly set x and y positions
        self.__canvas.coords(self.__currentImgOutput, self.__xpos, self.__ypos)

    def kill_Chicken(self):
        """Kills the chicken or sets the image of the current chicken image to its dead image and updates the canvas with the updated current image
        """
        # Set the current image to the image of the dead chicken
        self.__imgCurrent = self.__imgDead
        # Update and configure the canvas with the updated current image
        self.__canvas.itemconfig(self.__currentImgOutput, image=self.__imgCurrent)
        # Set the boolean dead variable to true
        self.__dead = True
    
    def isdead(self):
        """Returns a boolean determining whether the chicken is dead or not

        Returns:
            bool: Chicken's current state (Dead or Alive)
        """
        return self.__dead

    def reset(self):
        """Resets the state of the chicken to alive or sets the image of the current chicken image to its alive image and updates the canvas with the updated current image
        """
        # Reset the current image to the image of the alive chicken
        self.__imgCurrent = self.__imgChicken
        # Update and configure the canvas with the updated current image
        self.__canvas.itemconfig(self.__currentImgOutput, image=self.__imgCurrent)
        # Set the boolean dead variable to false
        self.__dead = False