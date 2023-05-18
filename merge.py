import os
import cv2
import glob
import numpy as np
import pathlib
import tkinter as tk
from PIL import Image
from natsort import natsorted
from tkinter import filedialog, messagebox

# メッセージボックス（情報） 
root = tk.Tk()
root.withdraw()
messagebox.showinfo('check', '結合元画像フォルダ選択')
root.destroy()

#フォルダ選択時の初期パス
input_dir = "C://Users/"
input_dir_name = str(input_dir)

#画像フォルダ選択
root = tk.Tk()
root.withdraw()
fld = pathlib.Path(filedialog.askdirectory(initialdir = input_dir))
input_fld_name = str(fld) + "\\"
root.destroy()

#GUIで縦横選択

def GUI():
    y = 0
    t = 0
    flext = ""

    def btn_click():
        global y
        global t
        global flext
        y = int(yoko.get())
        t = int(tate.get())
        flext = kaku.get()
        baseGround.quit()

    baseGround = tk.Tk()
    baseGround.title("分割数記入")
    baseGround.geometry("400x300")

    Label1 = tk.Label(text="行：分割数")
    Label1.place(x= 0, y=50)
    yoko = tk.Entry(width=15)
    yoko.place(x= 80, y=50)

    Label2 = tk.Label(text="列：分割数")
    Label2.place(x= 0, y=100)
    tate = tk.Entry(width=15)
    tate.place(x= 80, y=100)

    Label4 = tk.Label(text="画像ファイル拡張子 (.以降を入力)")
    Label4.place(x = 0, y= 250)
    kaku = tk.Entry(width=15)
    kaku.place(x= 80, y =300)
    

    buttonA = tk.Button(baseGround, text = "開始", command=btn_click).place(x= 50, y=350)

    baseGround.mainloop()

    return y, t, flext

GUI()
n, m, file_ext = y, t, flext
#nが行の分割数、mが列の分割数

#選択したフォルダ内のフォルダ一覧を取得し、リストへ格納
fld_path = "{}/*/".format(fld)
dirlist = list(glob.glob(fld_path))

if len(dirlist) == 0:
    dirlist = glob.glob(input_fld_name)

len_d = len(dirlist)


for j in range(len_d):
    #選択したフォルダ内の画像取得し、リストへ格納
    input_files = glob.glob(dirlist[j] + '/*.' + file_ext)

    # 空のリストを準備
    d = []

    # natsortedで自然順（ファイル番号の小さい順）に1個づつ読み込む
    for i in natsorted(input_files):
        img = Image.open(i)    # img は'JpegImageFile' object
        img = np.asarray(img)  # np.asarrayで img を ndarray に変換
        d.append(img)          # d にappend で img を追加
        
    # 画像の高さ方向と幅方向を結合
    h_list = []
    h_list_merge = []

    for k in range(n):
        h_list = np.hstack(d[k*m:(k+1)*m])
        h_list_merge.append(h_list)

    img_x = np.vstack(h_list_merge)

    # 色をBGR から RGB に変更
    img_x = cv2.cvtColor(img_x, cv2.COLOR_BGR2RGB)

    cv2.imwrite(os.path.join(dirlist[j] + 'merge.jpg'), img_x)
    
