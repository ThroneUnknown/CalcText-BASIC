COMING SOON: .exe version

---CalcText-BASIC---
BasicText CE is a utitily for writing code in Ti-BASIC meant to be used when writing programs primarily used to display text to the user (using the Draw screen) to automate a few issues with it. At a base level, this can be used to just simplify the process of writing these files by removing extraneous syntax, but actually can be used for much more.

FEATURES:
 - Character/Word wrapping around lines and pages
 - Automatically execute code at beginning of line, end of line, page
 - QOL features including simplification of text command
 - Add your own shortcuts for executing code
 - Highly customizable: change commands of what happens at the end of a line or page within your TI-BASIC program.

USAGE:
 - Must have python installed to run program, recommended version is 3.11 but anything above 3.6 should work. (NOTE: .exe version coming soon)
Windows: python calctext.py [input file] [output file]
Linux: python calctext.py [input file] [output file]
Example: python calctext.py noteinput.txt notes.txt

SYNTAX:
All commands 
NOTE: all commands in TI-BASIC will be run as is without modifications, so the color and position variables only matter if it is pseudocode using ,text

([y],[x])         Sets the position where the next text will be drawn.
              Rather than setting the position, it can be incremented by putting + or - before the number, or kept the same by not putting a number at all:
              Examples: (-3,) (,+5) (2,3)

<p>...</p>	  Set the code that will be executed for each new page.
              Inside the tags, any TI-BASIC code or pseudocode can be included, and can span multiple lines. Make sure that no unnecessary characters are included.
              Default: <p>Pause 
                       ClrDraw 
                       (0,0)</p>

<l>...</l>    Set the code that will be executed after each line.
              Inside the tags, any code or commands can be included, and can span multiple lines. Make sure that no unnecessary characters are included.
              Default: <l>(+12,)</l>

<b>...</b>    Set the code that will be executed at the beginning of each line

[character]TRIGGER [trigger]     Sets the trigger for a specific tag, such as <b>, <l>, <p>, or any user defined tags.
              Examples: aTRIGGER @@@ or fbTRIGGER BLINE
                                 
<[character]>...</[character]>   Used to set a tag, similar to <b> and <p>, but is not automatically run at any time. Instead a trigger must be set (eg. @@@)

,[text]         Replaced with Text(y,x,text) using the color that was last defined. The default character is , but can be defined with the TCHAR command.

;;;           Triggers new page immediately, can be changed with the TRIGGER command

,,,           Triggers new line immediately, can be changed with the TRIGGER command

TCHAR [text]  Set the default text at the beginning of a line that determines if it will be replaced with the default Text( command
              Default: ,

WWRAP [num]   Set if words are wrapped or just characters, eg. if a word will be split at the end of the line (half on one line, half on the next) or not.
              If 1, words are wrapped instead of characters.
			  Default: 1

SPLIT [text]  Sets the character that splits words apart, determines what is wrapped and what isn't.
              Default:   (literally just a space)

`             Splits line into multiple commands
              Example for <p>: Pause `(0,0)`BLACK

[Color]       Set the color that is used for all TCHAR Text( commands will use, defaults to black.
              Example: GRAY  (Yes its literally that simple)



EXAMPLE:
<p>Pause 
ClrDraw 
BLUE
(0,0)`,Gases
Line(~10,8,10,8
(18,0)</p>
;;;
,Gas Laws:
BLACK`(,+10)
,Boyle's Law:
GRAY`,Pressure and volume have an inverse relationship: P=1/V
BLACK`,Charle's Law:
GRAY`,Pressure and temperature have a proportional relationship: P=T
BLACK`,Avogadro's Law:
GRAY`,Pressure and moles of have a proportional relationship: P=n
,This is some more filler so i can test the overflow onto the next page, Ok this should be enough filler.
Pause

===========
converts to
===========

Pause 
ClrDraw 
TextColor(BLUE
Text(0,0,"Gases"
Line(~10,8,10,8
Text(18,0,"Gas Laws:"
TextColor(BLACK
Text(30,10,"Boyle's Law:"
TextColor(GRAY
Text(42,10,"Pressure and volume have an "
Text(54,10,"inverse relationship: P=1/V"
TextColor(BLACK
Text(66,10,"Charle's Law:"
TextColor(GRAY
Text(78,10,"Pressure and temperature have a "
Text(90,10,"proportional relationship: P=T"
TextColor(BLACK
Text(102,10,"Avogadro's Law:"
TextColor(GRAY
Text(114,10,"Pressure and moles of have a "
Text(126,10,"proportional relationship: P=n"
Text(138,10,"This is some more filler so i can test "
Text(150,10,"the overflow onto the next page, Ok "
Pause 
ClrDraw 
TextColor(BLUE
Text(0,0,"Gases"
Line(~10,8,10,8
TextColor(GRAY
Text(18,10,"this should be enough filler."
Pause
