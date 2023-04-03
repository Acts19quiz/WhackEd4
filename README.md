WhackEd4
========

Description
-----------
As a replacement for the DOS-based Dehacked, WhackEd4 allows you to load and edit Doom Dehacked files.
It also expands on the features of the original Dehacked:

- A configurable workspace with separate editor windows.
- Sprite previews from a loaded IWAD and PWADs.
- Full support for Boom's extensions such as codepointer and thing flag mnemonics.
- State animation preview with sound playback (where possible).
- Editing multiple states at the same time.
- Filtering the displayed list of states by thing states, weapon states or unused states.
- Does not require a Doom executable, but reads engine data from table files.
- State highlighting based on sprite index.
- Separate undo actions for every editor window.
- Copy and pasting things and states.
- Support for DeHackEd features of Doom 1.9, The Ultimate Doom 1.9, Boom, Marine's Best Friend, Doom Retro and ZDaemon.

Dependencies
------------
WhackEd4 is built with Python 2.7, wxPython and PyAudio. The user interface is designed using wxFormBuilder.
To build the setup executable you will need cx_Freeze and Inno Setup.

Detailed build instructions (Windows-only)
------------
* Download Python 2.7.18 (Python 3.x WILL NOT work!). https://www.python.org/downloads/release/python-2718/
  * Choose "Windows x86 MSI installer".
    * IMPORTANT! Even if you are on Windows 64-bit, this version of WhackEd is 32-bit-only, so everything you'll be downloading will be 32-bit versions.
* Run the Python 2.7 installer. On Windows, install in the default directory of C:\Python27\
* We need to customize Python 2.7.
  * When the window says "Customize Python 2.7", make sure "pip" is set to install. You can find it under "Python>pip".
  * Also go to the bottom and enable "Python>Add python.exe to Path". This might be disabled by default!
* Don't worry if you already have Python 3 installed. You can have both! You will just need to remember to use "pip3" when installing modules for Python 3, and "pip2" for Python 2.
* We need to install cx_Freeze 5.x (NOT 6!) manually.
  * Go to https://pypi.org/project/cx-Freeze/5.1.1/
  * Download "cx_Freeze-5.1.1-cp27-cp27m-win32.whl".
  * Open up "Command Prompt".
  * Wherever you downloaded "cx_Freeze-5.1.1-cp27-cp27m-win32.whl" to, type "cd " in Command Prompt, then the directory.
  * Type "pip2 install cx_Freeze-5.1.1-cp27-cp27m-win32.whl", and hit Enter.
* We'll repeat the process we took with cx_Freeze to install PyAudio. https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
  * Download "PyAudio-0.2.11-cp27-cp27m-win32.whl".
* Now we need wxPython. https://sourceforge.net/projects/wxpython/files/wxPython/3.0.2.0/
  * Download "wxPython3.0-win32-3.0.2.0-py27.exe". Just run the EXE, since we don't need pip2 here.
* OPTIONAL: If you want to create an installer:
  * Download Inno Setup. The most recent version (6.2.2 as of now) will work here. https://jrsoftware.org/isdl.php
  * If you download version 6, you'll need to change "build-release-package.cmd" in the WhackEd source. Change "set setup_compiler" from "Inno Setup 5" to "Inno Setup 6".
* OPTIONAL: If you want a 7z archive:
  * We need 7-zip. https://7-zip.org/download.html The latest version will work. Get "7-Zip Extra: standalone console version".
  * Unzip it.
  * We need to add 7-zip to the Windows "Path" Environment Variable.
    * Go to Control Panel, and search for "Environment".
    * Select "Edit the system environment variables".
    * When you make it to the "System Properties" window, select "Environment Variables..."
    * In the lower section that says "System variables", look down until you get to "Path". Select that, then hit "Edit...".
    * Select "New", and type "C:\****\7z####-extra" (or wherever you extracted the console version of 7-zip). Fill in the #s with the 7-zip version you downloaded. Hit "OK".
* Run "build-release-package.cmd".
  * If everything went well, the process will complete, there will be no errors, and you'll have the following in your WhackEd4 directory:
    * The program in the "build" directory.
    * "whacked4-setup-1.2.0.exe" in the root WhackEd4 directory (if you chose to create the Inno Setup installer).
    * "whacked4-1.2.0.7z" in the root WhackEd4 directory (if you chose to create the 7z archive).

Files changed from stock WhackEd 1.2.0
------------
\build-release-package.cmd
>"Inno Setup 5" to "Inno Setup 6"
>Add "-REDSKULL" to 7-zip instructions.
\README.md
\whacked4.iss
>Add "-REDSKULL" to "OutputBaseFilename".
