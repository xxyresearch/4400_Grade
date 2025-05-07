
define _add1_1 {
  bipush 33
  bipush 40
}
define _add1_2 {
  bipush 40
  bipush 33
}

define _add1 {
  _add1_1 OR _add1_2
  swap OR SKIP
  iadd
  i2c
}

within test1
    NAME char +
    MATCH _add1
done

# ============================================

define _add2_1 {
  bipush 48
  iload[ _]0
}
define _add2_2 {
  iload[ _]0
  bipush 48
}

define _add2 {
  _add2_1 OR _add2_2
  swap OR SKIP
  iadd
  i2c
}

within test2
    NAME char +
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
  i2c
}

within test3
    NAME char +
    MATCH _add3
done

# ============================================

define _sub1_1 {
  bipush 84
  bipush 35
  isub
  i2c
}
define _sub1_2 {
  bipush 35
  bipush 84
  swap
  isub
  i2c
}

within test4
    NAME char -
    MATCH _sub1_1 OR _sub1_2
done

# ============================================

define _sub2_1 {
  iload[ _]0
  bipush 32
  isub
  i2c
}
define _sub2_2 {
  bipush 32
  iload[ _]0
  swap
  isub
  i2c
}

within test5
    NAME char -
    MATCH _sub2_1 OR _sub2_2
done

# ============================================

define _sub3_1 {
  iload[ _]0
  iload[ _]1
  isub
  i2c
}
define _sub3_2 {
  iload[ _]1
  iload[ _]0
  swap
  isub
  i2c
}

within test6
    NAME char -
    MATCH _sub3_1 OR _sub3_2
done

