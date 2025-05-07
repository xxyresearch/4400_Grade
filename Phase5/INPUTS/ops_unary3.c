
// char to int
//

void test1()
{
    putchar( (int) 'H' );
    return;
}

void test2(char p)
{
    putchar( (int) p );
    return;
}

char LFUNC()
{
    return 'l';
}

void test3()
{
    putchar( (int) LFUNC() );
    return;
}

void test4()
{
    char p;
    p = 'l';
    putchar( (int) p );
    return;
}

void test5(char a)
{
    putchar( (int) (a + ' ') );
    return;
}

int main()
{
    test1();
    test2('e');
    test3();
    test4();
    test5('O');
    putchar(10);
    return 0;
}
