from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg

count=1
start=False
draw=0
mode='light'

#theme change
def Theme():
    global mode
    if(mode=='light'):
        mode='dark'
        header.config(bg='#171717')
        i.config(bg='#171717')
        title.config(bg='#171717')
        play.config(bg='#171717')
        help.config(bg='#171717')
        quit.config(bg='#171717')
        a.config(bg='#171717')
        b.config(bg='#171717')
        root.config(bg='#2C2C2C')
        match.config(bg='#2C2C2C')
        game_score.config(bg='#2C2C2C')
        game.config(bg='#FF8C00')
        score_O.config(bg='#2C2C2C',fg='deep sky blue')
        score_X.config(bg='#2C2C2C',fg='firebrick2')
        history.config(bg='#2C2C2C')
        for r in range(0,3):
            for c in range(0,3):
                box[r][c].config(bg='#2C2C2C')
        sphoto=Image.open("sun.png")
        sphoto=sphoto.resize((40,40))
        sphoto=ImageTk.PhotoImage(sphoto)
        theme.config(image=sphoto,bg='#171717')
        theme.image=sphoto
    else:
        mode='light'
        header.config(bg='DarkOrchid1')
        i.config(bg='DarkOrchid1')
        title.config(bg='DarkOrchid1')
        play.config(bg='DarkOrchid1')
        help.config(bg='DarkOrchid1')
        quit.config(bg='DarkOrchid1')
        a.config(bg='DarkOrchid1')
        b.config(bg='DarkOrchid1')
        root.config(bg='snow')
        match.config(bg='snow')
        game_score.config(bg='snow')
        game.config(bg='DarkOrchid1')
        score_O.config(bg='snow',fg='blue')
        score_X.config(bg='snow',fg='red2')
        history.config(bg='snow')
        for r in range(0,3):
            for c in range(0,3):
                box[r][c].config(bg='snow')
        theme.config(image=tphoto,bg='DarkOrchid1')
        theme.image=tphoto
        
#rules 
def rules():
    tmsg.showinfo('How to play',"1. Click 'Start' button to play the game\n2. Click 'Quit' button to exit\n3. Click 'Restart' button to play again\n\nRules\nPlayers take turns putting their marks in empty squares. The first player to get 3 of his/her marks in a row (up, down, across, or diagonally) is the winner. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie." )

#play function
def playfun():
    global start
    global count
    global match_count
    global draw
    global mode
    BG='snow'
    if(mode=='dark'):
        BG='#2C2C2C'
    if(play.cget('text')=="Start"):
        if(tmsg.askokcancel('Start',"Let's start the game")):
            start=True
            play.config(text='Restart')
            match_count+=1
            match.config(text=f"Matches Played : {match_count}")
    else:
        if(tmsg.askokcancel('Restart',"Do you want to play again?")):
            start=True
            draw=0
            count=1
            for r in range(0,3):
                for c in range(0,3):
                    box[r][c].config(text=' ',bg=BG)
            match_count+=1
            match.config(text=f"Matches Played : {match_count}")          
        
#exit function
def quitfun():
   t=tmsg.askyesno("Exit","Are you sure you want to quit the game?")
   if t:
      root.destroy()

#show score
def score(value):
    global x
    global o
    global draw

    if(value=='X'):
        x=x+1
        score_X.config(text=f"X  scored\n\n{x}")
        draw=1
    else:
        o=o+1
        score_O.config(text=f"O  scored\n\n{o}")
        draw=2

#check combination
def check():
    global start
    if(box[0][0].cget('text')==box[0][1].cget('text')==box[0][2].cget('text')=='O' or box[0][0].cget('text')==box[0][1].cget('text')==box[0][2].cget('text')=='X'):
        box[0][0].config(bg='green2')
        box[0][1].config(bg='green2')
        box[0][2].config(bg='green2')
        start=False
        score(box[0][0].cget('text'))

    elif(box[1][0].cget('text')==box[1][1].cget('text')==box[1][2].cget('text')=='O' or box[1][0].cget('text')==box[1][1].cget('text')==box[1][2].cget('text')=='X'):
        box[1][0].config(bg='green2')
        box[1][1].config(bg='green2')
        box[1][2].config(bg='green2')
        start=False
        score(box[1][0].cget('text'))

    elif(box[2][0].cget('text')==box[2][1].cget('text')==box[2][2].cget('text')=='O' or box[2][0].cget('text')==box[2][1].cget('text')==box[2][2].cget('text')=='X'):
        box[2][0].config(bg='green2')
        box[2][1].config(bg='green2')
        box[2][2].config(bg='green2')
        start=False
        score(box[2][0].cget('text'))

    elif(box[0][0].cget('text')==box[1][0].cget('text')==box[2][0].cget('text')=='O' or box[0][0].cget('text')==box[1][0].cget('text')==box[2][0].cget('text')=='X'):
        box[0][0].config(bg='green2')
        box[1][0].config(bg='green2')
        box[2][0].config(bg='green2')
        start=False
        score(box[0][0].cget('text'))

    elif(box[0][1].cget('text')==box[1][1].cget('text')==box[2][1].cget('text')=='O' or box[0][1].cget('text')==box[1][1].cget('text')==box[2][1].cget('text')=='X'):
        box[0][1].config(bg='green2')
        box[1][1].config(bg='green2')
        box[2][1].config(bg='green2')
        start=False
        score(box[0][1].cget('text'))

    elif(box[0][2].cget('text')==box[1][2].cget('text')==box[2][2].cget('text')=='O' or box[0][2].cget('text')==box[1][2].cget('text')==box[2][2].cget('text')=='X'):
        box[0][2].config(bg='green2')
        box[1][2].config(bg='green2')
        box[2][2].config(bg='green2')
        start=False
        score(box[0][2].cget('text'))

    elif(box[0][0].cget('text')==box[1][1].cget('text')==box[2][2].cget('text')=='O' or box[0][0].cget('text')==box[1][1].cget('text')==box[2][2].cget('text')=='X'):
        box[0][0].config(bg='green2')
        box[1][1].config(bg='green2')
        box[2][2].config(bg='green2')
        start=False
        score(box[0][0].cget('text'))

    elif(box[0][2].cget('text')==box[1][1].cget('text')==box[2][0].cget('text')=='O' or box[0][2].cget('text')==box[1][1].cget('text')==box[2][0].cget('text')=='X'):
        box[0][2].config(bg='green2')
        box[1][1].config(bg='green2')
        box[2][0].config(bg='green2')
        start=False
        score(box[0][2].cget('text'))
        
