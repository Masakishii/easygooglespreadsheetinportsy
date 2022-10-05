from tkinter import *
import os
from tkinter.tix import WINDOW
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
#Comments are written in Japanese for policy reasons.
#windows osで動かすことが前提
dir_f_01 = os.path.dirname(os.path.abspath(__file__))

#コードを書くことを楽するため捨てファイル作成
file_01 = dir_f_01+'/1a.txt'


#ファイルのあるところのディレクトリー編集
with open(file_01, mode="w", encoding="utf-8") as f:
    f.write(dir_f_01)
f = open(file_01,'w')
f.write(dir_f_01)
f.close()

#空白行削除処理
output=""

with open(file_01, encoding="utf-8") as f:
    for line in f:
        if not line.isspace():
            output+=line

f = open(file_01,"w")
f.write(output)
#文字列置換（""から"/"to、ダブルクォーテーション削除）をした後同じファイル名で保存
with open(file_01, encoding="utf-8") as f:
    data_lines = f.read()

    data_lines = data_lines.replace(chr(92),'/')
    data_lines = data_lines.replace('"','')

f = open( file_01 , 'r')

data = f.read()
f.close()

os.remove(file_01)

#データ処理フォーム入力後の処理（テキストボックスから値取得、リスト化）
def btn_clicked():
    print("Button Clicked")

    Day_01 = str(entry4.get())
    GP_02 = int(entry0.get())
    GP_03 = int(entry1.get())
    GP_04 = int(entry2.get())
    GP_05 = int(entry3.get())
    JP_02 = int(entry5.get())   
    JP_03 = int(entry6.get())   
    JP_04 = int(entry7.get())  
    JP_05 = int(entry8.get())

    inputlist_01 = ['APポイント',Day_01,GP_02,GP_03,GP_04,GP_05]
    inputlist_02 = ['BAポイント',Day_01,JP_02,JP_03,JP_04,JP_05]
    inputlist_03 = [inputlist_01,inputlist_02]
    
    #見ずらいから表示方法変更
    df = pd.DataFrame(inputlist_03)
    print(df)
    #リストの数（行列の把握）
    list_index_num = df.shape[0]
    list_cloum_num = df.shape[1]

    #これが繰り返す数　列：行（確認用）
    print(str(list_cloum_num) + ':' + str(list_index_num))
    #GooglAPI使用のための処理
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    #googleスプレッドシートの処理
    #ダウンロードしたjsonファイルをドライブにアップデートした際のパス（ローカル）
    json ='c:/ad/Apps/client_secret.json'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)

    gc = gspread.authorize(credentials)

    #書き込み先のスプレッドシートキーを追加
    SPREADSHEET_KEY = 'スプレッドシートキー'

    #これから下のコードが繰り返し処理
    i = 0       #行数処理用
    q = 0       #列数処理用


    input_data = inputlist_03
#googleスプレッドシートとのやり取り（リストからシート選択、セル入力）
    while i < list_index_num:
        Sheet_Name_01 = input_data[i][q]
       #シート選択 
        WS_01 = gc.open_by_key(SPREADSHEET_KEY).worksheet(Sheet_Name_01)
        #
        def next_available_row(WS_01):
            str_list = list(filter(None, WS_01.col_values(1)))
            return str(len(str_list)+1)
        next_row = next_available_row(WS_01)


        q = q + 1
        while q < list_cloum_num:
                Value_Get_01 = input_data[i][q]
                print(Value_Get_01)
                WS_01.update_cell(next_row,q,Value_Get_01)
                q = q+1   
        q = 0

        i = i + 1

    window.destroy()

def close_window():
    window.destroy()

#フォーム作成
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

background_img = PhotoImage(file = data + "/background.png")
background = canvas.create_image(
    434.0, 289.0,
    image=background_img)


entry0_img = PhotoImage(file = data + "/img_textBox0.png")
entry0_bg = canvas.create_image(
    122.0, 202.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#0d99ff",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry0.place(
    x = 39.0, y = 178,
    width = 166.0,
    height = 47)

entry1_img = PhotoImage(file = data + "/img_textBox1.png")
entry1_bg = canvas.create_image(
    330.0, 202.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#0d99ff",
    font = ("None",int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry1.place(
    x = 247.0, y = 178,
    width = 166.0,
    height = 47)

entry2_img = PhotoImage(file = data + "/img_textBox2.png")
entry2_bg = canvas.create_image(
    538.0, 202.5,
     image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#0d99ff",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry2.place(
    x = 455.0, y = 178,
    width = 166.0,
    height = 47)

entry3_img = PhotoImage(file = data + "/img_textBox3.png")
entry3_bg = canvas.create_image(
    746.0, 202.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#0d99ff",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry3.place(
    x = 663.0, y = 178,
    width = 166.0,
    height = 47)

entry4_img = PhotoImage(file = data + "/img_textBox4.png")
entry4_bg = canvas.create_image(
    743.5, 38.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#0d99ff",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry4.place(
    x = 650.0, y = 14,
    width = 187.0,
    height = 47)

entry5_img = PhotoImage(file = data + "/img_textBox5.png")
entry5_bg = canvas.create_image(
    122.0, 407.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#77ff0d",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry5.place(
    x = 39.0, y = 383,
    width = 166.0,
    height = 47)

entry6_img = PhotoImage(file = data + "/img_textBox6.png")
entry6_bg = canvas.create_image(
    330.0, 407.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#77ff0d",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry6.place(
    x = 247.0, y = 383,
    width = 166.0,
    height = 47)

entry7_img = PhotoImage(file = data + "/img_textBox7.png")
entry7_bg = canvas.create_image(
    538.0, 407.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#77ff0d",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry7.place(
    x = 455.0, y = 383,
    width = 166.0,
    height = 47)

entry8_img = PhotoImage(file = data + "/img_textBox8.png")
entry8_bg = canvas.create_image(
    746.0, 407.5, 
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#77ff0d",
    font = ("None", int(18.0)),
    justify = RIGHT,
    highlightthickness = 0)

entry8.place(
    x = 663.0, y = 383,
    width = 166.0,
    height = 47)

canvas.create_text(
    208.0, 30.0,
    text = "獲得ポイント入力フォーム",
    fill = "#000000",
    font = ("None", int(22.0)))

canvas.create_text(
    123.5, 130.0,
    text = "M&A",
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
    text = "DDE",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    332.0, 335.0,
    text = "FRD",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    539.0, 334.0,
    text = "XDQ",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    742.0, 335.0,
    text = "LOI",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    126.0, 81.0,
    text = "上》》APポイント　下》》ABポイント",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    583.0, 39.0,
    text = "日付：",
    fill = "#000000",
    font = ("None", int(30.0)))

img0 = PhotoImage(file = data + "/img0.png")
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

img1 = PhotoImage(file = data + "/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = close_window,
    relief = "flat")

b1.place(
    x = 482, y = 518,
    width = 142,
    height = 22)

window.resizable(False, False)
window.mainloop()