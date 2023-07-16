#palindrome
def check_naive(a):
    b = a[::-1]
    if a ==b:
        return True
    else:
        return False

print("enter the string:")
a = str(input())
print(check_naive(a))


def eff(z):
    n = len(z)
    i = 0
    j = n-1
    while i<=j:
        if z[i] != z[j]:
            return False

        i+=1
        j-=1
    return True

print("enter the string:")
z = str(input())
print(eff(z))
