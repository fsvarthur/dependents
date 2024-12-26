def return_list(file_name) -> str:
    file = open(file_name,"r+")
    lines = file.readlines()
    list_return = ""
    for line in lines:
        splited_lines = line.split(",")
        listt = splited_lines[0] + splited_lines[3] + splited_lines[5]
        list_return += listt
    return list_return

#return_list("/home/fsv/Downloads/171.csv")