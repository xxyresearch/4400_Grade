
define _val3 {
  iconst_3 OR [bs]ipush 3 OR ldc 3
}

define _val4 {
  iconst_4 OR [bs]ipush 4 OR ldc 4
}

define _add1_1 {
  _val3
  _val4
}
define _add1_2 {
  _val4
  _val3
}

define _add1 {
  _add1_1 OR _add1_2
  swap OR SKIP
  iadd
}

within test1
    NAME integer +
    MATCH _add1
done

# ============================================

define _val15 {
  [bs]ipush 15 OR ldc 15
}

define _add2_1 {
  _val15
  iload[ _]0
}
define _add2_2 {
  iload[ _]0
  _val15
}

define _add2 {
  _add2_1 OR _add2_2
  swap OR SKIP
  iadd
}

within test2
    NAME integer +
    MATCH _add2
done

# ============================================

define _add3_1 {
  iload[ _]0
  iload[ _]1
}
define _add3_2 {
  iload[ _]1
  iload[ _]0
}

define _add3 {
  _add3_1 OR _add3_2
  swap OR SKIP
  iadd
}

within test3
    NAME integer +
    MATCH _add3
done

# ============================================

define _val33 {
  [bs]ipush 33 OR ldc 33
}

define _val44 {
  [bs]ipush 44 OR ldc 44
}

define _sub1_1 {
  _val33
  _val44
  isub
}
define _sub1_2 {
  _val44
  _val33
  swap
  isub
}

within test4
    NAME integer -
    MATCH _sub1_1 OR _sub1_2
done

# ============================================

define _sub2_1 {
  _val15
  iload[ _]0
  isub
}
define _sub2_2 {
  iload[ _]0
  _val15
  swap
  isub
}

within test5
    NAME integer -
    MATCH _sub2_1 OR _sub2_2
done

# ============================================

define _sub3_1 {
  iload[ _]0
  iload[ _]1
  isub
}
define _sub3_2 {
  iload[ _]1
  iload[ _]0
  swap
  isub
}

within test6
    NAME integer -
    MATCH _sub3_1 OR _sub3_2
done

# ============================================

define _mul1_1 {
  _val33
  _val44
}
define _mul1_2 {
  _val44
  _val33
}

define _mul1 {
  _mul1_1 OR _mul1_2
  swap OR SKIP
  imul
}

within test7
    NAME integer *
    MATCH _mul1
done

# ============================================

define _mul2_1 {
  _val15
  iload[ _]0
}
define _mul2_2 {
  iload[ _]0
  _val15
}

define _mul2 {
  _mul2_1 OR _mul2_2
  swap OR SKIP
  imul
}

within test8
    NAME integer *
    MATCH _mul2
done

# ============================================

define _mul3_1 {
  iload[ _]0
  iload[ _]1
}
define _mul3_2 {
  iload[ _]1
  iload[ _]0
}

define _mul3 {
  _mul3_1 OR _mul3_2
  swap OR SKIP
  imul
}

within test9
    NAME integer *
    MATCH _mul3
done

# ============================================

define _val2 {
  iconst_2 OR [bs]ipush 2 OR ldc 2
}

define _mod1_1 {
  iload[ _]0
  _val2
  irem
}
define _mod1_2 {
  _val2
  iload[ _]0
  swap
  irem
}

within testA
    NAME integer %
    MATCH _mod1_1 OR _mod1_2
done

# ============================================

define _div1_1 {
  iload[ _]0
  iload[ _]2
  idiv
}
define _div1_2 {
  iload[ _]2
  iload[ _]0
  swap
  idiv
}

within testB
    NAME integer /
    MATCH _div1_1 OR _div1_2
done

