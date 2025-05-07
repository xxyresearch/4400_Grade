
int test1()
{
    return 3 + 4;
}


int test2(int x)
{
    return 15 + x;
}


int test3(int x, int y)
{
    return x + y;
}


int test4()
{
    return 33 - 44;
}


int test5(int x)
{
    return 15 - x;
}


int test6(int x, int y)
{
    return x - y;
}


int test7()
{
    return 33 * 44;
}


int test8(int x)
{
    return x * 15;
}


int test9(int x, int y)
{
    return y * x;
}


int testA(int x)
{
    return x % 2;
}


int testB(int x, int y, int z)
{
    return x / z;
}

void show(int x)
{
    putint(x);
    putchar(10);
    return;
}

int main()
{
    show(test1());

    show(test2(37));
    show(test2(99));

    show(test3(3, 1));
    show(test3(-6, 7));
    show(test3(655, 45));

    show(test4());

    show(test5(3));
    show(test5(-4));

    show(test6(88, 77));
    show(test6(144, 102));

    show(test7());

    show(test8(0));
    show(test8(1));
    show(test8(2));

    show(test9(5, 6));
    show(test9(7, 8));

    show(testA(15));
    show(testA(14));

    show(testB(3, 2, 1));
    show(testB(9, 1, 4));
    show(testB(8, 2, 6));

    return 0;
}
