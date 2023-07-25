#!/usr/bin/env python
# coding: utf-8

# # Q1. What is the role of try and exception block?

# The role of try and except block in Python is to handle exceptions that may occur during the execution of a program. Exceptions are events that disrupt the normal flow of the program and cause errors.
# 
# The try block contains the code that may raise an exception, while the except block contains the code that handles the exception if it occurs. The except block can specify the type of exception to catch, or catch all exceptions using a generic Exception class.
# 
# For example:

# In[1]:


try:
  # Code that may raise an exception
  x = int(input("Enter a number: "))
  y = 10 / x
  print(y)
except ZeroDivisionError:
  # Code to handle ZeroDivisionError
  print("You cannot divide by zero!")
except ValueError:
  # Code to handle ValueError
  print("Please enter a valid integer!")


# In this example, the try block may raise a ZeroDivisionError if the user enters 0, or a ValueError if the user enters a non-integer value. The except blocks handle these exceptions by printing appropriate messages.
# 
# The try and except block can also have an else clause and a finally clause. The else clause executes if no exception is raised in the try block, while the finally clause executes no matter what, providing a place for cleanup code

# # Q2. What is the syntax for a basic try-except block?

# In[6]:


try:
  # Code that may raise an exception

except ExceptionType:
  # Code to handle the exception


# Here, the try block contains the code that may raise an exception, while the except block contains the code that handles the exception if it occurs. The except block can specify the type of exception to catch, such as ZeroDivisionError, ValueError, etc. or use a generic Exception class to catch all exceptions.

# In[7]:


try:
  # Code that may raise an exception
  x = int(input("Enter a number: "))
  y = 10 / x
  print(y)
except ZeroDivisionError:
  # Code to handle ZeroDivisionError
  print("You cannot divide by zero!")
except ValueError:
  # Code to handle ValueError
  print("Please enter a valid integer!")


# In this example, the try block may raise a ZeroDivisionError if the user enters 0, or a ValueError if the user enters a non-integer value. The except blocks handle these exceptions by printing appropriate messages. 

# # Q3. What happens if an exception occurs inside a try block and there is no matching except block?

# If an exception occurs inside a try block and there is no matching except block, the exception will propagate to the outer scope and cause the program to terminate with an error message. This is undesirable as it may result in loss of data or resources, or leave the program in an inconsistent state. Therefore, it is recommended to handle all possible exceptions that may occur in the try block using appropriate except blocks.

# # Q4. What is the difference between using a bare except block and specifying a specific exception type?

# The difference between using a bare except block and specifying a specific exception type is that a bare except block will catch all exceptions that may occur in the try block, while a specific exception type will only catch the exceptions of that type or its subclasses. For example:

# In[9]:


try:
  # Code that may raise an exception
  x = int(input("Enter a number: "))
  y = 10 / x
  print(y)
except:
  # Bare except block that catches all exceptions
  print("Something went wrong!")


# In this example, the bare except block will catch any exception that may occur in the try block, such as ZeroDivisionError, ValueError, KeyboardInterrupt, etc. and print “Something went wrong!”.

# In[10]:


try:
  # Code that may raise an exception
  x = int(input("Enter a number: "))
  y = 10 / x
  print(y)
except ZeroDivisionError:
  # Specific except block that catches only ZeroDivisionError
  print("You cannot divide by zero!")


# In this example, the specific except block will only catch the ZeroDivisionError that may occur in the try block and print “You cannot divide by zero!”. If any other exception occurs, such as ValueError, KeyboardInterrupt, etc. it will not be handled by this except block and will propagate to the outer scope.

# # Q5. Can you have nested try-except blocks in Python? If yes, then give an example.

# Yes, you can have nested try-except blocks in Python. This means that you can put a try-except block inside another try-except block. This can be useful when you want to handle different types of exceptions at different levels of your code.
# 
# For example, suppose you have a function that takes a number as an input and returns the square root of its logarithm. You might want to handle the exceptions that could occur in this function, such as ValueError (if the input is negative or zero) or ZeroDivisionError (if the input is one). But you might also want to handle the exceptions that could occur when you call this function, such as TypeError (if the input is not a number) or NameError (if the input is not defined).
# 
# 

# # Q6. Can we use multiple exception blocks, if yes then give an example.

