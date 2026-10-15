from functools import partialmethod
import daft

class dag(daft.PGM):
    def __init__(self, *args, **kwargs):
        daft.PGM.__init__(self, *args, **kwargs)

    latNode = partialmethod(daft.PGM.add_node, scale=1.3, aspect=2.4,
                            fontsize=10, plot_params={"facecolor": "aliceblue"})
    detNode = partialmethod(daft.PGM.add_node, aspect=5.4, fontsize=9.25,
                            alternate=True, plot_params={"facecolor": "aliceblue"})

import numpy as np
rng = np.random.default_rng(seed=5)
n = 100_000

theta = rng.uniform(0.05, 0.09, size=n)   # parent first
x = rng.binomial(1, theta)              # child second, one x per theta
print(x.mean())                         # ~0.55, the middle of theta's range
