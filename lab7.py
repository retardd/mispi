import numpy as np

print("Введите порождающую матрицу построчно (конец матрицы enter):")
matr = []
new_str = input()
while new_str != "":
    matr.append(list(map(int, new_str.split())))
    new_str = input()
dl = len(matr)
matr2 = []
for i in range(pow(2, dl)):
    matr_buff = []
    for j in range(dl):
        matr_buff.append(0)
    matr2.append(matr_buff)
for i in range(pow(2, dl)):
    buff = int(format(i, 'b'))
    dl2 = dl - 1
    while buff != 0:
        matr2[i][dl2] = buff % 10
        buff = buff // 10
        dl2 -= 1


a = np.array(matr)
b = np.array(matr2)
new_matr = np.dot(b, a)
for c in new_matr:
    for v in range(len(c)):
        if c[v] % 2 == 0:
            c[v] = 0
        else:
            c[v] = 1

new_matr2 = []
for stroka in new_matr:
    str1 = ''
    for j in range(len(stroka)):
        str1 += str(stroka[j])
    new_matr2.append(str1)

min = len(new_matr[0])
for i in range(len(new_matr) - 1):
    for j in range(i + 1, len(new_matr)):
        count = 0
        for c in range(len(matr[0])):
            if new_matr2[i][c] != new_matr2[j][c]:
                count += 1
        if count < min:
            min = count

for str in new_matr:
    print(str)
print("Кодовое расстояние = ", min)