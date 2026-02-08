# Simple  Log analyzer (python)
This project is a small Python tool that analyzes SSH log files.

## What does it
- Detects failed SSH login attempts
-  Counts how often an IP address appears
-  Highlights suspicious IPs based on a threshold

## How it works (Short form)
- Reads the log file line by line 
- Filters for "Failed password"
- Extracts IP addresses
- Counts occurrences using Python Counter

## How to Run it
- Make sure that sampe.log and log_analyzer.py are in the same folder
- Then run The Python script and you are good to go
