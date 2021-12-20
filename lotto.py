import random

# First we define a function to generate a random number
# this will generate one random number, but we need 5
def gen():
    num = random.ranrange(69)
    return num

# We test the function and see that it returns a random numer
gen()

# We then mock up a ticket by making a list and using our gen method
# to populate 5 numbers and simulate a ticket
winning = [gen(),gen(),gen(),gen(),gen()]

# We then define a function to create a ticket
def ticket():
    ticket = [gen(),gen(),gen(),gen(),gen()] 
    return ticket

# We test the function and see that it returns a ticket
ticket()

# Now we know we can make ticket, so we create a winning ticket
winning = ticket()

# We check to see the winning lottery numbers
winning

# We create an empty list which will be our ticket in the future
new_tick = []

# We will need to keep count of how many tickets we "bought"
# so we create a variable to keep track of how many tickets we bought
count = 0

# Now that we have a winning ticket, we need to check if the user's ticket
# matches the winning ticket, we do this by comparing the two lists
# If they don't match, we increment the count (or loss) flag
while new_tick != winning:
    new_tick = ticket()
    count += 1
    
# Once this finishes running, we can check to see that the winning ticket
# was matched and the count is correct
winning
new_tick
count

# Now that we want to run it again, we need to reset the count, winning ticket, and new ticket
# we create a function to reset the game
# Notice this function retunrs three items, an empty count, a new winning ticket, and a new ticket
def reset():
    count = 0 
    winning = ticket()
    new_tick = [] 
    return count, winning, new_tick

# however, reset won't set the variables globally , so we need assign it to a variable
# we set three variables to the three items returned by reset
count, winning, new_tick = reset()

# Then we check to ensure we have an empty count, a new winning ticket, and a new ticket
count
winning
new_tick

# we run the game again to see our new odds
while new_tick != winning:
    new_tick = ticket()
    count += 1

# Once it finishes, we check to see the new count and winning ticket
count
