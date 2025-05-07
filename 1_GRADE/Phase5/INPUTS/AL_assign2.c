
char c;

void test1(int i)
{
    char A[10];

    A[i-3] = c;
    return;
}

void test2(float x, int b, int j)
{
    int A[11];

    A[A[j]] = b;
    return;
}

int the_index()
{
    return 7;
}

float test3()
{
    float F[12];
    return F[the_index()] = 3.14;
}

