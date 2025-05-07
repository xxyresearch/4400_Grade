
int i_tiny()
{
    return 2;
}

int i_byte()
{
    return 55;
}

int i_short()
{
    return 32105;
}

int i_int()
{
    return 87654321;
}

void println(int x)
{
    putint(x);
    putchar(10);
    return;
}

int main()
{
    int a, b, c, d, e;

    a=1;
    b=54;
    c=32104;
    d=87654320;

    println(0);
    println(a);
    println(i_tiny());

    println(53);
    println(b);
    println(i_byte());

    println(32103);
    println(c);
    println(i_short());

    println(87654319);
    println(d);
    println(i_int());

    return 0;
}
