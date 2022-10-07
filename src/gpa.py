import argparse


def average_grade(file_path):
    weighted_grades = 0.0
    points = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip('\n').split()
            point = float(line[0])
            weighted_grade = float(line[1]) * point
            points += point
            weighted_grades += weighted_grade
    return weighted_grades / points


def average_level_grade(file_path):
    weighted_grades = 0.0
    points = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip('\n').split()
            point = float(line[0])
            grade = float(line[1])
            if grade >= 90:
                weighted_grade = point * 4.0
            elif grade >= 80:
                weighted_grade = point * 3.0
            elif grade >= 70:
                weighted_grade = point * 2.0
            elif grade >= 60:
                weighted_grade = point * 1.0
            else:
                weighted_grade = 0.0
            points += point
            weighted_grades += weighted_grade
    return weighted_grades / points


def hk_grade(file_path):
    weighted_grades = 0.0
    points = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip('\n').split()
            point = float(line[0])
            grade = float(line[1])
            if grade >= 100:
                weighted_grade = point * 4.0
            elif grade >= 90:
                weighted_grade = point * 3.7
            elif grade >= 85:
                weighted_grade = point * 3.5
            elif grade >= 80:
                weighted_grade = point * 3.2
            elif grade >= 75:
                weighted_grade = point * 3.0
            points += point
            weighted_grades += weighted_grade
    return weighted_grades / points


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', type=str, default='level_grade')
    parser.add_argument('--file', type=str, default='data/bachelor_grade.txt')
    args = parser.parse_args()

    res = None
    if args.algorithm == 'average_grade':
        res = average_grade(args.file)
    elif args.algorithm == 'level_grade':
        res = average_level_grade(args.file)
    elif args.algorithm == 'hk_grade':
        res = hk_grade(args.file)

    print(args.algorithm, res)
