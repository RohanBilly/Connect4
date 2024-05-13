##This is the start if the code. To begin with I imported all
##the elements from Tkinter so that I could create my graphical
##interface. I also imported the threading module so that I
##could run multiple subprograms at once.
from tkinter import *
import operator
import random
global window
global Score
global TurnCounter
TurnCounter = 0
from threading import Thread
FirstTurn = True
Score = 0
window = Tk()
window.title("Connect 4!")
window.configure(background="#686868")
DifficultyCounter = 0
DataFile = open('DataFile.txt','r')
Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
SampleColours = ["#1c9eef","#e8634e","#f2e882","#f2bdfc",
    "#ffffff","#7fba7c","#543a63","#3a3a3a"]


##The GetName() subroutine fetches the user's name so that it can
##be used in the leaderboard. To do this, it creates a screen on
##the window that contains an entry box that the user can type
##their name into.
def GetName():
    global InputBox
    window.configure(background="#d6e5ff")
    T1 = Label(F0, width=31, text = "What is your name?", pady = 20,
    font=("Verdana bold", 14), bg="#d6e5ff")
    T1.pack()
    Gap = Label(F1, width=44, text =
    "     ", bg="#d6e5ff")
    Gap.pack()
    InputBox = Entry(F2)
    InputBox.pack()
    Gap2 = Label(F3, width=44, text =
    "     ", bg="#d6e5ff")
    Gap2.pack()
    button = Button(F4,text="Enter", font=("times new roman", 15),
    command=EnterPressed,width = 25,height = 1)
    button.pack()
    Gap3 = Label(F5, width=44, text =
    "     ", bg="#d6e5ff")
    Gap3.pack()    


##This is run when the enter button is pressed. It saves the inputted name
##from the user and creates the menu.
def EnterPressed():
    global Name
    Name = InputBox.get()
    BackToMenu()
    MakeMenu()


##This subroutine creates the game menu so that the player can navigate the
##different parts of the game. It only does this if the MakeMenu variable is
##False, this prevents multiple menus being displayed at once.
##It then opens the DataFile so it can retrieve the player's chosen theme
##colour for the menu.
##It then creates the menu screen by creating buttons for each menu option.
def MakeMenu():
    global MenuMade
    if MenuMade == False:
        SampleColoursTheme = ["#c3d7f7","#f4c3e6","#f4dfc3","#add179",
        "#dce0d7","#dbd9f9","#543a63","#ffa100","#6bb5f9"]
        DataFile = open('DataFile.txt','r')
        Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
        DataFile.close()
        MenuMade = True
        global GameRunning
        GameRunning = False
        window.configure(background="#686868")
        global MenuTopFrame
        MenuTopFrame = Frame(window,height = 27,bg="#686868")
        MenuTopFrame.pack(side=TOP)
        global Gap
        Gap = Frame(window,height = 10,bg="#686868")
        Gap.pack(side=TOP,pady=1)
        global MenuFirstFrame
        MenuFirstFrame = Frame(window,height = 27,bg="#686868")
        MenuFirstFrame.pack(side=TOP,pady=10)
        global MenuSecondFrame
        MenuSecondFrame = Frame(window,height = 27,bg="#686868")
        MenuSecondFrame.pack(side=TOP,pady=10)
        global MenuThirdFrame
        MenuThirdFrame = Frame(window,height = 27,bg="#686869")
        MenuThirdFrame.pack(side=TOP,pady=10)
        global MenuFourthFrame
        MenuFourthFrame = Frame(window,height = 27,bg="#680000")
        MenuFourthFrame.pack(side=TOP,pady=10)
        global MenuFifthFrame
        MenuFifthFrame = Frame(window,height = 27,bg="#686868")
        MenuFifthFrame.pack(side=TOP,pady=10)
        global MenuSixthFrame
        MenuSixthFrame = Frame(window,height = 27,bg="#686868")
        MenuSixthFrame.pack(side=TOP,pady=10)
        global Gap2
        Gap2 = Frame(window,height = 10,bg="#686868")
        Gap2.pack(side=TOP,pady=1)
        TextWindow = Label(MenuTopFrame, height=2, width=40, text = "CONNECT 4",
            font=("Verdana bold", 14), bg=(SampleColoursTheme[int(Lines[5])]))
        TextWindow.pack()
        button = Button(MenuFirstFrame,text="Start", font=("times new roman", 15),
            command=StartPressed,width = 25,height = 1)
        button.pack()
        button2 = Button(MenuSecondFrame,text="Instructions", font=("times new roman", 15),
            command=Instructions,width = 25,height = 1)
        button2.pack()
        button3 = Button(MenuThirdFrame,text="Customise Game", font=("times new roman", 15),
            command=CustomiseGame,width = 25,height = 1)
        button3.pack()
        button4 = Button(MenuFourthFrame,text="LeaderBoard", font=("times new roman", 15),
            command=Leaderboard,width = 25,height = 1)
        button4.pack()
        button5 = Button(MenuFifthFrame,text="Difficulty", font=("times new roman", 15),
            command=Difficulty,width = 25,height = 1)
        button5.pack()
        button6 = Button(MenuSixthFrame,text="Exit", font=("times new roman", 15),
            command=quit,width = 25,height = 1)
        button6.pack()
        Reset() 


##This subroutine deletes the menu screen so that another
##screen can be displayed.
##It then sets the MenuMade variable to False so that the
##menu can be made again.
def KillMenu():
    global MenuMade
    MenuTopFrame.destroy()
    MenuFirstFrame.destroy()
    MenuSecondFrame.destroy()
    MenuThirdFrame.destroy()
    MenuFourthFrame.destroy()
    MenuFifthFrame.destroy()
    MenuSixthFrame.destroy()
    Gap.destroy()
    Gap2.destroy()
    MenuMade = False


##This subroutine is run when the start button
##is pressed on the menu and it starts the game
##of connect 4.
##It sets the GameRunning variable to True so
##that the Check() subroutine can start.
##This subroutine also randomly decides weather
##the computer or player has the first turn.
def StartPressed():
    global FirstTurn
    global PlayerDone
    global GameRunning
    GameRunning = True
    KillMenu()
    MakeGameFrames()
    DisableButtons()
    Check()
    PlayerTurn = random.randint(1,2)
    if PlayerTurn == 1:
        FirstTurn = True
        NormaliseButtons()
        PlayerDone = False
        TextWindowText.set("YOUR TURN")
    else:
        PlayerDone = True
        GameOn()
        

