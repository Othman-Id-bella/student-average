N1=float(input("Give the value of the note N1:"))
N2=float(input("Give the value of the note N2:"))
N3=float(input("Give the value of the note N3:"))
           

while (N1<0 or N1>20 ):
   N1=float(input("Give the value of the note N1:"))
while (N2<0 or N2>20):
    N2=float(input("Give the value of the note N2:"))
while (N3<0 or N3>20):
    N3=float(input("Give the value of the note N3:"))
A=(N1+N2+N3)/3  
print(A)
if A>=16:
    B="Alright"
elif A<16 and A>14:
    B="Good"
elif A<14 and A>12:
    B=="pretty good"
elif A<12 and A>10:
    B="fair"
else:
    B="sufficient"
print("the studint mintion is:",B)
