# def calk1(a,b):
#     return a+b
# def calk2(a,b):
#     return a*b
# def math(op,x,y):
#     print(op(x,y))
# math(calk1,5,45)

# calk1=lambda a,b: a+b
# def math(op,x,y):
#     print(op(x,y))
# math(calk1,5,45)

def math(op,x,y):
    print(op(x,y))
math(lambda a,b: a+b,5,45)