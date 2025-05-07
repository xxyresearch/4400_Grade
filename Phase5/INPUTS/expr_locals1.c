
void dummy(char a)
{
    putchar((int)a);
    putchar(1+(int)a);
    putchar(10);
    return;
}

void func1(char a, char b, char c)
{
    char d, e;
    d=c;
    e='o';
    dummy(a);
    dummy(b);
    dummy(c);
    dummy(d);
    dummy(e);
    return;
}

void func2(char b, char c, char d, char e)
{
    char a;
    a='d';
    dummy(e);
    dummy(d);
    dummy(c);
    dummy(b);
    dummy(a);
    return;
}

int main()
{
    func1('h', 'e', 'l');
    putchar(10);
    func2('l', 'r', 'o', 'w');
    return 0;
}

