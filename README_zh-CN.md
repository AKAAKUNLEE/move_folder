<div align="center">
<p><h1>文件夹移动图形界面应用程序</h1></p>
</div>
<div align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.6+-blue.svg" alt="Python"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
<a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/GUI-Tkinter-orange.svg" alt="Tkinter"></a>
<a href="https://www.pyinstaller.org/"><img src="https://img.shields.io/badge/Packaging-PyInstaller-brightgreen.svg" alt="PyInstaller"></a>
<a href="https://github.com/AKAAKUNLEE/move_folder/releases"><img src="https://img.shields.io/github/v/release/AKAAKUNLEE/move_folder" alt="Releases"></a>
</div>

## 一、项目概述

这是一个基于Python开发的文件夹移动图形界面（GUI）小程序。它旨在为用户提供一个便捷的方式来移动计算机上的文件夹，无论是普通用户还是专业人士，都能轻松上手使用。

## 二、功能特性

1. **直观的图形界面**：采用Tkinter或PyQt5构建，用户通过按钮即可轻松选择源文件夹和目标文件夹，无需复杂的命令行操作。
2. **文件夹移动功能**：利用Python的 `shutil`模块，可靠且高效地将文件夹从一个位置移动到另一个位置。
3. **配置保存与加载**：支持将源文件夹和目标文件夹的路径保存为自定义后缀（如 `.mfc`）的配置文件。下次使用时，用户可以直接加载配置，无需重新选择路径。
4. **窗口特性**：窗口大小固定为500x400，程序启动时自动居中并置顶显示，为用户提供更好的操作体验。
5. **菜单栏功能**：拥有菜单栏，包含“文件”和“关于”菜单。“文件”菜单下有“保存配置”和“加载配置”选项，方便用户管理配置；“关于”菜单用于显示程序的相关信息。

## 三、使用说明

1. **选择文件夹**：点击“选择源文件夹”和“选择目标文件夹”按钮，在弹出的文件选择对话框中分别选择要移动的源文件夹和目标文件夹。
2. **移动文件夹**：选择好源文件夹和目标文件夹后，点击“移动文件夹”按钮，程序将执行文件夹移动操作，并在界面上显示操作状态，如成功或错误信息。
3. **保存配置**：若希望保存当前选择的文件夹路径，点击“文件”菜单中的“保存配置”选项。在弹出的保存文件对话框中选择保存位置并确认，配置文件将以 `.mfc`后缀保存。
4. **加载配置**：要加载之前保存的配置，点击“文件”菜单中的“加载配置”选项。在弹出的打开文件对话框中选择相应的配置文件，程序会自动填充源文件夹和目标文件夹路径。
5. **查看关于信息**：点击“关于”菜单中的“关于本程序”选项，可查看程序的简要介绍。

## 四、安装指南

1. **前提条件**：
   - 确保系统已安装Python 3.x。
   - 对于Tkinter版本，无需额外安装库，因为Tkinter是Python标准库的一部分。
   - 若使用PyQt5版本，需通过
     ```
     pip install PyQt5
     ```

     安装PyQt5库。
   - 如果要创建可执行文件（仅限Windows），需使用
     ```
     pip install pyinstaller
     ```

     安装 `pyinstaller`库。
2. **克隆仓库**：
   - 打开命令行工具，导航到本地希望存储项目的目录。
   - 运行
     ```
     git clone https://github.com/AKAAKUNLEE/move_folder.git
     ```

     从GitHub仓库克隆项目代码到本地。
3. **运行应用程序**：
   - **Python脚本方式**：在命令行中进入项目目录，运行
     ```
     python move_folder.py
     ```

     （假设主Python文件名为 `move_folder.py`）。
   - **可执行文件方式（仅限Windows）**：使用 `pyinstaller`将Python脚本打包成可执行文件后，在 `pyinstaller`生成的 `dist`文件夹中找到生成的 `.exe`文件，双击运行应用程序。

## 五、仓库结构

1. **`move_folder.py`**：基于Tkinter实现图形界面和文件夹移动功能的主Python脚本。
2. **`move_folder_pyqt.py`**：使用PyQt5实现图形界面的替代版本脚本。
3. **`associate_mfm.reg`**：Windows系统下用于将应用程序与自定义文件后缀（如 `.mfm`）相关联的注册表文件（若有此需求）。
4. **`README.md`**：即本文件，提供项目的详细说明。

## 六、未来规划

1. **跨平台文件关联**：目前自定义文件关联仅在Windows系统实现，计划未来在macOS和Linux系统上也支持类似功能。
2. **增强错误处理**：进一步完善错误处理机制，更友好地处理诸如权限不足、磁盘空间不足等各类错误情况。
3. **多语言支持**：添加多语言支持，使程序能服务全球更多用户。

## 七、贡献方式

非常欢迎大家为这个项目贡献力量！如果您发现了任何错误、有新功能的想法，或者希望改进现有代码，欢迎在GitHub仓库中提出问题（Issues）或提交拉取请求（Pull Requests）。

## 八、许可证

本项目基于[MIT]许可证发布。详细信息请查看项目中的 `LICENSE`文件。
