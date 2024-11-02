import sys

if len(sys.argv) != 4:
    print("Argument error")
    print("Usage: create_forward_functions.py <num_forwards> <num_ordinal_forwards> <num_shared_forwards>")
    exit()

number_of_forwards = int(sys.argv[1])
number_of_ordinal_forwards = int(sys.argv[2])
number_of_shared_forwards = int(sys.argv[3])
macros_num_columns = 50
vector_num_columns = 50
    
with open("forward_functions.txt", "w") as file:
    # Create normal forward macros
    for i in range(0, number_of_forwards):
        if i % macros_num_columns == 0 and i != 0:
            file.write("\n")
        file.write("GenerateForwardFunction(" + str(i) + ") ")
            
    # Create normal forwards
    file.write("\nstd::vector<void*> forwardAddresses = {")
    for i in range(0, number_of_forwards):
        if i % vector_num_columns == 0:
            file.write("\n    ")
        if i == number_of_forwards - 1:
            file.write("&Forward" + str(i))
        else:
            file.write("&Forward" + str(i) + ", ")
    file.write("\n};")

    file.write("\n\n")
    
    # Create ordinal forward macros
    for i in range(1, number_of_ordinal_forwards + 1):
        file.write("GenerateForwardOrdinalFunction(" + str(i) + ") ")
        if i % macros_num_columns == 0 and i != number_of_ordinal_forwards:
            file.write("\n")

    # Create ordinal forwards
    file.write("\nstd::vector<void*> forwardOrdinalAddresses = {")
    file.write("\n    ")
    for i in range(1, number_of_ordinal_forwards + 1):
        if i == number_of_ordinal_forwards:
            file.write("&ForwardOrdinal" + str(i))
        else:
            file.write("&ForwardOrdinal" + str(i) + ", ")
        if i % vector_num_columns == 0 and i != number_of_ordinal_forwards:
            file.write("\n    ")
    file.write("\n};")
    
    file.write("\n\n")
    
    # Create shared forward macros
    for i in range(0, number_of_shared_forwards):
        if i % macros_num_columns == 0 and i != 0:
            file.write("\n")
        file.write("GenerateForwardSharedFunction(" + str(i) + ") ")

    # Create shared forwards
    file.write("\nstd::vector<void*> forwardSharedAddresses = {")
    for i in range(0, number_of_shared_forwards):
        if i % vector_num_columns == 0:
            file.write("\n    ")
        if i == number_of_shared_forwards - 1:
            file.write("&ForwardShared" + str(i))
        else:
            file.write("&ForwardShared" + str(i) + ", ")
    file.write("\n};")