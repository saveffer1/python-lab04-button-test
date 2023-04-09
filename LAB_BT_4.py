from tkinter import*
from PIL import Image, ImageTk
from datetime import datetime
# color name :https://wiki.tcl.tk/37701

def record_transaction(menu_item):
    with open("sold.csv", mode='a', newline='', encoding='UTF-8') as f:
        price = menus[menu_item]
        dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f'{menu_item},{price}, {dt}\n')

#global variable
b1c = 0
b2c = 0
b3c = 0
b4c = 0
total_cnt = 0
total_p = 0
save1 = 0
save2 = 0
save3 = 0
save4 = 0
xp = 0

def b1_click():
    menu_item = "Blue Lemon Soda"
    global b1c
    global total_cnt
    global total_p
    global save1
    save1 += 55
    b1c += 1
    total_cnt += 1
    total_p += 55
    tv_b1.set("Amount: "+str(b1c))
    tv_total.set(f'Total = {total_cnt}')
    tv_price.set(f'Price = {total_p}')
    record_transaction(menu_item)

def b2_click():
    menu_item = "Apple Soda"
    global b2c
    global total_cnt
    global total_p
    global save2
    save2 += 65
    b2c += 1
    total_cnt += 1
    total_p += 65
    tv_b2.set("Amount: "+str(b2c))
    tv_total.set(f'Total = {total_cnt}')
    tv_price.set(f'Price = {total_p}')
    record_transaction(menu_item)

def b4_click():
    menu_item = "Strawberry Soda"
    global b4c
    global total_cnt
    global total_p
    global save4
    save4 += 45
    b4c += 1
    total_cnt += 1
    total_p += 45
    tv_b4.set("Amount: "+str(b4c))
    tv_total.set(f'Total = {total_cnt}')
    tv_price.set(f'Price = {total_p}')
    record_transaction(menu_item)

def b3_click():
    menu_item = "Bubble Tea"
    global b3c
    global total_cnt
    global total_p
    global save3
    save3 += 35
    b3c += 1
    total_cnt += 1
    total_p += 35
    tv_b3.set("Amount: "+str(b3c))
    tv_total.set(f'Total = {total_cnt}')
    tv_price.set(f'Price = {total_p}')
    record_transaction(menu_item)


root =Tk()

tv_b2 = StringVar()
tv_b3 = StringVar()
tv_b1 = StringVar()
tv_b4 = StringVar()
tv_total = StringVar()

tv_b2p = StringVar()
tv_b3p = StringVar()
tv_b1p = StringVar()
tv_b4p = StringVar()
global tv_price
tv_price = StringVar()

photo1 = PhotoImage(file="assets/t1.png")
photo2 = PhotoImage(file="assets/t2.png")
photo3 = PhotoImage(file="assets/t3.png")
photo4 = PhotoImage(file="assets/t4.png")

photo1 = photo1.subsample(1, 1)
photo1 = photo1.zoom(1, 1)
photo2 = photo2.subsample(1, 1)
photo2 = photo2.zoom(1, 1)
photo3 = photo3.subsample(1, 1)
photo3 = photo3.zoom(1, 1)
photo4 = photo4.subsample(1, 1)
photo4 = photo4.zoom(1, 1)

alltv = [tv_b1,tv_b2,tv_b3,tv_b4]
for i in range(0,4):
    alltv[0+i].set("Amount: "+str(0))
tv_total.set("Total = 0")

alltv = [tv_b1p,tv_b2p,tv_b3p,tv_b4p]
prze = [55,65,35,45]
for i in range(0,4):
    alltv[0+i].set("price: "+str(prze[i])+" ฿")
tv_price.set("Price = 0")
root.option_add("*Font", "consolas 45")

def proceed_click():
    global b1c
    global b2c
    global b3c
    global b4c
    global save1
    global save2
    global save3
    global save4
    global top
    global xxp
    xxp = StringVar()
    top = 0

    xxp.set(f'Price = {top}')
    #root.destroy()
    app  =Tk()
    Label(app, text="HALO Coffee Shop", bg = "mediumorchid2", width=15,height = 1, borderwidth=3).grid(row=0, columnspan=4, sticky="news")
    Label(app, text="BILL", bg = "snow3", width=15,height = 1, borderwidth=3).grid(row=1, columnspan=4, sticky="news")

    bnc = ["Blue Lemon Soda","Apple Soda","Bubble Tea","Strawberry Soda"]
    bgg = ["DeepSkyBlue3","green3","goldenrod1","salmon"]
    bsv = [save1,save2,save3,save4]
    btc = [b1c,b2c,b3c,b4c]

    for i in range(0,4):
        Label(app, text=bnc[i], bg=bgg[i], width=15,height = 1).grid(row=2+i, column=0, ipady=5)
        Label(app, text="Amount: "+str(btc[i]), bg=bgg[i], width=15,height = 1).grid(row=2+i, column=1, ipady=5)
        Label(app, text="Price: "+str(bsv[i])+" ฿", bg=bgg[i], width=15,height = 1).grid(row=2+i, column=2, ipady=5)
        top += bsv[i]

    Label(app, text = "Total Price: "+str(top)+" ฿", bg = "mediumorchid2", width=10,height = 1, borderwidth=3).grid(row=7,column = 0, columnspan=3, sticky="news")
    if app.protocol('WM_DadadadELETE_WINDOW'):
        doSomething()

    app.mainloop()

