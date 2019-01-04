#Day1
import re #Regex libary for Python

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#Since regular expressions frequently use backslashes in them,
#it is convenient to pass raw strings to the re.compile() function
#instead of typing extra backslashes.
#Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than
#typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.
mo = phoneNumRegex.search('My number is 415-555-4242.')
#A Regex objects search() method searches the string it 
#is passed for any matches to the regex. The search() method will 
#return None if the regex pattern is not found in the string. If the 
#pattern is found, the search() method returns a Match object. Match
#objects have a group() method that will return the actual matched
#text from the searched string.
print('Phone number found: ' + mo.group())
#Illustration of group() in Match object

phoneNumRegexGroupIllus = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
moGroupIllus = phoneNumRegexGroupIllus.search('My number is 451-556-7821. Or is it?')
#print(moGroupIllus.group()) #Return all
#print(moGroupIllus.group(0)) #Same as above
#print(moGroupIllus.group(1)) #First group
areaCode, mainNumber = moGroupIllus.groups() #Retrun tuple of groups
print(areaCode)
print(mainNumber)

#Parentheses have a special meaning in regular expressions
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
#mo.group(1) #'(415)'
#mo.group(2) #'555-4242'

#Matching multiple stuff using 'pipe' or | 