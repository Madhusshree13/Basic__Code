# Basic Python Codes 2
# #Python program to flatten tuple of list to tuple
# soruce credit:online resources.
# def flatten_tuple_of_lists(tup):
#     flat_list = [item for sublist in tup for item in sublist]
#     return tuple(flat_list)

# def main():
#     # Take user input for tuple of lists
#     input_string = input("Enter the tuple of lists (comma-separated elements within lists, semicolon-separated lists): ")
#     lists = input_string.split(';')
#     tuple_of_lists = [list(map(int, sublist.split(','))) for sublist in lists]
    
#     # Check if the input is valid
#     valid_input = True
#     for sublist in tuple_of_lists:
#         for item in sublist:
#             if not isinstance(item, int):
#                 valid_input = False
#                 break
#         if not valid_input:
#             break
    
#     if valid_input:
#         # Flatten the tuple of lists
#         flattened_tuple = flatten_tuple_of_lists(tuple_of_lists)
        
#         # Display the flattened tuple
#         print("Flattened tuple:", flattened_tuple)
#     else:
#         print("Invalid input. Please enter integer values separated by commas within lists and semicolon-separated lists.")

# if __name__ == "__main__":
#     main()



# #program to convert a tuple into set 
# myTuple=[]
# def create_Tuple():
#     global myTuple
#     y=eval(input("Enter the number of elements in the tuple:"))
#     for i in range(0,y):
#         x=eval(input("Enter the number:"))
#         myTuple.append(x)
#     return tuple(myTuple)
# myTuple = create_Tuple()
# print("The tuple with the entered values is:",myTuple)
# print(type(myTuple))
# convertedTupleToSet = set(myTuple)
# print("The converted tuple to set is",convertedTupleToSet)
# print(type(convertedTupleToSet))


# # program to convert a set into tuple
# mySet=[]
# def create_set():
#     global mySet
#     u=eval(input("Enter the number of elements in the set:"))
#     for index in range(0,u):
#         s=eval(input("Enter the number:"))
#         mySet.append(s)
#     return set(mySet)
# mySet=create_set()
# print("The set is:",mySet)
# print(type(mySet))
# convertedSetToTuple=tuple(mySet)
# print("The converted set to tuple is:",convertedSetToTuple)
# print(type(convertedSetToTuple))



# #to convert a list of dicts to tuple of lists
# # Sample list of dictionaries
# list_of_dicts = [{"name": "Madhusshree", "classSec": "Cse(AI-DE)"}, {"name": "Rhea", "classSec": "Cse gen"}]

# # Initialize empty lists to store values
# names = []
# classSecs = []

# # Extract values from each dictionary and append them to corresponding lists
# for d in list_of_dicts:
#     names.append(d.get("name"))
#     classSecs.append(d.get("classSec"))

# # Convert lists to a tuple
# tuple_of_lists = (names, classSecs)

# print("Tuple of lists:", tuple_of_lists)




# #sort tuple list by Nth element of tuple
# # Sample list of tuples
# tuple_list = [(3, 6, 2), (1, 8, 5), (4, 3, 9), (2, 7, 1)]

# # Function to get the nth element of a tuple
# def get_nth_element(item):
#     return item[n]  # Assuming n is the index of the element you want to sort by

# # Index of the element you want to sort by
# n = 1  # Sorting by the second element (index 1) of each tuple

# # Sort the list of tuples by the nth element
# sorted_tuple_list = sorted(tuple_list, key=get_nth_element)

# print("Sorted list of tuples by the nth element:", sorted_tuple_list)




# #finding tuple indices from other tuple list
# def find_indices(tuple_list, search_tuple):
#     indices = []
#     for i, tup in enumerate(tuple_list):
#         if tup == search_tuple:
#             indices.append(i)
#     return indices
# # Sample lists of tuples
# tuple_list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# tuple_list2 = [(4, 5, 6), (10, 11, 12), (7, 8, 9), (13, 14, 15)]
# # Find indices of tuples from tuple_list1 in tuple_list2
# for tup in tuple_list1:
#     indices = find_indices(tuple_list2, tup)
#     print(f"Tuples {tup} found at indices:", indices)





# #converting dict value list to dictionary list in python
# # Original dictionary with value lists
# original_dict = {'name': ['Alice', 'Bob', 'Charlie'],
#                   'age': [25, 30, 35],
#                   'city': ['New York', 'Los Angeles', 'Chicago']}


# # Get the keys and values from the original dictionary
# keys = original_dict.keys()
# values = original_dict.values()

# # Create a list of dictionaries
# result_list = [dict(zip(keys, v)) for v in zip(*values)]

# # Print the result list
# print(result_list)