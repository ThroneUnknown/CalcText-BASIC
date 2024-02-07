# CalcText-BASIC
BasicText CE is a utitily for writing code in Ti-BASIC meant to be used when writing programs primarily used to display text to the user (using the Draw screen) to automate a few issues with it. At a base level, this can be used to just simplify the process of writing these files by removing extraneous syntax, but actually can be used for much more.

### FEATURES:
 - Character/Word wrapping around lines
 - Automation of incrementing pages when one is filled (Pauses, then goes to next page)
 - Text alignment
 - Automation of incrementing lines (Increments pixels to next line)
 - Quality of life, you don't have to write out Text(x,y,"foobar"), but rather just ,foobar to show text
 - Highly customizable: change commands of what happens at the end of a line or page within your TI-BASIC program.

### USAGE:
 - Must have python installed to run program, recommended version is 3.11 but anything above 3.6 should work.
 - Windows: python basictextce.py [input file] [output file]
 - Linux: python basictextce.py [input file] [output file]

Commands can be found in README.txt