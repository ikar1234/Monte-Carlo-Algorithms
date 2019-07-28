from Hardcore import Hardcore

l = []
size =10
for i in range(10**4):
    h = Hardcore(size)
    h.change(times=400)
    l.append(h.count_ones())

print(f"Expected number with size {size} is",sum(l)/len(l))
