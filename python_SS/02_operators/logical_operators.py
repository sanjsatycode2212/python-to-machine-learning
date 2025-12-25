# ## Logical operators in Python are used to combine multiple conditions and return a Boolean result (True or False)

# #### there are three logical operators in Python:

# # and    >> returns True if both conditions are True
# # or     >> returns True if at least one condition is True
# # not    >> returns True if the condition is False (negates the condition)

# ## now we will see each operator with example.

# # >>>   and operator  <<<

# a = 10
# b = 20
# c = 30
# result = (a < b) and (b < c)  ## dono conditions true hain to ye True dega.
# print("AND Operator: ", result)  # Output: True
# # Explanation: Here, both conditions (a < b) and (b < c) are true, so the result is True.

# # >>>   or operator  <<<

# a = 10
# b = 20
# c = 5
# result = (a > b) or (b > c)  ## ek condition true hai to ye True dega.
# print("OR Operator: ", result)  # Output: True
# # Explanation: Here, the first condition (a > b) is false, but the second condition (b > c) is true, so the result is True.

# # >>>   not operator  <<<

# a = 10
# b = 20
# result = not (a > b)  ## condition false hai to ye True dega.
# print("NOT Operator: ", result)  # Output: True
# # Explanation: Here, the condition (a > b) is false, so the not operator negates it and the result is True.


# ## ye the logical operators ke examples.
# # logical operators are used to combine multiple conditions and return a boolean result (True or False).
# # they help in making complex decisions in code by allowing multiple conditions to be evaluated together.
# # they are essential for controlling the flow of a program based on multiple conditions.




# >>>>>>>>>>>>>>>>>>>      now we will do some questions   <<<<<<<<<<<<<<<<<<<<<<<<<<<


a = 15
b = 25

# Question 1: Check if both a and b are greater than 10
result1 = (a > 10) and (b > 10)
print("Question 1 - Both a and b greater than 10: ", result1)  # Output: True



# Question 2: Check if either a or b is less than 20
result2 = (a < 20) or (b < 20)
print("Question 2 - Either a or b less than 20: ", result2)
# Output: True



# Question 3: Check if a is not equal to b
result3 = not (a == b)
print("Question 3 - a is not equal to b: ", result3)  # Output: True








# # >>>>>>>>>>>>>>>>>>>>>             end of the code           <<<<<<<<<<<<<<<<<<<<<<<