##In order to create a new window, frames
##must be created, this creates the frames
##for the main grid.
def MakeGameFrames():
    global topFrame
    topFrame = Frame(window)
    topFrame.pack(side=TOP)
    global firstFrame
    firstFrame = Frame(window)
    firstFrame.pack(side=TOP)
    global secondFrame
    secondFrame = Frame(window)
    secondFrame.pack(side=TOP)
    global thirdFrame
    thirdFrame = Frame(window)
    thirdFrame.pack(side=TOP)
    global fourthFrame
    fourthFrame = Frame(window)
    fourthFrame.pack(side=TOP)
    global fifthFrame
    fifthFrame = Frame(window)
    fifthFrame.pack(side=TOP)
    global sixthFrame
    sixthFrame = Frame(window)
    sixthFrame.pack(side=TOP)
    global seventhFrame
    seventhFrame = Frame(window)
    seventhFrame.pack(side=TOP)
    global eighthFrame
    eighthFrame = Frame(window)
    eighthFrame.pack(side=TOP)
    global ninthFrame
    ninthFrame = Frame(window)
    ninthFrame.pack(side=TOP)
    global tenthFrame
    tenthFrame = Frame(window)
    tenthFrame.pack(side=TOP)
    MakeGrid()


##The MakeButtons subroutine creates the buttons that allow the player to
##select which column to drop a counter into. It opens the DataFile so it
##can retrieve the theme colour that has been slected by the player.
def MakeButtons() :
    SampleColoursTheme = ["#c3d7f7","#f4c3e6","#f4dfc3","#add179",
                          "#dce0d7","#dbd9f9","#543a63","#ffa100","#6bb5f9"]
    DataFile = open('DataFile.txt','r')
    Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
    DataFile.close()
    global btn
    btn = Button(topFrame, text="column1", state=NORMAL, command = Column_1,
        bg=(SampleColoursTheme[int(Lines[5])]))
    btn.pack(side=LEFT)
    global btn2
    btn2 = Button(topFrame, text="column2", state=NORMAL, command = Column_2,
        bg=(SampleColoursTheme[int(Lines[5])]))
    btn2.pack(side=LEFT)
    global btn3
    btn3 = Button(topFrame, text="column3", state=NORMAL, command = Column_3,
        bg=(SampleColoursTheme[int(Lines[5])]))
    btn3.pack(side=LEFT)
    global btn4
    btn4 = Button(topFrame, text="column4", state=NORMAL, command = Column_4,
        bg=(SampleColoursTheme[int(Lines[5])]))
    btn4.pack(side=LEFT)
    global btn5
    btn5 = Button(topFrame, text="column5", state=NORMAL, command = Column_5,
        bg=(SampleColoursTheme[int(Lines[5])]))
    btn5.pack(side=LEFT)
    global btn6
    btn6 = Button(topFrame, text="column6", state=NORMAL, command = Column_6,
        bg=(SampleColoursTheme[int(Lines[5])]))
    btn6.pack(side=LEFT)
    global btn7
    btn7 = Button(topFrame, text="column7", state=NORMAL, command = Column_7,
        bg=(SampleColoursTheme[int(Lines[5])]))
    btn7.pack(side=LEFT)
    

##The MakeGrid() subroutine creates the grid for the game. Each space in the grid
##is reprented by a canvas that can change colour depending
##on what counter has been dropped into that space.
def MakeGrid():
    SampleColoursTheme = ["#c3d7f7","#f4c3e6","#f4dfc3","#add179",
        "#dce0d7","#dbd9f9","#543a63","#ffa100","#6bb5f9"]
    DataFile = open('DataFile.txt','r')
    Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
    DataFile.close()
    row = 1
    Colours = ["gray","gray40","gray","gray40","gray","gray40","gray"]
    Counter = 0
    for column in ("a", "b", "c", "d", "e", "f", "g"):
        index = (row, column)
        canvases[index] = Canvas(firstFrame,width=54,height=54,
            bg=(Colours[Counter]), highlightbackground="#262626")
        canvases[(row,column)].pack(side=LEFT)
        Counter = Counter + 1
    row = 2
    Colours = ["gray40","gray","gray40","gray","gray40","gray","gray40"]
    Counter = 0
    for column in ("a", "b", "c", "d", "e", "f", "g"):
        index = (row, column)
        canvases[index] = Canvas(secondFrame,width=54,height=54,
            bg=(Colours[Counter]), highlightbackground="#262626")
        canvases[(row,column)].pack(side=LEFT)
        Counter = Counter + 1
    row = 3
    Colours = ["gray","gray40","gray","gray40","gray","gray40","gray"]
    Counter = 0
    for column in ("a", "b", "c", "d", "e", "f", "g"):
        index = (row, column)
        canvases[index] = Canvas(thirdFrame,width=54,height=54,
            bg=(Colours[Counter]), highlightbackground="#262626")
        canvases[(row,column)].pack(side=LEFT)
        Counter = Counter + 1
    row = 4
    Colours = ["gray40","gray","gray40","gray","gray40","gray","gray40"]
    Counter = 0
    for column in ("a", "b", "c", "d", "e", "f", "g"):
        index = (row, column)
        canvases[index] = Canvas(fourthFrame,width=54,height=54,
            bg=(Colours[Counter]), highlightbackground="#262626")
        canvases[(row,column)].pack(side=LEFT)
        Counter = Counter + 1
    row = 5
    Colours = ["gray","gray40","gray","gray40","gray","gray40","gray"]
    Counter = 0
    for column in ("a", "b", "c", "d", "e", "f", "g"):
        index = (row, column)
        canvases[index] = Canvas(fifthFrame,width=54,height=54,
            bg=(Colours[Counter]), highlightbackground="#262626")
        canvases[(row,column)].pack(side=LEFT)
        Counter = Counter + 1
    row = 6
    Colours = ["gray40","gray","gray40","gray","gray40","gray","gray40"]
    Counter = 0
    for column in ("a", "b", "c", "d", "e", "f", "g"):
        index = (row, column)
        canvases[index] = Canvas(sixthFrame,width=54,height=54,
            bg=(Colours[Counter]), highlightbackground="#262626")
        canvases[(row,column)].pack(side=LEFT)
        Counter = Counter + 1
    global TextWindowText
    global TextWindowGame
    TextWindowText = StringVar()
    TextWindowText.set('Start')
    TextWindowGame = Label(seventhFrame, height=2, width=36, textvariable = TextWindowText,
        font=("Verdana bold", 12), bg=(SampleColoursTheme[int(Lines[5])]))
    TextWindowGame.pack(side=TOP)
    Gap = Label(eighthFrame, width=44, text =
    "     ",font=("times new roman", 1), background="#686868")
    Gap.pack()
    button = Button(ninthFrame,text="Back to menu",
        font=("times new roman", 12),command=KillGrid,width = 20)
    button.pack()
    Gap2 = Label(tenthFrame, width=44, text =
    "     ",font=("times new roman", 1), background="#686868")
    Gap2.pack()
    MakeButtons()

