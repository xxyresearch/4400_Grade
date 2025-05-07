
define _add1_1 {
  ldc [+]?3[.]
  ldc [+]?4[.]1
}
define _add1_2 {
  ldc [+]?4[.]1
  ldc [+]?3[.]
}

define _add1 {
  _add1_1 OR _add1_2
  swap OR SKIP
  fadd
}

within test1
    NAME float +
    MATCH _add1
done

# ============================================

define _add2_1 {
  ldc [+]?1[.]5
  fload[ _]0
}
define _add2_2 {
  fload[ _]0
  ldc [+]?1[.]5
}

define _add2 {
  _add2_1 OR _add2_2
  swap OR SKIP
  fadd
}

within test2
    NAME float +
    MATCH _add2
done

# ============================================

define _add3_1 {
  fload[ _]0
  fload[ _]1
}
define _add3_2 {
  fload[ _]1
  fload[ _]0
}

define _add3 {
  _add3_1 OR _add3_2
  swap OR SKIP
  fadd
}

within test3
    NAME float +
    MATCH _add3
done

# ============================================

define _sub1_1 {
  ldc [+]?3[.]3
  ldc [+]?1[.] OR fconst_1
  fsub
}
define _sub1_2 {
  ldc [+]?1[.] OR fconst_1
  ldc [+]?3[.]3
  swap
  fsub
}

within test4
    NAME float -
    MATCH _sub1_1 OR _sub1_2
done

# ============================================

define _sub2_1 {
  ldc [+]?1[.]5
  fload[ _]0
  fsub
}
define _sub2_2 {
  fload[ _]0
  ldc [+]?1[.]5
  swap
  fsub
}

within test5
    NAME float -
    MATCH _sub2_1 OR _sub2_2
done

# ============================================

define _sub3_1 {
  fload[ _]0
  fload[ _]1
  fsub
}
define _sub3_2 {
  fload[ _]1
  fload[ _]0
  swap
  fsub
}

within test6
    NAME float -
    MATCH _sub3_1 OR _sub3_2
done

# ============================================

define _mul1_1 {
  ldc [+]?0[.]33
  ldc [+]?4[.]4
}
define _mul1_2 {
  ldc [+]?4[.]4
  ldc [+]?0[.]33
}

define _mul1 {
  _mul1_1 OR _mul1_2
  swap OR SKIP
  fmul
}

within test7
    NAME float *
    MATCH _mul1
done

# ============================================

define _mul2_1 {
  fconst_2
  fload[ _]0
}
define _mul2_2 {
  fload[ _]0
  fconst_2
}

define _mul2 {
  _mul2_1 OR _mul2_2
  swap OR SKIP
  fmul
}

within test8
    NAME float *
    MATCH _mul2
done

# ============================================

define _mul3_1 {
  fload[ _]0
  fload[ _]1
}
define _mul3_2 {
  fload[ _]1
  fload[ _]0
}

define _mul3 {
  _mul3_1 OR _mul3_2
  swap OR SKIP
  fmul
}

within test9
    NAME float *
    MATCH _mul3
done

# ============================================

define _div1_1 {
  fload[ _]0
  fload[ _]2
  fdiv
}
define _div1_2 {
  fload[ _]2
  fload[ _]0
  swap
  fdiv
}

within testB
    NAME float /
    MATCH _div1_1 OR _div1_2
done

