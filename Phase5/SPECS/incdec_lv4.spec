
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

define _intm1tofloat {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    i2f
}

# --------------------------------------------------

define _dupi0 {
    dup
    istore[ _]0
}
define _stldi0 {
    istore[ _]0
    iload[ _]0
}

define _subi0a {
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    _dupi0 or _stldi0
}

define _subi0b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]0
    swap
    isub
    _dupi0 or _stldi0
}

define _subi0c {
    iload[ _]0
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    _dupi0 or _stldi0
}

define _subi0d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    iload[ _]0
    swap OR SKIP
    iadd
    _dupi0 or _stldi0
}

within test1
    NAME return --a
    MATCH iinc 0 -1  OR  _subi0a  OR  _subi0b  OR  _subi0c  OR  _subi0d
done

# --------------------------------------------------

define _dupf0 {
    dup
    fstore[ _]0
}
define _stldf0 {
    fstore[ _]0
    fload[ _]0
}

define _subf0a {
    fload[ _]0
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    _dupf0 or _stldf0
}

define _subf0b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]0
    swap
    fsub
    _dupf0 or _stldf0
}

define _subf0c {
    fload[ _]0
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    _dupf0 or _stldf0
}

define _subf0d {
    ldc [-]1[.]0 OR _intm1tofloat
    fload[ _]0
    swap OR SKIP
    fadd
    _dupf0 or _stldf0
}

within test2
    NAME return --x
    MATCH _subf0a  OR  _subf0b  OR  _subf0c  OR  _subf0d
done

# --------------------------------------------------

define _dupi1 {
    dup
    istore[ _]1
}
define _stldi1 {
    istore[ _]1
    iload[ _]1
}

define _subi1a {
    iload[ _]1
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    _dupi1 or _stldi1
}

define _subi1b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]1
    swap
    isub
    _dupi1 or _stldi1
}

define _subi1c {
    iload[ _]1
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    _dupi1 or _stldi1
}

define _subi1d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    iload[ _]1
    swap OR SKIP
    iadd
    _dupi1 or _stldi1
}

within test3
    NAME return --b
    MATCH iinc 1 -1  OR  _subi1a  OR  _subi1b  OR  _subi1c  OR  _subi1d
done

# --------------------------------------------------

define _dupf1 {
    dup
    fstore[ _]1
}
define _stldf1 {
    fstore[ _]1
    fload[ _]1
}

define _subf1a {
    fload[ _]1
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    _dupf1 or _stldf1
}

define _subf1b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]1
    swap
    fsub
    _dupf1 or _stldf1
}

define _subf1c {
    fload[ _]1
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    _dupf1 or _stldf1
}

define _subf1d {
    ldc [-]1[.]0 OR _intm1tofloat
    fload[ _]1
    swap OR SKIP
    fadd
    _dupf1 or _stldf1
}

within test4
    NAME return --y
    MATCH _subf1a  OR  _subf1b  OR  _subf1c  OR  _subf1d
done


