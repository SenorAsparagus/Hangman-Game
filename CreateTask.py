import tkinter as tk
import time
from tkinter import Button, Frame, Tk 
from tkinter import *
from tkinter import messagebox
import random as rand
from unicodedata import name
from doctest import master
import os
import sys

# First Window that displays a main menu screen displaying the games title, the rules of the game and asks the user for their name
class MyClass:
    
    def __init__(self, master):

        
        self.master = master
        
        self.frame = tk.Frame(self.master, width = 1520, height = 1080)
        self.frame.pack()

        self.Name = Label (self.master, text = "Enter your name to begin", font = ("comicsans"))
        self.Name.place( x = 650, y = 500)

        self.Rules = Label (self.master, text = "How to play", font = ("comicsans, 20"))
        self.Rules.place( x = 1180, y = 100)

        self.Rulebook = Label (self.master, text = "You will be given a category and a certain number of underlines on the screen. \nThe underlines represent the number of letters and/or spaces/hyphens in the given word. \n You must then guess the given word by using the alphabet provided,\n when you click a letter it will reveal all of that letter that is in the word, \n if there are none of that letter you will lose a life, once you have lost all five lives you lose, \n if you can guess the word by inputting all of its letters you win.", font = ("comicsans, 10"))
        self.Rulebook.place( x = 990, y = 200)

        self.Categories = Label (self.master, text = "Categories", font = ("comicsans, 20"))
        self.Categories.place( x = 200, y = 100)

        self.Categories = Label (self.master, text = Categories, font = ("comicsans, 10"))
        self.Categories.place( x = 85, y = 200)

        self.TitleCard = Label (self.master, text = "Welcome \nTo \nHangman", font = ("comicsans, 50"))
        self.TitleCard.place( x = 600, y = 100)

        #Create an Entry widget to accept User Input
        self.entry= Entry(self.master, width= 40)
        self.entry.focus_set()
        self.entry.place( x = 620, y = 550)

        self.button = Button(self.frame, text="Enter", command=self.func)
        self.button.place (x = 710, y = 600)

        # Binds the enter key to the function that accepts the username
        master.bind( '<Return>', lambda event: self.func())
    
    # Function that deletes the window and saves the user entry as soon as a name is inputted 
    def func(self):
        global entry
        global name 
        name = self.entry.get()
        print (name)
        root.destroy()

# CONFIG Variables
Square_variable = 125
Underscore_variable = 100
Lives = 5
LetterIndex = 0
count = -1

# CONFIG Lists 
alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "] 

Buttons = []

Underscores = []

Categories = ["Fruits", "Animals", "Space", "Veggies", "Mythical Creatures", "Star Wars"]

Veggies = ["Carrot", "Lettuce", "Asparagus", "Cauliflower", "Beat", "Radish"]

Space = ["Rocket", "Star", "Mercury", "Venus", "Milky Way", "Asteroid", "Kuiper Belt", 
"Big Dipper", "Alpha Centauri", "Jupiter", "Uranus", "Hubble Telescope", "Saturn V", "NASA", 
"Nebula", "Galaxy", "Andromeda Galaxy", "Black Hole", "Mars", "Pluto", "Neil Armstrong", "Buzz Aldrin", "Comet", "Meteor"]

Animals = ["Bear", 'Camel', "Cat", "dog", "Ostrich", "Penguin", "Sheep", "Goat"]

Fruits = ["Banana", "Apple", "Pear", "Grapefruit", "Orange", "Lime", "Lemon", "Strawberry", "Papaya"]

Mythical_Creatures = ["Yeti", "Centaur", "Satyr", "Unicorn", "Dragon", "Griffin", "Minotaur", 
"Cyclops", "Manticore", "Chimera", "Hydra", "Sphynx", "Gargoyle", "Werewolf", "Leprechaun", 'Basilisk', 
"Fairy", "Dryads", "Sirens","Zombie", "Vampire", "Dwarf", "Elfs", "Trolls", 'Goblins', "Godzilla", "King Kong"]

Star_Wars = ["Han Solo", "Luke Skywalker", "Darth Vader", "Boba fett", "Jango Fett", "Chewbacca", 
"Obi-Wan Kenobi", "Yoda", "Lando Calrissian", "Darth Maul", "Mace Windu", "Admiral Ackbar", "Grand Moff Tarkin", 
"Ahsoka Tano", "Count Dooku", "Qui-Gon Jinn", "Sandcrawler", "Mos Eisley", "Mos Espa", "Tatooine", "Sarlacc", 
"The Mandalorian", "Tusken Raider", "Rancor", "Hoth", "Dagobah", "Death Star", "Jawa", "Grogu", "Gamorrean", 
"Cad Bane", "Bantha", "Captain Rex", "Commander Cody", "Fives", "Heavy", "Aayla Secura", "Plo Koon", 
"Commander Fox", "Crosshair", "Hunter", "Echo", "Bad Batch", "Omega", "Wrecker", "Tech", "Droideka", 
"Millennium Falcon", "Tie Fighter", "Kit Fisto", "Star Destroyer", "Bendu", "Kanan Jarrus", "Anakin Skywalker", 
"Emperor Palpatine" ]


# End of the first screen
root = Tk()
root.geometry( "1580x1080")
abc = MyClass( root )       
root.mainloop()

# New Window
Root = tk.Tk()
Root.resizable(True, True )
Root.title( "Hangman" )
Root.geometry( "1520x1080" )

Frame = tk.Frame( Root )
Frame.pack( fill=tk.BOTH, expand=True )
Frame.configure(bg = 'white')

