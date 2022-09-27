import re, pyperclip

phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?      # area code
                        (\s|-|\.)?              # separator
                        (\d{3})                 # first 3 digits
                        (\s|-|\.)               # separator
                        (\d{4})                 # last 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
                        )''', re.VERBOSE)


emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+ # username
                         @ # @ symbol
                        [a-zA-Z0-9.-]+ # domain name
                        (\.[a-zA-Z]{2,4}) # dot-something
                         )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for i in phoneRegex.findall(text):
    phoneNum = '-'.join([i[1], i[3], i[5]])
    if i[8] != '':
        phoneNum += ' x' + i[8]
        matches.append(phoneNum)
for i in emailRegex.findall(text):
    matches.append(i[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
