import os
import cv2
import numpy as np
import pathlib
import tkinter as tk
from tkinter import filedialog, messagebox

# メッセージボックス（情報） 
root = tk.Tk()
root.withdraw()
messagebox.showinfo('check', '分割元画像フォルダ選択')
root.destroy()

#フォルダ選択時の初期パス
input_dir = "C://Users/"
input_dir_name = str(input_dir)

#画像フォルダ選択
root = tk.Tk()
root.withdraw()
fld = filedialog.askdirectory(initialdir = input_dir)
root.destroy()

#GUIで縦横選択

def GUI():
    y = 0
    t = 0
    svfld = ""
    flext = ""

    def btn_click():
        global y
        global t
        global svfld
        global flext
        y = int(yoko.get())
        t = int(tate.get())
        svfld = save_fld.get()
        flext = kaku.get()
        baseGround.quit()

    baseGround = tk.Tk()
    baseGround.title("分割数記入")
    baseGround.geometry("600x500")

    Label1 = tk.Label(text="行：分割数")
    Label1.place(x= 0, y=50)
    yoko = tk.Entry(width=15)
    yoko.place(x= 80, y=50)

    Label2 = tk.Label(text="列：分割数")
    Label2.place(x= 0, y=100)
    tate = tk.Entry(width=15)
    tate.place(x= 80, y=100)

    Label3 = tk.Label(text="保存フォルダ名（半角英数字のみ）")
    Label3.place(x= 0, y=150)
    save_fld = tk.Entry(width=15)
    save_fld.place(x= 80, y=200)

    Label4 = tk.Label(text="画像ファイル拡張子 (.以降を入力)")
    Label4.place(x = 0, y= 250)
    kaku = tk.Entry(width=15)
    kaku.place(x= 80, y =300)
    

    buttonA = tk.Button(baseGround, text = "開始", command=btn_click).place(x= 50, y=350)

    baseGround.mainloop()

    return y, t, svfld, flext

GUI()
n, m, svfld_name, file_ext = y, t, svfld, flext

#選択したフォルダ内の画像取得し、リストへ格納
input_list = list(pathlib.Path(fld).glob('**/*.' + flext))
input_fld_name = str(fld)


#リストへ格納した画像を1つずつ取り出して処理
for i in range(len(input_list)):
    #画像ファイル名取り出し
    img_file_name = str(input_list[i])
    basename_without_ext = os.path.splitext(os.path.basename(img_file_name))[0]
    basename = str(basename_without_ext)

    #取り出したファイル名の画像読み込み
    image = cv2.imread(img_file_name)
    
    #画像サイズを調べる（高さ：h 、幅：w）
    h, w = image.shape[:2]
    x0, out_h = divmod(h, n)
    y0, out_w = divmod(w, m)
    #y0 = int(h/n)
    #x0 = int(w/m) 
    # 分割した画像を内包表記でリスト化
    c = [image[x0*x:x0*(x+1), y0*y:y0*(y+1)] for x in range(n) for y in range(m)]

    #保存先フォルダ作成
    path = os.path.join(pathlib.Path(fld), svfld_name, basename)
    path_name = str(path)
    os.makedirs(path_name, exist_ok=True)

    # c のリストから1つずつ取り出して
    # ファイル番号（0.jpg、1.jpg、・・）を付けて、split/元画像名フォルダに保存
    for j, img in enumerate(c):
        cv2.imwrite(os.path.join(path, '{}{}{}.jpg'.format(j, "_", basename)), img)

print("Done!")