##These are the functions that run when the buttons on the grid are pressed.
##Column_1() happens when the first button is pressed etc.
##It adds 10 to the appropriate column list, this creates a map of the grid
##that can be used to easily see if a player has won the game.
##It then disables the buttons so that the player can't move until it is
##their turn. The PlayerDone variable is set to True so that the program
##knows when the computer should make it's turn.
##Each Turn the TurnCounter variable is increaced by one so that when the
##grid is full of counters (when the TurnCounter variable gets to 42), the
##game will end as a draw.
def Column_1():
    global TurnCounter
    if len(columns.get("1")) < 6:
        TextWindowText.set("MY TURN")
        columns.get("1").append(10)
        rows.get(str(len(columns.get("1"))))[0] = 10
        canvases[(7-len(columns.get("1")),"a")].configure(background=
            (SampleColours[int(Lines[1])]))
        TurnCounter = TurnCounter + 1
        DisableButtons()
        global PlayerDone
        global FirstTurn
        PlayerDone = True
        WinCheck()
        if FirstTurn:
            FirstTurn = False
            GameOn()
        
def Column_2():
    global TurnCounter
    if len(columns.get("2")) < 6:
        TextWindowText.set("MY TURN")
        columns.get("2").append(10)
        rows.get(str(len(columns.get("2"))))[1] = 10
        canvases[(7-len(columns.get("2")),"b")].configure(background=
            (SampleColours[int(Lines[1])]))
        TurnCounter = TurnCounter + 1
        DisableButtons()
        global PlayerDone
        global FirstTurn
        PlayerDone = True
        WinCheck()
        if FirstTurn:
            FirstTurn = False
            GameOn()
        
def Column_3():
    global TurnCounter
    if len(columns.get("3")) < 6:
        TextWindowText.set("MY TURN")
        columns.get("3").append(10)
        rows.get(str(len(columns.get("3"))))[2] = 10
        canvases[(7-len(columns.get("3")),"c")].configure(background=
            (SampleColours[int(Lines[1])]))
        TurnCounter = TurnCounter + 1
        DisableButtons()
        global PlayerDone
        global FirstTurn
        PlayerDone = True
        WinCheck()
        if FirstTurn:
            FirstTurn = False
            GameOn()
        
def Column_4():
    global TurnCounter
    if len(columns.get("4")) < 6:
        TextWindowText.set("MY TURN")
        columns.get("4").append(10)
        rows.get(str(len(columns.get("4"))))[3] = 10
        canvases[(7-len(columns.get("4")),"d")].configure(background=
            (SampleColours[int(Lines[1])]))
        TurnCounter = TurnCounter + 1
        DisableButtons()
        global PlayerDone
        global FirstTurn
        PlayerDone = True
        WinCheck()
        if FirstTurn:
            FirstTurn = False
            GameOn()
        
def Column_5():
    global TurnCounter
    if len(columns.get("5")) < 6:
        TextWindowText.set("MY TURN")
        columns.get("5").append(10)
        rows.get(str(len(columns.get("5"))))[4] = 10
        canvases[(7-len(columns.get("5")),"e")].configure(background=
            (SampleColours[int(Lines[1])]))
        TurnCounter = TurnCounter + 1
        DisableButtons()
        global PlayerDone
        global FirstTurn
        PlayerDone = True
        WinCheck()
        if FirstTurn:
            FirstTurn = False
            GameOn()
        
def Column_6():
    global TurnCounter
    if len(columns.get("6")) < 6:
        TextWindowText.set("MY TURN")
        columns.get("6").append(10)
        rows.get(str(len(columns.get("6"))))[5] = 10
        canvases[(7-len(columns.get("6")),"f")].configure(background=
            (SampleColours[int(Lines[1])]))
        TurnCounter = TurnCounter + 1
        DisableButtons()
        global PlayerDone
        global FirstTurn
        PlayerDone = True
        WinCheck()
        if FirstTurn:
            FirstTurn = False
            GameOn()
        
def Column_7():
    global TurnCounter
    if len(columns.get("7")) < 6:
        TextWindowText.set("MY TURN")
        columns.get("7").append(10)
        rows.get(str(len(columns.get("7"))))[6] = 10
        canvases[(7-len(columns.get("7")),"g")].configure(background=
            (SampleColours[int(Lines[1])]))
        TurnCounter = TurnCounter + 1
        DisableButtons()
        global PlayerDone
        global FirstTurn
        PlayerDone = True
        WinCheck()
        if FirstTurn:
            FirstTurn = False
            GameOn()        


##This subroutine disbales the buttons
##so that the player can't move when it's
##not their turn
def DisableButtons():
    if GameRunning == True:
        btn.configure(state=DISABLED)
        btn2.configure(state=DISABLED)
        btn3.configure(state=DISABLED)
        btn4.configure(state=DISABLED)
        btn5.configure(state=DISABLED)
        btn6.configure(state=DISABLED)
        btn7.configure(state=DISABLED)

##This subroutine enables the buttons 
def NormaliseButtons():
    if GameRunning == True:
        btn.configure(state="normal")
        btn2.configure(state="normal")
        btn3.configure(state="normal")
        btn4.configure(state="normal")
        btn5.configure(state="normal")
        btn6.configure(state="normal")
        btn7.configure(state="normal")


##This subroutine creates the
##frames for any selection from
##the menu. This saves me creating
##different frames for each menu option
def MenuSelection():
    global F0
    global F1
    global F2
    global F3
    global F4
    global F5
    global F6
    global F7
    global F8
    global F9
    global F10
    global F11
    global F12
    global F13
    global F14
    global F15
    global F16
    global F17
    global F18
    global F19
    global F20
    global F21
    global F22
    global Gap
    global Gap1
    global Gap2
    global Gap3
    global Gap4
    global Gap5
    global Gap6
    F0 = Frame(window)
    F0.pack(side=TOP)
    F1 = Frame(window)
    F1.pack(side=TOP)
    F2 = Frame(window)
    F2.pack(side=TOP)
    F3 = Frame(window)
    F3.pack(side=TOP)
    F4 = Frame(window)
    F4.pack(side=TOP)
    F5 = Frame(window)
    F5.pack(side=TOP)
    F6 = Frame(window)
    F6.pack(side=TOP)
    F7 = Frame(window)
    F7.pack(side=TOP)
    F8 = Frame(window)
    F8.pack(side=TOP)
    F9 = Frame(window)
    F9.pack(side=TOP)
    F10 = Frame(window)
    F10.pack(side=TOP)
    F11 = Frame(window)
    F11.pack(side=TOP)
    F12 = Frame(window)
    F12.pack(side=TOP)
    F13 = Frame(window)
    F13.pack(side=TOP)
    F14 = Frame(window)
    F14.pack(side=TOP)
    F15 = Frame(window)
    F15.pack(side=TOP)
    F16 = Frame(window)
    F16.pack(side=TOP)
    F17 = Frame(window)
    F17.pack(side=TOP)
    F18 = Frame(window)
    F18.pack(side=TOP)
    F19 = Frame(window)
    F19.pack(side=TOP)
    F20 = Frame(window)
    F20.pack(side=TOP)
    F21 = Frame(window)
    F21.pack(side=TOP)
    F22 = Frame(window)
    F22.pack(side=TOP)


