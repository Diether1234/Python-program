from tkinter import *
import tkinter.messagebox as msg 
digits = [1,2,3,4,5,6,7,8,9]
mark = ''
count = 0
panels = ["panel"]*10
# print(panels)
root=Tk()
root.title('Tic-Tac-Toe')
root.geometry("800x800")
root.resizable(0,0)
Label(root,text='Player1 : X', font='Times 20').grid(row=0, column=1)
Label(root,text='Player2 : O', font='Times 20').grid(row=0, column=2)
def win(panels, sign):
    return((panels[1]==panels[2]==panels[3]==sign)
    or (panels[1]==panels[4]==panels[7]==sign)
    or(panels[2]==panels[5]==panels[8]==sign)
    or(panels[3]==panels[6]==panels[9]==sign)
    or(panels[4]==panels[5]==panels[6]==sign)
    or(panels[7]==panels[8]==panels[9]==sign)
    or (panels[1]==panels[5]==panels[9]==sign)
    or(panels[3]==panels[5]==panels[7]==sign) )
def checker(digit):
    global mark, count, digits
    if digit==1:
        digits.remove(digit)
        if count%2==0:
            mark="X"
            panels[digit]=mark
        elif count%2!=0:
            mark = "O"
            panels[digit]=mark
        button1.config(text=mark)
        count = count+1
        sign=mark
        if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
            msg.showinfo("Result:","Player one has won!")
            root.destroy()
        elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
            msg.showinfo("Result:","Player two has won!")
            root.destroy()
        
        


    if digit==2:
        digits.remove(digit)
        if count%2==0:
            mark="X"
            panels[digit]=mark
        elif count%2!=0:
            mark = "O"
            panels[digit]=mark
        button2.config(text=mark)
        count = count+1
        sign=mark
        if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
            msg.showinfo("Result:","Player one has won!")
            root.destroy()
        elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
            msg.showinfo("Result:","Player two has won!")
            root.destroy()


    if digit==3:
            digits.remove(digit)
            if count%2==0:
                mark="X"
                panels[digit]=mark
            elif count%2!=0:
                mark = "O"
                panels[digit]=mark
            button3.config(text=mark)
            count = count+1
            sign=mark
            if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
             msg.showinfo("Result:","Player one has won!")
             root.destroy()
            elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
                msg.showinfo("Result:","Player two has won!")
                root.destroy()

            

    if digit==4:
            digits.remove(digit)
            if count%2==0:
                mark="X"
                panels[digit]=mark
            elif count%2!=0:
                mark = "O"
                panels[digit]=mark
            button4.config(text=mark)
            count = count+1
            sign=mark 
            if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
                msg.showinfo("Result:","Player one has won!")
                root.destroy()
            elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
             msg.showinfo("Result:","Player two has won!")
             root.destroy()

            

    if digit==5:
            digits.remove(digit)
            if count%2==0:
                mark="X"
                panels[digit]=mark
            elif count%2!=0:
                mark = "O"
                panels[digit]=mark
            button5.config(text=mark)
            count = count+1
            sign=mark
            if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
                msg.showinfo("Result:","Player one has won!")
                root.destroy()
            elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
                msg.showinfo("Result:","Player two has won!")
                root.destroy()


    if digit==6:
            digits.remove(digit)
            if count%2==0:
                mark="X"
                panels[digit]=mark
            elif count%2!=0:
                mark = "O"
                panels[digit]=mark
            button6.config(text=mark)
            count = count+1
            sign=mark
            if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
                msg.showinfo("Result:","Player one has won!")
                root.destroy()
            elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
                msg.showinfo("Result:","Player two has won!")
                root.destroy()


    if digit==7:
            digits.remove(digit)
            if count%2==0:
                mark="X"
                panels[digit]=mark
            elif count%2!=0:
                mark = "O"
                panels[digit]=mark
            button7.config(text=mark)
            count = count+1
            sign=mark
            if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
             msg.showinfo("Result:","Player one has won!")
             root.destroy()
            elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
                msg.showinfo("Result:","Player two has won!")
                root.destroy()


    if digit==8:
            digits.remove(digit)
            if count%2==0:
                mark="X"
                panels[digit]=mark
            elif count%2!=0:
                mark = "O"
                panels[digit]=mark
            button8.config(text=mark)
            count = count+1
            sign=mark
            if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
                msg.showinfo("Result:","Player one has won!")
                root.destroy()
            elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
                msg.showinfo("Result:","Player two has won!")
                root.destroy()


    if digit==9:
            digits.remove(digit)
            if count%2==0:
                mark="X"
                panels[digit]=mark
            elif count%2!=0:
                mark = "O"
                panels[digit]=mark
            button9.config(text=mark)
            count = count+1
            sign=mark
            if (win(panels, sign) and sign=="X"):
            # print("Player one has won!")
                msg.showinfo("Result:","Player one has won!")
                root.destroy()
            elif (win(panels, sign) and sign=="O"):
            # print("Player two has won!")
                msg.showinfo("Result:","Player two has won!")
                root.destroy()
    
    if(count>8 and win(panels, "X")==False and win(panels,"O")==False):
        msg.showinfo("Result: ", "Draw!")
        root.destroy()
        



        



    

button1=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(1))
button1.grid(row=1,column=1)
button2=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(2))
button2.grid(row=1,column=2)
button3=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(3))
button3.grid(row=1,column=3)
button4=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(4))
button4.grid(row=2,column=1)
button5=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(5))
button5.grid(row=2,column=2)
button6=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(6))
button6.grid(row=2,column=3)
button7=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(7))
button7.grid(row=3,column=1)
button8=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(8))
button8.grid(row=3,column=2)
button9=Button(root,width=15, height=7, font=('Times 20 bold'), command=lambda:checker(9))
button9.grid(row=3,column=3)

root.mainloop()
