#import numpy as np
#rng = np.random.default_rng(seed=42)
#n = 100_000

#rate = rng.uniform(20, 60, size=n)    # parent first: patients per week
#time = rng.gamma(400, 1/rate)         # child second, one time per simulated rate

#print(time[:10])   # e.g. [ 8.3  10.9  8.3 ] , three simulated futures
import numpy as np
rng = np.random.default_rng(seed=0)
store_a = rng.normal(252, 25, size=100_000)
store_b = rng.normal(177, 29, size=100_000)
total = store_a + store_b
print(np.quantile(total, 0.95))
