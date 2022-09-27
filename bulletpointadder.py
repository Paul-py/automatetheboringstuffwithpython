import pyperclip

text = pyperclip.paste()


lines = text.split('\n')
print(lines)
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]


text = '\n'.join(lines)
pyperclip.copy(text)
print(text)
