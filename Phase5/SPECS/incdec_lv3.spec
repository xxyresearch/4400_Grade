
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

define _intm1tofloat {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    i2f
}

# --------------------------------------------------

define _subi0a {
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    dup OR SKIP
    istore[ _]0
}

define _subi0b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]0
    swap
    isub
    dup OR SKIP
    istore[ _]0
}

define _subi0c {
    iload[ _]0
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    dup OR SKIP
    istore[ _]0
}

define _subi0d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    iload[ _]0
    swap OR SKIP
    iadd
    dup OR SKIP
    istore[ _]0
}

within test1
    NAME --a
    MATCH iinc 0 -1  OR  _subi0a  OR  _subi0b  OR  _subi0c  OR  _subi0d
done

# --------------------------------------------------

define _subf0a {
    fload[ _]0
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    dup OR SKIP
    fstore[ _]0
}

define _subf0b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]0
    swap
    fsub
    dup OR SKIP
    fstore[ _]0
}

define _subf0c {
    fload[ _]0
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    dup OR SKIP
    fstore[ _]0
}

define _subf0d {
    ldc [-]1[.]0 OR _intm1tofloat
    fload[ _]0
    swap OR SKIP
    fadd
    dup OR SKIP
    fstore[ _]0
}

within test2
    NAME --x
    MATCH _subf0a  OR  _subf0b  OR  _subf0c  OR  _subf0d
done

# --------------------------------------------------

define _subi1a {
    iload[ _]1
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    dup OR SKIP
    istore[ _]1
}

define _subi1b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]1
    swap
    isub
    dup OR SKIP
    istore[ _]1
}

define _subi1c {
    iload[ _]1
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    dup OR SKIP
    istore[ _]1
}

define _subi1d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    iload[ _]1
    swap OR SKIP
    iadd
    dup OR SKIP
    istore[ _]1
}

within test3
    NAME --b
    MATCH iinc 1 -1  OR  _subi1a  OR  _subi1b  OR  _subi1c  OR  _subi1d
done

# --------------------------------------------------

define _subf1a {
    fload[ _]1
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    dup OR SKIP
    fstore[ _]1
}

define _subf1b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]1
    swap
    fsub
    dup OR SKIP
    fstore[ _]1
}

define _subf1c {
    fload[ _]1
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    dup OR SKIP
    fstore[ _]1
}

define _subf1d {
    ldc [-]1[.]0 OR _intm1tofloat
    fload[ _]1
    swap OR SKIP
    fadd
    dup OR SKIP
    fstore[ _]1
}

within test4
    NAME --y
    MATCH _subf1a  OR  _subf1b  OR  _subf1c  OR  _subf1d
done