##This displays the instructions to the user.
def Instructions():
    global MenuMade
    MenuMade = False
    KillMenu()
    MenuSelection()
    window.configure(background="#7fba7c")
    T1 = Label(F0, width=31, text = "Instructions:",
        pady = 15, font=("Verdana bold", 14), bg="#7fba7c")
    T1.pack()
    Gap = Label(F1, width=44, text =
    "     ", bg="#7fba7c")
    Gap.pack()
    T2 = Label(F2, width=44, text =
    "By pressing the buttons at the top of the screen,",
        font=("Verdana bold", 11), bg="#7fba7c")
    T2.pack()
    T3 = Label(F3, width=44, text =
    "drop counters into the grid. ", font=("Verdana bold", 11),
        bg="#7fba7c")
    T3.pack()
    Gap2 = Label(F4, width=44, text =
    "     ", bg="#7fba7c")
    Gap2.pack()
    T4 = Label(F5, width=44, text =
    "To win, connect 4 counters of your colour horizontally,",
        font=("Verdana bold", 11), bg="#7fba7c")
    T4.pack()
    T5 = Label(F6, width=44, text =
    "vertically or diagonally.", font=("Verdana bold", 11),
    bg="#7fba7c")
    T5.pack()
    Gap3 = Label(F7, width=44, text =
    "     ", bg="#7fba7c")
    Gap3.pack()
    T6 = Label(F8, width=44, text =
    "You also need to prevent your opponent from",
        font=("Verdana bold", 11),bg="#7fba7c")
    T6.pack()
    T7 = Label(F9, width=44, text =
    "connecting 4 of their counters.", font=("Verdana bold", 11),
        bg="#7fba7c")
    T7.pack()
    Gap4 = Label(F10, width=44, text =
    "     ", bg="#7fba7c")
    Gap4.pack()
    T8 = Label(F11, width=44, text =
    "The harder the difficulty, the more",
        font=("Verdana bold", 11), bg="#7fba7c")
    T8.pack()
    T9 = Label(F12, width=44, text =
    "score you earn.", font=("Verdana bold", 11), bg="#7fba7c")
    T9.pack()
    Gap5 = Label(F13, width=44, text =
    "     ", pady = 3, bg="#7fba7c")
    Gap5.pack()
    T10 = Label(F14, width=44, text =
    "Good luck!", font=("Verdana bold", 11), bg="#7fba7c")
    T10.pack()
    Gap6 = Label(F15, width=44, text =
    "     ", pady = 3, bg="#7fba7c")
    Gap6.pack()
    button = Button(F16,text="Back to menu", font=("times new roman", 15),
        command=BackToMenu,width = 25,height = 1)
    button.pack()
    Gap7 = Label(F17, width=44, text =
    "     ", bg="#7fba7c")
    Gap7.pack()


##This destroys all frames in the window
##So that the menu can be created.
def BackToMenu():
    global MenuMade
    if MenuMade == False:
        F0.destroy()
        F1.destroy()
        F2.destroy()
        F3.destroy()
        F4.destroy()
        F5.destroy()
        F6.destroy()
        F7.destroy()
        F8.destroy()
        F9.destroy()
        F10.destroy()
        F11.destroy()
        F12.destroy()
        F13.destroy()
        F14.destroy()
        F15.destroy()
        F16.destroy()
        F17.destroy()
        F18.destroy()
        F19.destroy()
        F20.destroy()
        F21.destroy()
        F22.destroy()
        MakeMenu()
        MenuMade = True


##This allows the player to change some cosmetic options in the game.
##It displays the currently selected colours and allows the user to
##change the the colour of theme, the player counter and the computer
##counter by pressing a button.
##T
def CustomiseGame():
    global Lines
    global SampleColour1
    global SampleColour2
    global SampleColour3
    global SampleColours
    global SampleCounterPlayer
    global SampleCounterComputer
    global SampleCounterTheme
    global MenuMade
    DataFile = open('DataFile.txt','r')
    Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
    MenuMade = False
    window.configure(background="#bcd6db")
    SampleCounterTheme = Lines[5]
    SampleCounterComputer = Lines[3]
    SampleCounterPlayer = Lines[1]
    SampleColours = ["#1c9eef","#e8634e","#f2e882","#f2bdfc",
        "#ffffff","#7fba7c","#543a63","#3a3a3a"]
    SampleColoursTheme = ["#c3d7f7","#f4c3e6","#f4dfc3",
        "#add179","#dce0d7","#dbd9f9","#543a63","#ffa100","#6bb5f9"]
    KillMenu()
    MenuSelection()
    T1 = Label(F0, width=31, text = "Customise Game:", pady = 15,
        font=("Verdana bold", 14), bg="#bcd6db")
    T1.pack()
    Gap1 = Label(F1, width=44, text ="     ",bg="#bcd6db")
    Gap1.pack()
    T2 = Label(F2, width=31, text = "Change player counter colour:",
        font=("Verdana bold", 12), bg="#bcd6db")
    T2.pack()
    Gap2 = Label(F3, width=44, text ="     ",font=("Verdana bold", 1),
        bg="#bcd6db")
    Gap2.pack()
    button = Button(F4,text="Next colour", font=("times new roman", 14),
        command=ChangePlayerColour,width = 25,height = 1)
    button.pack()
    Gap3 = Label(F5, width=44, text ="     ",bg="#bcd6db")
    Gap3.pack()
    SampleColour1 = Canvas(F6,width=54,height=54,
    bg=(SampleColours[int(SampleCounterPlayer)]), highlightbackground="#262626")
    SampleColour1.pack()
    Gap4 = Label(F7, width=44, text ="     ",bg="#bcd6db")
    Gap4.pack()
    T3 = Label(F8, width=31, text = "Change computer counter colour:",
        font=("Verdana bold", 12), bg="#bcd6db")
    T3.pack()
    Gap5 = Label(F9, width=44, text ="     ",font=("Verdana bold", 1)
        ,bg="#bcd6db")
    Gap5.pack()
    button2 = Button(F10,text="Next colour", font=("times new roman", 14),
        command=ChangeComputerColour,width = 25,height = 1)
    button2.pack()
    Gap6 = Label(F11, width=44, text ="     ",bg="#bcd6db")
    Gap6.pack()
    SampleColour2 = Canvas(F12,width=54,height=54,
    bg=(SampleColours[int(SampleCounterComputer)]), highlightbackground="#262626")
    SampleColour2.pack()
    Gap7 = Label(F13, width=44, text ="     ",bg="#bcd6db")
    Gap7.pack()
    Gap6 = Label(F14, width=44, text =
    "     ", bg="#bcd6db")
    Gap6.pack()
    T4 = Label(F15, width=31, text = "Change theme colour:",
        font=("Verdana bold", 12), bg="#bcd6db")
    T4.pack()
    Gap7 = Label(F16, width=44, text ="     ",font=("Verdana bold", 1),
        bg="#bcd6db")
    Gap7.pack()
    button3 = Button(F17,text="Next colour", font=("times new roman", 14),
        command=ChangeThemeColour,width = 25,height = 1)
    button3.pack()
    Gap8 = Label(F18, width=44, text ="     ",bg="#bcd6db")
    Gap8.pack()
    SampleColour3 = Canvas(F19,width=54,height=54,
    bg=(SampleColoursTheme[int(SampleCounterTheme)]), highlightbackground="#262626")
    SampleColour3.pack()
    Gap9 = Label(F20, width=44, text ="     ",bg="#bcd6db")
    Gap9.pack()
    button4 = Button(F21,text="Back to menu", font=("times new roman", 15),
        command=BackToMenu,width = 25,height = 1)
    button4.pack()
    Gap10 = Label(F22, width=44, text ="     ",bg="#bcd6db")
    Gap10.pack()
    
