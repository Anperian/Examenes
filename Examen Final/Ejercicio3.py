def suma(funcion_a):
    def dec1(*args, **kwargs):
        result = sum(funcion_a(*args, **kwargs))
        print("La suma es:", result)
        return result
    return dec1


@suma
def mult(*args):
    result = 1
    for num in args:
        result = result * num
    return [result]


mult(13, 7, 3)
mult(2, 3, 7, 9)
mult(11, 2, 8, 4)
mult(3, 2, 4, 2)
