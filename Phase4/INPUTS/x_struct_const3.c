
struct pair {
    int x, y;
};

void evil()
{
    struct pair {
        const int x, y;
    };

    struct pair P;
    P.x;
    P.y;
}

void evil2()
{
    struct pair P;
    P.x;
    P.y;
}
