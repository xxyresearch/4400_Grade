
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
    dup OR SKIP
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    istore[ _]0
}

define _subi0b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]0
    swap
    isub
    istore[ _]0
}

define _subi0c {
    iload[ _]0
    dup OR SKIP
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    istore[ _]0
}

define _subi0d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    iload[ _]0
    swap OR SKIP
    iadd
    istore[ _]0
}

within test1
    NAME a--
    MATCH iinc 0 -1  OR  _subi0a  OR  _subi0b  OR  _subi0c  OR  _subi0d
done

# --------------------------------------------------

define _subf0a {
    fload[ _]0
    dup OR SKIP
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    fstore[ _]0
}

define _subf0b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]0
    swap
    fsub
    fstore[ _]0
}

define _subf0c {
    fload[ _]0
    dup OR SKIP
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    fstore[ _]0
}

define _subf0d {
    ldc [-]1[.]0 OR _intm1tofloat
    fload[ _]0
    swap OR SKIP
    fadd
    fstore[ _]0
}

within test2
    NAME x--
    MATCH _subf0a  OR  _subf0b  OR  _subf0c  OR  _subf0d
done

# --------------------------------------------------

define _subi1a {
    iload[ _]1
    dup OR SKIP
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    istore[ _]1
}

define _subi1b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]1
    swap
    isub
    istore[ _]1
}

define _subi1c {
    iload[ _]1
    dup OR SKIP
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    istore[ _]1
}

define _subi1d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    iload[ _]1
    swap OR SKIP
    iadd
    istore[ _]1
}

within test3
    NAME b--
    MATCH iinc 1 -1  OR  _subi1a  OR  _subi1b  OR  _subi1c  OR  _subi1d
done

# --------------------------------------------------

define _subf1a {
    fload[ _]1
    dup OR SKIP
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    fstore[ _]1
}

define _subf1b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]1
    swap
    fsub
    fstore[ _]1
}

define _subf1c {
    fload[ _]1
    dup OR SKIP
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    fstore[ _]1
}

define _subf1d {
    ldc [-]1[.]0 OR _intm1tofloat
    fload[ _]1
    swap OR SKIP
    fadd
    fstore[ _]1
}

within test4
    NAME y--
    MATCH _subf1a  OR  _subf1b  OR  _subf1c  OR  _subf1d
done


