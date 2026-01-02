import argparse

def newton(f, x=0, h=0, n=0, precision=0):

    for i in range(n):
        f_x = f(x)

        if abs(f_x) < precision:
            print(f"miejsce zerowe: {x}, po {i} krokach")
            return x

        df = (f(x + h) - f_x) / h

        if df == 0:
            print("pochodna = 0")
            return None
        x -= (f_x / df)

    print(f"nie udalo sie po {n} krokach, ostatnie x = {x}")


parser = argparse.ArgumentParser(description="miejsca zerowe metoda newtona")
parser.add_argument("f", type=str, help="funkcja jednoargumentowa")
parser.add_argument("--start", type=float, default=1.0, help="punkt startowy")
parser.add_argument("--h", type=float, default=1e-5, help="wielkość kroku w pochodnej")
parser.add_argument("--steps", type=int, default=100, help="ilosć kroków metody")
parser.add_argument("--precision", type=float, default=1e-6, help="dokładność")
args = parser.parse_args()

def make_f(expr):
    return lambda x: eval(expr, {"x": x, "__builtins__": {}})

f = make_f(args.f)

newton(f, x=args.start, h=args.h, n=args.steps, precision=args.precision)
