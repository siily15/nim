def pricey_prod(d):
    return sorted((k for k,v in d.items() if v >= 500), key=lambda x: -d[x])



print(pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50})
print(pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501})
print(pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20})
