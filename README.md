# PQC_Cortex-M4_NTRU-NTT
For testing Efficient, Verifiable and Large enough $\large q$ over $\large \mathbb{Z}_{q}$ NTRU / NTT Multiplication in Academia Sinica IIS.

1. For [Pqc_ntruhps2048677_primeANDroot](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/tree/main/Pqc_ntruhps2048677_primeANDroot), We use [Decode.fr/Prime-Numbers-Search](https://www.dcode.fr/prime-numbers-search) to find 1000 Closest Primes larger than $\large q'$ ( $\large{q > 2 * (\pm} \Large{\frac{q}{2}} \large{)^2 * n = 2 * (} \Large{\frac{2048}{2}} \large{)^2 * 677}$ ) and put in **Prime_list** because of the Specification of ntruhps2048677 (Details see in [Multi-Parameter Support with NTTs for NTRU...](https://troll.iis.sinica.edu.tw/by-publ/recent/ntt_ntru_ntrup.pdf)).

2. We tested and used the **Prime_list** to find three Roots $\large{x\ =\ y\ *\ z;\ (y^3)\mod\ q'\ =\ (z^512)\mod\ q'\ =\ 1}$ over $\large \mathbb{Z}_{2048}$ for NTT. 
> ![image](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/assets/67849251/6a156270-95a9-4333-8bf1-82cc03b1951a)
