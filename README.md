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
WhackEd4 is built with [Python 3.7](https://www.python.org/downloads/release/python-379/), [wxPython](https://pypi.org/project/wxPython/), and PyAudio. The user interface is designed using [wxFormBuilder v3.9.0](https://github.com/wxFormBuilder/wxFormBuilder/releases/tag/v3.9.0) (or later).
To build the setup executable you will need [cx_Freeze 6.x](https://pypi.org/project/cx-Freeze/#history) and [Inno Setup 6.x](https://jrsoftware.org/isdl.php).

About
-----
This is a [forked version](https://github.com/GitExl/WhackEd4/commits?after=25cd23dbc3968c4b1d385177884953bd5a18158e+34) of the (until now!) un-released WhackEd4 version 1.2.4. Specifically, it's forked from [a commit](https://github.com/GitExl/WhackEd4/commit/6360ccee77339ce0ebc38cbee5a15a0fa2962981) between 1.2.4 and 1.3.0 beta (1).

The reason for selecting that commit is that it's the last working commit before the [introduction of the Things tab editor](https://github.com/GitExl/WhackEd4/commit/880b4bbb6be8b429fbb324d20d576e877721338b). [This commit](https://github.com/GitExl/WhackEd4/commit/218e6cf4303ba7622655d6859702ace5c7b25846) (and many after it) are non-working developer builds.

The reasons for this fork's existence:

- v1.2.3's Python 3 upgrade introduced the concept of inputting fixed point numbers (i.e., numbers with a set number of decimal points) into a Thing's Radius and Height properties. Earlier versions of WhackEd4 with this functionality had an issue where patches would be saved with ".0" appended to Radius and Height lines, and could cause those lines to be discarded upon load due to invalid data. This could cost users a lot of time in a time-consuming restoration process for a large patch. To expedite patch editing and make it a lot faster, this functionality (that 99% of users will never use) was removed.
- v1.3.0 introduced a tabbed Things editor, where information for Things are separated into several tabs. Having the Things editor de-cluttered in this fashion is beneficial in some situations (all of the freed real estate goes to the right hand table column that shows Thing names, which can now theoretically display names of around two-hundred characters, though WhackEd4 has a hard limit of sixty-four). However, I spend a lot of time directly comparing all changes made between two things, and the tabbed display would multiply my work time exponentially. This helps me more than widening the Thing name column.
- Desired support for a number of ZDaemon and MBF21 modifiers, and DEH-style string replacements not in the original doom19 and doom19u tables, that heretofore have required hand-edited patches. WhackEd4 can't preserve this extraneous information when loading such patches.
- A number of improvements and fixes (caused by the Python 3 upgrade) were moved downstream to the pre-Things tabs version, including [chex.wad and chex3.wad compatibility](https://github.com/GitExl/WhackEd4/commit/7cb4d525331a83f248d57bee98ea554a3ac20403), and crashes in the ZDaemon configuration with the "Game" and "Render style" drop-down menus.

Credit Greg Lewis for the original DeHacked, and Exl for the original WhackEd4. This fork of the former is by Acts 19 quiz. The RSKU sprite from the preview banner is from [DOOM HD weapons and objects mod](https://www.moddb.com/mods/doom-hd-weapons-and-objects). WhackEd4 REDSKULL is publicly provided in the hopes that someone else might find its niche purposes useful.

