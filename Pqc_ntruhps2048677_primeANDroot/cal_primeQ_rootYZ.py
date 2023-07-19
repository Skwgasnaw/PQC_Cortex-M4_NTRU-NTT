def read_file_lines_to_list(file_path):
    result_list = []
    with open(file_path, 'r') as file:
        for line in file:
            result_list.append(line.strip())
    return result_list


def find_modular_base(b, n):
    for a in range(2, n):
        if pow(a, b, n) == 1:
            return a
    return None


b1 = 3
b2 = 512
prime = read_file_lines_to_list('prime_list')
prime3_find = 0
prime512_find = 0

for j in prime:
    prime3_find = find_modular_base(b1, int(j))
    if prime3_find != 0:
        prime512_find = find_modular_base(b2, int(j))
        if prime512_find != 0:
            print(f"The y is: {prime3_find}")
            print(f"The z is: {prime512_find}")
            print(f"The prime is: {j}")
            break
        else:
            print("None")
            prime3_find = 0
            prime512_find = 0

if prime3_find == 0 or prime512_find == 0:
    print("There's no prime GG")
