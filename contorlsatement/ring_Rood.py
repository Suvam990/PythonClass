
rat = 15
Ring_Rood = print('Chooies your location\n 1)Bundahara\n 2)chakrapath\n 3)lazingpath\n 4)Blakhu\n 5)Swayambhu\n 6)Chabhil')

current_loction = int(input('Your current loction: '))



if current_loction >=7:
    print("You chooes a wrong loction")
elif current_loction == 1:
    Destination_loction = int(input('Your Destionation loction: '))
    if Destination_loction == 2:
        print('your total fear:Rs',rat)
    if Destination_loction == 3:
        print('your total fear:Rs',rat*3)  
    if Destination_loction == 4:
        print('your total fear:Rs',rat*4)
    if Destination_loction == 5:
        print('your total fear:Rs',rat*5)
    if Destination_loction == 6:
        print('you total fear: Rs', rat*6)
elif current_loction == 2:
    Destination_loction = int(input('Your Destionation loction: '))
    if Destination_loction == 3:
        print('your total fear:Rs',rat)
    if Destination_loction == 4:
        print('your total fear:Rs',rat*3)  
    if Destination_loction == 5:
        print('your total fear:Rs',rat*4)
    if Destination_loction == 6:
        print('your total fear:Rs',rat*5)
    if Destination_loction == 1:
        print('you total fear: Rs', rat*6)
elif current_loction == 3:
    Destination_loction = int(input('Your Destionation loction: '))
    if Destination_loction == 4:
        print('your total fear:Rs',rat)
    if Destination_loction == 5:
        print('your total fear:Rs',rat*3)  
    if Destination_loction == 6:
        print('your total fear:Rs',rat*4)
    if Destination_loction == 1:
        print('your total fear:Rs',rat*5)
    if Destination_loction == 2:
        print('you total fear: Rs', rat*6)
elif current_loction == 4:
    Destination_loction = int(input('Your Destionation loction: '))
    if Destination_loction == 5:
        print('your total fear:Rs',rat)
    if Destination_loction == 6:
        print('your total fear:Rs',rat*3)  
    if Destination_loction == 1:
        print('your total fear:Rs',rat*4)
    if Destination_loction == 2:
        print('your total fear:Rs',rat*5)
    if Destination_loction == 3:
        print('you total fear: Rs', rat*6)                                  
elif current_loction == 5:
    Destination_loction = int(input('Your Destionation loction: '))
    if Destination_loction == 6:
        print('your total fear:Rs',rat)
    if Destination_loction == 1:
        print('your total fear:Rs',rat*3)  
    if Destination_loction == 2:
        print('your total fear:Rs',rat*4)
    if Destination_loction == 3:
        print('your total fear:Rs',rat*5)
    if Destination_loction == 4:
        print('you total fear: Rs', rat*6)
elif current_loction == 6:
    Destination_loction = int(input('Your Destionation loction: '))
    if Destination_loction == 1:
        print('your total fear:Rs',rat)
    if Destination_loction == 2:
        print('your total fear:Rs',rat*3)  
    if Destination_loction == 3:
        print('your total fear:Rs',rat*4)
    if Destination_loction == 4:
        print('your total fear:Rs',rat*5)
    if Destination_loction == 6:
        print('you total fear: Rs', rat*6)

    
      

    


# # for loction in Ring_Rood:
# #     print(Ring_Rood)




# # charge of each loction 15
# # current loction

# # destination loction




# List of locations
# locations = ["Basundhara", "Chakrapath", "Lazingpath", "Jamal", "Swayambu"]

# # Distance and charge
# distance_per_location = 5  # km
# charge_per_km = 15  # charge per 5 km

# # Function to calculate the charge based on user input
# def calculate_charge(start_location, destination_location, locations, distance_per_location, charge_per_km):
#     # Check if both locations are valid
#     if start_location not in locations or destination_location not in locations:
#         print("Invalid location input. Please choose from the available locations.")
#         return
    
#     # Get the index of the start and destination locations
#     start_index = locations.index(start_location)
#     destination_index = locations.index(destination_location)
    
#     # Ensure the destination is after the start location
#     if start_index > destination_index:
#         print("Destination should be after the start location.")
#         return
    
#     # Calculate the distance
#     total_distance = (destination_index - start_index) * distance_per_location  # km
#     total_charge = total_distance * charge_per_km  # Total charge
    
#     return total_distance, total_charge

# # Display the available locations with integer choices
# print("Choose your starting location and destination:")
# print("1. Basundhara")
# print("2. Chakrapath")
# print("3. Lazingpath")
# print("4. Jamal")
# print("5. Swayambu")

# # Get user input for start and destination
# try:
#     start_choice = int(input("Enter the starting location (1-5): "))
#     destination_choice = int(input("Enter the destination location (1-5): "))
    
#     # Validate choices
#     if start_choice < 1 or start_choice > 5 or destination_choice < 1 or destination_choice > 5:
#         print("Invalid choice. Please choose between 1 and 5.")
#     else:
#         start_location = locations[start_choice - 1]
#         destination_location = locations[destination_choice - 1]
        
#         # Calculate the charge for the given route
#         result = calculate_charge(start_location, destination_location, locations, distance_per_location, charge_per_km)

#         # Display the result
#         if result:
#             total_distance, total_charge = result
#             print(f"Total distance: {total_distance} km")
#             print(f"Total charge: {total_charge} units")
# except ValueError:
#     print("Invalid input. Please enter a number between 1 and 5.")

