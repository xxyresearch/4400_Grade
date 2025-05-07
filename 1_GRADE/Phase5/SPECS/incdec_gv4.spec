
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
    putstatic [Ff]ield .* counter I
}
define _stldi0 {
    putstatic [Ff]ield .* counter I
    getstatic [Ff]ield .* counter I
}

define _subi0a {
    getstatic [Ff]ield .* counter I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    _dupi0 or _stldi0
}

define _subi0b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* counter I
    swap
    isub
    _dupi0 or _stldi0
}

define _subi0c {
    getstatic [Ff]ield .* counter I
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    _dupi0 or _stldi0
}

define _subi0d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    getstatic [Ff]ield .* counter I
    swap OR SKIP
    iadd
    _dupi0 or _stldi0
}

within test1
    NAME return --counter
    MATCH _subi0a  OR  _subi0b  OR  _subi0c  OR  _subi0d
done

# --------------------------------------------------

define _dupf0 {
    dup
    putstatic [Ff]ield .* mass F
}
define _stldf0 {
    putstatic [Ff]ield .* mass F
    getstatic [Ff]ield .* mass F
}

define _subf0a {
    getstatic [Ff]ield .* mass F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    _dupf0 or _stldf0
}

define _subf0b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* mass F
    swap
    fsub
    _dupf0 or _stldf0
}

define _subf0c {
    getstatic [Ff]ield .* mass F
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    _dupf0 or _stldf0
}

define _subf0d {
    ldc [-]1[.]0 OR _intm1tofloat
    getstatic [Ff]ield .* mass F
    swap OR SKIP
    fadd
    _dupf0 or _stldf0
}

within test2
    NAME return --mass
    MATCH _subf0a  OR  _subf0b  OR  _subf0c  OR  _subf0d
done

