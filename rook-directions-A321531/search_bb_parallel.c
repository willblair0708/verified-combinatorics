// A321531 (directions) exact solver, parallel. Same complete B&B as search_bb.c,
// but work is split over (p[0],p[1]) prefixes across threads, with a SHARED global
// best so every thread prunes against the best found anywhere (faster + lighter).
//
// Build: cc -O3 -pthread -o /tmp/a321531_par /tmp/a321531_par.c
// Run:   /tmp/a321531_par <n> [num_threads]   (default threads = cores-2)
//        /tmp/a321531_par calib [num_threads]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

static int N, NCLASS;
static int CLASS_OF[40][40];

static int gcd_i(int a,int b){ while(b){int t=a%b;a=b;b=t;} return a; }
static void build_classes(int n){
    static int key2id[40][40];
    for(int i=0;i<40;i++) for(int j=0;j<40;j++) key2id[i][j]=-1;
    NCLASS=0;
    for(int dc=1;dc<n;dc++) for(int dr=1;dr<n;dr++){
        int g=gcd_i(dc,dr); int a=dc/g,b=dr/g; int lo=a<b?a:b, hi=a<b?b:a;
        if(key2id[lo][hi]==-1) key2id[lo][hi]=NCLASS++;
        CLASS_OF[dc][dr]=key2id[lo][hi];
    }
}
static inline int Cn2(int k){ return k*(k-1)/2; }

static volatile int g_best;          // shared best (monotone increasing)
static int g_best_perm[40];
static pthread_mutex_t best_mu = PTHREAD_MUTEX_INITIALIZER;

// work queue of (r0,r1) prefixes
static int (*WORK)[2]; static int WORK_N; static int work_idx;
static pthread_mutex_t work_mu = PTHREAD_MUTEX_INITIALIZER;

typedef struct { int p[40], used[40], cnt[1024], distinct; } St;

static void dfs(St*s, int col){
    if(col==N){
        if(s->distinct>g_best){
            pthread_mutex_lock(&best_mu);
            if(s->distinct>g_best){ g_best=s->distinct; memcpy(g_best_perm,s->p,sizeof(int)*N); }
            pthread_mutex_unlock(&best_mu);
        }
        return;
    }
    int rem=Cn2(N)-Cn2(col); int ub=s->distinct+rem; if(ub>NCLASS) ub=NCLASS;
    if(ub<=g_best) return;                       // prune against GLOBAL best
    for(int r=0;r<N;r++){
        if(s->used[r]) continue;
        int touched[40], nt=0;
        for(int i=0;i<col;i++){
            int dc=col-i, dr=r-s->p[i]; if(dr<0)dr=-dr;
            int c=CLASS_OF[dc][dr];
            if(s->cnt[c]++==0) s->distinct++;
            touched[nt++]=c;
        }
        s->p[col]=r; s->used[r]=1;
        dfs(s,col+1);
        s->used[r]=0;
        for(int t=0;t<nt;t++){ int c=touched[t]; if(--s->cnt[c]==0) s->distinct--; }
    }
}

static void* worker(void*arg){
    (void)arg;
    for(;;){
        int idx;
        pthread_mutex_lock(&work_mu); idx=work_idx++; pthread_mutex_unlock(&work_mu);
        if(idx>=WORK_N) break;
        int r0=WORK[idx][0], r1=WORK[idx][1];
        St s; memset(&s,0,sizeof s);
        s.p[0]=r0; s.used[r0]=1;
        s.p[1]=r1; s.used[r1]=1;
        // pair (col0,col1): dc=1
        int dr=r1-r0; if(dr<0)dr=-dr; int c=CLASS_OF[1][dr];
        s.cnt[c]++; s.distinct=1;
        dfs(&s,2);
    }
    return NULL;
}

static int amax(int n, int nthreads){
    N=n; build_classes(n);
    g_best=0; work_idx=0;
    // build work items: r0 in lower half (vertical-reflection symmetry), r1 != r0
    static int buf[40*40][2];
    WORK=buf; WORK_N=0;
    for(int r0=0;r0<=(n-1)-r0;r0++)
        for(int r1=0;r1<n;r1++) if(r1!=r0){ WORK[WORK_N][0]=r0; WORK[WORK_N][1]=r1; WORK_N++; }
    if(n<3){ // tiny
        // handle directly
        int best=0; // brute for n<=2
        if(n==2) best=1;
        return best;
    }
    pthread_t th[256]; if(nthreads>256) nthreads=256;
    for(int i=0;i<nthreads;i++) pthread_create(&th[i],NULL,worker,NULL);
    for(int i=0;i<nthreads;i++) pthread_join(th[i],NULL);
    return g_best;
}

int main(int argc,char**argv){
    int ncpu=sysconf(_SC_NPROCESSORS_ONLN); int defth=ncpu>2?ncpu-2:1;
    if(argc>=2 && strcmp(argv[1],"calib")==0){
        int nt=argc>=3?atoi(argv[2]):defth;
        int known[14]={-1,0,1,2,4,6,8,11,14,18,23,28,33,38};
        printf("CALIBRATION A321531 parallel (%d threads):\n",nt);
        for(int n=2;n<=13;n++){ int v=amax(n,nt); printf("  a(%2d)=%2d expected %2d %s\n",n,v,known[n],v==known[n]?"OK":"MISMATCH"); fflush(stdout);}
        return 0;
    }
    int n=argc>=2?atoi(argv[1]):14;
    int nt=argc>=3?atoi(argv[2]):defth;
    int v=amax(n,nt);
    printf("a(%d) = %d   (NCLASS=%d, threads=%d)\nwitness(1-based): ",n,v,NCLASS,nt);
    for(int c=0;c<n;c++) printf("%d ",g_best_perm[c]+1); printf("\n");
    return 0;
}
