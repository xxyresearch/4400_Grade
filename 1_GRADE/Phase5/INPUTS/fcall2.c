
void writebits(int d0, int d1, int d2, int d3)
{
    putchar(d3+48);
    putchar(d2+48);
    putchar(d1+48);
    putchar(d0+48);
    return;
}

void write_low4(int hd)
{
    int b3, b2, b1;

    b3 = (hd/8)%2;
    b2 = (hd/4)%2;
    b1 = (hd/2)%2;
    hd = hd % 2;

    writebits(hd, b1, b2, b3);
    return;
}

void writebinary(float x)
{
    int d;
    d = (int) x;
    write_low4(d);
    putchar(46);
    d = (int) (x * 16.0);
    write_low4(d);
    d = (int) (x * 256.0);
    write_low4(d);
    putchar(10);
    return;
}

int main()
{
    float x;
    x = getfloat();
    putfloat(x);
    putchar(10);
    writebinary(x);
    return 7;
}
