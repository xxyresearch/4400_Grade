
struct bizarre {
    int a;
    int b;
    const int c;
};

void foo()
{
    struct bizarre B;
    B;
    B.a;
    B.b;
    B.c;

    const struct bizarre C;
    C;
    C.a;
    C.b;
    C.c;

    struct bizarre D[10];
    D;
    D[0];
    D[0].a;
    D[0].b;
    D[0].c;

    const struct bizarre E[10];
    E;
    E[1];
    E[1].a;
    E[1].b;
    E[1].c;
}
