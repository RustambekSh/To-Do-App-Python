# styles.py

# Colors
BACKGROUND_COLOR = "#2E3440"
TEXT_COLOR = "#D8DEE9"
BUTTON_COLOR = "#5E81AC"
DELETE_BUTTON_COLOR = "#BF616A"
PROGRESS_BAR_COLOR = "#5E81AC"
PRIORITY_HIGH_COLOR = "#BF616A"
PRIORITY_MEDIUM_COLOR = "#EBCB8B"
PRIORITY_LOW_COLOR = "#A3BE8C"
DUE_DATE_COLOR = "#81A1C1"
TAGS_COLOR = "#88C0D0"
COMPLETED_COLOR = "#A3BE8C"  # Green for completed tasks
TIMER_COLOR = "#EBCB8B"  # Yellow for timed tasks

# Fonts
FONT_FAMILY = "Arial"
FONT_SIZE = 14
HEADER_FONT_SIZE = 24

# Styles
INPUT_STYLE = f"""
    padding: 8px; 
    font-size: {FONT_SIZE}px; 
    border: 1px solid #4C566A; 
    border-radius: 10px;
"""

BUTTON_STYLE = f"""
    background-color: {BUTTON_COLOR}; 
    color: white; 
    padding: 8px; 
    font-size: {FONT_SIZE}px; 
    border: none; 
    border-radius: 10px;
"""

DELETE_BUTTON_STYLE = f"""
    background-color: {DELETE_BUTTON_COLOR}; 
    color: white; 
    padding: 8px; 
    font-size: {FONT_SIZE}px; 
    border: none; 
    border-radius: 10px;
"""

PROGRESS_BAR_STYLE = f"""
    QProgressBar {{ 
        background-color: #3B4252; 
        color: {TEXT_COLOR}; 
        border-radius: 5px; 
    }}
    QProgressBar::chunk {{ 
        background-color: {PROGRESS_BAR_COLOR}; 
        border-radius: 5px; 
    }}
"""

COMPLETED_TASK_STYLE = f"""
    background-color: {COMPLETED_COLOR}; 
    color: {TEXT_COLOR}; 
    border-radius: 10px; 
    padding: 8px;
"""

TIMER_TASK_STYLE = f"""
    background-color: {TIMER_COLOR}; 
    color: {TEXT_COLOR}; 
    border-radius: 10px; 
    padding: 8px;
"""