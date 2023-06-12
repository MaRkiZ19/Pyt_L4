# С клавиатуры вводится набор чиел, в качестве разделителя используют пробел.
# Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

data = '15 156 96 3 5 8 52 5'
print(type(data))
print(data)

# data = data.split()
# print(type(data))
# print(data)
# for .......

data=list(map(int,data.split()))
print(data)
print(type(data))
print(type(data[3]))
