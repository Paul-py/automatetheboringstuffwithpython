import re

'''phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
areaCode, mainNumber = mo.groups()
print(areaCode)'''

'''Batregex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = Batregex.search('Batmobile lost a wheel')
print(mo.group())'''

'''batregex = re.compile(r'Bat(wo)*man')
mo = batregex.search('The adventures of Batman')
print(mo.group())'''

#Findallmethod
'''phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)'''

#CHARACTER CLASS
food = re.compile(r'[aeiouAEIOU]')
mo = food.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)
