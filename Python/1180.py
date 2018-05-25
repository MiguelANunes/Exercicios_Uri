N = int(input())
V = [int(i) for i in input().split()]

print("Menor valor: {:d}".format(min(V)))
print("Posicao: {:d}".format(V.index(min(V))))
