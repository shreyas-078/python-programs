s = input("Enter your string")
maxsubstr = 0
for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        flag = 0
        for k in range(len(s[i:j])):
            if s[i:j].count(s[i:j][k]) > 1:
                flag=1
        if flag==0:
            maxsubstr = max(len(s[i:j]), maxsubstr)
print("Length of Longest substring without repeating characters is", maxsubstr)