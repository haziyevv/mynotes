import math
import numpy as np
import pdb

def calc_p(ta, tb, hc):
    tc = 10 - hc
    pa = math.pow(ta, hc) * math.pow((1-ta), tc)
    pb = math.pow(tb, hc) * math.pow((1-tb), tc)
    psa = pa/(pa+pb)
    psb = pb/(pa+pb)
    return psa, psb


def maximization(results):
    heads = sum([x[0] for x in results])
    tails = sum([x[1] for x in results])

    e_after = heads / (heads + tails)
    return e_after


experiments = [5,9,8,4,7]
#coins = np.array([0.2, 0.1])
ea, eb = 0.2, 0.1
iterations = 100


def expectations(experiments):
    coina_res, coinb_res = [], []
    for exp in experiments:
        psa, psb = calc_p(ea, eb, exp)
        coina_res.append((exp*psa, (10-exp)*psa))
        coinb_res.append((exp*psb, (10-exp)*psb))
    return coina_res, coinb_res

for i in range(iterations):
    pdb.set_trace()
    expa, expb = expectations(experiments)
    ea, eb = maximization(expa), maximization(expb)
    print(i, ea, eb)
