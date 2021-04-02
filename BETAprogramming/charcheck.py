text = input()
flag = 0
for ch in text:
    if ch.isupper():
        flag += 1
    if ch.islower():
        flag += 2
if flag == 2*len(text):
    print('All Small Letter')
elif flag == len(text):
    print('All Capital Letter')
else:
    print('Mix')
