import os
import tkinter as tk
import pathlib
import shutil
from tkinter import filedialog, messagebox

messagebox.showinfo('openfolder', '元画像フォルダを選択')

#フォルダ選択時の初期パス
input_dir = "D://"
input_dir_name = str(input_dir)

#画像フォルダ選択
root = tk.Tk()
root.withdraw()
fld = filedialog.askdirectory(initialdir = input_dir)
root.destroy()

files = os.listdir(fld)
files_dir = [f for f in files if os.path.isdir(os.path.join(fld, f))]

messagebox.showinfo('openfolder', '整理フォルダ選択')

#画像フォルダ選択
root = tk.Tk()
root.withdraw()
ori_fld = filedialog.askdirectory(initialdir = fld)
root.destroy()

#リストへ格納したフォルダ名を1つずつ取り出して処理
for i in files_dir:
    #画像ファイル名取り出し
    ori_file_name = i

    #1つのフォルダ内の画像リスト取得
    img_fld = os.path.join(pathlib.Path(ori_fld),i)
    img_file = os.listdir(img_fld)
    
    for n in img_file
        img_file_path = pathlib.Path(n)
        basename_list = list[os.path.basename(img_file_path)]
        for m in basename_list
            img_name = 
            if '{}{}.jpg'.format(**, "_", "analysied")

    #元ファイル名の含まれるすべての画像をリストへ格納
    #input_list = list(pathlib.Path(ori_fld).glob('./**/*' + ori_file_name + '*.jpg'))
    
    #ファイル移動
    if input_list:
        #保存先フォルダ作成
        #save_path = os.path.join(pathlib.Path(arrange_fld), i,)
        #path_name = str(save_path)
        #os.makedirs(path_name, exist_ok=True)
        
        for j in input_list:
            
            save_path = os.path.join(pathlib.Path(move_fld), i,)
            shutil.move(str(j), save_path)

print("Done!")