##This is run when the player presses the button to
##change their counter colour. When the button is pressed,
##the SampleCounterPlayer variable is changed by 1 so that
##the player counter colour is set to the next colour in
##the list.
##The updated counter is then written into the DataFile so
##that the colour selection is saved.
##Both the ChangeComputerColour() and the ChangeThemeColour()
##work the same way.
def ChangePlayerColour():
    global SampleCounterPlayer
    global SampleColour1
    global SampleColours
    if int(SampleCounterPlayer) < 7:
        SampleCounterPlayer = int(SampleCounterPlayer) + 1
        Lines[1] = str(SampleCounterPlayer)
        DataFile = open('DataFile.txt','w')
        for line in Lines:
            DataFile.write(line)
            DataFile.write("\n")
        DataFile.close()
    else:
        SampleCounterPlayer = 0
        Lines[1] = str(SampleCounterPlayer)
        DataFile = open('DataFile.txt','w')
        for line in Lines:
            DataFile.write(line)
            DataFile.write("\n")
        DataFile.close()
    SampleColours = ["#1c9eef","#e8634e","#f2e882",
        "#f2bdfc","#ffffff","#7fba7c","#543a63","#3a3a3a"]
    SampleColour1.configure(background=SampleColours[SampleCounterPlayer])


##This is run when the player presses the button to
##change the computer counter colour
def ChangeComputerColour():
    global SampleCounterComputer
    global SampleColour2
    if int(SampleCounterComputer) < 7:
        SampleCounterComputer = int(SampleCounterComputer) + 1
        Lines[3] = str(SampleCounterComputer)
        DataFile = open('DataFile.txt','w')
        for line in Lines:
            DataFile.write(line)
            DataFile.write("\n")
        DataFile.close()
    else:
        SampleCounterComputer = 0
        Lines[3] = str(SampleCounterComputer)
        DataFile = open('DataFile.txt','w')
        for line in Lines:
            DataFile.write(line)
            DataFile.write("\n")
        DataFile.close()
    SampleColours = ["#1c9eef","#e8634e","#f2e882","#f2bdfc",
        "#ffffff","#7fba7c","#543a63","#3a3a3a",]
    SampleColour2.configure(background=SampleColours[SampleCounterComputer])


##This is run when the player presses the button to
##change the theme colour
def ChangeThemeColour():
    global SampleCounterTheme
    global SampleColour3
    if int(SampleCounterTheme) < 8:
        SampleCounterTheme = int(SampleCounterTheme) + 1
        Lines[5] = str(SampleCounterTheme)
        DataFile = open('DataFile.txt','w')
        for line in Lines:
            DataFile.write(line)
            DataFile.write("\n")
        DataFile.close()
    else:
        SampleCounterTheme = 0
        Lines[5] = str(SampleCounterTheme)
        DataFile = open('DataFile.txt','w')
        for line in Lines:
            DataFile.write(line)
            DataFile.write("\n")
        DataFile.close()
    SampleColoursTheme = ["#c3d7f7","#f4c3e6","#f4dfc3",
        "#defcd4","#ffffff","#dbd9f9","#543a63","#ffa100","#6bb5f9"]
    SampleColour3.configure(background=SampleColoursTheme[SampleCounterTheme])


##This displays the leaderboard to the user by creating a new screen.
def Leaderboard():
    global MenuMade
    MenuMade = False
    KillMenu()
    MenuSelection()
    DataFile = open('DataFile.txt','r')
    Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
    DataFile.close()
    window.configure(background="#d6a284")
    T1 = Label(F0, width=31, text = "Leaderboard:", pady = 20,
        font=("Verdana bold", 14), bg="#d6a284")
    T1.pack()
    T2 = Label(F2, width=44, text = ("#1:\t"+Lines[15]+"\t"+Lines[16]),
        font=("Verdana bold", 11), bg="#d6a284")
    T2.pack()
    Gap1 = Label(F3, width=44, text ="     ", bg="#d6a284")
    Gap1.pack()
    T3 = Label(F4, width=44, text =("#2:\t"+Lines[13]+"\t"+Lines[14]),
        font=("Verdana bold", 11), bg="#d6a284")
    T3.pack()
    Gap2 = Label(F5, width=44, text ="         ", bg="#d6a284")
    Gap2.pack()
    T4 = Label(F6, width=44, text =("#3:\t"+Lines[11]+"\t"+Lines[12]),
        font=("Verdana bold", 11), bg="#d6a284")
    T4.pack()
    Gap3 = Label(F7, width=44, text ="     ", bg="#d6a284")
    Gap3.pack()
    T5 = Label(F8, width=44, text =("#4:\t"+Lines[9]+"\t"+Lines[10]),
        font=("Verdana bold", 11), bg="#d6a284")
    T5.pack()
    Gap4 = Label(F9, width=44, text ="         ", bg="#d6a284")
    Gap4.pack()
    T6 = Label(F10, width=44, text =("#5:\t"+Lines[7]+"\t"+Lines[8]),
        font=("Verdana bold", 11), bg="#d6a284")
    T6.pack()
    Gap5 = Label(F11, width=44, text ="     ", bg="#d6a284")
    Gap5.pack()
    button = Button(F12,text="Back to menu", font=("times new roman", 15),
        command=BackToMenu,width = 25,height = 1)
    button.pack()
    Gap6 = Label(F13, width=44, text ="     ", bg="#d6a284")
    Gap6.pack()