# Displays the amount of lives the user has left 
label_lives = Label(Root, text = Lives, font = ('comicsans, 350'), bg = 'white')
label_lives.place(x = 1000, y = 200)


# Creates buttons For letters a-x
for y in range( 4 ):
    for x in range( 6 ):
        count += 1

        Button = tk.Button( Frame,
        text=alphabet[count], 
        compound="center",
        font=("comic sans", 25),
        bd=10, 
        relief=tk.RAISED, 
        fg="white",
        bg="pink",
        activebackground = "purple",
        activeforeground= "white",
        width=3,
        height=1
        )

        # Places Each button in accordance with where the previous button was placed
        Button.place ( x=1250/2 - 4.2*Square_variable + x/1.2*Square_variable + 7, y=750/2 - 1.5*Square_variable + y/1.2*Square_variable + 60 )
        Buttons.append ( Button )

# Creates Buttons For letters y-z
for y in range( 1 ):
    for x in range( 2 ):
        count += 1

        Button = tk.Button( Frame,
        text=alphabet[count], 
        compound="center",
        font=("comic sans", 25),
        bd=10, 
        relief=tk.RAISED, 
        fg="white",
        bg="pink",
        activebackground = "purple",
        activeforeground= "white",
        width=3,
        height=1
        )
        
        
        Button.place ( x=1250/2 - 4.2*Square_variable + x/1.2*Square_variable + 7, y=750/2 - 1.5*Square_variable + 4/1.2*Square_variable + 60 ) 
        Buttons.append ( Button )

# Creates the button for the space bar 
Button = tk.Button( Frame,
        text= "Space", 
        compound="center",
        font=("comic sans", 25),
        bd=10, 
        relief=tk.RAISED, 
        fg="white",
        bg="pink",
        activebackground = "purple",
        activeforeground= "white",
        width=9,
        height=1
        )

Buttons.append( Button )
Button.place(x = 520, y= 665)

# Function That randomly chooses the category from a list of all the avalible categories
Category = Categories[rand.randint(0,5)]

# Function That chooses a random word from the category selected
if Category == "Veggies":
    Word = Veggies[rand.randint(0, len(Veggies)-1)]
elif Category == "Space":
    Word = Space[rand.randint(0, len(Space)-1)]
elif Category == "Animals":
    Word = Animals[rand.randint(0, len(Animals)-1)]
elif Category == "Mythical Creatures":
    Word = Mythical_Creatures[rand.randint(0, len(Mythical_Creatures)-1)]
elif Category == "Star Wars":
    Word = Star_Wars[rand.randint(0, len(Star_Wars)-1)]
else:
    Word = Fruits[rand.randint(0, len(Fruits)-1)]

Letters =  len(Word)

# Lists for letters A-Z
List = [ [] for x in range( 27 ) ]

for i in range( len(alphabet)):
    for pos, char in enumerate( Word.lower() ):
        if char == alphabet[ i ]:
            List[ i ].append( pos )

print(Word)
print(List)

# Creates the Labels for the chosen hidden word
for x in range( Letters ):

    Underscore = tk.Label( Frame,
    text="_", 
    compound="center",
    font=("comic sans", 15),
    bd=10, 
    relief=tk.SUNKEN, 
    fg="white",
    bg="purple",
    width=3,
    height=1
    )
    Underscore.place ( x=1050/2 - 4.2*Underscore_variable + x/1.2*Underscore_variable + 7, y=100 ) 

    Underscores.append( Underscore )


# Category Title
Title = tk.Label( Frame,
text = Category,
compound = "center",
font = ("comic sans", 30),
bd = 10,
relief = tk.FLAT,
bg = "white",
fg = "black",
width = 15,
height = 1
)

Title.place(x = 650, y =10)

# Main Function that detects whether or not the chosen letter is in the word, 
# and if it is it will change the underscore in the word to that respective letter
def Set( Button ):
    
    def Letter_Stuff():
        global Lives
        
        Index = Buttons.index( Button )

        # Configures each button to its corrisponding alphabetical letter
        for i in range( len( List[ Index ] ) ):
            Underscores[ List[ Index ][ i ] ].config( text=alphabet[Index] )

        # Changes the color of the button to green if the correspnfding letter is in the word, 
        # and if not it changes the button to red and subtracts one life from the lives counter 
        if len( List[ Index ] ) == 0:
            Lives -= 1
            Button.config (bg = "red")

            label_lives.config( text=str(Lives) )
            
            # If the lives run out the program displays a message box telling the user they have lost 
            if Lives <= 0: 
                MsgBox = messagebox.showinfo(name + "Lost", "     YOU LOST \n             - \n     Try Again")
                
                if MsgBox:
                    Root.destroy()

        else:
            Button.config (bg = "green")

            THERE_IS_NO_UNDERSCORES = True

            # Function That loops through the list of underscores and checks if there are any underscores left
            for Underscore in Underscores:
                if Underscore.cget("text") == "_":
                    THERE_IS_NO_UNDERSCORES = False

             # If  the player has correctly guessed the word then a message box appears informing the user they won
            if THERE_IS_NO_UNDERSCORES: 
                MsgBox = messagebox.showinfo(name + " is a Winner", "     You Win \n             - \n     Go Again")
                
                if MsgBox:
                    Root.destroy()
            
            
    Button.config ( command=Letter_Stuff )

# Gives each button a seperate command corresponding to the letter it is in the alphabet
for Button in Buttons:
    Set( Button )
     
# Main Loop
Root.mainloop()
       
