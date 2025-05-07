
/* Nested structs */

struct pair {
  int x, y;
};

struct window {
  struct pair upper_left;
  struct pair size;
  char title[256];
};

struct screen {
  struct window W[1000];  /* Ugly but we don't get pointers */
  int num_windows;
};

void test()
{
  struct pair P;
  struct window W;
  struct screen S;

  struct local {
      int a;
      struct pair W;
      struct window S;
  };

  struct local L;

  L;
  P;
  W;
  S;
}
