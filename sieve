var L;
var R;
var M;
var arr[100];
var i;
var sq;
var t;
var counts;
var res[100];
var ptr1;
var sv;
var size;

def sqrt(x) {
	R = x + 1;

    while (L != R - 1)
    {
        M = (L + R) / 2;

		if (M * M <= x) 
			L = M;
		else 
			R = M;
	}

    return L;
}

def sieve(n) {
    arr[0] = 1;
    arr[1] = 1;
    i = 2;
    sq = sqrt(n);
    while (i <= sq) {
        if (arr[i] == 0) {
            t = i*i;
            while (t <= n) {
                arr[t] = 1;
                t = t+i;
            }
        }
    }
    counts = 0;
    i = 0;
    while (i <= n) {
        if (!arr[i]) {
           counts = counts+1; 
        }
        i = i+1;
    }
    res[0] = counts;
    ptr1 = 1;
    i = 0;
    while (i <= n) {
        if (!arr[i]) {
            res[ptr1] = i;
            ptr1 = ptr1+1;
        }
        i = i+1;
    }
    return res;
}

sv = sieve(atoi(input()));
size = sv[0];
i = 1;
while (i <= size) {
    printi(sv[i]);
    println();
    i = i+1;
}





