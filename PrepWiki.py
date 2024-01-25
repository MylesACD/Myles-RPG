import re
import os
def replace_between_symbols(html_content):
    pattern = r"#([\w\.\,\:\;\s\'\/\"\-\’]*)#"
    replaced_content = re.sub(pattern, repl, html_content)
    return replaced_content

def repl(match):
    def find(s, ch):
     return [i for i, ltr in enumerate(s) if ltr == ch]
    indecies = find(match.group(0)," ")
    rtn = '█' * len(match.group(0))
    for i in indecies:
      rtn = rtn[:i] + " " + rtn[i + 1:]
    return rtn

path = r"C:\\Users\\Myles\\Documents\\Ethos Project\\Ethos-Project\\Wiki\\Ethos\\HTML"
with os.scandir(path) as folder:
    for entry in folder:
        if entry.name.endswith(".html") and entry.is_file():
            file_path = path +"\\"+ entry.name
            # Read the HTML file
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            # Replace characters between # symbols
            modified_content = replace_between_symbols(html_content)
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)



print("Redaction Complete")
