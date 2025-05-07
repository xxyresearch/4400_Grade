
char  CA[10];
int   IA[11];
float FA[12];

void test1()
{
    char c;
    CA[3] = c;
    return;
}

void test2(int b)
{
    IA[2] = b;
    return;
}

float test3(int i)
{
    return FA[i] = 2.7;
}

