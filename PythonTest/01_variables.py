
# Write a function that
# 1. asks the user for their email address and Gameloft studio
# 2. stores it in the user_info dictionary
# 3. prints the information stored
user_info = {}
def record_information():
    user_info['email'] = input("Enter email:")
    user_info['studio'] = input("Enter studio:")
    print(user_info)
    pass

record_information()