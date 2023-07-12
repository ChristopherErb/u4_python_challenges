# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


def min_Sec(mins):
    return mins * 60
def hour_Sec(hours):
    return hours * 3600
def day_Sec():
    return 1 * 24 * 3600
def june_hours():
    return 30 * 24
def aug_Mins():
   return 31 * 24 * 60 
def main():
    # Test the functions
    minutes = 5
    print(f"{minutes} minutes is equal to {min_Sec(minutes)} seconds.")

    hours = 56732
    print(f"{hours} hours is equal to {hour_Sec(hours)} seconds.")
    print(f" {day_Sec()} seconds in a day.")
    print(f" {june_hours()} hours in the month of June.")
    print(f" {aug_Mins()} minutes in the month of August.")

if __name__ == "__main__":
    main()




# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------





#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should 
# extract and return the middle letter. If there is no middle letter, your function 
# should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


def mid(Str):

    length = len(Str)
    if length % 2 == 0:
        return Str[length //2]
    else:
        return("failboat")



# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. 
# It should return a string where all the characters are hidden 
# with an asterisk except the last four. For example, if the function
# gets sent "1234567894444", then it should return "*********4444".



def hideIt(CcNum):
    hide = len(CcNum)-4
    masked = '*' * hide + CcNum[-4:]
    return masked

#This one was confusing and took a minute of figuring out how to make stuff the *


    


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is 
# a dictionary that maps from strings of names to the string "online" or "offline", 
# as seen above.
# Your function should return the number of people who are online.

def online_count(Status):
    count = 0
    for status in status.values():
        if status == "online":
            count += 1
    return count








# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full 
# price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. 
# For example, if the price is 100 and the discount is 20, the function should return 80.

def whatDiscound(FullPrice, DiscPerc):
    return FullPrice * (DiscPerc / 100)

#This seemd too easy?




# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs 
# of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of 
# a triangle, and returns an integer of the Hypotenouse


def hyPot(leg1, leg2):
    return ((leg1**2)+(leg2**2))

#Again, seems to easy?





# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the 
# recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals 
# using the Fibonacci Sequence


def Fib(num1, num2):
    fibList = [num1, num2]
    while len(fibList) < 11:
        next_num = fibList[-1] + fibList[-2]
        fibList.append(next_num)

    return fibList[2:]


#I had knew how to do this one already!  It's like fizzbuzz.  Everywhere. 


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
