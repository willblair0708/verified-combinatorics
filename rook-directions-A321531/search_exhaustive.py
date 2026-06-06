# A321531: max distinct directions among n non-attacking rooks. Direction = sorted(|di|,|dj|)/gcd
# (up to scaling + dihedral action of the square). Exhaustive max over all permutations.
import sys, itertools
from math import gcd
from multiprocessing import Pool

def build(n):
    # class index for each primitive sorted pair (a,b), a<=b, from da,db in 1..n-1
    idx={}; 
    for da in range(1,n):
        for db in range(1,n):
            g=gcd(da,db); a,b=da//g,db//g; key=(min(a,b),max(a,b))
            if key not in idx: idx[key]=len(idx)
    pm=[[0]*(n) for _ in range(n)]   # pm[da][db] bitmask  (da,db in 1..n-1)
    for da in range(1,n):
        for db in range(1,n):
            g=gcd(da,db); a,b=da//g,db//g
            pm[da][db]=1<<idx[(min(a,b),max(a,b))]
    return pm

def count_perm(p, pm):
    n=len(p); m=0
    for i in range(n):
        pi=p[i]
        for j in range(i+1,n):
            db=p[j]-pi; db=db if db>=0 else -db
            m|=pm[j-i][db]
    return bin(m).count("1")

def amax_small(n):
    pm=build(n); best=0
    for p in itertools.permutations(range(n)):
        c=count_perm(p,pm); 
        if c>best: best=c
    return best

# multiprocessing for n=11: partition by first two elements
PM=None; N=None
def _init(n): 
    global PM,N; N=n; PM=build(n)
def _work(prefix):
    rest=[x for x in range(N) if x not in prefix]
    best=0; bp=None
    for tail in itertools.permutations(rest):
        p=prefix+tail; c=count_perm(p,PM)
        if c>best: best=c; bp=p
    return best,bp
def amax_par(n, workers=12):
    prefixes=[(a,b) for a in range(n) for b in range(n) if b!=a]
    with Pool(workers, initializer=_init, initargs=(n,)) as pool:
        res=pool.map(_work, prefixes)
    return max(res, key=lambda r:r[0])

if __name__=="__main__":
    known={1:0,2:1,3:2,4:4,5:6,6:8,7:11,8:14,9:18,10:23}
    print("CALIBRATION (must match OEIS A321531):")
    ok=True
    for n in range(2,10):
        v=amax_small(n); m=(v==known[n]); ok&=m
        print(f"  a({n})={v}  expected {known[n]}  {'OK' if m else 'MISMATCH'}")
    if not ok:
        print("CALIBRATION FAILED -- aborting"); sys.exit(1)
    print("calibration PASS. Computing a(11) exhaustively (40M perms, parallel)...")
    best,bp=amax_par(11, 12)
    # independent re-verify the witness
    chk=count_perm(bp, build(11))
    print(f"a(11) = {best}  (witness re-verify={chk})  permutation(1-based)={[v+1 for v in bp]}")
    print(f"  prior on OEIS: a(10)=23 ; SA lower bound found earlier: 28")
