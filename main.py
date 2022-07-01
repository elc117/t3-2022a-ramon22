import math
from ntpath import join
import sys


def svgBegin(l, a):
    return "<svg width='{w}' height='{h}' xmlns='http://www.w3.org/2000/svg'>\n".format(w = l, h = a)

# circulo svg
def svgCircle(x,style):
    return "<circle cx='{X}' cy='{Y}' r='{R}' style = '{S}' />\n".format (X=x[0], Y=x[1], R=x[2], S=style)

# fim do svg
def svgEnd():
    return "</svg>"

def svgStyle(x):
    return "fill:rgb({R},{G},{B}); mix-blend-mode: screen;".format(R=x[0], G=x[1], B=x[2])

def loop(nume,deno):
    if(deno % nume == 0):
        return True
    else:
        return False


def rosa_polar(n,d,r):
    if (loop(n,d)==True):
        loops = d/n
    else:
        loops = d
    list =  []
    j =0.0
    for i in range(0,int(200*math.pi*loops),1):
        j+=0.01
        list.append((750+200*(math.cos(n/d*j))*(math.cos(j)), 350+200*(math.cos(n/d*j))*(math.sin(j)), r))
    return list

def oscar_borboleta(n,d,r):
    if(loop(n,d)== True):
        loops = n/d
    elif(n>d):
        loops = n
    else:
        loops = d
    list =[]
    j =0.0
    for i in range(0,int(200*math.pi*n),1):
        j+=0.01
        list.append((750-200*(math.cos(n*j)*math.cos(n*j) + math.sin(d*j) +0.3)*(math.cos(j)), 350-200*(math.cos(n*j)*math.cos(n*j) + math.sin(d*j) +0.3)*(math.sin(j)), r))
    return list

def limason(a,b,r):
    if (loop(a,b) == True):
        loops = b/a
    else:
        loops = b
    list = []
    j = 0.0
    for i in range(0,int(200*math.pi*loops),1):
        j+=0.01
        list.append(( 750 -(a+ b*(math.cos(j))*math.cos(j)), 350 -(a+ b*(math.sin(j)))*math.cos(j), r))
    return list 

def switch_color(case):
    if (case == "red" or case == "Red" or case =="RED"):
        return (255,0,0)
    elif (case == "blue" or case == "Blue" or case =="BLUE"):
        return (0,0,255)
    elif (case == "green" or case == "Green" or case =="GREEN"):
        return (0,255,0)
    elif (case == "gold" or case == "Gold" or case =="GOLD"):
        return (255,215,0)
    elif (case == "black" or case == "Black" or case =="BLACK"):
        return (0,0,0)

def coloracao(n,d,cores,str):
    if(str=="borbo"):
        if(loop(n,d)== True):
            loops = n/d
        elif(n>d):
            loops = n
        else:
            loops = d
    elif (loop(n,d) == True):
        loops = d/n
    else:
        loops = d
    list =[]
    for i in range(0,int(200*math.pi*loops),1):
        list.append(switch_color (cores))
    return list

def svgElements(func, elements, style):
    return ' '.join(map(func,elements,style))

def svgAll(str,n,d,r,str_cor):
    if(str == "rosa"):
        fig = rosa_polar(n,d,r)
    elif(str == "borbo"):
        fig = oscar_borboleta(n,d,r)
    elif(str == "limason"):
        fig = limason(n,d,r)
    else:
        print("entrada incorreta!")
    palette = coloracao (n, d, str_cor, str)
    return svgElements(svgCircle,fig,map(svgStyle,palette))

# main 
def main():
    str = (sys.argv[1])
    n = float (sys.argv[2]) 
    d = float (sys.argv[3]) 
    r = float (sys.argv[4]) 
    cor = sys.argv[5]
    print ( (svgBegin (1500, 700)) + (svgAll (str,n,d,r,cor)) + svgEnd())

# improvisa uma main() em python
if __name__ == "__main__":
    main()