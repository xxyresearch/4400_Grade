
char c;

void test1(int i)
{
    char A[10];

    c = A[i-3];
    return;
}

void test2(float x, int b, int j)
{
    int A[11];

    b = A[A[j]];
    return;
}

int the_index()
{
    return 7;
}

float test3()
{
    float F[12];
    return F[the_index()];
}

