# MILA Research Compute — pilot evidence

**Date:** 2026-11-26. **Status:** prototype 0.1.0-candidate, local launcher 0.1.1. No remote integration or unattended operation claimed.

Workloads of the local prototype include SAT, Möbius/Mertens, modular powers, modular polynomials, dense matrices and finite numerical eta sums. The latter are not certified zeta evaluations.

Owner-supplied terminal reports show 27/27 engine CPU tests passing on Linux and a successful two-GPU 120-second run after correcting the launcher admission transition. CuPy 14.2.0, NumPy 2.4.6, Python 3.14.10, CUDA runtime 12.9, two NVIDIA P106-090 cards (CC 6.1). No driver change was required. Reported wall time 120.420469725 seconds; final ok=true, no telemetry error in the received tail.

| Metric | GPU 0 | GPU 1 |
|---|---:|---:|
| Mean sampled utilization | 98.605% | 98.134% |
| Peak sampled utilization | 99% | 99% |
| Peak temperature | 58 C | 62 C |
| Peak total GPU memory used | 146 MiB | 145 MiB |
| Utilization samples | 119 | 119 |

This is owner-supplied evidence, not an independent live attestation. The beginning of the long run's result was absent, so the complete work count is unknown; no throughput estimate is claimed. The benchmark repeats a finite search and is not a proof of P vs NP. Thermal shutdown under load was not demonstrated merely by temperatures staying below the limit.

The first admission failure between consecutive benchmarks occurred because a GPU was still reported busy; the corrected launcher waited for three qualifying idle samples. This negative result is retained. The public standard-library verifier can reproduce the small SAT truth table without GPU hardware.

GPU testing requires compatible CuPy/CUDA and nvidia-smi. Check idle GPUs, thermal limits, memory budgets and other workloads before any explicit run. Do not run stress tests unattended. Telemetry monitoring is not a hard hardware watchdog. Aggregate agreement is not full pointwise certification.

References: [CuPy installation](https://docs.cupy.dev/en/stable/install.html), [NVIDIA CUDA documentation](https://docs.nvidia.com/cuda/).
