cars = ["lamborghini", "ferari", "mclaren"]
for x in cars:
    print(x)
#---------------------------------------
for x in "lamborghini":
    print(x)
#---------------------------------------
cars = ["lamborghini", "ferari", "mclaren"]
for x in cars:
    print(x)
    if x == "ferari":
        break
#---------------------------------------
cars = ["lamborghini", "ferari", "mclaren"]
for x in cars:
    if x == "ferari":
        break
    print(x)
#---------------------------------------
cars = ["lamborghini", "ferari", "mclaren"]
for x in cars:
    if x == "ferari":
        continue
    print(x)