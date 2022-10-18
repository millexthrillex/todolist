### Beginning of the script

### Create a user menu
### Options: Choose existing user, Create new user

print("What would you like to do?")

print("1. Choose exiting user")
print("2. Create new user")

### Define Options

def Options():
    if Options(1):
        print("Which user?")
    elif Options(2):
        print("Enter your username")


Options()

existing_user = "1"
new_user = "2"

##enter a user input here

#insert line break here

print("Welcome, (user_name)")

### After user selection, choose an option.

Choose = input("Welcome, please choose an option. \n ")


Options = [ "Show List", "Add to list", "Remove from list" ]
for o in Options:
	print(o)
