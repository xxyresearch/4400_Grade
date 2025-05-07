
void test1()
{
    putint(-(2));
    putchar(10);
    return;
}

void test2(int x)
{
    putint(-x);
    putchar(10);
    return;
}

void test3()
{
    int y;
    y = 4;
    putint(-y);
    putchar(10);
    return;
}

int seven()
{
    return -7;
}

void test4()
{
    putint(-seven());
    putchar(10);
    return;
}

void test5(int z)
{
    putint(-(-z));
    putchar(10);
    return;
}

int main()
{
    test1();
    test2(15);
    test2(-(16));
    test3();
    test4();
    test5(45);
    test5(-(46));
    test5(- -(47));
    return 0;
}