##This subprogram creates the screen that allows the player to change
##the difficulty.
def Difficulty():
    Difficulties = ["Easy","Medium","Hard"]
    global MenuMade
    MenuMade = False
    KillMenu()
    MenuSelection()
    window.configure(background="#a7dce5")
    T1 = Label(F0, width=31, text = "Difficulty:", pady = 20,
        font=("Verdana bold", 14), bg="#a7dce5")
    T1.pack()
    Gap = Label(F1, width=44, text =
    "     ", bg="#a7dce5")
    Gap.pack()
    T2 = Label(F2, width=44, text = (
    "Change Difficulty"), font=("Verdana bold", 11), bg="#a7dce5")
    T2.pack()
    Gap2 = Label(F3, width=44, text =
    "     ", bg="#a7dce5")
    Gap2.pack()
    global ButtonText
    ButtonText = StringVar()
    ButtonText.set(Difficulties[DifficultyCounter])
    button = Button(F4,textvariable=ButtonText, font=("times new roman", 15),
        command=ChangeDifficulty,width = 25,height = 1)
    button.pack()
    Gap3 = Label(F5, height=2, width=44, text =
    "     ", bg="#a7dce5")
    Gap3.pack()
    button2 = Button(F6,text="Back to menu", font=("times new roman", 15),
        command=BackToMenu,width = 25,height = 1)
    button2.pack()
    Gap4 = Label(F7, width=44, text =
    "     ", bg="#a7dce5")
    Gap4.pack()


##This is the function of the button created in the
##Difficulty() subroutine.
##When the player presses the button, the difficulty toggles
##between Easy Medium and Hard.
def ChangeDifficulty():
    global DifficultyCounter
    if DifficultyCounter == 2:
        DifficultyCounter = 0
    else:
        DifficultyCounter = DifficultyCounter + 1
    Difficulties = ["Easy","Medium","Hard"]
    ButtonText.set(Difficulties[DifficultyCounter])


##This subprogram starts the game.
##It starts by starting the ColumnSelect() subroutine which decides where the computer
##counters go.
##If the difficulty is Easy (0), the computer makes a random move, this makes the game
##easiest as it won't try and block the player or try to win.
##If the difficulty is Medium (1), a list is made of all the ways the computer could
##block the player or win, it then adds a random column into the list. It chooses
##a random column from the list to make a move. This works well as a medium difficulty
##as it sometimes makes random moves that appear to be mistakes just like a human player.
##If the difficulty is Hard (2), the computer wins the game if it can, if not it blocks the
##player if it can and if it can't do that it makes a random move.
##I used recursion to keep running this subroutine until the game finishes.
def GameOn():
    global TurnCounter
    global running
    global PlayerDone
    if running == True:
        ColumnSelect()
        if DifficultyCounter == 0:
            ComputerColumn = random.randint(1,7)
            WinCheck()
        elif DifficultyCounter == 1:
            PossibleOptions = []
            for i in range (0,len(PossibleBlocks)):
                PossibleOptions.append(PossibleBlocks[i])
            for i in range (0,len(PossibleWins)):
                PossibleOptions.append(PossibleWins[i])
            PossibleOptions.append(random.randint(1,7))
            ComputerColumn = PossibleOptions[(random.randint(1,len(PossibleOptions)))-1]
            WinCheck()
        elif DifficultyCounter == 2:
            if len(PossibleWins) == 0:
                if len(PossibleBlocks) != 0:
                    ComputerColumn = PossibleBlocks[(random.randint(1,len(PossibleBlocks)))-1]
                    WinCheck()
                else:
                    ComputerColumn = random.randint(1,7)
                    WinCheck()
            else:
                ComputerColumn = PossibleWins[(random.randint(1,len(PossibleWins)))-1]
                WinCheck()
        if PlayerDone:
            if FourInRow == False:
                if len(columns.get(str(ComputerColumn))) < 6:
                    columns.get(str(ComputerColumn)).append(1)
                    rows.get(str(len(columns.get(str(ComputerColumn)))))[ComputerColumn-1] = 1
                    if GameRunning == True:
                        DataFile = open('DataFile.txt','r')
                        Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
                        DataFile.close()
                        SampleColours = ["#1c9eef","#e8634e","#f2e882","#f2bdfc","#ffffff",
                            "#7fba7c","#543a63","#3a3a3a"]
                        canvases[(7-len(columns.get(str(ComputerColumn))),
                        columnLetters[int(ComputerColumn)-1])].configure(background=
                            (SampleColours[int(Lines[3])]))
                        TurnCounter = TurnCounter + 1
                    WinCheck()
    
                else:
                    GameOn()
        NormaliseButtons()
        if FourInRow == False:
            TextWindowText.set("YOUR TURN")
        PlayerDone = False
        if FourInRow == False:
            window.after(2000, GameOn)


##This subprogram constantly checks to see
##if the game is finished. It only runs when
##the running variable is True so that it only
##runs when the game is runnning to avoid crashing.
##I used a time delay so that the computer doesn't
##instantly make a move because real people leave
##some time before making a move.
##I used recurion on this subroutine so that it
##can keep checking to see if a player has won
##and end the game as quickly as possible.
    
def Check():
    global FourInRow
    global running
    if running == True:
        if FourInRow:
            DisableButtons()
            running = False
            TimeDelay()
        else:
            window.after(1000, Check)

##As tkinter doesnt work with the time.sleep() funtion
##I had to make my own. To do this I used the after()
##funtion to wait 3500ms before lauching the next function.
##This means there is a small ammount of time before the
##game ends for the user to see how they won or lost the game.
def TimeDelay():
    window.after(3500,KillGrid)


##This removes the grid from the window
##so that the menu can be made
def KillGrid():
    global MenuMade
    topFrame.destroy()
    firstFrame.destroy()
    secondFrame.destroy()
    thirdFrame.destroy()
    fourthFrame.destroy()
    fifthFrame.destroy()
    sixthFrame.destroy()
    seventhFrame.destroy()
    eighthFrame.destroy()
    ninthFrame.destroy()
    tenthFrame.destroy()
    global canvases
    global running
    global GameRunning
    GameRunning = False
    canvases = {}
    running = False
    if MenuMade == False:
        MakeMenu()


