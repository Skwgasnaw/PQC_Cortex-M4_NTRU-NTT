import secrets

staticN = 677
staticQ = 2048
static_Qmask = 0x03FF
static_Qprime = 1419778561
staticZ = 4360860
staticSize = 1536
staticPFA_N1 = 3
staticPFA_N2 = 512
nttK3y1_List1 = [[0]*staticPFA_N2]*staticPFA_N1
nttK3y1_List2 = [[0]*staticPFA_N2]*staticPFA_N1
nttK3y1_final = [[0]*staticPFA_N2]*staticPFA_N1


def classic_schoolbook_multiplication(polylist1, polylist2):
    final = [0] * staticN
    for i in range(0, staticN):
        for j in range(0, staticN):
            final_index = i + j

            if final_index > staticN - 1:
                final_index -= staticN

            final[final_index] += polylist1[i] * polylist2[j]

    for i in range(0, staticN):
        final[i] = pow(final[i], 1, staticQ)
    return final


def pfa_good_permutation(polylist1, polylist2):
    global nttK3y1_List1
    global nttK3y1_List2
    for i in range(0, staticPFA_N1):
        for j in range(0, staticPFA_N2):
            nttK3y1_List1[i][j] = polylist1[pow(i * staticPFA_N2 + j * staticPFA_N1, 1, staticSize)]
            nttK3y1_List2[i][j] = polylist2[pow(i * staticPFA_N2 + j * staticPFA_N1, 1, staticSize)]


def cal_ntt_coefficient():
    cal_indexA = [0, 4, 2, 6, 1, 5, 3, 7]
    for i in range(0, 3):
        cal_indexA = [j * 2 for j in cal_indexA]
        cal_indexB = [j + 1 for j in cal_indexA]
        cal_indexC = cal_indexA + cal_indexB
        cal_indexC = [j * 2 for j in cal_indexC]
        cal_indexB = [j + 1 for j in cal_indexC]
        cal_indexA = cal_indexC + cal_indexB
    return cal_indexA


def cooley_tukey_butterfly():
    global nttK3y1_List1
    global nttK3y1_List2
    index_coefficient = cal_ntt_coefficient()
    for stage in range(0, 9):
        binary = pow(2, stage)
        zeta_index = [a * ((staticPFA_N2 // 2) // binary) for a in range(0, binary)]
        for index_x in range(0, staticPFA_N1):
            for index_yi in range(0, staticPFA_N2 // (2 * binary)):
                for index_yj in range(0, binary):
                    cache = pow(nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]]\
                            * pow(staticZ, zeta_index[index_yj], static_Qprime), 1, static_Qprime)
                    nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]] = \
                        nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] - cache
                    nttK3y1_List1[index_x][index_coefficient[(index_yi * binary*2) + index_yj]] += cache

                    cache = pow(nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]]\
                            * pow(staticZ, zeta_index[index_yj], static_Qprime), 1, static_Qprime)
                    nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]] = \
                        nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] - cache
                    nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] += cache

def convolution():
    global nttK3y1_List1
    global nttK3y1_List2
    global nttK3y1_final
    for i in range(0, 512):
        for j in range(0, 3):
            for k in range(0, 3):
                index = j + k
                if index >= 3:
                    index -= 3
                nttK3y1_final[index][i] += pow(nttK3y1_List1[j][i]*nttK3y1_List2[k][i], 1, pow(staticZ, 3) - 1)


def inverse_ntt():
    global nttK3y1_final
    index_coefficient = cal_ntt_coefficient()
    for stage in range(8, -1, -1):
        binary = pow(2, stage)
        zeta_index = [a * ((staticPFA_N2 // 2) // binary) for a in range(0, binary)]
        for index_x in range(0, staticPFA_N1):
            for index_yi in range(0, staticPFA_N2 // (2 * binary)):
                for index_yj in range(0, binary):
                    cache = pow(nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]]
                                * pow(staticZ, zeta_index[index_yj], static_Qprime), 1, static_Qprime)
                    nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]] = \
                        nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] - cache
                    nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] += cache


def inverse_pfa_good_permutation():
    global nttK3y1_final
    polylist_final = [0] * staticSize
    for i in range(0, 3):
        for j in range(0, 512):
            index = pow((1024 * i + 513 * j), 1, staticSize)
            polylist_final[index] = nttK3y1_final[i][j]
    return polylist_final


def final_state(polyList_final):
    for i in range(staticN, staticSize):
        index = i - staticN
        for j in range(0, 2):
            if index > (2 * staticN) + 1:
                index -= staticN
            else:
                break
        polyList_final[index] += polyList_final[i]
    for i in range(0, staticN):
        polyList_final[i] &= static_Qmask
    return polyList_final[0:677]

# initialization
private_k3y_generator = secrets.SystemRandom()
polyK3y_List1 = [private_k3y_generator.randint(0, staticQ) for i in range(0, staticN)]
polyK3y_List2 = [private_k3y_generator.randint(0, staticQ) for j in range(0, staticN)]

print("***===***===***===***===***===***===***===***===\n",
      f"First List is {polyK3y_List1[0]}, {polyK3y_List1[1]}, ..., {polyK3y_List1[675]}, {polyK3y_List1[676]}.", sep="\n")
print(f"Second List is {polyK3y_List2[0]}, {polyK3y_List2[1]}, ..., {polyK3y_List2[675]}, {polyK3y_List2[676]}.",
      "\n***===***===***===***===***===***===***===***===\n", sep="\n")

# Schoolbook multiplication of polynomial
poly_publicK3y = classic_schoolbook_multiplication(polyK3y_List1, polyK3y_List2)

## Result of Schoolbook multiplication
print(f"The Polynomial Result of doing School Book Multiplication is {poly_publicK3y[0]}, {poly_publicK3y[1]}, ..., "
      f"{poly_publicK3y[675]}, {poly_publicK3y[676]}.\n")

# Good-Thomas (Prime-factor FFT Algorithm)
## Zero Padding
polyK3y_List1 += [0] * (staticSize - staticN)
polyK3y_List2 += [0] * (staticSize - staticN)

## PFA re-indexing
pfa_good_permutation(polyK3y_List1, polyK3y_List2)

# Cooley-Tukey FFT
cooley_tukey_butterfly()

# Convolution
convolution()

# Inverse-NTT
inverse_ntt()

# Inverse-Good-Thomas
poly_ntruhps2048677_publicK3y = final_state(inverse_pfa_good_permutation())

# Final state
print(f"The Polynomial Result of using NTT Multiplication on Three 9-stage 512 Butterflies is {poly_ntruhps2048677_publicK3y[0]}"
      f", {poly_ntruhps2048677_publicK3y[1]}, ..., {poly_ntruhps2048677_publicK3y[675]}, {poly_ntruhps2048677_publicK3y[676]} for ntruhps2048677.",
      "\n***===***===***===***===***===***===***===***===", sep="\n")

print("Final check the result by compare two ways of Multiplication... ", f"\n\nResult: {poly_ntruhps2048677_publicK3y==poly_publicK3y}",
      "\n***===***===***===***===***===***===***===***===")
