# Python Basic :snake:

## Strings

### f-String

A better way to write string after python 3.6 (more [detailed reading](https://realpython.com/python-f-strings/))

__Simple Syntax__
```python
name = "Eric"
age = 74
f"Hello, {name}. You are {age}."
```

### String Method
Here are some of the most common string methods. A method is like a function, but it runs "on" an object.
If the variable s is a string, then the code s.lower() runs the lower() method on that string object and
returns the result (this idea of a method running on an object is one of the basic ideas that make up
Object Oriented Programming, OOP). Here are some of the most common string methods:

* s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
* __s.strip()__ -- returns a string with whitespace removed from the start and end
* s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
* s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
* s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the
first index where it begins or -1 if not found
* s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
* __s.split('delim')__ -- returns a list of substrings separated by the given delimiter. The delimiter is not
a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special
case s.split() (with no arguments) splits on all whitespace chars.
* __s.join(list)__ -- opposite of split(), joins the elements in the given list together using the string as
the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

## Arrays

### 2-d Array
We can implement [2-d array in python](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/) using list of list:
```python
rows, cols = (5, 5) 
arr = [[0 for i in range(cols)] for j in range(rows)] 
arr[0][0] = 1

# avoid shallow lists when initializing list of lists
arr = [[0]*cols]*rows
arr[0][0] = 1 # will make 0 col all 1
```

### Lists

An array-like data structure in python. Mutable unlike strinf is unmutable.

__Simple Syntax__
```python
list = [0, 1, 2]

# modifiers - return nothing.
list.append(3) # append a new element. Return nothing
list.pop(0)
del list[1]
len(list) # just like string get the size of this list

# looping through a list
for num in list:
    print num

# check if an element exist
VALUE in list
```

__Sorting__

`sorted()` can sort any type of sequencial data structure in python.
```python
sorted(list) # notice sorted() is a function and it will create a new list (i.e. a copy) sort it and return it unlike .sort() is a method and modify the list in-place (retun none) 
sorted(list, reverse=true) # sort in the decending order
list = sorted(list)
```

In Python it also allows us to do customed sorting without using a comparator function. It creats a shallow list sort based on the element in the shallow list but the result it's a sorted orginal list.

```python
a = ['dd', 'c', 'aaaa', 'bb']
sorted(a, key=len)

#using a customized function as key
def Last(s):
    return s[-1]
sorted(a, key=Last)
```
__List to String__
```python
"<deliminator>".join(list)
s.split('<deliminator')

s = "1:2:3:4"
s.split(':')
```
Lastly do not modify a list while iterating through.

__[List Methods (Return None):](https://developers.google.com/edu/python/lists#list-methods)__
* list.append(elem)
* list.insert(index, elem)
* list.extend(list2) - adds the elements in list2 to the end of the list. using + or += on a list is similiar to using extend()
* list.remove(elem) - searches for the first instance and remove it (ValurError if not present)
* list.sort() - *unlike sorted(), .sort() is a modifier and return nothing*
* list.reverse()
* list.pop(index) - removes and returns the element at the given index


### Tuples

Pack fixed number of things together. But a tuple is immutable like string.

__Simple Syntax__
```python
t = (1,2,3)
len(t)
t[0]

# parallel assignment - note this is not a tuple
(a, b) = (1, 2)
```

## Dicts and Files

```python
## Can build up a dict by starting with the the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print dict['a']     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print dict['z']                  ## Throws KeyError
if 'z' in dict: print dict['z']     ## Avoid KeyError
print dict.get('z')  ## None (instead of KeyError)
```
A for loop on a dictionary iterates over its keys by default.
The keys will appear in an arbitrary order. The methods dict.keys() and dict.values() return lists
of the keys or values explicitly. There's also an items() which returns a list of (key, value) tuples,
which is the most efficient way to examine all the key value data in the dictionary.
All of these lists can be passed to the sorted() function.

```python
## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in dict: print key
## prints a g o

## Exactly the same as above
for key in dict.keys(): print key

## Get the .keys() list:
print dict.keys()  ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print dict.values()  ## ['alpha', 'omega', 'gamma']

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
print key, dict[key]

## .items() is the dict expressed as (key, value) tuples
print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print k, '>', v
## a > alpha    o > omega     g > gamma
```

__Del Operator__
Similar to list. Del operator does deletions of an object.

```python
var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print list      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print dict      ## {'a':1, 'c':3}
```

__Files__
```python
# Echo the contents of a file
f = open('foo.txt', 'rU')
for line in f:   ## iterates over the lines of the file
print line,    ## trailing , so print does not add an end-of-line char
                ## since 'line' already includes the end-of-line.

text = f.read() # read all lines into one string
f.close()
```
*Lecturer's tip:* programming incrementally when writing Python is helpful - debugging and verifying while coding

## Stack & Queue
Python does not have built-in stack or queue data structures but we can implemented it using collections.deque or List.
However, __collections.deque should always be preferred (faster)__ since it's internally implemented using a doubly
linked list therefore have constant append(push) and pop time whereas list's append() and pop() may be slower because
of it's implemented as a block of memory and have memory reallocation issue.

Note: collections.deque is faster in append() and pop() but it has O(n) accessing time comparing with List. But you probably won't access anything except top when using stack.

```python
from collections import deque
# FILO principle
stack = deque()
# push(ele)
stack.append(element)
# pop()
stack.pop()
# top()
stack[-1]

# FIFO principle
queue = deque()
queue.append(element)
queue.popleft()
```
Queue can be implemented using collections.deque as well. Again always prefer collections.deque since insert at the beginning have constant time while List has to shift all elements in the memory to the right by one.


## Regular Expressions

Regular expressions are a powerful language for matching text patterns. Please see more details in Google's Python Class [Page](https://developers.google.com/edu/python/regular-expressions).

In python a regular expression search is typically written as: `match = re.search(pat, str)`

The re.search() method takes a regular expression pattern and a string and searches for that pattern within the string.
If the search is successful, search() returns a match object or None otherwise. Therefore, the search is usually immediately
followed by an if-statement to test if the search succeeded, as shown in the following example which searches for the pattern
'word:' followed by a 3 letter word (details below):

```python
import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'
```

The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change which is very handy for regular expressions (Java needs this feature badly!). I recommend that you always write pattern strings with the 'r' just as a habit.


__For the following key points please refer to the Google's page:__
* Basic patterns (e.g. .(a period), \w )
* Repetition (+ -- 1 or more occurrences of the pattern to its left)
* Finding email example using square bracket []
* Group extraction ()
* __findall()__: probably the single most powerful function in the re module. Above we used re.search() to find the first match for a pattern. findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.

```python
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
# do something with each found email string
print email
```

* findall() with files

```python
# Open file
f = open('test.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'some pattern', f.read())
```

* findall() with groups -- return a list a tuples. each pattern will be "disassembled" into a tuple based on ()

__RE Workflow and Debug__
Regular expression patterns pack a lot of meaning into just a few characters , but they are so dense, you can spend a lot of time debugging your patterns. Set up your runtime so you can run a pattern and print what it matches easily, for example by running it on a small test text and printing the result of findall(). If the pattern matches nothing, try weakening the pattern, removing parts of it so you get too many matches. When it's matching nothing, you can't make any progress since there's nothing concrete to look at. Once it's matching too much, then you can work on tightening it up incrementally to hit just what you want.

## Exceptions

An exception represents a run-time error that halts the normal execution at a particular line and transfers control to error handling code. Learn more in [the exceptions tutorial](https://docs.python.org/3/tutorial/errors.html) and see [the entire exception list](https://docs.python.org/3/library/exceptions.html).

```python
try:
    ## Either of these two lines could throw an IOError, say
    ## if the file does not exist or the read() encounters a low level error.
    f = open(filename, 'rU')
    text = f.read()
    f.close()
except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
    sys.stderr.write('problem reading:' + filename)
## In any case, the code then continues with the line after the try/except
```

## HTTP -- urllib.request

This is my personal favorite module in python. With it and beautifulsoup, you can do so many things such as scrapping web data from an url link. See more details in [urllib module doc](https://docs.python.org/3/library/urllib.html) and [beautifulsoup doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). 

Beautifulsoup has built-in method to get html source code so urllib.open() becomes not a must but it's good to know. Otherwise you can easily use beautifulsoup to get html source code parse it quickly to extract useful information.

## List Comprehension Syntax

A more *Pythonic* way to construct a list other than using for loop or map(). The basic syntax is: 
`new_list = [expression for member in iterable (if conditional)]`

Here is an simple example:
```python
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

# list comprehension syntax
final_prices = [get_price_with_tax(i) for i in txns]
final_prices
```
Besides that there are also set comprehension and dict comprehension in Python. See details in this [link](https://realpython.com/list-comprehension-python/)

## Pythonic

### enmerate() in Looping
* Simplify looping with counter: enumerate(). With enumerate(), you don’t need to remember to access the item from the iterable, and you don’t need to remember to advance the index at the end of the loop. 

```python
# when you want to have access to current iteration count in a loop
# Normal way
for index in range(len(values)):
    value = values[index]
    print(index, value)

# or
index = 0
for value in values:
    print(index, value)
    index += 1

# *pythonic way
>>> for count, value in enumerate(values):
...     print(count, value)
...
0 a
1 b
2 c

>>> for count, value in enumerate(values, start=1):
...     print(count, value)
...
1 a
2 b
3 c
```
The use of the two loop variables, count and value, separated by a comma is an example of __argument unpacking__. 


### Miscellaneous

* Assigning values to variables
```python
a, b, c = 1, 2, "name"
```

* Check if an iterable object is empty (e.g. sting, list, dict)
```python
# pythonic
if not lis:
    print('the list is empty')

# explicitly
if len(string) == 0:
    print('the str is empty)
```

## Conclusion

Python is a language with powerful module library and easy-to-read coding syntax style. Strive to master it and write *Pythonic* code whenever it's possible would benefit you for life. A good [post](https://realpython.com/courses/idiomatic-python-101/) about what *Pythonic* real means and examples.