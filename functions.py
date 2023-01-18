def promos(mye, grade):
    '''Takes in float mye and str grade. returns float: the required score for promos.'''

    # convert grade (str) to minimum grade score (int)
    grade_dict = {
        "A": 70,
        "B": 60,
        "C": 55,
        "D": 50,
        "E": 45,
        "S": 35,
        "U": 0
    }
    grade = grade_dict[grade]

    promos = (grade - 0.2*mye) / 0.8
    promos = round(promos, 2)
    return max(promos, 0)