class calculsbasics:
    """Esta classe conté la funcio max3 per calcular el maxim de 3 numeros i
   la funció DescHoraria per calcular el temps"""
    def max3(a,b,c):
        """La funcio max3 el que fa es calcular entre 3 numeros quin es el mes gran. """
        if a>b and a>c:print(a)
        elif b>a and b>c:print(b)
        else:print(c)

    def DescHoraria(n):
        """La funcio DescHoraria el que fa es calcular quants Hores, minuts i segons son 86500 segons"""
        h = n // 3600
        m = (n % 3600) // 60
        s = n % 60
        suma=str(h)+str("Horas ")+str(m)+str("Minuts ")+str(s)+str("Segons")
        return "El resultat es "+ suma

help(calculsbasics)
