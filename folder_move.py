import os
import tkinter as tk
import pathlib
import shutil
from tkinter import filedialog, messagebox

messagebox.showinfo('openfolder', '元画像フォルダを選択')

#フォルダ選択時の初期パス
input_dir = "C://Users/"
input_dir_name = str(input_dir)

#画像フォルダ選択
root = tk.Tk()
root.withdraw()
fld = filedialog.askdirectory(initialdir = input_dir)
root.destroy()

files = os.listdir(fld)
files_dir = [f for f in files if os.path.isdir(os.path.join(fld, f))]

messagebox.showinfo('openfolder', '移動元フォルダ選択')

#画像フォルダ選択
root = tk.Tk()
root.withdraw()
ori_fld = filedialog.askdirectory(initialdir = fld)
root.destroy()

messagebox.showinfo('openfolder', '移動先フォルダ選択')

#画像フォルダ選択
root = tk.Tk()
root.withdraw()
move_fld = filedialog.askdirectory(initialdir = fld)
root.destroy()

#リストへ格納したフォルダ名を1つずつ取り出して処理
for i in files_dir:
    #画像ファイル名取り出し
    ori_file_name = i

    #元ファイル名の含まれるすべての画像をリストへ格納
    input_list = list(pathlib.Path(ori_fld).glob('./**/*' + ori_file_name + '*.jpg'))
    
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