
void test1(int a)
{
    putchar(a=5);
    a=6;
    return;
}

void test2(int a, int b)
{
    a = ( b += 15 );

    b += 17;
    return;
}

void test3(int a)
{
    int b;
    b = a = 11;

    a = 22;
    return;
}

void need4(int a, int b)
{
    b = a + 9;
}

void omit4(int a)
{
    a + 9;
}
