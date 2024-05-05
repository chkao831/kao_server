import os
from pathlib import Path


class StockController:
    def __init__(self) -> None:
        self.RoleList = []

DATA_DIR = os.environ.get("DATA_DIR", "data")

class ChapterController:
    def __init__(self) -> None:
        self.data_dir_abs = os.path.abspath(DATA_DIR)

    def get_txt(self, chapter_id) -> None:
        txt_path = Path(self.data_dir_abs) / f"{chapter_id}.txt"
        # return txt_path
        try:
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
                html_content = text_to_html(text)
                return html_content
        except FileNotFoundError:
            raise Exception("Chapter not found")
          
def text_to_html(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Extract the first line as title and the rest as content
    chapter_title = lines[0].strip()
    chapter_content = '\n'.join(lines[1:])
    
    # Add three spaces at the beginning of each content line
    spaced_lines = ['       ' + line for line in chapter_content.split('\n')]
    text_with_spaces = '\n'.join(spaced_lines)
    
    # Simple text replacements for basic HTML conversion
    html_text = text_with_spaces.replace('\n\n', '\n<br>\n<br>\n')  # Double blank lines
    html_text = html_text.replace('\n', '<br>\n')  # Single new line to <br>

    # Wrap text in a basic HTML structure with inline CSS
    html = f"""
    <html>
    <head>
        <title>{chapter_title}</title>
        <style>
            body {{
                font-family: 'SimHei', 'SimSun', 'FangSong', Arial, sans-serif;
                line-height: 1.2;
                white-space: pre-wrap;  /* Maintains whitespace formatting */
                background-color: #383838;  /* Background color */
                color: #bbbbbb;  /* Text color */
            }}
            .chapter-title {{
                font-size: 36px;  /* Larger than the body text */
                font-weight: bold;  /* Make the title bold */
                color: #eeeeee;
                /* margin: 20px 0;  Add some space around the title */
            }}
            .chapter-author {{
                font-size: 16px;  /* Smaller than the title */
                color: #eeeeee;
            }}
            .chapter-content {{
                font-size: 26px;  /* Size of the body text */
            }}
        </style>
    </head>
    <body>
        <div class="chapter-title">{chapter_title}</div>
        <div class="chapter-author">     Copyright © DoorWoodBDX (LOFTER/AFDian)</div>
        <div class="chapter-content">
            {html_text}
        </div>
    </body>
    </html>
    """
    return html