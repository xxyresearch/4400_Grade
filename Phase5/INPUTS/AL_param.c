
void test1C(char A[])
{
    char c;
    c = A[0];
    return;
}

void test2C(int n, char B[])
{
    test1C(B);
    return;
}

void test3C()
{
    char C[4];
    test2C(4, C);
    return;
}

int test1I(int A[])
{
  return A[0];
}

void test2I(int n, int B[])
{
    test1I(B);
    return;
}

void test3I()
{
    int C[4];
    test2I(4, C);
    return;
}

void test1F(float A[])
{
    putfloat(A[0]);
    return;
}

void test2F(int n, float B[])
{
    test1F(B);
    return;
}

void test3F()
{
    float X[10];
    test2F(4, X);
    return;
}
