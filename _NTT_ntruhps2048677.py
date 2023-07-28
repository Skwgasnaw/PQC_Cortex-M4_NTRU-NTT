import secrets

staticN = 677
staticQ = 2048
static_Qprime = 1419778561
staticZ = 4360860
staticSize = 1536
staticPFA_N1 = 3
staticPFA_N2 = 512
nttK3y1_List1 = [[0]*staticPFA_N2 for _ in range(staticPFA_N1)]
nttK3y1_List2 = [[0]*staticPFA_N2 for _ in range(staticPFA_N1)]
nttK3y1_final = [[0]*staticPFA_N2 for _ in range(staticPFA_N1)]


def classic_schoolbook_multiplication(polylist1, polylist2):
    final = [0] * staticN
    for i in range(0, staticN):
        for j in range(0, staticN):
            final_index = i + j

            while(final_index > staticN - 1):
                final_index -= staticN

            final[final_index] += pow(polylist1[i] * polylist2[j], 1, staticQ)
            final[final_index] = pow(final[final_index], 1, staticQ)
    return final


def pfa_good_permutation(polylist1, polylist2):
    global nttK3y1_List1
    global nttK3y1_List2
    for i in range(0, staticPFA_N1):
        for j in range(0, staticPFA_N2):
            nttK3y1_List1[i][j] = polylist1[pow(i * staticPFA_N2 + j * staticPFA_N1, 1, staticSize)]
            nttK3y1_List2[i][j] = polylist2[pow(i * staticPFA_N2 + j * staticPFA_N1, 1, staticSize)]


def cal_ntt_coefficient(judge):
    cal_indexA = [0, 4, 2, 6, 1, 5, 3, 7]
    for i in range(0, 3):
        cal_indexA = [j * 2 for j in cal_indexA]
        cal_indexB = [j + 1 for j in cal_indexA]
        cal_indexC = cal_indexA + cal_indexB
        if judge == "zeta" and i == 2:
            return cal_indexC
        else:
            cal_indexC = [j * 2 for j in cal_indexC]
            cal_indexB = [j + 1 for j in cal_indexC]
            cal_indexA = cal_indexC + cal_indexB
    return cal_indexA


def cooley_tukey_butterfly():
    global nttK3y1_List1
    global nttK3y1_List2
    index_coefficient = cal_ntt_coefficient("brv")
    for stage in range(0, 9):
        binary = pow(2, stage)
        zeta_index = cal_ntt_coefficient("zeta")
        print(nttK3y1_List1[0])
        for index_x in range(0, staticPFA_N1):
            for index_yi in range(0, staticPFA_N2 // (2 * binary)):
                for index_yj in range(0, binary):
                    cache = pow(nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]]
                                * pow(staticZ, zeta_index[index_yj], static_Qprime), 1, static_Qprime)
                    nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]] = \
                        pow(nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] - cache, 1, static_Qprime)
                    nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] = \
                        pow(nttK3y1_List1[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] + cache, 1, static_Qprime)

                    cache = pow(nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]]
                                * pow(staticZ, zeta_index[index_yj], static_Qprime), 1, static_Qprime)
                    nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]] = \
                        pow(nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] - cache, 1,
                            static_Qprime)
                    nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] = \
                        pow(nttK3y1_List2[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] + cache, 1,
                            static_Qprime)

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
                nttK3y1_final[index][i] += pow(nttK3y1_List1[j][i] * nttK3y1_List2[k][i], 1, pow(staticZ, 3, static_Qprime) - 1)
                nttK3y1_final[index][i] = pow(nttK3y1_final[index][i], 1, static_Qprime)


def inverse_ntt():
    global nttK3y1_final
    index_coefficient = cal_ntt_coefficient("brv")
    for stage in range(0, 9):
        binary = pow(2, stage)
        zeta_index = cal_ntt_coefficient("zeta")
        zeta_coefficient = 0
        print(nttK3y1_final[0])
        for index_x in range(0, staticPFA_N1):
            for index_yi in range(0, staticPFA_N2 // (2 * binary)):
                for index_yj in range(0, binary):
                    cacheA = (nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] +
                              nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]]) // 2
                    cacheB = (nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] -
                              nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]]) // 2
                    nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj]] = pow(cacheA, 1, static_Qprime)
                    nttK3y1_final[index_x][index_coefficient[(index_yi * binary * 2) + index_yj + binary]] = \
                        pow(cacheB * pow(staticZ, -zeta_index[zeta_coefficient], static_Qprime), 1, static_Qprime)
                    zeta_coefficient += 1
                    if zeta_coefficient >= staticPFA_N2 // (2 * binary):
                        zeta_coefficient = 0


def inverse_pfa_good_permutation():
    global nttK3y1_final
    polylist_final = [0] * staticSize
    for i in range(0, staticPFA_N1):
        for j in range(0, staticPFA_N2):
            index = pow((staticPFA_N2 * i + staticPFA_N1 * j), 1, staticSize)
            polylist_final[index] = nttK3y1_final[i][j]
    return polylist_final


def final_stage(polyList_final):
    polyStage_final = [0] * staticN
    for i in range(0, staticSize):
        index = pow(i, 1, staticN)
        polyStage_final[index] += pow(polyList_final[i], 1, staticQ)
        polyStage_final[index] = pow(polyStage_final[index], 1, staticQ)
    for i in range(0, staticN):
        polyStage_final[i] = pow(polyList_final[i], 1, staticQ)
    return polyStage_final


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
polyK3y_List1 = [0] * (staticSize - staticN) + polyK3y_List1
polyK3y_List2 = [0] * (staticSize - staticN) + polyK3y_List2

## PFA re-indexing
pfa_good_permutation(polyK3y_List1, polyK3y_List2)

# Cooley-Tukey FFT
cooley_tukey_butterfly()

# Convolution
convolution()

# Inverse-NTT
inverse_ntt()

# Inverse-Good-Thomas
poly_ntruhps2048677_publicK3y = final_stage(inverse_pfa_good_permutation())

# Final stage
print(f"The Polynomial Result of using NTT Multiplication on Three 9-stage 512 Butterflies is {poly_ntruhps2048677_publicK3y[0]}"
      f", {poly_ntruhps2048677_publicK3y[1]}, ..., {poly_ntruhps2048677_publicK3y[675]}, {poly_ntruhps2048677_publicK3y[676]} for ntruhps2048677.",
      "\n***===***===***===***===***===***===***===***===", sep="\n")

print("Final check the result by comparing two ways of Multiplication... ", f"\n\nResult: {poly_ntruhps2048677_publicK3y==poly_publicK3y}",
      "\n***===***===***===***===***===***===***===***===")
