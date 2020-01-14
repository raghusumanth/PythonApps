




#namespace and scope
"""
Namespaces and Scope in Python
What is namespace:
A namespace is a system to have a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. Let’s go through an example, a directory-file system structure in computers. Needless to say, that one can have multiple directories having a file with the same name inside of every directory. But one can get directed to the file, one wishes, just by specifying the absolute path to the file.

On the similar lines, Python interpreter understands what exact method or variable one is trying to point to in the code, depending upon the namespace. So, the division of the word itself gives little more information. Its Name (which means name, an unique identifier) + Space(which talks something related to scope). Here, a name might be of any Python method or variable and space depends upon the location from where is trying to access a variable or a method.

Types of namespaces :

When Python interpreter runs solely without and user-defined modules, methods, classes, etc. Some functions like print(), id() are always present, these are built in namespaces. When a user creates a module, a global namespace gets created, later creation of local functions creates the local namespace. The built-in namespace encompasses global namespace and global namespace encompasses local namespace.


Lifetime of a namespace :

A lifetime of a namespace depends upon the scope of objects, if the scope of an object ends, the lifetime of that namespace comes to an end. Hence, it is not possible to access inner namespace’s objects from an outer namespace.

As shown in the following figure, same object name can be present in multiple namespaces as isolation between the same name is maintained by their namespace.

But in some cases, one might be interested in updating or processing global variable only, as shown in the following example, one should mark it explicitly as global and the update or process.


"""

# var1 is in the global namespace
var1 = 5
def some_func():

    # var2 is in the local namespace
    var2 = 6

    def some_inner_func():

        # var3 is in the nested local
        # namespace
        var3 = 7
        print(var3)
        print(var2)
        print(var1)
    some_inner_func()

some_func()

# Python program processing
# global variable

count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()


"""
Scope of Objects in Python :
Scope refers to the coding region from which particular Python object is accessible. Hence one cannot access any particular object from anywhere from the code, the accessing has to be allowed by the scope of the object.
# Python program showing 
# a scope of object 
  
def some_func(): 
    print("You are welcome to some_func") 
    print(var) 
some_func()

As can be seen in the above output the function some_func() is in the scope from main but var is not avaialable in the scope of main. Similarly, in case of inner functions, outer functions don’t have accessibility of inner local variables which are local to inner functions and out of scope for outer functions. Lets take an example to have details understanding of the same:

# Python program showing 
# a scope of object 
  
def some_func(): 
    print("Inside some_func") 
    def some_inner_func(): 
        var = 10
        print("Inside inner function, value of var:",var) 
    some_inner_func() 
    print("Try printing var from outer function: ",var) 
some_func()


Statement, Indentation and Comment in Python



Statement, Indentation and Comment in Python
Instructions written in the source code for execution are called statements. There are different types of statements in the Python programming language like Assignment statement, Conditional statement, Looping statements etc. These all help the user to get the required output. For example, n = 50 is an assignment statement.

Multi-Line Statements: Statements in Python can be extended to one or more lines using parentheses (), braces {}, square brackets [], semi-colon (;), continuation character slash (\). When the programmer needs to do long calculations and cannot fit his statements into one line, one can make use of these characters.

Declared using Continuation Character (\):
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

Declared using parentheses () :
n = (1 * 2 * 3 + 7 + 8 + 9)

Declared using square brackets [] :
footballer = ['MESSI',
          'NEYMAR',
          'SUAREZ']

Declared using braces {} :
x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}

Declared using semicolons(;) :
flag = 2; ropes = 3; pole = 4

A block is a combination of all these statements. Block can be regarded as the grouping of statements for a specific purpose. Most of the programming languages like C, C++, Java use braces { } to define a block of code. One of the distinctive features of Python is its use of indentation to highlight the blocks of code. Whitespace is used for indentation in Python. All statements with the same distance to the right belong to the same block of code. If a block has to be more deeply nested, it is simply indented further to the right.






"""
# Python program showing
# indentation

site = 'gfg'

if site == 'gfg':
    print('Logging on to geeksforgeeks...')
else:
    print('retype the URL.')
print('All set !')

#single line comments
"""
multiline comments
"""

'''
another way for multiline comments
'''

"""
Structuring in python program
"""

"""
Mostly, python statements are written in such a format that one statement is only written in a single line. The interpreter considers the ‘new line character’ as the terminator of one instruction. But, writing multiple statements per line is also possible that you can find below.

"""
print('Welcome to Geeks for Geeks')

# Example 2

x = [1, 2, 3, 4]

# x[1:3] means that start from the index
# 1 and go upto the index 2
print(x[1:3])

""" In the above mentioned format, the first  
index is included, but the last index is not 
included."""


"""
Multiple Statements per Line We can also write multiple statements per line, but it is not a good practice as it reduces the readability of the code. Try to avoid writing multiple statements in a single line. But, still you can write multiple lines by terminating one statement with the help of ‘;’. ‘;’ is used as the terminator of one statement in this case.

Line Continuation to avoid left and right scrolling
Some statements may become very long and may force you to scroll the screen left and right frequently. You can fit your code in such a way that you do not have to scroll here and there. Python allows you to write a single statement in multiple lines, also known as line continuation. Line continuation enhances readability as well.

Types of Line Continuation
In general, there are two types of line continuation

Implicit Line Continuation
This is the most straightforward technique in writing a statement that spans multiple lines.
Any statement containing opening parentheses (‘(‘), brackets (‘[‘), or curly braces (‘{‘) is presumed to be incomplete until all matching parentheses, square brackets, and curly braces have been encountered. Until then, the statement can be implicitly continued across lines without raising an error.


"""

# Example 1

# The following code is valid
a = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]

print(a)

# Example 2
# The following code is also valid

person_1 = 18
person_2 = 20
person_3 = 12

if (
        person_1 >= 18 and
        person_2 >= 18 and
        person_3 < 18
):
    print('2 Persons should have ID Cards')

"""
Explicit Line Continuation
Explicit Line joining is used mostly when implicit line joining is not applicable. In this method, you have to use a character that helps the interpreter to understand that the particular statement is spanning more than one lines.
Backslash (\) is used to indicate that a statement spans more than one line. The point is to be noted that ” must be the last character in that line, even white-space is not allowed.
        
        
        
"""

x = \
    1 + 2 \
    + 5 + 6 \
    + 10

print(x)

"""
Note Do note that Hash (#) inside a string does not make it a comment. Consider the following example for demonstration.

"""

# Example

""" The following statement prints the string stored 
    in the variable """

a = 'This is # not a comment #'
print(a) # Prints the string stored in a


a = 1-2  # Better way is a = 1 - 2

print(a)

x = 10
flag =(x == 10)and(x<12)
print(flag)



