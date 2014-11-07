'''
Kodutoo 14
07.11.2014
Andres Liiver
'''

import sympy

def main():
    a, x = sympy.symbols('a x')
    f1 = x**3 + 4*x**2 + 100
    f2 = 4*sympy.sin(x) + sympy.cos(x)
    S = sympy.Abs(sympy.integrate(f2-f1, (x,0,a)))
    print(S)
    print(S.subs(a, 20))
    print(S.evalf(subs={a: 20}))

if __name__ == "__main__":
    main()
