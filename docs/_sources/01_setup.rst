Desktop Environment 
===================

The environment setup is the first step to start working with the Touch Dot S3 board.
The following steps will guide you through the setup process.

1. Install the required software
2. Set up the development environment
3. Install the required libraries
4. Set up the board


Install the required software
-----------------------------

The following software is required to start working with the Touch Dot S3 board:

1. **Git**: Git is required to clone the Touch Dot S3 board repository.
2. **Python 3.7 or later (Optional)**: Python is required to run the scripts and tools provided by the Touch Dot S3 board.
3. **Visual Studio Code**: Visual Studio Code is a code editor that is required to write and compile the code.


This section will guide you through the installation process of the required software.

Visual Studio Code
------------------

Visual Studio Code is a code editor that is required to write and compile the code.

To install Visual Studio Code, follow the instructions below:

1. Download the Visual Studio Code installer from the

    .. raw:: html
        
        <a href="https://code.visualstudio.com/download" target="_blank">Visual Studio Code website</a>


2. Run the installer and follow the instructions.

.. figure:: /_static/img/vscode.png
    :width: 80%
    :align: center

    Visual Studio Code installer

.. note::

    During the installation process, make sure to check the box that says "Open with Code".


3. Open a terminal and run the following command to verify the installation:

.. code-block:: bash

   code --version

4. Install extensions for Visual Studio Code:

    .. figure:: /_static/img/vscode_gf.png
        :width: 80%
        :align: center

        Visual Studio Code extensions


Arduino IDE Installation
------------------------

The Arduino IDE is a popular open-source platform for building and programming microcontroller-based projects. It provides a user-friendly interface and a wide range of libraries to simplify the development process.

To install the Arduino IDE, follow the instructions below:

1. Download the Arduino IDE installer from the

    .. raw:: html

        <a href="https://www.arduino.cc/en/software/" target="_blank">Arduino IDE download page</a>

2. Run the installer and follow the instructions.

3. For additional guidance, refer to the

    .. raw:: html

        <a href="https://wiki.uelectronics.com/tutoriales/inicio-arduino" target="_blank">Arduino Compatibility Guide</a>

.. figure:: /_static/img/arduino_ide.png
    :width: 80%
    :align: center

    Arduino IDE installation


Thonny IDE Installation
-----------------------

Thonny is a Python IDE designed for beginners. It provides a simple interface and built-in support for MicroPython, making it an excellent choice for programming the Touch Dot S3 board.

To install Thonny IDE, follow the instructions below:

1. Download the Thonny IDE installer from the

    .. raw:: html

        <a href="https://thonny.org/" target="_blank">Thonny IDE download page</a>

2. Run the installer and follow the instructions.

3. For MicroPython support documentation, visit the

    .. raw:: html

        <a href="https://wiki.uelectronics.com/tutoriales/inicio-arduino" target="_blank">MicroPython Compatibility Guide</a>

.. figure:: /_static/img/thonny_ide.png
    :width: 80%
    :align: center

    Thonny IDE installation



Git
---

Git is a version control system that is required to clone the repositories in general.
To install Git, follow the instructions below:

1. Download the Git installer from the

    .. raw:: html
        
        <a href="https://git-scm.com/downloads" target="_blank">Git website</a>

2. Run the installer and follow the instructions.
3. Open a terminal and run the following command to verify the installation:

.. code-block:: bash

   git --version

If the installation was successful, you should see the Git version number.


Python 3.7 or later (Optional)
------------------------------

Python is a programming language that is required to run the scripts and tools, 

To install Python, follow the instructions below:

1. Download the Python installer from the:

    .. raw:: html
        
        <a href="https://www.python.org/downloads/" target="_blank">Python website</a>

2. Run the installer and follow the instructions.

.. figure:: /_static/img/python.png
    :width: 80%
    :align: center

    Add python to PATH


.. attention::

   Make sure to check the box that says "Add Python to PATH" during the installation process.

Open a terminal and run the following command to verify the installation:

.. code-block:: bash

   python --version

If the installation was successful, you should see the Python version number.



