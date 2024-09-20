#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Week 2 Python lab Work: 
# Task 1: Convert a distance in kilometers to miles 
# Task 2: Convert a temperature in degrees Celsius to Fahrenheit 
# Task 3: Convert a binary number to decimal


# In[8]:


# Task 1: Convert a distance entered in kilometers to miles (1 km = 0.62137119 mi)

kilometersValid = False
while not kilometersValid:
    kilometersValid = True
    print ("\nEnter a kilometer distance to convert to miles:")
    try:
        kilometers = float(input())
    except:
        kilometersValid = False
        print ("\nInvalid input for number of kilometers. Try again.")
if kilometersValid:
    miles = kilometers * 0.62137119
    print ("\n" + format(kilometers, ".2f") + " kilometers is " + format(miles, ".2f") + " miles")


# In[10]:


# Task 2: Convert a temperature entered in degrees Celsius to Fahrenheit (F = 9/5 * C + 32)

celsiusValid = False
while not celsiusValid:
    celsiusValid = True
    print ("\nEnter a temperature in degrees Celsius to convert to Fahrenheit:")
    try:
        celsius = float(input())
    except:
        celsiusValid = False
        print ("\nInvalid input for Celsius degrees. Try again.")

if celsiusValid:
    fahrenheit = celsius * 9/5 + 32
    print ("\n" + format(celsius, ".2f") + " Celsius is " + format(fahrenheit, ".2f") + " Fahrenheit")


# In[2]:


# Task 3: Convert a binary number entered as a string of 0s and 1s to decimal

binaryValid = False
while not binaryValid:
    print ("\nEnter a binary number to convert to decimal:")
    binaryValid = True
    try:
        binaryNumber = input()
    except:
        binaryValid = False
    if len(binaryNumber) == 0:
        binaryValid = False
    if binaryValid:
        decimalNumber = 0
        for bitPlace in range(len(binaryNumber)):
            bit = binaryNumber[len(binaryNumber) - (bitPlace+1)]
            if bit == "1":
                decimalNumber += 2**bitPlace
            elif bit != "0":
                binaryValid = False
    if binaryValid:
        print ("\n" + str(binaryNumber) + " binary is " + str(decimalNumber) + " decimal")
    else:
        print("\nInvalid input for binary number. Only digits 0 and 1 are valid. Try again.")


# In[8]:


# Prompt for text to pause for a while so that screen doesn't clear
print("Enter any text to end program:")
input()

