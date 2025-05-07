
void show(int x)
{
    putint(x);
    putchar(10);
    return;
}

void func1(int a, int b)
{
    show(a+b*2);
    return;
}

void func2(int a, int b)
{
    show(a+b/2);
    return;
}

void func3(int a, int b)
{
    show(2*a+b);
    return;
}

int rand(int x)
{
    return 888*x % 32749;
}

int main()
{
    func1(10, 11);
    func1(32, 5);

    func2(26, 18);
    func2(55, 40);

    func3(10, 11);
    func3(32, 5);

    show(rand(100));
    show(rand(rand(100)));
    show(rand(rand(rand(100))));
    show(rand(rand(rand(rand(100)))));

    show(rand(3061));
    return 0;
}

