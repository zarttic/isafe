def vig(n, key):
    for i in range(len(n)):
        if n[i].isalpha():
            if n[i].isupper():
                print(chr((ord(n[i]) + ord(key[i % len(key)]) - 130) % 26 + 65), end="")
            else:
                print(chr((ord(n[i]) + ord(key[i % len(key)]) - 95*2) % 26 + 95), end="")
        else:
            print("", end=" ")


# n = input()
# key = input()

vig("meet me after the togo party".upper(), "word")