##This resets all varaibles and lists so that
##the game can be run again.
def Reset():
    global running
    global FourInRow
    global PossibleBlocks
    global PossibleWins
    global PlayerTurn
    global columns
    global rows
    global FirstTurn
    global PlayerDone
    global canvases
    global columnLetters
    global TurnCounter
    TurnCounter = 0
    columnLetters = ["a","b","c","d","e","f","g"]
    canvases = {}
    PossibleWins = []
    PossibleBlocks = []
    finished = False
    running = True
    FourInRow = False
    col1=[]
    col2=[]
    col3=[]
    col4=[]
    col5=[]
    col6=[]
    col7=[]
    columns = {
        "1" : col1,
        "2" : col2,
        "3" : col3,
        "4" : col4,
        "5" : col5,
        "6" : col6,
        "7" : col7
    }
    row1=[0,0,0,0,0,0,0]
    row2=[0,0,0,0,0,0,0]
    row3=[0,0,0,0,0,0,0]
    row4=[0,0,0,0,0,0,0]
    row5=[0,0,0,0,0,0,0]
    row6=[0,0,0,0,0,0,0]
    rows = {
        "1" : row1,
        "2" : row2,
        "3" : row3,
        "4" : row4,
        "5" : row5,
        "6" : row6
    }



def ColumnSelect():
    QuickList = []
    global FourInRow
    global columns
    #Vertical check
    #This part checks the vertical sets of 4 to see if either the user
    #or the computer is close to winning, it puts the columns that could
    #result in a win or loss into a list.
    for i in range (1,8):
        for b in range (0,3):
            QuickList = []
            if len(columns.get(str(i))) > (2+b):
                QuickList.append(columns.get(str(i))[b])
                QuickList.append(columns.get(str(i))[b+1])
                QuickList.append(columns.get(str(i))[b+2])
                if len(columns.get(str(i))) == (3+b):
                    if QuickList[0] + QuickList[1] + QuickList[2] == 30:
                        if i not in PossibleBlocks:
                            PossibleBlocks.append(i)
                    elif QuickList[0] + QuickList[1] + QuickList[2] == 3:
                        if i not in PossibleWins:
                            PossibleWins.append(i)
                    elif i in PossibleWins:
                        PossibleWins.remove(i)
                    elif i in PossibleBlocks:
                        PossibleBlocks.remove(i)


    #Horizontal check
    #This checks every horizontal set of 4 in the grid
    for i in range (1,7):
        TempRow = rows.get(str(i)).copy()
        for b in range (0,5):
            QuickList = []
            if len(TempRow) > (3+b):
                QuickList.append(TempRow[b])
                QuickList.append(TempRow[b+1])
                QuickList.append(TempRow[b+2])
                QuickList.append(TempRow[b+3])
                if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 30:
                    for c in range (0,4):
                        if QuickList[c] == 0:
                            if i > 1:
                                if rows.get(str(i-1))[b+c] != 0:
                                    if (b+c+1) not in PossibleBlocks:
                                        PossibleBlocks.append(b+c+1)
                            else:
                                if (b+c+1) not in PossibleBlocks:
                                    PossibleBlocks.append(b+c+1)
                elif QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 3:
                    for c in range (0,4):
                        if QuickList[c] == 0:
                            if i > 1:
                                if rows.get(str(i-1))[b+c] != 0:
                                    if (b+c+1) not in PossibleWins:
                                        PossibleWins.append(b+c+1)
                            else:
                                if (b+c+1) not in PossibleWins:
                                    PossibleWins.append(b+c+1)
                #Removes column from PossibleWins or PossibleBlocks list when a block is made
                if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 31:
                    for c in range (0,4):
                        if QuickList[c] == 1:
                            if (b+c+1) in PossibleBlocks:
                                PossibleBlocks.remove(b+c+1)
                if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 13:
                    for c in range (0,4):
                        if QuickList[c] == 10:
                            if (b+c+1) in PossibleWins:
                                PossibleWins.remove(b+c+1)

    #Right diagonal check
    #This checks every possible diagonal (going up and to the right) set of 4
    for i in range (0,4):
        for b in range (1,4):
            QuickList = []
            for d in range (0,4):
                QuickList.append(rows.get(str(b+d))[i+d])
            if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 30:
                for c in range (0,4):
                    if QuickList[c] == 0:
                        if c > 0 or (b > 0 and c > 0):
                            if rows.get(str(c-1+b))[i+c] != 0:
                                if (i+c+1) not in PossibleBlocks:
                                    PossibleBlocks.append(i+c+1)
                        else:
                            if (i+c+1) not in PossibleBlocks:
                                PossibleBlocks.append(i+c+1)
            elif QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 3:
                for c in range (0,4):
                    if QuickList[c] == 0:
                        if c > 0 or (b > 0 and c > 0): 
                            if rows.get(str(c-1+b))[i+c] != 0:
                                if (i+c+1) not in PossibleWins:
                                    PossibleWins.append(i+c+1)
                        else:
                            if (i+c+1) not in PossibleWins:
                                PossibleWins.append(i+c+1)
            if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 31:
                for c in range (0,4):
                    if QuickList[c] == 1:
                        if (i+c+1) in PossibleBlocks:
                            PossibleBlocks.remove(i+c+1)
            if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 13:
                for c in range (0,4):
                    if QuickList[c] == 10:
                        if (i+c+1) in PossibleWins:
                            PossibleWins.remove(i+c+1)
                            
    #Left diagonal check
    #This checks every possible diagonal (going up and to the left) set of 4
    for i in range (0,4):
        for b in range (1,4):
            QuickList = []
            for d in range (0,4):
                QuickList.append(rows.get(str(b+d))[6-i-d])
            if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 30:
                for c in range (0,4):
                    if QuickList[c] == 0:
                        if c < 3 or b > 0:
                            try:
                                if rows.get(str(c+b-1))[6-i-c] != 0:
                                    if (6-i-c+1) not in PossibleBlocks:
                                        PossibleBlocks.append(6-i-c+1)
                            except:
                                print(" ")
                        else:
                            if (6-i-c+1) not in PossibleBlocks:
                                PossibleBlocks.append(6-i-c+1)
            elif QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 3:
                for c in range (0,4):
                    if QuickList[c] == 0:
                        if c < 3 or i > 0:
                            if rows.get(str(c+b-1))[6-i-c] != 0:
                                if (6-i-c+1) not in PossibleWins:
                                    PossibleWins.append(6-i-c+1)
                        else:
                            if (6-i-c+1) not in PossibleWins:
                                PossibleWins.append(6-i-c+1)
            if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 31:
                for c in range (0,4):
                    if QuickList[c] == 1:
                        if (6-i-c+1) in PossibleBlocks:
                            PossibleBlocks.remove(6-i-c+1)
            if QuickList[0] + QuickList[1] + QuickList[2] + QuickList[3] == 13:
                for c in range (0,4):
                    if QuickList[c] == 10:
                        if (6-i-c+1) in PossibleWins:
                            PossibleWins.remove(6-i-c+1)

    #This part removes any full columns from the possible
    #wins or blocks because no more counters can be put
    #into those columns.
    for i in range (1,8):
        if len(columns.get(str(i))) == 6:
            if (i) in PossibleWins:
                            PossibleWins.remove(i)
            if (i) in PossibleBlocks:
                            PossibleBlocks.remove(i)


