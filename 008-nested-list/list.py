if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1], reverse=False)

    st = set(score for name, score in students)
    second_list = sorted(st)[1]

    second_list_students = [name for name, score in students if score == second_list]

    for name in sorted(second_list_students):
        print(name)

