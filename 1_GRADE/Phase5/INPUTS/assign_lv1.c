
int thing1()
{
    int a;
    a = 1;
    return a;
}

float thing2()
{
    float b;
    b = 2.0;
    return b;
}

char thing3()
{
    char c;
    c = 'C';
    return c;
}

int main()
{
    putint(thing1());
    putchar(10);
    putfloat(thing2());
    putchar(10);
    putchar((int) thing3());
    putchar(10);
    return 0;
}
