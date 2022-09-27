'''
(?xi)
\b
(                       # Capture 1: entire matched URL
  (?:
    [a-z][\w-]+:            # URL protocol and colon
    (?:
      /{1,3}                    # 1-3 slashes
      |                         #   or
      [a-z0-9%]                 # Single letter or digit or '%'
                                # (Trying not to match e.g. "URI::Escape")
    )
    |                       # or
    www\d{0,3}[.]               # "www.", "www1.", "www2." … "www999."
  )
  (?:                       # One or more:
    [^\s()<>]+                  # Run of non-space, non-()<>
    |                           #   or
    \([^\s()<>]+\)              # a matching set of parens
  )+
  (?:                       # End with:
    \([^\s()<>]+\)                  # a set of parens
    |                               #   or
    [^`!()\[\]{};:'".,<>?«»“”‘’\s]  # not a space or one of these punct chars
  )
)
'''
'''
import re


def Find(string):
  # findall() has been used
  # with valid conditions for urls in string
  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex, string)
  return [x[0] for x in url]


# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))'''
'''
import re

url = '<p>Hello World</p><a href="http://example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>'

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)

>>> print urls
['http://example.com', 'http://example2.com']
'''
'''
import re
text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
#print("Urls: ",urls)
S
print (*urls)'''

'''
import re
var= 'You can understand the regular expressions in this link https://en.wikipedia.org/wiki/Regular_expression and you can get more practice using http://www.i2tutorials.com and you can get the python documentation from http://python.org'
urls = re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', var)

print(urls)'''
'''
Output:

[('https', 'en.wikipedia.org', '/wiki/Regular_expression'),
 ('http', 'www.i2tutorials.com', ''),
 ('http', 'python.org', '')] '''
L = ['H', 'P', 'K']

#for i in L:
print(L[i])
