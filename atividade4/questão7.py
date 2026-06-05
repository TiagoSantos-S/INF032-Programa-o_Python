# 7. Crie a = {"x": 1, "y": 2} e b = {"y": 20, "z": 3}. agora crie um dicionario ‘z’, com a mesclagem de
# ‘a’ e ‘b’

a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}
z = {**a, **b}  

print(z)