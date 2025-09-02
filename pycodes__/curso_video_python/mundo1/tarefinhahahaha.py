reta1, reta2, reta3 = input().split()
reta1, reta2, reta3 = float(reta1), float(reta2), float(reta3)

lado_a = reta1 #MAIOR

if reta2 > reta3 and reta2 > reta1:
    lado_a = reta2
    
if reta3 > reta1 and reta3 > reta2:
    lado_a = reta3
    
lado_c = reta1 #menor

if reta2 < reta3 and reta2 < reta1:
    lado_c = reta2
    
if reta3 < reta1 and reta3 < reta2:
    lado_c = reta3
    
lado_b = reta1 #do meio

if reta2 < lado_a and reta2 > lado_c:
    lado_b = reta2
    
if reta3 < lado_a and reta3 > lado_c:
    lado_b = reta3
    

if lado_a >= lado_b + lado_c:
    print('NAO FORMA TRIANGULO')
    
else:
    if lado_a**2 > lado_b**2 + lado_c**2:
        print('TRIANGULO OBTUSANGULO')
        
    else:
        if lado_a**2 < lado_b**2 + lado_c**2:
            print('TRIANGULO ACUTANGULO')
            

if lado_a == lado_b and lado_b == lado_c and lado_c == lado_a:
    print('TRIANGULO EQUILATERO')
        
else:
    if lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
        print('TRIANGULO ISOSCELES')
            
    else:
        if lado_a**2 == lado_b**2 + lado_c**2:
            print('TRIANGULO RETANGULO')