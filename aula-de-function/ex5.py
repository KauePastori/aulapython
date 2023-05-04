def area(raio, area):
    area = 3.14 * raio ** 2
    return area 

def perimetro(raio, perimetro):
    perimetro = 2 * 3.14 * raio
    return perimetro 

area = 0 
perimetro = 0 
raio = int(input("Digite o valor do raio: "))
area(raio, area)
perimetro(raio, perimetro) 
