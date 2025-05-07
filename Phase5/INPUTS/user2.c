// YESDOT

char func1(int a)
{
    return (char) (a+48);
}

float func2(int s, char a[])
{
    float x;
    x = (float) a[0];
    x = x * 10.0;
    x = x + (float) a[1];
    x = x * 10.0;
    x = x + (float) a[2];
    x = x / 10.0;
    return x * (float) s;
}

int func3(int a[], int b)
{
    int c, d, e, f, g, h, i, j, k;
    c = a[b];
    d = a[c];
    e = a[d];
    f = a[e];
    g = a[f];
    h = a[g];
    i = a[h];
    j = a[i];
    k = a[j];
    return a[k];
}

float sqr(float x)
{
    return x*x;
}

float dist4(float w1, float x1, float y1, float z1,
            float w2, float x2, float y2, float z2)
{
    return sqr(w1-w2) + sqr(x1-x2) + sqr(y1-y2) + sqr(z1-z2);
}

void bigstack(float x, float y)
{
    putfloat(dist4(x, 1.0, 2.0, 3.0, 4.0, y, 5.0, dist4(0.6, 0.7, 0.8, 0.9, 1.10, 1.11, 1.12, 1.13+1.14)));
}
