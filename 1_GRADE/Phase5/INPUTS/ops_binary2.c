
float test1()
{
    return 3.0 + 4.1;
}


float test2(float x)
{
    return 1.5 + x;
}


float test3(float x, float y)
{
    return x + y;
}


float test4()
{
    return 3.3 - 1.0;
}


float test5(float x)
{
    return 1.5 - x;
}


float test6(float x, float y)
{
    return x - y;
}


float test7()
{
    return 0.33 * 4.4;
}


float test8(float x)
{
    return x * 2.0;
}


float test9(float x, float y)
{
    return y * x;
}


float testB(float x, float y, float z)
{
    return x / z;
}

void show(float x)
{
    putfloat(x);
    putchar(10);
    return;
}

int main()
{
    show(test1());

    show(test2(4.2));
    show(test2(2.4));

    show(test3(3.0, 1.0));
    show(test3(-6.5, 2.4));
    show(test3(12.3, -4.5));

    show(test4());

    show(test5(3.9));
    show(test5(-4.1));

    show(test6(88.0, 79.0));
    show(test6(144.0, 138.5));

    show(test7());

    show(test8(0.0));
    show(test8(1.6));
    show(test8(2.7));

    show(test9(1.4, 1.4));
    show(test9(7.25, 0.8));

    show(testB(3.3, 2.4, 1.5));
    show(testB(9.6, 1.7, 4.8));
    show(testB(8.9, 2.0, 6.1));

    return 0;
}
