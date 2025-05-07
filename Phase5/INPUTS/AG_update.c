
char    arrayC[12];
int     arrayI[12];
float   arrayF[12];

void test1()
{
  arrayC[0]  += '0';
  return;
}

void test2(int i)
{
  arrayI[i]  *= 49;
  return;
}

void test3(int i)
{
  arrayF[i-1] /= 3.0;
  return;
}

void test4(int i)
{
  arrayC[++i] -= '3';
  return;
}

float test5(int i)
{
  return arrayF[3] += 7.7;
}

int test6(int i)
{
  return arrayI[i++] -= 11;
}
