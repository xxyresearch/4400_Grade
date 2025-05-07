
struct bizarre {
    int a;
    int b;
    const int c;
};

void foo()
{
    const struct bizarre B;
    B;
    B.a++;
    B.b++;
    B.c++;
}
