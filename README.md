# PQC_Cortex-M4_NTRU-NTT
For testing efficient, verifiable and Large enough $q$ for $mathbb{Z}_{q}$ NTRU / NTT Multiplication in Academia Sinica IIS.

1. For [Pqc_ntruhps2048677_primeANDroot](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/tree/main/Pqc_ntruhps2048677_primeANDroot), we use [Decode.fr/Prime-Numbers-Search](https://www.dcode.fr/prime-numbers-search) to find 1000 closest primes to $q'$ ( $q > 2 * (\pm q/2) * n = 2 * (2048/2) * 677$ ) and put in prime_list because of specification of ntruhps2048677 (details see in [Multi-Parameter Support with NTTs for NTRU...](https://troll.iis.sinica.edu.tw/by-publ/recent/ntt_ntru_ntrup.pdf).

2. We tested and used the prime_list to find three roots $x = y * z $ ; $ (y^3) mod q'= (z^512) mod q' = 1$ over $\Z_{2048}$ for NTT. ![image](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/assets/67849251/6a156270-95a9-4333-8bf1-82cc03b1951a)
