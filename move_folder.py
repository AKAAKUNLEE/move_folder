# 导入必要的库
import tkinter as tk  # GUI库
from tkinter import filedialog  # 文件对话框
import shutil  # 文件操作库
import configparser  # 配置文件解析库

# 选择源文件夹函数
def select_source_folder():
    global source_folder  # 声明全局变量
    source_folder = filedialog.askdirectory()  # 弹出文件夹选择对话框
    source_folder_entry.delete(0, tk.END)  # 清空输入框
    source_folder_entry.insert(0, source_folder)  # 将选择的路径插入输入框

# 选择目标文件夹函数
def select_destination_folder():
    global destination_folder  # 声明全局变量
    destination_folder = filedialog.askdirectory()  # 弹出文件夹选择对话框
    destination_folder_entry.delete(0, tk.END)  # 清空输入框
    destination_folder_entry.insert(0, destination_folder)  # 将选择的路径插入输入框

# 移动文件夹函数
def move_folder():
    if source_folder and destination_folder:  # 检查路径是否已选择
        try:
            shutil.move(source_folder, destination_folder)  # 执行文件夹移动
            status_label.config(text="文件夹移动成功！")  # 更新状态标签
        except Exception as e:  # 捕获异常
            status_label.config(text=f"移动文件夹时出错: {str(e)}")  # 显示错误信息

# 保存配置函数
def save_config():
    config = configparser.ConfigParser()  # 创建配置解析器
    config['PATHS'] = {  # 创建PATHS节
       'source_folder': source_folder,  # 保存源文件夹路径
        'destination_folder': destination_folder  # 保存目标文件夹路径
    }
    # 弹出保存文件对话框
    file_path = filedialog.asksaveasfilename(defaultextension=".mfc",
                                             filetypes=[("Move Folder Config", "*.mfc")])
    if file_path:  # 如果选择了文件
        with open(file_path, 'w') as configfile:  # 打开文件
            config.write(configfile)  # 写入配置

# 加载配置函数
def load_config():
    global source_folder, destination_folder  # 声明全局变量
    # 弹出打开文件对话框
    file_path = filedialog.askopenfilename(filetypes=[("Move Folder Config", "*.mfc")])
    if file_path:  # 如果选择了文件
        config = configparser.ConfigParser()  # 创建配置解析器
        config.read(file_path)  # 读取配置文件
        if 'PATHS' in config:  # 检查是否存在PATHS节
            # 获取源文件夹路径
            source_folder = config.get('PATHS','source_folder', fallback='')
            # 获取目标文件夹路径
            destination_folder = config.get('PATHS', 'destination_folder', fallback='')
            source_folder_entry.delete(0, tk.END)  # 清空源文件夹输入框
            source_folder_entry.insert(0, source_folder)  # 插入源文件夹路径
            destination_folder_entry.delete(0, tk.END)  # 清空目标文件夹输入框
            destination_folder_entry.insert(0, destination_folder)  # 插入目标文件夹路径

# 创建主窗口
root = tk.Tk()
root.title("移动文件夹程序")  # 设置窗口标题

# 初始化全局变量
source_folder = ""
destination_folder = ""

# 创建源文件夹UI组件
tk.Label(root, text="源文件夹:").grid(row = 0, column = 0, padx = 10, pady = 10)  # 标签
source_folder_entry = tk.Entry(root, width = 50)  # 输入框
source_folder_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
tk.Button(root, text="选择源文件夹", command = select_source_folder).grid(row = 0, column = 2, padx = 10, pady = 10)  # 按钮

# 创建目标文件夹UI组件
tk.Label(root, text="目标文件夹:").grid(row = 1, column = 0, padx = 10, pady = 10)  # 标签
destination_folder_entry = tk.Entry(root, width = 50)  # 输入框
destination_folder_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
tk.Button(root, text="选择目标文件夹", command = select_destination_folder).grid(row = 1, column = 2, padx = 10, pady = 10)  # 按钮

# 创建移动文件夹按钮
tk.Button(root, text="移动文件夹", command = move_folder).grid(row = 2, column = 1, padx = 10, pady = 10)

# 创建保存配置按钮
save_config_button = tk.Button(root, text="保存配置", command = save_config)
save_config_button.grid(row = 3, column = 0, padx = 10, pady = 10)

# 创建加载配置按钮
load_config_button = tk.Button(root, text="加载配置", command = load_config)
load_config_button.grid(row = 3, column = 1, padx = 10, pady = 10)

# 创建状态标签
status_label = tk.Label(root, text="")
status_label.grid(row = 3, column = 2, padx = 10, pady = 10)

# 启动主循环
root.mainloop()
