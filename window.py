from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("868x578")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 578,
    width = 868,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    434.0, 289.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 690, y = 518,
    width = 142,
    height = 22)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 482, y = 518,
    width = 142,
    height = 22)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    122.0, 202.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#0d99ff",
    highlightthickness = 0)

entry0.place(
    x = 39.0, y = 178,
    width = 166.0,
    height = 47)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    330.0, 202.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#0d99ff",
    highlightthickness = 0)

entry1.place(
    x = 247.0, y = 178,
    width = 166.0,
    height = 47)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    538.0, 202.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#0d99ff",
    highlightthickness = 0)

entry2.place(
    x = 455.0, y = 178,
    width = 166.0,
    height = 47)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    746.0, 202.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#0d99ff",
    highlightthickness = 0)

entry3.place(
    x = 663.0, y = 178,
    width = 166.0,
    height = 47)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    743.5, 38.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#0d99ff",
    highlightthickness = 0)

entry4.place(
    x = 650.0, y = 14,
    width = 187.0,
    height = 47)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    122.0, 407.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#77ff0d",
    highlightthickness = 0)

entry5.place(
    x = 39.0, y = 383,
    width = 166.0,
    height = 47)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    330.0, 407.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#77ff0d",
    highlightthickness = 0)

entry6.place(
    x = 247.0, y = 383,
    width = 166.0,
    height = 47)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    538.0, 407.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#77ff0d",
    highlightthickness = 0)

entry7.place(
    x = 455.0, y = 383,
    width = 166.0,
    height = 47)

entry8_img = PhotoImage(file = f"img_textBox8.png")
entry8_bg = canvas.create_image(
    746.0, 407.5,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#77ff0d",
    highlightthickness = 0)

entry8.place(
    x = 663.0, y = 383,
    width = 166.0,
    height = 47)

canvas.create_text(
    208.0, 30.0,
    text = "ポイント管入力フォーム",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    123.5, 130.0,
    text = "M&A ",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    332.5, 130.0,
    text = "28A",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    539.5, 129.0,
    text = "AON",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    742.5, 130.0,
    text = "H2o",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    125.0, 335.0,
    text = "df",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    332.0, 335.0,
    text = "sh",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    539.0, 334.0,
    text = "rv",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    742.0, 335.0,
    text = "jk",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    126.0, 81.0,
    text = "adポイント",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    583.0, 39.0,
    text = "日付：",
    fill = "#000000",
    font = ("None", int(30.0)))

window.resizable(False, False)
window.mainloop()
