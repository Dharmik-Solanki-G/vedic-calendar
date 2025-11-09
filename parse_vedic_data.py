# Script to parse all Vedic calendar TXT files and generate JavaScript data
# This will be used to create comprehensive event arrays

import os
import re
from datetime import datetime

def parse_date(date_str):
    """Parse date string to JavaScript Date object format"""
    months = {
        'January': 0, 'February': 1, 'March': 2, 'April': 3,
        'May': 4, 'June': 5, 'July': 6, 'August': 7,
        'September': 8, 'October': 9, 'November': 10, 'December': 11,
        'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3,
        'May': 4, 'Jun': 5, 'Jul': 6, 'Aug': 7,
        'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
    }
    
    # Try different date formats
    patterns = [
        r'(\w+)\s+(\d+),\s+(\d+)',  # January 2, 2026
        r'(\d+)\s+(\w+)\s+(\d+)',   # 2 January 2026
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str)
        if match:
            if len(match.groups()) == 3:
                if match.group(1).isdigit():
                    day, month_name, year = match.groups()
                else:
                    month_name, day, year = match.groups()
                
                month = months.get(month_name)
                if month is not None:
                    return f"new Date({year}, {month}, {int(day)})"
    return None

def parse_time(time_str):
    """Parse time string"""
    match = re.search(r'(\d{1,2}):(\d{2})\s*(AM|PM)', time_str, re.IGNORECASE)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2))
        ampm = match.group(3).upper()
        if ampm == 'PM' and hour != 12:
            hour += 12
        elif ampm == 'AM' and hour == 12:
            hour = 0
        return f"{hour}, {minute}"
    return "0, 0"

# This script would parse all files and generate the data
# For now, I'll create the comprehensive calendar directly

