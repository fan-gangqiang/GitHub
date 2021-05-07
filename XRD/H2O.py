import math

def H2OCalculation():
    langthofHO = 0.98
    angleofHOkey = 104.5

    siteofHx = langthofHO * math.cos(math.radians(180-angleofHOkey))
    siteofHy = langthofHO * math.sin(math.radians(180-angleofHOkey))

    print("O : 0.00  0.00\n")
    print("H1: 0.98  0.00\n")
    print("H2: ",siteofHx,"  ",siteofHy)

if __name__ == '__main__':
    H2OCalculation()