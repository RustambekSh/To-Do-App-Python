
BACKGROUND_COLOR = "#FFFFFF"  # White
TEXT_COLOR = "#333333"  # Dark Gray
PRIMARY_COLOR = "#B4D4EE"  # Soft Blue
SECONDARY_COLOR = "#FFD700"  # Gold (for accents)
DANGER_COLOR = "#FF6B6B"  # Soft Red (for errors/danger)
CARD_COLOR = "#F5F5F5"  # Light Gray (for cards/widgets)

# Fonts
FONT_FAMILY = "Arial"
FONT_SIZE = 14
HEADER_FONT_SIZE = 24

# Styles
INPUT_STYLE = f"""
    padding: 8px; 
    font-size: {FONT_SIZE}px; 
    border: 1px solid #CCCCCC; 
    border-radius: 10px;
    background-color: {CARD_COLOR}; 
    color: {TEXT_COLOR};
"""

BUTTON_STYLE = f"""
    background-color: {PRIMARY_COLOR}; 
    color: {TEXT_COLOR}; 
    padding: 8px; 
    font-size: {FONT_SIZE}px; 
    border: none; 
    border-radius: 10px;
"""

SECONDARY_BUTTON_STYLE = f"""
    background-color: {SECONDARY_COLOR}; 
    color: {TEXT_COLOR}; 
    padding: 8px; 
    font-size: {FONT_SIZE}px; 
    border: none; 
    border-radius: 10px;
"""

DELETE_BUTTON_STYLE = f"""
    background-color: {DANGER_COLOR}; 
    color: {TEXT_COLOR}; 
    padding: 8px; 
    font-size: {FONT_SIZE}px; 
    border: none; 
    border-radius: 10px;
"""

CARD_STYLE = f"""
    background-color: {CARD_COLOR}; 
    color: {TEXT_COLOR}; 
    border-radius: 10px; 
    padding: 8px;
"""

PROGRESS_BAR_STYLE = f"""
    QProgressBar {{
        background-color: {CARD_COLOR}; 
        color: {TEXT_COLOR}; 
        border-radius: 5px; 
    }}
    QProgressBar::chunk {{
        background-color: {PRIMARY_COLOR}; 
        border-radius: 5px; 
    }}
"""
