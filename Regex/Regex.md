# Regex Expressions

The module used for regex is 

```python
import re
```



**re.compile()** is used to compile the expression to regex expression.

```python
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```

Since regular expressions frequently use backslashes in them, it is convenient to pass raw strings to the re.compile() function instead of typing extra backslashes.
Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.



Now ``phoneNumRegex`` contain regex expression.

**search()** is used to search the string for any matches to the regex.

```python
mo = phoneNumRegex.search('My number is 415-555-4242.')
```

The search() method will return None if the regex pattern is not found in the string. If the 
pattern is found, the search() method returns a **Match** object. **Match** objects have a **group()** method that will return the actual matched text from the searched string.



```python
print('Phone number found: ' + mo.group())
```

The above prints the matching groups..

```python
mo.group() #Return all
mo.group(0) #Same as above
mo.group(1) #First group
mo.groups() #Return tuple of groups
```



Parentheses have a special meaning in regular expressions
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
#mo.group(1) #'(415)'
#mo.group(2) #'555-4242'

#Matching multiple stuff using 'pipe' or | 