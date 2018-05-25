A, B = map(float, input().split())

Delta = B - A
Percent = (Delta*100)/A
print("{:.2f}%".format(Percent))
