
void print_row(float a, float b)
{
    putfloat(a);
    putchar(32);
    putchar(32);
    putchar(32);
    putchar(32);
    putfloat(b);
    putchar(10);
    return;
}

void print2x2(float a11, float a12, float a21, float a22)
{
    print_row(a11, a12);
    print_row(a21, a22);
    return;
}

void mults(float p11, float p12, float p21, float p22, float q11)
{
    float q12, q21, q22;

    putchar(80);
    putchar(94);
    putchar(49);
    putchar(61);
    putchar(10);

    print2x2(p11, p12, p21, p22);

    /*
     q = p * p, as 2x2 matrices
    */

    q11 = p11*p11 + p12*p21;
    q12 = p11*p12 + p12*p22;
    q21 = p21*p11 + p22*p21;
    q22 = p21*p12 + p22*p22;

    putchar(80);
    putchar(94);
    putchar(50);
    putchar(61);
    putchar(10);

    print2x2(q11, q12, q21, q22);

    /*
     p = q * q, as 2x2 matrices
    */

    p11 = q11*q11 + q12*q21;
    p12 = q11*q12 + q12*q22;
    p21 = q21*q11 + q22*q21;
    p22 = q21*q12 + q22*q22;

    putchar(80);
    putchar(94);
    putchar(52);
    putchar(61);
    putchar(10);

    print2x2(p11, p12, p21, p22);

    /*
     q = p * p, as 2x2 matrices
    */

    q11 = p11*p11 + p12*p21;
    q12 = p11*p12 + p12*p22;
    q21 = p21*p11 + p22*p21;
    q22 = p21*p12 + p22*p22;

    putchar(80);
    putchar(94);
    putchar(56);
    putchar(61);
    putchar(10);

    print2x2(q11, q12, q21, q22);

    /*
     p = q * q, as 2x2 matrices
    */

    p11 = q11*q11 + q12*q21;
    p12 = q11*q12 + q12*q22;
    p21 = q21*q11 + q22*q21;
    p22 = q21*q12 + q22*q22;

    putchar(80);
    putchar(94);
    putchar(49);
    putchar(54);
    putchar(61);
    putchar(10);

    print2x2(p11, p12, p21, p22);

    /*
     q = p * p, as 2x2 matrices
    */

    q11 = p11*p11 + p12*p21;
    q12 = p11*p12 + p12*p22;
    q21 = p21*p11 + p22*p21;
    q22 = p21*p12 + p22*p22;

    putchar(80);
    putchar(94);
    putchar(51);
    putchar(50);
    putchar(61);
    putchar(10);

    print2x2(q11, q12, q21, q22);

    return;
}


int main()
{
    mults(0.8, 0.2, 0.3, 0.7, 0.0);
    return 0;
}
