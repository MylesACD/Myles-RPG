import re
import os

def write_modified(func,path):
    with open(path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        # Replace characters between # symbols
        modified_content = func(html_content)
        # Write the modified content back to the file
        with open(path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

def redact(og_content):
    def replace_between_symbols(html_content):
        pattern = r"#([\w\.\,\:\;\s\'\/\"\-\’\[\]\<\>\=\@\!\$\%\^\&\*\(\)\/]*)#"
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

    return replace_between_symbols(og_content)

def django_template_blockify(og_content):
    repl1 = "{% extends \"wiki/wiki-base.html\" %}{% block content %}" + "\n"
    pattern1 = r"<([\w\.\,\:\;\s\'\/\"\-\’\[\]\<\>\=\@\!\$\%\^\&\*\(\)\/]*)(<body class=\"wikidpad\">)"
    
    repl2 = "{% endblock content%}"
    pattern2 = r"(<\/body>)\s\S*(<\/html>)"
    def replace_between_symbols(pattern, repl, html_content):
        replaced_content = re.sub(pattern, repl, html_content)
        return replaced_content
    decapitated = replace_between_symbols(pattern1,repl1,og_content)
    return replace_between_symbols(pattern2, repl2, decapitated)

folder = r"C:\\Users\\Myles\\Documents\\Ethos Project\\Ethos-Project\\Wiki\\Ethos\\HTML"
for file in os.scandir(folder):
   
    if file.name.endswith(".html"): 
        write_modified(redact, file)
        write_modified(django_template_blockify, file)
    elif file.name.endswith(".css"):
        os.remove(file)