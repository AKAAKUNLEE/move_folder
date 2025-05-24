import tkinter as tk
from tkinter import filedialog
import shutil
import configparser


def select_source_folder():
    global source_folder
    source_folder = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, source_folder)


def select_destination_folder():
    global destination_folder
    destination_folder = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(0, destination_folder)


def move_folder():
    if source_folder and destination_folder:
        try:
            shutil.move(source_folder, destination_folder)
            status_label.config(text="文件夹移动成功！")
        except Exception as e:
            status_label.config(text=f"移动文件夹时出错: {str(e)}")


def save_config():
    config = configparser.ConfigParser()
    config['PATHS'] = {
       'source_folder': source_folder,
        'destination_folder': destination_folder
    }
    file_path = filedialog.asksaveasfilename(defaultextension=".mfc",
                                             filetypes=[("Move Folder Config", "*.mfc")])
    if file_path:
        with open(file_path, 'w') as configfile:
            config.write(configfile)


def load_config():
    global source_folder, destination_folder
    file_path = filedialog.askopenfilename(filetypes=[("Move Folder Config", "*.mfc")])
    if file_path:
        config = configparser.ConfigParser()
        config.read(file_path)
        if 'PATHS' in config:
            source_folder = config.get('PATHS','source_folder', fallback='')
            destination_folder = config.get('PATHS', 'destination_folder', fallback='')
            source_folder_entry.delete(0, tk.END)
            source_folder_entry.insert(0, source_folder)
            destination_folder_entry.delete(0, tk.END)
            destination_folder_entry.insert(0, destination_folder)


root = tk.Tk()
root.title("移动文件夹程序")

source_folder = ""
destination_folder = ""

tk.Label(root, text="源文件夹:").grid(row = 0, column = 0, padx = 10, pady = 10)
source_folder_entry = tk.Entry(root, width = 50)
source_folder_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
tk.Button(root, text="选择源文件夹", command = select_source_folder).grid(row = 0, column = 2, padx = 10, pady = 10)

tk.Label(root, text="目标文件夹:").grid(row = 1, column = 0, padx = 10, pady = 10)
destination_folder_entry = tk.Entry(root, width = 50)
destination_folder_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
tk.Button(root, text="选择目标文件夹", command = select_destination_folder).grid(row = 1, column = 2, padx = 10, pady = 10)

tk.Button(root, text="移动文件夹", command = move_folder).grid(row = 2, column = 1, padx = 10, pady = 10)

save_config_button = tk.Button(root, text="保存配置", command = save_config)
save_config_button.grid(row = 3, column = 0, padx = 10, pady = 10)

load_config_button = tk.Button(root, text="加载配置", command = load_config)
load_config_button.grid(row = 3, column = 1, padx = 10, pady = 10)

status_label = tk.Label(root, text="")
status_label.grid(row = 3, column = 2, padx = 10, pady = 10)

root.mainloop()
