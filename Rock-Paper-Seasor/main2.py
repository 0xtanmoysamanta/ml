i = 3651** 365 
print (i)
j = 3650** 365
h = i/j
print (h)
with open("score2.tex", 'a', encoding ='utf-8', ) as Fil:
     Fil.write(f" Result : {h}")
