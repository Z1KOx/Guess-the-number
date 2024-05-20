@echo off

rem Change directory to the location of the python script
cd src
if errorlevel 1 (
    echo Failed to change directory to src. Exiting...
    ping 127.0.0.1 -n 3 > nul
    exit
)

rem Execute python script
python main.py