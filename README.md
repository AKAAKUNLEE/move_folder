# Folder Moving GUI Application

<div align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.6+-blue.svg" alt="Python"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
<a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/GUI-Tkinter-orange.svg" alt="Tkinter"></a>
<a href="https://www.pyinstaller.org/"><img src="https://img.shields.io/badge/Packaging-PyInstaller-brightgreen.svg" alt="PyInstaller"></a>
<a href="https://github.com/AKAAKUNLEE/move_folder/releases"><img src="https://img.shields.io/github/v/release/AKAAKUNLEE/move_folder" alt="Releases"></a>
</div>

🌐 [English](README.md) | [简体中文](README_zh-CN.md)

## 1. Project Overview

This is a GUI (Graphical User Interface) application developed in Python for moving folders. It provides users, whether novice or professional, with a convenient way to manage folder relocation tasks on their computers.

## 2. Features

1. **Intuitive Graphical Interface**: Built with either Tkinter or PyQt5, the application offers an easy-to-use interface. Users can effortlessly select the source and destination folders through dedicated buttons, eliminating the need for complex command-line operations.
2. **Folder Moving Functionality**: Leveraging Python's `shutil` module, it can reliably and efficiently move folders from one location to another.
3. **Configuration Saving and Loading**: Supports saving the paths of the source and destination folders as a configuration file with a custom suffix (e.g., `.mfc`). Users can load the configuration later, avoiding the need to re-select the paths every time.
4. **Window Characteristics**: The window size is fixed at 500x400. When the application starts, the window is automatically centered and置顶, providing a better user experience.
5. **Menu Bar Functionality**: Features a menu bar with "File" and "About" menus. The "File" menu contains options for "Save Configuration" and "Load Configuration" to facilitate configuration management, while the "About" menu displays information about the application.

## 3. Usage Instructions

1. **Select Folders**: Click the "Select Source Folder" and "Select Destination Folder" buttons. In the pop-up file selection dialogs, choose the source folder to be moved and the destination folder respectively.
2. **Move Folders**: After selecting the source and destination folders, click the "Move Folder" button. The application will execute the folder-moving operation and display the operation status, such as success or error messages, on the interface.
3. **Save Configuration**: To save the currently selected folder paths, click the "Save Configuration" option in the "File" menu. In the pop-up save file dialog, select the save location and confirm. The configuration file will be saved with a `.mfc` suffix.
4. **Load Configuration**: To load a previously saved configuration, click the "Load Configuration" option in the "File" menu. In the pop-up open file dialog, select the corresponding configuration file, and the application will automatically fill in the source and destination folder paths.
5. **View About Information**: Click the "About This Program" option in the "About" menu to view a brief introduction to the application.

## 4. Installation Guide

1. **Prerequisites**:
   - Ensure that Python 3.x is installed on the system.
   - For the Tkinter version, no additional libraries need to be installed as Tkinter is part of the Python standard library.
   - If using the PyQt5 version, install the PyQt5 library via:
     ```bash
     pip install PyQt5
     ```
   - If creating an executable file (Windows only), install the `pyinstaller` library using:
     ```bash
     pip install pyinstaller
     ```
2. **Clone the Repository**:
   - Open the command-line tool and navigate to the local directory where you want to store the project.
   - Run:
     ```bash
     git clone https://github.com/AKAAKUNLEE/move_folder.git
     ```
3. **Run the Application**:
   - **Python Script Method**: Enter the project directory in the command line and run:
     ```bash
     python move_folder.py
     ```
   - **Executable File Method (Windows only)**: After using `pyinstaller` to package the Python script into an executable file, find the generated `.exe` file in the `dist` folder created by `pyinstaller` and double-click to run the application.

## 5. Repository Structure

1. **`move_folder.py`**: The main Python script implementing the graphical interface and folder-moving functionality based on Tkinter.
2. **`move_folder_pyqt.py`**: An alternative version of the script using PyQt5 to implement the graphical interface.
3. **`associate_mfm.reg`**: A registry file for Windows systems to associate the application with a custom file suffix (e.g., `.mfm`) if needed.
4. **`README.md`**: This file, providing detailed project documentation.

## 6. Future Plans

1. **Cross-Platform File Association**: Currently, custom file association is only implemented on Windows. Plans are underway to support similar functionality on macOS and Linux systems in the future.
2. **Enhanced Error Handling**: Further improve the error-handling mechanism to more gracefully handle various error conditions, such as insufficient permissions and low disk space.
3. **Multilingual Support**: Add multilingual support to make the application accessible to a global user base.

## 7. Contribution Guidelines

Contributions to this project are highly welcome! If you find any bugs, have ideas for new features, or wish to improve the existing code, please feel free to raise issues or submit pull requests in the GitHub repository.

## 8. License

This project is licensed under the [MIT]. For detailed information, please refer to the `LICENSE` file in the project.
