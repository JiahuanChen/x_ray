import sys

def zeff(data):
    # [index, number, index, number ...]
    total_z = 0
    total_e = 0
    for i,n in zip(data[::2], data[1::2]):
        i = float(i)
        n = float(n)
        total_z += (i ** 2.94) * n * i
        total_e += n * i
    print (total_z / total_e) ** (1 / 2.94)

if __name__ == '__main__':
    zeff(sys.argv[1:])