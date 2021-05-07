import math

def CellValueCalculation():
    d = 0
    a = 0

    h = float(input("input h:"))
    k = float(input("input k:"))
    l = float(input("input l:"))
    two_theta = float(input("input 2 Theta:"))
    theta = two_theta / 2
    lambda_Kalpha = 1.5406

    d = lambda_Kalpha / (2 * math.sin(math.radians(theta)))

    a = ((d ** 2) * ((h ** 2) + (k ** 2) + (l ** 2))) ** 0.5
    print("a = ", a)

if __name__ == '__main__':
    CellValueCalculation()