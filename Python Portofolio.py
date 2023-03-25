#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Variables and Type


# In[24]:


## "String: %s" %, "Float; %f" %, "Integer: %d" % --> The %s operator lets you add a value into a Python string. The %s signifies that you want to add a string value into a string. The % operator can be used with other configurations, such as %d, to format different types of values.In more modern versions of Python, 
## the % syntax has become less widely used in favor of f strings and the format() method.
## %s - String (or any object with a string representation, like numbers)
## %d - Integers
## %f - Floating point numbers
## %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
## %x/%X - Integers in hex representation (lowercase/uppercase)


# In[25]:


##String formatting


# In[26]:


###You will need to write a format string which prints out the data using the following syntax: 
##Hello Merry. Your current balance is $200.0.


# In[27]:


data = ("Merry", 200.0)
format_string = "Hello %s. Your current balance is $%s."

print(format_string % data)


# In[3]:


# change this code
Stringku = "Hallo, apakabar?"
Floatku = 17.0
Intku = 100

# testing code
if Stringku == "Hallo, apakabar?":
    print("String: %s" % Stringku)
if isinstance(Floatku, float) and Floatku == 17.0:
    print("Float: %f" % Floatku)
if isinstance(Intku, int) and Intku == 100:
    print("Integer: %d" % Intku)


# In[6]:


## isinstance --> membuktikan apakah nilai suatu variable bertipe integer, float atau string


# In[15]:


x=1
isinstance(x,int)


# In[16]:


x="a"
isinstance(x,int)


# In[17]:


x="A"
isinstance(x,str)


# In[18]:


x=60.0
isinstance(x,float)


# In[19]:


# Lists


# In[20]:


numbers = []
strings = []
names = ["Anya", "Erica", "Jessi"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Erica).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


# In[21]:


##Basic Operators


# In[22]:


##The target of this exercise is to create two lists called x_list and y_list, 
###which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, 
###which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

# TODO: change this code
x_list = [x] *10
y_list = [y] *10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


# In[28]:


#Basic String operations


# In[29]:


s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))


# In[34]:


data=("This", "lesson", "day")
time= "%s %s stop here at 10.23. Will be continue next %s."

print(time% data)


# In[ ]:




