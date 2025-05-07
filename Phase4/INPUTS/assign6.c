
void tests(int a)
{
    a = 3;
    a += 4;
    a -= tests(3);      // type error
}