#update boxes
def update(event):
    global start
    if start==True:
        active=event.widget
        global count
        if( active.cget('text')==" "):
            if(count%2==0):
                active.config(text='X',fg='red1')
            else:
                active.config(text='O',fg='blue')
            count=count+1
            check()
            if draw==1:
                history.config(text="Last Match : X won")
            elif draw==2:
                history.config(text="Last Match : O won")
            if draw==0 and count==10:
                history.config(text="Last Match : Draw!")

#create window
root=Tk()
root.geometry("800x500")
root.minsize(800,500)
root.maxsize(800,500)
root.configure(bg='snow')

#title and logo
header=Frame(root,bg='DarkOrchid1',padx='10')
header.pack(fill=X)

photo=Image.open("566294.png")
rphoto=photo.resize((60,60))
photo=ImageTk.PhotoImage(rphoto)
i=Label(header,image=photo,bg='DarkOrchid1')
i.grid(row=0,column=0)

title=Label(header,text="Tic Tac Toe",bg='DarkOrchid1',fg='azure',font=("Cooper Black","36","bold"),padx='20')
title.grid(row=0,column=1)
a=Label(header,width=8,bg='DarkOrchid1')
a.grid(row=0,column=2)

#play button
play=Button(header,text='Start',bg='DarkOrchid1',fg='white',bd=0,font=("Book Antique","18","bold"),padx=5,command=playfun)
play.grid(row=0,column=3)

#help button
help=Button(header,text='Help',bg='DarkOrchid1',fg='white',bd=0,font=("Book Antique","18","bold"),padx=5,command=rules)
help.grid(row=0,column=4)

#Quit button
quit=Button(header,text='Quit',bg='DarkOrchid1',fg='white',bd=0,font=("Book Antique","18","bold"),padx=5,command=quitfun)
quit.grid(row=0,column=5)

#for spacing
b=Label(header,width=2,bg='DarkOrchid1')
b.grid(row=0,column=6)

#theme button
tphoto=Image.open("moon.png")
tphoto=tphoto.resize((32,32))
tphoto=ImageTk.PhotoImage(tphoto)
theme=Button(header,image=tphoto,bg='DarkOrchid1',bd=0,command=Theme)
theme.grid(row=0,column=7)

#match count
match_count=0
match=Label(root,text=f"Matches Played : {match_count}",fg='green2',bg='snow',font=("Book Antique","24","bold"))
match.pack(pady=20)

#game and score
game_score=Frame(root,bg='snow')
game_score.pack(anchor='w')

# score of O
o=0
score_O=Label(game_score,text=f"O  scored\n\n{o}",fg='blue',bg='snow',font=("Book Antique","24","bold"))
score_O.grid(row=0,column=0,padx=20)

#game part
game=Frame(game_score,bg='DarkOrchid1')
game.grid(row=0,column=1,padx=80)
box=[['1','2','3'],
     ['4','5','6'],
     ['7','8','9']]
for r in range(0,3):
    for c in range(0,3):
        box[r][c]=Button(game,bg='snow',text=" ",bd=0,font=("Book Antique","30","bold"),height=1,width=3)
        box[r][c].bind('<Button-1>',update)
box[0][0].grid(row=0,column=0)
box[0][1].grid(row=0,column=1,padx=10)
box[0][2].grid(row=0,column=2)
box[1][0].grid(row=1,column=0,pady=10)
box[1][1].grid(row=1,column=1,padx=10,pady=10)
box[1][2].grid(row=1,column=2,pady=10)
box[2][0].grid(row=2,column=0)
box[2][1].grid(row=2,column=1,padx=10)
box[2][2].grid(row=2,column=2)

#X scorecard
x=0
score_X=Label(game_score,text=f"X  scored\n\n{x}",fg='red1',bg='snow',font=("Book Antique","24","bold"))
score_X.grid(row=0,column=2,padx=10)

#match count
history=Label(root,text="Last Match : ",fg='green2',bg='snow',font=("Book Antique","24","bold"))
history.pack(pady=30)

root.mainloop()