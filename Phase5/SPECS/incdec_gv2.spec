
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

# --------------------------------------------------

define _dupi0 {
    dup
    putstatic [Ff]ield .* stan I
}
define _stldi0 {
    putstatic [Ff]ield .* stan I
    getstatic [Ff]ield .* stan I
}

define _addi0 {
    getstatic [Ff]ield .* stan I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    _dupi0 OR _stldi0
}

define _addi0s {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* stan I
    swap OR SKIP
    iadd
    _dupi0 OR _stldi0
}

within test1
    NAME return ++a
    MATCH _addi0  OR  _addi0s
done

# --------------------------------------------------

define _dupf0 {
    dup
    putstatic [Ff]ield .* gorax F
}
define _stldf0 {
    putstatic [Ff]ield .* gorax F
    getstatic [Ff]ield .* gorax F
}

define _addf0 {
    getstatic [Ff]ield .* gorax F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    _dupf0 OR _stldf0
}

define _addf0s {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* gorax F
    swap OR SKIP
    fadd
    _dupf0 OR _stldf0
}

within test2
    NAME return ++x
    MATCH _addf0  OR  _addf0s
done

