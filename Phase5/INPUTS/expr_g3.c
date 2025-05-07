
float x, y, z;

int square(float x)
{
    return (int) (x*x);
}

void print4(int d)
{
    putchar(square(x));
    putchar(square(y));
    putchar(square(z));
    putchar(d);
}

int main()
{
    x = 8.486;
    y = 10.05;
    z = 10.4;
    print4(108);
    z = 9.33;
    y = 5.66;
    x = 10.54;
    print4(111);
    y = 10.4;
    x = 10.678;
    z = 10.0;
    print4(10);
    return 0;
}

