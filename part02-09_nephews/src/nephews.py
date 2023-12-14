# Taking input for the user's name
name = input("Please type in your name: ")

# Checking if the name matches one of Donald Duck's nephews
if name in ["Huey", "Dewey", "Louie"]:
    print("I think you might be one of Donald Duck's nephews.")
# Checking if the name matches one of Mickey Mouse's nephews
elif name in ["Morty", "Ferdie"]:
    print("I think you might be one of Mickey Mouse's nephews.")
# If the name doesn't match any known nephews
else:
    print("You're not a nephew of any character I know of.")
