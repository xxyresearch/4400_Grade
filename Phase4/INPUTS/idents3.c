
void myfunc(int a, float b, char c)
{
    a;
    b;
    c;
}

char a;  /* OK */

int foo(int b)    /* Also OK */
{
    int c;

    a;
    b;
    c;
}
