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
