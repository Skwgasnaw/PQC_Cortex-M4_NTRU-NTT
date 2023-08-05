# PQC_Cortex-M4_NTRU-NTT
For testing Efficient, Verifiable and Large enough $\large q$ over $\mathbb{Z}_{q}$ NTRU / NTT Multiplication in Academia Sinica IIS.

1. For [Pqc_ntruhps2048677_primeANDroot](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/tree/main/Pqc_ntruhps2048677_primeANDroot), We use [Decode.fr/Prime-Numbers-Search](https://www.dcode.fr/prime-numbers-search) to find 1000 Closest Primes larger than $\large q'$ ($\large{q' > 2 * (\pm} \Large{\frac{q}{2}} \large{)^2 * n = 2 * (} \Large{\frac{2048}{2}} \large{)^2 * 677}$ ) and put in **Prime_list** because of the Specification of ntruhps2048677 (Details see in [Multi-Parameter Support with NTTs for NTRU...](https://troll.iis.sinica.edu.tw/by-publ/recent/ntt_ntru_ntrup.pdf)).
> The prime $\large q'$ must be $\large q_{i}' = 1536k + 1$
2. We tested and used the **Prime_list** to find three Roots $\large{x = yz;\ (y^3)\ mod\ q' =(z^{512})\ mod\ q'=1}$ over $\large \mathbb{Z}_{2048}$ for NTT. 
> ![image](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/assets/67849251/f6c7c821-eca7-45b3-8d91-358062e15a44)
3.
> ![image](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/assets/67849251/3ad8f269-94e1-41b4-80da-93ebad533da9)
> ![image](https://github.com/Skwgasnaw/PQC_Cortex-M4_NTRU-NTT/assets/67849251/9df7a4e4-8042-496b-98a4-0076c8efabbb)