def doSomething():
    global b1c
    global b2c
    global b3c
    global b4c
    global save1
    global save2
    global save3
    global save4

    save1 = 0
    save2 = 0
    save3 = 0
    save4 = 0
    tv_price = 0
    tv_total = 0
    b1c = 0
    b2c = 0
    b3c = 0
    b4c = 0

menus = {"Blue Lemon Soda":55, "Apple Soda":65, "Bubble Tea":35,
"green tea":25, "tea":20, "thai tea":30,"Strawberry Soda":45}

#banner
Label(root, text="HALO Coffee Shop", bg = "mediumorchid2", width=15,height = 1, borderwidth=3).grid(row=0, columnspan=4, sticky="news")

root.option_add("*Font", "consolas 20")

#category
Label(root, text = "Image", bg = "snow3", width=15,height = 1).grid(row=1, column=0, sticky="news")
Label(root, text = "Menu", bg = "snow3", width=15,height = 1).grid(row=1, column=1, sticky="news")
Label(root, text = "Price", bg = "snow3", width=15,height = 1).grid(row=1, column=2, sticky="news")
Label(root, text = "Amount", bg = "snow3", width=15,height = 1).grid(row=1, column=3,sticky="news")

#Lemon soda
Button(root, text="Blue Lemon Soda", bg="DeepSkyBlue3", width=5,height = 1, command=b1_click,image=photo1, borderwidth=3).grid(row=2, column=0, sticky="news")
Button(root, text="Blue Lemon Soda", bg="DeepSkyBlue3", width=25,height = 1, command=b1_click).grid(row=2, column=1, ipady=5)
Label(root, textvariable = tv_b1p, bg = "DeepSkyBlue3", width=10,height = 1).grid(row=2, column=2, sticky="news")
Label(root, textvariable = tv_b1, bg = "DeepSkyBlue3", width=10,height = 1).grid(row=2, column=3, sticky="news")

#apple soda
Button(root, text="Apple Soda", bg="green3", width=5,height = 1, command=b2_click,image=photo2, borderwidth=3).grid(row=3, column=0, sticky="news")
Button(root, text="Apple Soda", bg="green3", width=25,height = 1, command=b2_click).grid(row=3, column=1, ipady=5)
Label(root, textvariable=tv_b2p, bg = "green3", width=10,height = 1).grid(row=3, column=2,sticky="news")
Label(root, textvariable=tv_b2, bg = "green3", width=10,height = 1).grid(row=3, column=3,sticky="news")

#Bubble tea
Button(root, text="Bubble Tea", bg="goldenrod1", width=5,height = 1, command=b3_click,image=photo3, borderwidth=3).grid(row=4, column=0, sticky="news")
Button(root, text="Bubble Tea", bg="goldenrod1", width=25,height = 1, command=b3_click).grid(row=4, column=1, ipady=5)
Label(root, textvariable=tv_b3p, bg = "goldenrod1", width=10,height = 1).grid(row=4, column=2, sticky="news")
Label(root, textvariable=tv_b3, bg = "goldenrod1", width=10,height = 1).grid(row=4, column=3, sticky="news")

#strawberry soda
Button(root, text="Strawberry Soda", bg="salmon", width=5,height = 1, command=b4_click,image=photo4, borderwidth=3).grid(row=5, column=0, sticky="news")
Button(root, text="Strawberry Soda", bg="salmon", width=25,height = 1, command=b4_click).grid(row=5, column=1, ipady=5)
Label(root, textvariable=tv_b4p, bg = "salmon", width=10,height = 1).grid(row=5, column=2,sticky="news")
Label(root, textvariable=tv_b4, bg = "salmon", width=10,height = 1).grid(row=5, column=3,sticky="news")


#total price
Label(root, textvariable=tv_total, bg = "mediumorchid2", width=10,height = 1, borderwidth=3).grid(row=6, columnspan=3, sticky="news")
Label(root, textvariable=tv_price, bg = "mediumorchid2", width=10,height = 1, borderwidth=3).grid(row=6,column = 3, columnspan=1, sticky="news")
Button(root, text = "Proceed...", bg = "firebrick1", width=10,height = 1, borderwidth=3, command=proceed_click).grid(row=7, columnspan=4, sticky="news")
"""
scrollbar = Scrollbar(root)
scrollbar.grid(row = 0,rowspan = 6,column = 5,sticky="news")
mylist = Listbox(root, yscrollcommand = scrollbar.set )
"""

root.mainloop()