##The WinCheck() subroutine checks the grid to see if either the player or computer
##has won. It does this by checking the values given to each set of four spaces in
##the grid, as 10 represents a player counter and 1 represents a computer counter,
##if the values add up to 40 it means the player has won the game and if the values
##add up to 4 the computer has won the game.
##Once the player wins, their score is increaces (varying on what difficulty is
##selected) and the FourInRow variable is set to True so that the game can end.
def WinCheck():
    global FourInRow
    global TurnCounter
    global columns
    global Score
    TempList = []
    #Vertical check, checks every vertical set of 4.
    for i in range (1,8): 
        for b in range (0,3):
            if len(columns.get(str(i))) > (3+b):
                ColumnValue = (columns.get(str(i))[b] + columns.get(str(i))[b+1] +
                    columns.get(str(i))[b+2] + columns.get(str(i))[b+3])
                if ColumnValue == 40:
                    TextWindowText.set("YOU WIN")
                    Score = Score + (50 + (DifficultyCounter * 50))
                    FlashWin()
                    FourInRow = True
                elif ColumnValue == 4:
                    TextWindowText.set("YOU LOSE")
                    FlashLose()
                    SaveScore()
                    FourInRow = True
    #Horizontal check, checks every horizontal set of 4.
    for i in range (1,6):
        for b in range (0,4):
            if len(rows.get(str(i))) > (3+b):
                RowValue = (rows.get(str(i))[b] + rows.get(str(i))[b+1] +
                    rows.get(str(i))[b+2] + rows.get(str(i))[b+3])
                if RowValue == 40:
                    TextWindowText.set("YOU WIN")
                    Score = Score + (50 + (DifficultyCounter * 50))
                    FlashWin()
                    FourInRow = True
                elif RowValue == 4:
                    TextWindowText.set("YOU LOSE")
                    FlashLose()
                    SaveScore()
                    FourInRow = True
    #Right diagonal check, checks every diagonal (up and to the right) set of 4.
    for i in range(1,4):
        for b in range (0,4):
            for c in range (0,4):
                try:
                    TempList.append(rows.get(str(i+c))[b+c])
                except:
                    TempList.append(0)
            if len(TempList) > 3:
                if (TempList[0] + TempList[1] + TempList[2] + TempList[3]) == 40:
                    TextWindowText.set("YOU WIN")
                    Score = Score + (50 + (DifficultyCounter * 50))
                    FlashWin()
                    FourInRow = True
                elif (TempList[0] + TempList[1] + TempList[2] + TempList[3]) == 4:
                    TextWindowText.set("YOU LOSE")
                    FlashLose()
                    SaveScore()
                    FourInRow = True
            TempList = []
    #Left diagonal check, checks every diagonal (up and to the left) set of 4.
    for i in range(1,4):
        for b in range (0,4):
            for c in range (0,4): 
                try:
                    TempList.append(rows.get(str(i+c))[6-b-c])
                except:
                    TempList.append(0)
            if len(TempList) > 3:
                if (TempList[0] + TempList[1] + TempList[2] + TempList[3]) == 40:
                    TextWindowText.set("YOU WIN")
                    Score = Score + (50 + (DifficultyCounter * 50))
                    FlashWin()
                    FourInRow = True
                elif (TempList[0] + TempList[1] + TempList[2] + TempList[3]) == 4:
                    TextWindowText.set("YOU LOSE")
                    FlashLose()
                    SaveScore()
                    FourInRow = True
            TempList = []
    if TurnCounter == 42:
        TextWindowText.set("DRAW")
        FourInRow = True


##This flashes the grid green when the player wins
def FlashWin():
    btn.configure(background="#cff9b3")
    btn2.configure(background="#cff9b3")
    btn3.configure(background="#cff9b3")
    btn4.configure(background="#cff9b3")
    btn5.configure(background="#cff9b3")
    btn6.configure(background="#cff9b3")
    btn7.configure(background="#cff9b3")
    TextWindowGame.configure(bg="#cff9b3")


##This flashes the grid red when the player loses
def FlashLose():
    btn.configure(background="#ff9191")
    btn2.configure(background="#ff9191")
    btn3.configure(background="#ff9191")
    btn4.configure(background="#ff9191")
    btn5.configure(background="#ff9191")
    btn6.configure(background="#ff9191")
    btn7.configure(background="#ff9191")
    TextWindowGame.configure(bg="#ff9191")


##The SaveScore() subroutine adds the players score to the dictionary of
##recored scores, sorts the dictionary into acsending order of scores then
##removes the lowest score. This keeps the leaderboard at 5 scores only.
##It then writes the scores into the textfile so that they can be carried
##over into the next game.
def SaveScore():
    global Name
    DataFile = open('DataFile.txt','r')
    Lines = [line.rstrip('\n') for line in open('DataFile.txt')]
    DataFile.close()
    CurrentScores = {}
    CurrentScores = {
        (Lines[8]) : int(Lines[7]),
        (Lines[10]) : int(Lines[9]),
        (Lines[12]) : int(Lines[11]),
        (Lines[14]) : int(Lines[13]),
        (Lines[16]) : int(Lines[15])
    }
    CurrentScores[Name] = Score
    SortedScores = sorted(CurrentScores.items(), key=operator.itemgetter(1))
    if len(SortedScores) > 5:
        del SortedScores[0]
    Lines[7] = str(SortedScores[0][1])
    Lines[8] = str(SortedScores[0][0])
    Lines[9] = str(SortedScores[1][1])
    Lines[10] = str(SortedScores[1][0])
    Lines[11] = str(SortedScores[2][1])
    Lines[12] = str(SortedScores[2][0])
    Lines[13] = str(SortedScores[3][1])
    Lines[14] = str(SortedScores[3][0])
    Lines[15] = str(SortedScores[4][1])
    Lines[16] = str(SortedScores[4][0])
    DataFile = open('DataFile.txt','w')
    for line in Lines:
        DataFile.write(line)
        DataFile.write("\n")
    DataFile.close()

running = False
MenuMade = False
MenuSelection()
GetName()
##This starts a new thread so that the check()
##subroutine can run alongside the main program
if __name__ == "__main__":
    Thread(target = Check).start()    
    
window.mainloop()
