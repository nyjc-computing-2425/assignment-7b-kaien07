# Built-in imports
import math

# Your code below
GRADE = {}
for i in range(1, 101):
    if i >= 70:
        GRADE.update({i: 'A'})
    elif i >= 60:
        GRADE.update({i: 'B'})
    elif i >= 55:
        GRADE.update({i: 'C'})
    elif i >= 45:
        GRADE.update({i: 'D'})
    elif i >= 40:
        GRADE.update({i: 'E'})
    else:
        GRADE.update({i: 'U'})


def read_testscores(filename):
    """
    reads data from file filename and represents each row's data as a dict

    Parameters
    ------------
    filename: string
        file to be read
    ------------

    Returns
    ------------
    list
        formatted list of dictionaries of data from every row
    ------------
    """
    data = []
    with open(filename, 'r') as file:
        header = file.readline().split(',')
        for elem in file:
            class_, name = elem.split(',')[0:2]
            papers = tuple(map(int, elem.strip().split(',')[2:]))
            p1, p2, p3, p4 = papers
            overall = math.ceil((p1 / 30 * 15) + (p2 / 40 * 30) +
                                (p3 / 80 * 35) + (p4 / 30 * 20))
            grade = GRADE.get(overall)
            data_line = {
                "class": class_,
                "name": name,
                "overall": overall,
                "grade": grade
            }
            data.append(data_line)
    return (data)


def analyze_grades(studentdata):
    """
    takes student data and returns a dict representing count of each grade for each class

    Parameters
    ------------
    studentdata: list
        list of grades to be analyzed
    ------------

    Returns
    ------------
    list
        list of count of grades for each class
    ------------
    """
    class_list = []
    grades_dict_line = {}
    grades_dict = {}
    for elem in studentdata:
        if elem.get("class") not in class_list:  # initializes class_list
            class_list.append(elem.get("class"))
    for class_ in class_list:
        grades_dict_line = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'S': 0,
            'U': 0
        }
        for elem in studentdata:
            if elem.get("class") == class_:
                grade = elem.get("grade")
                grades_dict_line.update(
                    {grade: grades_dict_line.get(grade) + 1})
        grades_dict.update({class_: grades_dict_line})
    return (grades_dict)
