def sample():
    line = []
    sample_file = open("fairfield.data", "r")
    for file_line in sample_file:
        line.append(file_line.strip().split("\t"))  #Line in file -> list of list of varaibles

    # Create a list of dictionaries
    sample_list = []
    for data_row in line:
        if data_row == line[0]: #First element is varaible lable
            continue
        line_dic = {}
        for x in enumerate(data_row):   # enumerate: x -> [count , item] 
            line_dic[line[0][x[0]]] = x[1]  # Assign key-value pairs
        sample_list.append(line_dic)
    return sample_list

# Example
print(sample()[0]["Fish"])