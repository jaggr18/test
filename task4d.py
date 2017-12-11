from task4a import add_grade
from task4b import get_list_lectures
from task4c import get_ects_by_semester
from task4c import get_lectures_by_semester

add_grade("my_studies.txt")
print(get_list_lectures("my_studies.txt"))
print(get_lectures_by_semester("my_studies.txt"))
print(get_ects_by_semester("my_studies.txt"))
