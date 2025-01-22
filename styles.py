BACKGROUND_COLOR = "#FBF5DD"  
TEXT_COLOR = "#333333"  
PRIMARY_COLOR = "#A6CDC6"  
SECONDARY_COLOR = "#FFD700"  
DANGER_COLOR = "#FF6B6B"  
CARD_COLOR = "#F5F5F5"  

FONT_FAMILY = "Arial"
FONT_SIZE = 15
HEADER_FONT_SIZE = 28

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
    background-color: #DDA853
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
