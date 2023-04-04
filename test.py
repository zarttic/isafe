import rsa
p = 5
q = 17

print(rsa.encode(ord("L") - 65,5,17,11))
print(rsa.encode(ord("Y") - 65,5,17,11))
print(rsa.encode(ord("J") - 65,5,17,11))
print(rsa.decode(rsa.encode(7,5,17,11),p,q,11))
print()