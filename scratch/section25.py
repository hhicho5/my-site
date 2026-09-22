import numpy as np

rng = np.random.default_rng(seed=1)
sunny = rng.binomial(1, 0.35, size=100_000)
hit = rng.binomial(1, np.where(sunny == 1, 0.75, 0.28))
print(round(sunny[hit == 1].mean(), 5))