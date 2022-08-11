for i in range (1,2):
    for j in range(1,2):
        m = i * j
        print(str(i) + "x" + str(j) +"=" + str(m))


#182
for a in ("fox"):
    print(a)


#183
animals= ("dog","cat","duck","chicken")
for x in animals:
    print(x)
     


#185
cars = ("lexus","honda","bmw","toyota")
for x in cars:
    print(x)
    if x == ("honda"):
        break

#188
cars = ("lexus","honda","bmw","toyota")
for x in cars:
    if x == "bmw":
        continue
    print(x)
        
    

