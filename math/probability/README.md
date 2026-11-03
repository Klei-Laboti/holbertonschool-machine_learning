# Probability

Classes representing common probability distributions, built without
importing any module. Irrational constants are approximated by hand
(pi = 3.1415926536, e = 2.7182818285).

## Requirements
- Ubuntu 20.04 LTS, Python 3.9
- pycodestyle 2.11.1
- No imports allowed
- All files start with `#!/usr/bin/env python3` and are executable

## Files
| File | Class | Methods |
|------|-------|---------|
| `poisson.py` | `Poisson` | `__init__`, `pmf`, `cdf` |
| `exponential.py` | `Exponential` | `__init__`, `pdf`, `cdf` |
| `normal.py` | `Normal` | `__init__`, `z_score`, `x_value`, `pdf`, `cdf` |
| `binomial.py` | `Binomial` | `__init__`, `pmf`, `cdf` |

## Author
Kleant Laboti
