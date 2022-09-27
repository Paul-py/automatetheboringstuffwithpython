import re, pyperclip

#Find website URLs that begin with http:// or https://.

URLREGEX = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')


text = str(pyperclip.paste())
url = URLREGEX.findall(text)


#for i in url:
print(url[0 + i])


#TODO: include the pyperclip.copy option.


'''
p = 0
while p < len(url):
    print(url[0 + p])
    p += 1

print(len(url))'''