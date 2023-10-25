phy = input().split(",")
math = input().split(",")
chem = input().split(",")
comp = input().split(",")

count = 0
fail = []

for i in phy:
    if i not in fail:
        fail.append(i)

for i in math:
    if i not in fail:
        fail.append(i)

for i in chem:
    if i not in fail:
        fail.append(i)

for i in comp:
    if i not in fail:
        fail.append(i)

print(len(fail))
