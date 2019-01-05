#Day1
import re #Regex libary for Python

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
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
hero = re.compile(r'Batman|Robin')
mo1 = hero.search('Batman and Robin are great DC combos.')
mo2 = hero.search('Robin and Batman')
print(mo1.group())
print(mo2.group())
#the first ocurrence of matching group is returned

hero = re.compile(r'Bat(man|mobile|copter|bat)')
mo = hero.search('Batman lost his Batcopter and Batbat')
print(mo.groups())
#similar to above but for finding Batman,Batmobile,etc They have same prefix and 
#done like above

h = re.compile(r'Bat(wo)?man')
mo1 = h.search('The adventures of Batman')
mo2 = h.search('The adventures of Batwoman')
print(mo1.group())
print(mo2.group())
#Optional regexing by '?' [matching zero or one of group]
