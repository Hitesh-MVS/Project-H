def ramu(s):
    if s=="":
        return 0
    else:
        return 1+ramu(s[1:])

s="hitesh"
res=ramu(s)
print(res)