prime_Q = 1419778561;
#prime_Q = 1419780097;
#prime_Q = 1419781633;

k = (prime_Q - 1) // 1536 ;
ub = 1536;

Q_list = [];
final_list = [];
z_list = [];

for i in range(2, ub+1):
    if( pow(i, 1536*k, prime_Q) == 1 ):
        Q_list += [pow(i, k, prime_Q)]
        #print("a =",i,"found :", pow(i, k, prime_Q));

#print("------------------------------");
for ak in Q_list:
    for j in range(2,1536):
        if(int(pow(ak, j, prime_Q))==1):
            #print("a =",Q_list.index(a)+2,"fail at power",j);
            break;
        elif(j == 1535):
            final_list += [ak];
#print("------------------------------");
if final_list:
    #print("primitive 1536-th root :", final_list,"\n");
    print("primitive 1536-th root found");
else:
    print("primitive 1536-th root not found\n");

for ak in final_list:
    z_list += [pow(ak, 3, prime_Q)];

z_list.sort();
print("minimum primitive 512-th root :",z_list[0],"\n");