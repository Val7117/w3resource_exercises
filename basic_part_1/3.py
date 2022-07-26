#!/usr/bin/env python3

# Display the current date and time

from datetime import datetime

date_time = datetime.now()
resultString = str(date_time)[:-7]
print(f"Current date and time:\n{resultString}")
