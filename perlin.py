
import matplotlib.pyplot as plt
from math import sqrt, floor
from random import uniform, randint, choice, seed

def enlarge(img):
    x,y = len(img[0]),len(img)
    new = [[] for i in range(y)]
    for i in range(y):
        for j in range(x):
            new[i].append(img[i][j])
            try:
                new[i].append(((img[i][j]+img[i][j+1])/2))
            except:
                break

    line_collection = []
    
    for i in range(y):
        line = []
        for j in range(len(new[0])+1):
            
            try:
                line.append((((new[i][j]+new[i+1][j])/2)))
            except:
                break
        line_collection.append(line)
            

    out=[]
    
    for i in range(y):
        out.append(new[i])
        if line_collection[i] != []:
            out.append(line_collection[i])
        
    return out

def Lerp(t, a1, a2):
    return a1 + t*(a2-a1)

def smoothstep(left, right, val):
    val = clamp((val - left) / (right - left), 0, 1)
    return val**2*(3-2*val)
    #return val**3*(val*(val*6-15)+15)

def clamp(x, lowerlimit, upperlimit):
    if (x < lowerlimit):
        x = lowerlimit
    if (x > upperlimit):
        x = upperlimit
    return x
    
def interp(img, smooth_val):
    for i in range(smooth_val):
        img = enlarge(img)
    return img

def smooth1(dots,range_):
    x,y = len(dots),len(dots[0])
    out = [[0 for j in range(x)] for i in range(y)]
    for i in range(y):
        for j in range(x):
            avg = 0
            for i0 in range(i-range_,i+range_):
                for j0 in range(j-range_,j+range_):
                    avg += dots[i0%y][j0%x]/2**((abs(i-i0)+abs(j-j0))+2)
            out[i][j] = avg
    return out


def SmoothedNoise(x, y, maxx, maxy, matr):
    corners = 0
    sides = 0
    try:
        corners += matr[y-1][x-1]
    except:
        pass
    try:
        corners += matr[y+1][x-1]
    except:
        pass
    try:
        corners += matr[y-1][x+1]
    except:
        pass
    try:
        corners += matr[y+1][x+1]
    except:
        pass
    
    try:
        sides += matr[y][x-1]
    except:
        pass
    try:
        sides += matr[y][x+1]
    except:
        pass
    try:
        sides += matr[y+1][x]
    except:
        pass
    try:
        sides += matr[y-1][x]
    except:
        pass
    corners /= 16
    sides /= 8
    center = matr[y][x] / 4
    return corners + sides + center

    
def map_to(val,min_input,max_input,min_out,max_out):
    return (val - min_input) * (max_out - min_out) / (max_input - min_input) + min_out

def direct(array2d):
    out = []
    for i in array2d:
        for j in i:
            out.append(j)
    return out

    
def invert_array(array):
    out = [[0 for i in range(len(array))] for j in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            out[i][j] = -1*array[i][j]
    return out

def enlarge(img):
    x,y = len(img[0]),len(img)
    new = [[] for i in range(y)]
    for i in range(y):
        for j in range(x):
            new[i].append(img[i][j])
            try:
                new[i].append(((img[i][j]+img[i][j+1])/2))
            except:
                break

    line_collection = []
    
    for i in range(y):
        line = []
        for j in range(len(new[0])+1):
            
            try:
                line.append((((new[i][j]+new[i+1][j])/2)))
            except:
                break
        line_collection.append(line)
            

    out=[]
    
    for i in range(y):
        out.append(new[i])
        if line_collection[i] != []:
            out.append(line_collection[i])
        
    return out


def loop(arr,range_,sm):
    for i in range(sm):
        arr = smooth1(arr,range_)
    return arr

def perlin(x,y,gradient_size,smoothness):
    vectors = []
    for i in range(x+1):
        line = []
        for j in range(y+1):
            line.append((uniform(-1,1),uniform(-1,1)))
        vectors.append(line)
    lines = [[] for i in range(y*gradient_size)]
    for i in range(y):
        for j in range(x):
            for k in range(gradient_size):
                for l in range(gradient_size):
                    vector1 = vectors[i][j]
                    vector2 = vectors[i+1][j]
                    vector3 = vectors[i][j+1]
                    vector4 = vectors[i+1][j+1]
                    v1_val = (vector1[0]-k)*vector1[0]+(vector1[1]-l)*vector1[1]
                    v2_val = (vector2[0]-gradient_size+k)*vector2[0]+(vector1[1]-l)*vector2[1]
                    v3_val = (vector3[0]-k)*vector3[0]+(vector1[1]-gradient_size+l)*vector3[1]
                    v4_val = (vector4[0]-gradient_size+k)*vector4[0]+(vector1[1]-gradient_size+l)*vector4[1]
                    #avg_1 = Lerp(.5,v3_val,v4_val)
                    #avg_2 = Lerp(.5,v1_val,v2_val)
                    #lines[j*gradient_size+k].append(Lerp(.5,avg_1,avg_2))
                    lines[j*gradient_size+k].append((v1_val+v2_val+v3_val+v4_val)/4)
    s = gradient_size-abs(gradient_size%2-1)
    return interp(loop(lines,s,s),smoothness)

seed(1234567)
img = perlin(14,14,6,1)
plt.imshow(img,'gray')
plt.show()
