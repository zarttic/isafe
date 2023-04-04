def caesar(n, ss):
    for i in ss:
        if i.isalpha():
            if i.islower():
                print(chr((ord(i) - 97 + n) % 26 + 97), end="")
            else:
                print(chr((ord(i) - 65 + n) % 26 + 65), end="")
        else:
            print("", end=" ")
    print()


for i in range(2):
    n = eval(input())
    caesar(n, "meet me after the togo party".upper())
#     # caesar(n, "f xj x pqrabkq jxglofkd fk zljmrqbo".upper())
#     caesar(n, "tomorrow is an another day")

# for i in range(0,26):
#     print(i)
#     caesar(i,"q iu i abclmvb,ug bmipbz qa tq")