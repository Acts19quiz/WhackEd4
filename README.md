# WhackEd4

## Description

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

## Dependencies

WhackEd4 is built with Python 2.7, wxPython and PyAudio. The user interface is designed using wxFormBuilder.
To build the setup executable you will need cx_Freeze and Inno Setup.

For detailed build instructions, visit the local Wiki, [Detailed build instructions (Windows only)](https://github.com/Acts19quiz/WhackEd4/wiki/Detailed-build-instructions-(Windows-only)).

## About

This is a [forked version](https://github.com/GitExl/WhackEd4/commits?after=25cd23dbc3968c4b1d385177884953bd5a18158e+104) of WhackEd4 version 1.2.2. Specifically, it's forked from [a commit](https://github.com/GitExl/WhackEd4/commit/ac38c2e6ddb4bd7caaf6dd62b7e91f6427524e4a) between 1.2.2 and 1.2.3. The reasons for this fork's existence:

- Compiling with Python 3 (instead of 2.7) in WhackEd4 v1.2.3 introduced new crashes. The primary one of note is that in the ZDaemon configuration, when going to the Things editor, and selecting the "Game" or "Render style" drop-down menus, picking any option will cause a crash. There are other random crashes, as well, such as when having the program open for an extended time and having the program out of focus for awhile. I'm not certain of the exact reproduction steps.
- v1.2.3's Python 3 upgrade also introduced the concept of inputting floating point numbers (i.e., numbers with decimal points) into a Thing's Radius and Height properties. Seeing a Height of "16.0" displayed encourages the idea of putting in "56.0" or something similar. The problem here is that WhackEd4 doesn't support floating point numbers for Radius and Height in DEH or BEX patches. Loading them back will make WhackEd4 strip these edits from your patches. Even if you put in "56", WhackEd4 will append ".0" to the end when going between WhackEd4 windows. Restoring all of my Radius and Height edits in a big, complicated patch can be a time consuming process.
- v1.3.0 introduced a tabbed Things editor, where information for Things are separated into several tabs. Having the Things editor de-cluttered in this fashion is beneficial in some situations. However, I spend a lot of time directly comparing all changes made between two things, and the tabbed display would multiply my work time exponentially. Added to this is the fact that all of the freed up real estate goes to the right hand table showing a list of Thing names. Having the ability to see Things with a name of two hundred or so characters isn't as beneficial to me in this situation (particularly when WhackEd4 only supports Thing names of sixty-four characters, making the freed space moot).
- Desired support for a number of ZDaemon and MBF21 modifiers, and DEH-style string replacements not in the original doom19 and doom19u tables, that heretofore have required hand-edited patches. WhackEd4 can't preserve this extraneous information when loading such patches.

Credit Greg Lewis for the original DeHacked, and Exl for the original WhackEd4. This fork of the former is by Acts 19 quiz. The RSKU sprite from the preview banner is from [DOOM HD weapons and objects mod](https://www.moddb.com/mods/doom-hd-weapons-and-objects). WhackEd4 REDSKULL is publically provided in the hopes that someone else might find its niche purposes useful.
