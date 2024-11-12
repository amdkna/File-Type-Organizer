@echo off
rem FileType Organizer Launcher
rem Author: Arash Naderian (amdkna)
rem Project Repository: https://github.com/amdkna/File-Type-Organizer
rem 
rem This batch file serves as a launcher for the Python FileType Organizer script.
rem It allows you to run the Python script with command-line arguments by calling this .bat file.

rem Ensure that the path to the Python script is correctly specified.
rem Replace the path below if your Python script is located elsewhere.
rem For example, if you moved the script to "D:\Scripts", update the path like this:
rem python D:\Scripts\filetype-organizer.py %*

python C:\A\py\Tools\filetype_organizer\filetype-organizer.py %*
