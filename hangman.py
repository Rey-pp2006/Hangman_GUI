from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
from random import choice
from string import ascii_uppercase


root = Tk()
root.title("hangman")
root.call('wm', 'iconphoto', root._w,PhotoImage(file='Img/icon.png'))


            
Button_counter = 9
counter = 9
guessed = []
exit_button = Button(root , text = "    X    " , bg = "#951732" , fg = "#ffffff", relief=SUNKEN , anchor =E , command = root.destroy ).grid(row = 0 , column = 1 , columnspan = 9 ,sticky = E)

img1 = ImageTk.PhotoImage(Image.open("Img/1.png"))
img2 = ImageTk.PhotoImage(Image.open("Img/2.png"))
img3 = ImageTk.PhotoImage(Image.open("Img/3.png"))
img4 = ImageTk.PhotoImage(Image.open("Img/4.png"))
img5 = ImageTk.PhotoImage(Image.open("Img/5.png"))
img6 = ImageTk.PhotoImage(Image.open("Img/6.png"))
img7 = ImageTk.PhotoImage(Image.open("Img/7.png"))
img8 = ImageTk.PhotoImage(Image.open("Img/8.png"))
img9 = ImageTk.PhotoImage(Image.open("Img/9.png"))
img10 = ImageTk.PhotoImage(Image.open("Img/10.png"))

Image_list = [img1 , img2 , img3 , img4 , img5 , img6 , img7 , img8 , img9 , img10]

#Set Image

img_panel = Label(root , image = Image_list[counter] ) 
img_panel.grid(row = 1, column = 0 , columnspan =4 , pady = 40 )


#choosing words randomly
def new_game():
    
    global img_panel
    global Image_list
    global word
    global guesses
    global guess
    global guess_panel
    counter = 9
    guessed = []
    Button_counter = 9
    file = open("words.txt")
    read = file.read()
    words=read.split()
    word =choice(words).upper()
    guesses = ["____"] *len(word)
    guess = StringVar() 
    guess.set(" ".join(guesses))
    guess_panel = Label(root , textvariable = guess , font = "Consolas 14 bold").grid(row = 1 , column =3 ,columnspan = 4)
    img_panel = Label(root , image = Image_list[counter] ) 
    img_panel.grid(row = 1, column = 0 , columnspan =4 , pady = 40 )
new_game()


def clicked(letter):
    global Image_list
    global counter
    global word
    global guess_panel
    global guesses
    global response
    global lives_panel
    global img_panel
    global guessed

    if letter in guessed :
        response = messagebox.showinfo("Hangman!" , "You guessed that before!")
    if letter in word and letter not in guessed :
        guessed.append(letter)
        response = messagebox.showinfo("hangman" , "you guessed correctly !")
        for i in range(len(word)):
            if word[i] == letter :
                guesses[i] = letter
                guess.set("  ".join(guesses))
                guess_panel = Label(root , textvariable = guess , font = "Consolas 14 bold").grid(row = 1 , column =3 ,columnspan = 4)
        
        if (word.upper()) == ("".join(guesses)) :
            response = messagebox.askyesno("hangman" , "You Won! Do you want to play again ?")
            if response == 0 :
                root.destroy()
            elif response == 1 :
                guessed = []
                counter = 9
                new_game()
       
    elif letter not in word and letter not in guessed :
        
        guessed.append(letter)
        response = messagebox.showinfo("Hangman!" , "You guessed wrong. Try again!")
        if counter > 0 :
            counter -= 1
            img_panel.configure(image = Image_list[counter])
            guess_panel = Label(root , textvariable = guess , font = "Consolas 14 bold").grid(row = 1 , column =3 ,columnspan = 4)
        elif counter == 0 :
            response = messagebox.askyesno("hangman" , "You lost! Do you want to play again ?")
            if response == 0 :
                root.destroy()
            elif response == 1 :
                guessed = []
                counter = 9
                new_game()
           
            
            
for letter in ascii_uppercase :
    Button( root , text = letter , font = "Helvetica 10" , bd = 3, command = lambda letter=letter : clicked(letter) , width = 15).grid(row = 1+Button_counter // 9 , column = Button_counter % 9)
    Button_counter += 1 



root.mainloop()