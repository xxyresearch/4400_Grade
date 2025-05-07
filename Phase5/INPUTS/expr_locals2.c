
void dummy(int a)
{
    putchar(a);
    putchar(1+a);
    putchar(10);
    return;
}

void func1(int a, int b)
{
    dummy(b);
    dummy(a);
    return;
}

void func2(int c)
{
    dummy(c);
    dummy(c);
    return;
}

void func3(int a, int c)
{
    int b;
    b = 44;
    dummy(c);
    dummy(b);
    dummy(a);
    return;
}

void func4(int b, int d, int l, int o, int w)
{
    int r;
    r = o+3;
    dummy(w);
    dummy(o);
    dummy(r);
    dummy(l);
    dummy(d);
    dummy(b);
    return;
}

int main()
{
    func1(101, 72);
    func2(108);
    func3(32, 111);
    func4(33, 100, 108, 111, 119);
    return 0;
}

