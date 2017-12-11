def get_list_lectures(filename, rating="passed"):
    with open(filename, "r") as f:
        line = f.readlines()
        lst = []
        for el in line:
            lst.append(el.split('\t'))
        new_list = []
        if rating == "passed":
            for char in lst:
                if float(char[1]) >= 4:
                    new_list.append(char[2])
        else:
            for char in lst:
                if float(char[1]) < 4:
                    new_list.append(char[2])
    f.close()
    return new_list
