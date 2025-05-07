
struct evil {
    int a, b, c;
};

void foo(struct evil e)
{
    struct local {
        int d;
        int e;
    };
    struct local l;

    l;
    e;
}

void bar()
{
    struct local {
        int a;
        float b;
    };

    struct local l;
    struct evil x;

    l;
    x;

    foo(x);
}

void barf()
{
    struct evil {
        int bwahahaha;
    };

    struct evil E;
    E;

    foo(E);
}
