paisA = 5000000
paisB = 7000000

anos = 0

while paisA <= paisB:
    paisA *= 1.03
    paisB *= 1.02
    anos += 1

print("Anos necessários:", anos)
print("População A:", int(paisA))
print("População B:", int(paisB))