from collections import OrderedDict

static_Size = 1536


def read_file_lines_to_list(file_path):
    result_list = []
    with open(file_path, 'r') as file:
        for line in file:
            result_list.append(line.strip())
    return result_list


def find_modular_base(n, k):
    base_a_findlist = []
    judge = 0
    for base_a in range(2, static_Size):
        if pow(base_a, static_Size * k, n) == 1:
            for i in range(1, 512):
                if pow(base_a, 3 * k * i, n) == 1:
                    judge = 1
                    break
            for i in range(1, 3):
                if pow(base_a, 512 * k * i, n) == 1:
                    judge = 1
                    break
            if judge == 1:
                judge = 0
                continue
            base_a_findlist += [base_a]
    return base_a_findlist


final_512rootZ_Dic = {}
final_3rootY_Dic = {}
prime = read_file_lines_to_list('prime_list')
for j in prime:
    proot_k = (int(j) - 1) // static_Size
    rootA_findList = find_modular_base(int(j), proot_k)
    if rootA_findList:
        for u in rootA_findList:
            print("---")
            cacheY = pow(u, 512 * proot_k, int(j))
            print(f"The y is: {cacheY}")
            cacheZ = pow(u, 3 * proot_k, int(j))
            final_512rootZ_Dic[cacheZ] = [j, cacheY]
            print(f"The z is: {cacheZ}")

        print(f"The prime is: {j}", end="\n===")
    else:
        print(f"For the prime {j}, there are no roots y,z")

FinalDict = OrderedDict(sorted(final_512rootZ_Dic.items()))
print("***===***===***===***===***===***===***===***===",
      f"Found the final prime {list(FinalDict.values())[0][0]}",
      f"The primitive root Y of {list(FinalDict.values())[0][0]} is {list(FinalDict.values())[0][1]}",
      f"The primitive root Zeta(w) of {list(FinalDict.values())[0][0]} is {list(FinalDict.keys())[0]}",
      f"The lowest primitive root Y is 394137924",
      "x = yz; y^3 = z^512 = 1",
      "===***===***===***===***===***===***===***===***===", sep="\n")
