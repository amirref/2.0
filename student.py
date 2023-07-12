num_students = int(input("tedad daneshjooyan kelas ra vared konid: "))

sum_grades = 0
mx_nomre=-float("inf")
min_nomre = float("inf")

for i in range(num_students):
    m=i+1
    print("lotfan nomre daneshjooye shomare",m,"ra vared konid")
    nomre=float(input("nomre daneshjoo:"))
    sum_grades+=nomre
    if nomre > mx_nomre:
        mx_nomre = nomre
    if nomre < min_nomre:
        min_nomre = nomre
mean_nomre = sum_grades / num_students        


print("miangin nomarat:",mean_nomre,)
print("bishtarin nomre:",mx_nomre,)
print("kamtarin nomre:",min_nomre,)




