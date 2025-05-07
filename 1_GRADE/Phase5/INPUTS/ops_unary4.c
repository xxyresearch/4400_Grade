
// float to int
//

void test1()
{
    putint( (int) 1.23 );
    putchar(10);
    return;
}

void test2(float p)
{
    putint( (int) p );
    putchar(10);
    return;
}

float pi()
{
    return 3.14159;
}

void test3()
{
    putint( (int) pi() );
    putchar(10);
    return;
}

void test4()
{
    float p;
    p = 4.44;
    putint( (int) p );
    putchar(10);
    return;
}

void test5(float a)
{
    putint( (int) (a - 0.6) );
    putchar(10);
    return;
}

int main()
{
    test1();
    test2(2.1);
    test3();
    test4();
    test5(5.678);
    return 0;
}