# Yes, we can use multiple exception blocks in Python. This means that we can handle different types of exceptions that may occur in the try block with different except blocks. There are two ways to use multiple exception blocks in Python:
# 
# 1. The first way is to use multiple except blocks one after another. Each except block specifies a type of exception that it can handle. 
# 2. The second way is to use a tuple of exceptions in a single except block. This way, we can handle multiple types of exceptions with the same code

# # Q7. Write the reason due to which following errors are raised:
# ### a. EOFError
# ### b. FloatingPointError
# ### c. IndexError
# ### d. MemoryError
# ### e. OverflowError
# ### f. TabError
# ### g. ValueError

# Here are the reasons due to which the following errors are raised:
# 
# a. EOFError: This error is raised when the input() function hits an end-of-file condition (EOF) without reading any data. This usually happens when the user presses Ctrl+D or Ctrl+Z on the keyboard, or when the input source is a file that is empty or has reached the end.
# 
# b. FloatingPointError: This error is raised when a floating point operation fails. This can occur when the result of the operation is not a representable number, such as infinity, NaN, or a value too large or too small to be stored. This error is not raised by default, but can be enabled by setting the sys.float_info variable to a non-zero value.
# 
# c. IndexError: This error is raised when a sequence subscript (index) is out of range. This means that the index is either negative or greater than or equal to the length of the sequence. For example, trying to access the fourth element of a list that has only three elements will raise an IndexError.
# 
# d. MemoryError: This error is raised when an operation runs out of memory. This typically occurs when the system has no more memory available to allocate to your Python program, either due to insufficient memory resources or because your program is consuming too much memory23
# 
# e. OverflowError: This error is raised when the result of an arithmetic operation is too large to be represented. This can happen when you are working with integers that exceed the maximum size of a C long, which is usually 32 bits or 64 bits depending on the platform. For example, trying to compute 2**1000 as an integer will raise an OverflowError.
# 
# f. TabError: This error is raised when indentation contains an inconsistent use of tabs and spaces. Python uses indentation to indicate blocks of code, and it requires that one level of indentation is consistent throughout the block. Mixing tabs and spaces can cause confusion and lead to unexpected results. For example, using four spaces for one line and one tab for another line in the same block will raise a TabError.
# 
# g. ValueError: This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError or KeyError. For example, trying to convert a string that does not represent a number to an int will raise a ValueError.

# # Q8. Write code for the following given scenario and add try-exception block to it.
# ### a. Program to divide two numbers
# ### b. Program to convert a string to an integer
# ### c. Program to access an element in a list
# ### d. Program to handle a specific exception
# ### e. Program to handle any exception

# a. Program to divide two numbers

# In[15]:


# Get the input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Try to convert the input to float and perform division
try:
    num1 = float(num1)
    num2 = float(num2)
    result = num1 / num2
    print(f"The result of {num1} / {num2} is {result}")
# Handle the possible exceptions
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("You cannot divide by zero")


# b. Program to convert a string to an integer

# In[21]:


# Get the input from the user
string = input("Enter a string: ")

# Try to convert the string to an integer
try:
    number = int(string)
    print(f"The integer value of {string} is {number}")
# Handle the possible exception
except ValueError:
    print("Please enter a string that represents an integer")


# c. Program to access an element in a list

# In[18]:


# Define a list of elements
my_list = ["apple", "banana", "cherry", "date"]

# Get the input from the user
index = input("Enter an index: ")

# Try to access the element at the given index
try:
    index = int(index)
    element = my_list[index]
    print(f"The element at index {index} is {element}")
# Handle the possible exceptions
except ValueError:
    print("Please enter a valid integer index")
except IndexError:
    print("The index is out of range")


# d. Program to handle a specific exception

# In[22]:


# Define a function that raises a specific exception
def raise_error():
    raise RuntimeError("Something went wrong")

# Try to call the function
try:
    raise_error()
# Handle the specific exception
except RuntimeError as e:
    print(f"Caught a RuntimeError: {e}")


# e. Program to handle any exception

# In[27]:


# Define a function that may raise any exception
def do_something():
    # Some code that may raise any exception


    
# Try to call the function
try:
    do_something()
# Handle any exception using a generic except block
except Exception as e:
    print(f"Caught an exception: {e}")


# In[ ]:




