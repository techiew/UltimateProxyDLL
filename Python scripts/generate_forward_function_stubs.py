number_of_forwards = int(input("Enter amount of forward function stubs to generate: "))
number_of_shared_forwards = int(input("Enter amount of shared forward function stubs to generate: "))

num_columns = 100

with open("forward_function_stubs.txt", "w") as file:
    # Generate function stubs
    for i in range(1, number_of_forwards + 1):
        if i % num_columns == 0:
            file.write("\n")
        file.write(f'extern "C" const char* forward{i}() {{ return("F{i}"); }} ')
        
    file.write("\n\n")
    
    # Generate ordinal function stubs
    for i in range(1, number_of_forwards + 1):
        if i % num_columns == 0:
            file.write("\n")
        file.write(f'extern "C" const char* forward_ordinal{i}() {{ return ("FO{i}"); }} ')

    file.write("\n\n")
    
    # Generate shared function stubs
    for i in range(1, number_of_shared_forwards + 1):
        if i % num_columns == 0:
            file.write("\n")
        file.write(f'extern "C" const char* forward_shared{i}() {{ return ("FS{i}"); }} ')

    file.write("\n\n")

    # Generate list of function addresses
    file.write(f"const std::vector<void*> forward_function_stubs =\n{{\n    ")
    for i in range(1, number_of_forwards + 1):
        if i == number_of_forwards:
            file.write("&forward" + str(i))
        elif i % num_columns == 0:
            file.write("\n    ")
        else:
            file.write("&forward" + str(i) + ", ")
    file.write("\n};")

    file.write("\n\n")

    # Generate list of ordinal function addresses
    file.write(f"const std::vector<void*> forward_ordinal_function_stubs =\n{{\n    ")
    for i in range(1, number_of_forwards + 1):
        if i == number_of_forwards:
            file.write("&forward_ordinal" + str(i))
        elif i % num_columns == 0:
            file.write("\n    ")
        else:
            file.write("&forward_ordinal" + str(i) + ", ")
    file.write("\n};")
    
    file.write("\n\n")
    
    # Generate list of shared function addresses
    file.write(f"const std::vector<void*> forward_shared_function_stubs =\n{{\n    ")
    for i in range(1, number_of_shared_forwards + 1):
        if i == number_of_shared_forwards:
            file.write("&forward_shared" + str(i))
        elif i % num_columns == 0:
            file.write("\n    ")
        else:
            file.write("&forward_shared" + str(i) + ", ")
    file.write("\n};")
    
    file.write("\n\n")
    
    # Generate ordinal export macros
    for i in range(1, number_of_forwards + 1):
        if i % num_columns == 0:
            file.write("\n")
        file.write(f'EXPORT_ORDINAL({i}) ')

    file.write("\n")
    
    print("Generated", number_of_forwards + number_of_shared_forwards, "functions in forward_function_stubs.txt")