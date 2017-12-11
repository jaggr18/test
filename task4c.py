def get_lectures_by_semester(filename):
    with open(filename, 'r') as f:
        line = f.readlines()
        lst = []
        for el in line:
            lst.append(el.split('\t'))
        my_dict = {}
        for char in lst:
            my_dict[char[3][:4]] = []
        for elm in lst:
            my_dict.setdefault(elm[3][:4], []).append(elm[2])
    f.close()
    return my_dict


def get_ects_by_semester(filename):
    with open(filename, 'r') as f:
        line = f.readlines()
        lst = []
        for el in line:
            lst.append(el.split('\t'))
        my_dict = {}
        for char in lst:
            my_dict[char[3][:4]] = []
        for elm in lst:
            if float(elm[1]) >= 4:
                my_dict.setdefault(elm[3][:4], []).append(elm[0])
        new_dict = {}
        for i in my_dict.items():
            sum_ects = 0
            for x in i[1]:
                sum_ects += float(x)
                new_dict[i[0]] = sum_ects
        return new_dict
