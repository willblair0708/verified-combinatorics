// A321531: max number of distinct directions among n non-attacking rooks on n x n.
// Direction class = sorted(|dcol|,|drow|)/gcd  (scaling + dihedral-of-square quotient).
// Exhaustive max via DFS (column by column) with incremental class-counting and a
// branch-and-bound upper bound. Vertical-reflection symmetry breaks the first rook.
//
// Build: cc -O3 -o /tmp/a321531 /tmp/a321531.c
// Run:   /tmp/a321531 <n>        (prints a(n) + a witness)
//        /tmp/a321531 calib      (prints a(2..11), must match OEIS)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int N;
static int CLASS_OF[32][32];   // CLASS_OF[dcol][adrow] -> class id (dcol,adrow in 1..N-1)
static int NCLASS;
static int cls_a[1024], cls_b[1024];

static int gcd_i(int a,int b){ while(b){int t=a%b;a=b;b=t;} return a; }

static void build_classes(int n){
    // map each primitive sorted pair to a contiguous id
    static int key2id[32][32];
    for(int i=0;i<32;i++) for(int j=0;j<32;j++) key2id[i][j]=-1;
    NCLASS=0;
    for(int dc=1;dc<n;dc++){
        for(int dr=1;dr<n;dr++){
            int g=gcd_i(dc,dr); int a=dc/g, b=dr/g;
            int lo=a<b?a:b, hi=a<b?b:a;
            if(key2id[lo][hi]==-1){ key2id[lo][hi]=NCLASS; cls_a[NCLASS]=lo; cls_b[NCLASS]=hi; NCLASS++; }
            CLASS_OF[dc][dr]=key2id[lo][hi];
        }
    }
}

static int p[32];          // p[col]=row
static int used_row[32];
static int cnt[1024];      // how many placed pairs currently realize each class
static int distinct;       // number of classes with cnt>0
static int best;
static int best_perm[32];

static inline int Cn2(int k){ return k*(k-1)/2; }

static void dfs(int col){
    if(col==N){
        if(distinct>best){ best=distinct; memcpy(best_perm,p,sizeof(int)*N); }
        return;
    }
    // branch-and-bound: optimistic = distinct + (#pairs not yet formed), capped at NCLASS
    int pairs_remaining = Cn2(N) - Cn2(col);
    int ub = distinct + pairs_remaining;
    if(ub > NCLASS) ub = NCLASS;
    if(ub <= best) return;

    for(int r=0;r<N;r++){
        if(used_row[r]) continue;
        if(col==0 && r > (N-1)-r) continue;  // vertical reflection: first rook in lower half
        // add pairs (i,col) for i<col
        int touched[32]; int nt=0;
        for(int i=0;i<col;i++){
            int dc=col-i;
            int dr=r-p[i]; if(dr<0) dr=-dr;
            int c=CLASS_OF[dc][dr];
            if(cnt[c]++ ==0){ distinct++; }
            touched[nt++]=c;
        }
        p[col]=r; used_row[r]=1;
        dfs(col+1);
        used_row[r]=0;
        // undo
        for(int t=0;t<nt;t++){ int c=touched[t]; if(--cnt[c]==0) distinct--; }
    }
}

static int amax(int n){
    N=n; build_classes(n);
    memset(used_row,0,sizeof(used_row));
    memset(cnt,0,sizeof(cnt));
    distinct=0; best=0;
    dfs(0);
    return best;
}

int main(int argc,char**argv){
    if(argc>=2 && strcmp(argv[1],"calib")==0){
        int known[12]={-1,0,1,2,4,6,8,11,14,18,23,28};
        printf("CALIBRATION A321531 (must match OEIS through a(10), a(11)=28 = our result):\n");
        for(int n=2;n<=11;n++){
            int v=amax(n);
            printf("  a(%2d)=%2d  expected %2d  %s\n", n, v, known[n], v==known[n]?"OK":"MISMATCH");
            fflush(stdout);
        }
        return 0;
    }
    int n = argc>=2 ? atoi(argv[1]) : 12;
    int v = amax(n);
    printf("a(%d) = %d   (NCLASS=%d)\n", n, v, NCLASS);
    printf("witness (1-based rows by column): ");
    for(int c=0;c<n;c++) printf("%d ", best_perm[c]+1);
    printf("\n");
    return 0;
}
