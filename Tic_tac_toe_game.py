import tkinter as tk
from tkinter import messagebox as m_box

win=tk.Tk()
win.title("Tic Tac Toe ")
win.configure(bg='black')

winner=False
click=True
count=0

frame=tk.Frame(win,bg='red')
frame.grid(row=0,column=0,pady=4,padx=4)

def reset():
    global click,count,winner,turn_indicator_label
    click=True
    count=0
    winner=False
    turn_indicator_label.config(text='Player 1 will choose',bg='lightgreen')
    b1.config(text=" ",state='normal',bg='lightgreen')
    b2.config(text=" ",state='normal',bg='lightgreen')
    b3.config(text=" ",state='normal',bg='lightgreen')
    b4.config(text=" ",state='normal',bg='lightgreen')
    b5.config(text=" ",state='normal',bg='lightgreen')
    b6.config(text=" ",state='normal',bg='lightgreen')
    b7.config(text=" ",state='normal',bg='lightgreen')
    b8.config(text=" ",state='normal',bg='lightgreen')
    b9.config(text=" ",state='normal',bg='lightgreen')
    
def clicked(button):
    global count,click,turn_indicator_label
    if(button["text"]==" " and click==True):
        turn_indicator_label.config(text='Player 2 will choose')
        button.config(text="X")
        click=False
        count+=1
    elif(button["text"]==" " and click==False):
        turn_indicator_label.config(text='Player 1 will choose')
        button.config(text="0")
        click=True
        count+=1
    else:
        m_box.showerror("Tic Tac Toe","Select Another Box,this box is already filled")
    if(count>=5):
        checkwinner(button)

def disable_all_buttons():
    b1.config(state='disabled')
    b2.config(state='disabled')
    b3.config(state='disabled')
    b4.config(state='disabled')
    b5.config(state='disabled')
    b6.config(state='disabled')
    b7.config(state='disabled')
    b8.config(state='disabled')
    b9.config(state='disabled')

def checkwinner(b):
    # Checking Value 'X' for Victory
    #Checking Row1
    global winner,turn_indicator_label
    if(b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X'):
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()

    #Checking row2
    elif(b4["text"]=='X' and b5["text"]=='X' and b6["text"]=='X'):
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()

    #Checking Row3
    elif(b7['text']=='X' and b8['text']=='X' and b9['text']=='X'):
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()

    #Checking Column1
    elif(b1['text']=='X' and b4['text']=='X' and b7['text']=='X'):
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()

    #Checking Column2
    elif(b2['text']=='X' and b5['text']=='X' and b8['text']=='X'):
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()

    #Checking Column3
    elif(b3['text']=='X' and b6['text']=='X' and b9['text']=='X'):
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()

    #Checking Diagonal from left to right
    elif(b1['text']=='X' and b5['text']=='X' and b9['text']=='X'):
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()

    #Checking Diagonal from right to left
    elif(b3['text']=='X' and b5['text']=='X' and b7['text']=='X'):
        b[2].config(bg='red')
        b[5].config(bg='red')
        b[8].config(bg='red')
        turn_indicator_label.config(text='Player 1 wins',fg='black')
        m_box.showinfo("Victory","Player 1 wins")
        winner=True
        disable_all_buttons()


    # Checking Value '0' for Victory
    #Checking Row1
    if(b1["text"]=='0' and b2["text"]=='0' and b3["text"]=='0'):
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()

    #Checking row2
    elif(b4["text"]=='0' and b5["text"]=='0' and b6["text"]=='0'):
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()

    #Checking Row3
    elif(b7['text']=='0' and b8['text']=='0' and b9['text']=='0'):
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()

    #Checking Column1
    elif(b1['text']=='0' and b4['text']=='0' and b7['text']=='0'):
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()

    #Checking Column2
    elif(b2['text']=='0' and b5['text']=='0' and b8['text']=='0'):
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()

    #Checking Column3
    elif(b3['text']=='0' and b6['text']=='0' and b9['text']=='0'):
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()

    #Checking Diagonal from left to right
    elif(b1['text']=='0' and b5['text']=='0' and b9['text']=='0'):
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()

    #Checking Diagonal from right to left
    elif(b3['text']=='0' and b5['text']=='0' and b7['text']=='0'):
        b[2].config(bg='red')
        b[5].config(bg='red')
        b[8].config(bg='red')
        turn_indicator_label.config(text='Player 2 wins',fg='black')
        m_box.showinfo("Victory","Player 2 wins")
        winner=True
        disable_all_buttons()
    
    elif(count==9 and winner==False):
        turn_indicator_label.config(text='Match Drawn',fg='black')
        m_box.showinfo('Tic Tac Toe','Match Drawn')
        disable_all_buttons()
    
#Label to indicate which player will choose
turn_indicator_label=tk.Label(frame,text='Player 1 will choose',bg='lightgreen',font='helvetica 14 bold')
turn_indicator_label.grid(row=0,columnspan=3,pady=1)

#Creating Buttons
b1=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b1))
b2=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b2))
b3=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b3))
b4=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b4))
b5=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b5))
b6=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b6))
b7=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b7))
b8=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b8))
b9=tk.Button(frame,text=" ",font='helvetica 20 bold',width=4,height=2,bg="lightgreen",command=lambda:clicked(b9))

#Creating Reset game button to reset game
reset_game_button=tk.Button(win,width=30,text="New Game",bg='lightgreen',font='helvetica 10 bold',command=reset,pady=1) 

#Positioning Buttons 
b1.grid(row=1,column=0,padx=1,pady=1)
b2.grid(row=1,column=1,padx=1,pady=1)
b3.grid(row=1,column=2,padx=1,pady=1)
b4.grid(row=2,column=0,padx=1,pady=1)
b5.grid(row=2,column=1,padx=1,pady=1)
b6.grid(row=2,column=2,padx=1,pady=1)
b7.grid(row=3,column=0,padx=1,pady=1)
b8.grid(row=3,column=1,padx=1,pady=1)
b9.grid(row=3,column=2,padx=1,pady=1)

reset_game_button.grid(row=4,columnspan=3)

win.mainloop()