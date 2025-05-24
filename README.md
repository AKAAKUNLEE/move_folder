# Move Folder GUI Application

🌐 [简体中文](README_zh-CN.md) | [English](README.md)

## Introduction

This is a simple yet practical Python - based GUI application designed to facilitate the movement of folders on your computer. Whether you are a novice user looking for an easy - to - use tool or a professional needing to streamline your file management tasks, this application can come in handy.

## Features

1. **User - Friendly GUI**: Built using either Tkinter or PyQt5 (the choice depends on the implementation), the application offers an intuitive graphical interface. Users can easily select the source and destination folders through dedicated buttons, eliminating the need for complex command - line operations.
2. **Folder Moving Functionality**: The core feature of this application is its ability to move entire folders from one location to another. It utilizes Python's `shutil` module to perform this operation, ensuring reliability and efficiency.
3. **Configuration Saving**: The application allows users to save the source and destination folder paths as a custom - formatted configuration file (with a user - defined suffix like `.mfc`). This means that if you frequently move folders between the same two locations, you don't need to re - select the paths every time. Just load the saved configuration, and you're good to go.
4. **Custom File Association (Windows - specific)**: For Windows users, the application can be associated with a custom file suffix (e.g.,.mfm). This means that by double - clicking on a file with this custom suffix, the application will launch, potentially with some context related to the clicked file (although in this case, mainly for convenience in launching the folder - moving tool).

## How to Use

1. **Select Folders**: Click the "Select Source Folder" and "Select Destination Folder" buttons to choose the folders you want to move from and to, respectively.
2. **Move Folder**: After selecting the folders, click the "Move Folder" button. The application will then attempt to move the source folder to the destination folder. A status message will be displayed indicating whether the operation was successful or if any errors occurred.
3. **Save Configuration**: If you want to save the current source and destination folder paths for future use, click the "Save Configuration" button. You will be prompted to choose a location to save the configuration file with the custom suffix (e.g.,.mfc).
4. **Load Configuration**: To load a previously saved configuration, click the "Load Configuration" button and select the appropriate configuration file. The application will then populate the source and destination folder fields with the saved paths.

## Installation

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - For the Tkinter - based version, no additional libraries need to be installed as Tkinter is part of the Python standard library. For the PyQt5 - based version, you need to install PyQt5 using `pip install PyQt5`.
   - If you plan to create the executable and use the custom file association (Windows - only), you need to install `pyinstaller` using `pip install pyinstaller`.
2. **Clone the Repository**:
   - Navigate to the directory where you want to store the project on your local machine.
   - Run `git clone [repository - url]` to clone the project from the GitHub repository.
3. **Running the Application**:
   - For the Python script: Navigate to the project directory in the command line and run `python move_folder.py` (assuming the main Python file is named `move_folder.py`).
   - For the executable (Windows - only, after creating with `pyinstaller`): Locate the generated `exe` file in the `dist` folder created by `pyinstaller` and double - click on it to run the application.

## Repository Structure

- **`move_folder.py`**: The main Python script containing the code for the Tkinter - based GUI and folder - moving functionality.
- **`move_folder_pyqt.py`**: An alternative implementation using PyQt5 for the GUI.
- **`associate_mfm.reg`**: A Windows - specific registry file used to associate the application with the custom file suffix (e.g.,.mfm).
- **`README.md`**: This file, providing an overview of the project, its features, usage, and installation instructions.

## Future Improvements

1. **Cross - Platform File Association**: Currently, the custom file association is only implemented for Windows. In the future, efforts could be made to support similar functionality on macOS and Linux systems.
2. **Enhanced Error Handling**: While basic error handling is in place for folder moving operations, more comprehensive error handling could be added to handle cases such as insufficient permissions, disk full errors, etc., in a more user - friendly way.
3. **Multi - language Support**: Adding support for multiple languages to make the application more accessible to a global audience.

## Contributing

Contributions to this project are welcome! If you find any bugs, have suggestions for new features, or want to improve the existing code, feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT] license. See the `LICENSE` file for details.
