#Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and
#2015/3/14) by replacing them with dates in a single, standard format.
'''
import re

DateRegex = re.compile()
datesfound = DateRegex.findall()

"^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"

"^(?:\\d{4})-(?:\\d{2})-(?:\\d{2})T(?:\\d{2}):(?:\\d{2}):(?:\\d{2}(?:\\.\\d*)?)(?:(?:-(?:\\d{2}):(?:\\d{2})|Z)?)$"
'''
import re

# Validate ISO date
#date_pattern = "^(?:\\d{4})-(?:\\d{2})-(?:\\d{2})T(?:\\d{2}):(?:\\d{2}):(?:\\d{2}(?:\\.\\d*)?)(?:(?:-(?:\\d{2}):(?:\\d{2})|Z)?)$"
#re.match(date_pattern, '2021-11-04T22:32:47.142354-10:00') # Returns Match object

# Extract ISO date from a string
date_extract_pattern = "(?:\d{4}-\d{2}-\d{2}(T(?:\d{2}:\d{2}:\d{2}\.\d*-\d{2}:\d{2}|Z))?)"
p = re.findall(date_extract_pattern, '2017-05-23T15:02:27Z | WARN | Record not found\n2018-05-23T15:02:28Z | WARN | Project with the id ’53’ was not 2018-05-23 found') # returns ['2017-05-23T15:02:27Z', '2018-05-23T15:02:28Z']
print(p)