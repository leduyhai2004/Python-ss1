def gpaConverter(gpa):
    try:
        gpa = float(gpa)
        if gpa < 0 or gpa > 10:
            return 'Please enter a gpa score in 10-point scale'
        elif gpa >= 9.0:
            return 4.0
        elif gpa >= 8.5:
            return 3.7
        elif gpa >= 8.0:
            return 3.5
        elif gpa >= 7.0:
            return 3.0
        elif gpa >= 6.0:
            return 2.5
        elif gpa >= 5.5:
            return 2.0
        elif gpa >= 5.0:
            return 1.5
        elif gpa >= 4.0:
            return 1.0
        else:
            return 0
    except (ValueError, TypeError):
        return 'Please enter a gpa score in 10-point scale'