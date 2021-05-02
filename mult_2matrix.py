import sys

matrix1 = []
matrix2 = []

def matrix_created():
    try:

        r1 = int(input("Введите число строк матрицы No1: "))
        c1 = int(input("Введите число столбцов матрицы No1: "))
        r2 = int(input("Введите число строк матрицы No2: "))
        c2 = int(input("Введите число столбцов матрицы No2: "))

        if c1 != r2:
            print("Ошибка Число столбцов матрицы №1 должно совпадать с числом  строк матрицы №2!")
            sys.exit(1)

    except ValueError:
        print('Ошибка! Должно быть целое число!')
        sys.exit(1)

    for i in range(r1):
        a = []
        for j in range(c1):
            a.append(int(input(f'Введите {j+1} число {i+1} строки матрицы 1:')))
        matrix1.append(a)

    for i in range(r2):
        a = []
        for j in range(c2):
            a.append(int(input(f'Введите {j+1} число {i+1} строки матрицы 2:')))
        matrix2.append(a)

def multiplication():
    i = 0
    result = []
    for m in range(len(matrix1)):
        row = []
        k = 0
        result.append(row)

        for l in range(len(matrix2[1])):
            j=0
            number_to_sum = []
            for t in range(len(matrix1[0])):
                number_to_sum.append(matrix1[i][j]*matrix2[j][k])
                j+=1
            k+=1
            row.append(sum(number_to_sum))
        i+=1
    return print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result]))

def run():
    matrix_created()
    multiplication()

if __name__ == '__main__':
    run()