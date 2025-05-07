
char  CA[10];
int   IA[11];
float FA[12];

void test1(int i)
{
    char c;
    c = CA[i-3];
    return;
}

void test2(float x, int b, int j)
{
    b = IA[IA[j]];
    return;
}

int the_index()
{
    return 7;
}

float test3()
{
    return FA[the_index()];
}

