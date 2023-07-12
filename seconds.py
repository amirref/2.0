S=int(input("lotfan saniye ra vared konid."))
H=S//3600
R=S%3600
M=R//60
s=R%60
print(H,"saat va",M,"daghighe va",s,"saniye")
print(H,":",M,":",s,)
L=input("mayel hastid saat ra ham be daghighe tabdil konim?""___""[bale] ya [kheir]")
print()
if L=="bale" :
    h=float(input("lotfan saat ra vared konid ta mohasebe konam."))
    m=h*60
    print(h,"saat mosavi ast ba",int(m),"daghighe")
    print("************Good luck************")
if L=="kheir" :
    print("************Good luck************")




