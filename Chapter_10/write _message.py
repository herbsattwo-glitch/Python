#Writing Multiple Lines
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path(r'C:\Users\Samue\OneDrive\Attachments\Desktop\Python\Chapter_10\Play2.txt')
path.write_text(contents)

