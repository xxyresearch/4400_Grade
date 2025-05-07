
void test1()
{
    putfloat(-(1.25));
    putchar(10);
    return;
}

void test2(float x)
{
    putfloat(-x);
    putchar(10);
    return;
}

void test3()
{
    float y;
    y = -4.00;
    putfloat(-y);
    putchar(10);
    return;
}

float seven()
{
    return 5.25;
}

void test4()
{
    putfloat(-seven());
    putchar(10);
    return;
}

void test5(float z)
{
    putfloat(-(-z));
    putchar(10);
    return;
}

int main()
{
    test1();
    test2(-(2.5));
    test2(3.75);
    test3();
    test4();
    test5(6.5);
    test5(-(7.75));
    test5(- -(8.875));
    return 0;
}
