import tkinter as tk
import tkinter.messagebox as tmsg

def screen_menu(menu):
  txt = ""
  for value,key in menu.items():
    txt +=value+" : "+str(key)+"円 \n"
  return txt

def focus(en):
    globals() [en].delete(0, tk.END)

def getClick(Num): #人数を確認するフレーム
  a = edit_box1.get()
  print(a)
  Num = int(a)
  screen_people_num.pack_forget()
  screen_b.pack()

def show_b():
  screen_b.pack_forget()

def getMainOrder(count):
  for key,value in count.items():
    entry_name = "edit_"+key
    a = globals() [entry_name].get()
    count[key] = int (a)

#データの定義
main = {"ラーメン":600,"餃子":400,"チャーハン":500}
sub = {}
count_main = {"ラーメン":0,"餃子":0,"チャーハン":0}

#root main window の定義
root = tk.Tk()
root.geometry = ("800x400+500+300")
root.title("ラーメン屋")

screen_people_num = tk.Frame(root,width=500,height=200)
screen_people_num.pack()

label = tk.Label (screen_people_num,text="人数の入力")
label.place(x=20,y=20)

edit_box1 = tk.Entry(screen_people_num,width = 20)
edit_box1.place(x=20,y=40)

Num_people = 0

button1 = tk.Button(screen_people_num,text = "チェック",command=lambda:getClick(Num_people))
button1.place(x = 20, y = 60)


#screenB
screen_b = tk.Frame(root,width=800,height=600)


label_b = tk.Label(screen_b,text = "メニュー")
label_b.pack()

label_b_2 = tk.Label(screen_b,text=screen_menu(main),font=("Times",12))
label_b_2.pack()

for key,value in main.items():
  label_name = "label_" + key
  globals() [label_name] =  tk.Label(screen_b, text = key )
  entry_name  ="edit_" +key
  globals() [entry_name] = tk.Entry(screen_b,width=20)
  globals() [label_name].pack()
  globals() [entry_name].pack()
  globals() [entry_name].insert(tk.END,"注文数を入力")
  globals() [entry_name].bind("<Button-1>", focus(entry_name))

button2 = tk.Button(screen_b, text = "確定",command=lambda: getMainOrder(count_main))
button2.pack()


root.mainloop()


