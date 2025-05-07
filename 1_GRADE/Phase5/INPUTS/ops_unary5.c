
// int to float
//

void test1()
{
    putfloat( (float) 9 );
    putchar(10);
    return;
}

void test2(int p)
{
    putfloat( (float) p );
    putchar(10);
    return;
}

int seven()
{
    return 7;
}

void test3()
{
    putfloat( (float) seven() );
    putchar(10);
    return;
}

void test4()
{
    int p;
    p = 6;
    putfloat( (float) p );
    putchar(10);
    return;
}

void test5(int a)
{
    putfloat( (float) (55-a) );
    putchar(10);
    return;
}

int main()
{
    test1();
    test2(8);
    test3();
    test4();
    test5(50);
    return 0;
}
