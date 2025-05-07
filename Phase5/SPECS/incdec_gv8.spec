
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
    getstatic [Ff]ield .* these_are_horrible I
    dup OR getstatic [Ff]ield .* these_are_horrible I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    putstatic [Ff]ield .* these_are_horrible I
}

define _subi0b {
    getstatic [Ff]ield .* these_are_horrible I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* these_are_horrible I
    swap
    isub
    putstatic [Ff]ield .* these_are_horrible I
}

define _subi0c {
    getstatic [Ff]ield .* these_are_horrible I
    dup OR getstatic [Ff]ield .* these_are_horrible I
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* these_are_horrible I
}

define _subi0d {
    getstatic [Ff]ield .* these_are_horrible I
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    iload[ _]0
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* these_are_horrible I
}

within test1
    NAME return int --
    MATCH _subi0a  OR  _subi0b  OR  _subi0c  OR  _subi0d
done

# --------------------------------------------------

define _subf0a {
    getstatic [Ff]ield .* uses_for_globals F
    dup OR getstatic [Ff]ield .* uses_for_globals F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    putstatic [Ff]ield .* uses_for_globals F
}

define _subf0b {
    getstatic [Ff]ield .* uses_for_globals F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* uses_for_globals F
    swap
    fsub
    putstatic [Ff]ield .* uses_for_globals F
}

define _subf0c {
    getstatic [Ff]ield .* uses_for_globals F
    dup OR getstatic [Ff]ield .* uses_for_globals F
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    putstatic [Ff]ield .* uses_for_globals F
}

define _subf0d {
    getstatic [Ff]ield .* uses_for_globals F
    ldc [-]1[.]0 OR _intm1tofloat
    getstatic [Ff]ield .* uses_for_globals F
    swap OR SKIP
    fadd
    putstatic [Ff]ield .* uses_for_globals F
}

within test2
    NAME return float--
    MATCH _subf0a  OR  _subf0b  OR  _subf0c  OR  _subf0d
done

