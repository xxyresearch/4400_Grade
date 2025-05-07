
char a, b, c;

void print4(int d)
{
    putchar((int) a);
    putchar((int) b);
    putchar((int) c);
    putchar(d);
}

int main()
{
    a = 'H';
    b = 'e';
    c = 'l';
    print4((int) c);
    c = 'W';
    b = ' ';
    a = 'o';
    print4((int) a);
    b = 'l';
    a = 'r';
    c = 'd';
    print4(10);
    return 0;
}

