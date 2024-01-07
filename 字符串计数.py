s = ''
dic ={}
for i in (list(set(list(s.lower())))):
    dic[i] = s.lower().count(i)
item = (sorted(dic.items(), key=lambda x: x[0], reverse=False))
print(item)
