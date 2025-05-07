
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
    getstatic [Ff]ield .* pennies I
    dup OR SKIP
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    putstatic [Ff]ield .* pennies I
}

define _subi0b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* pennies I
    swap
    isub
    putstatic [Ff]ield .* pennies I
}

define _subi0c {
    getstatic [Ff]ield .* pennies I
    dup OR SKIP
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* pennies I
}

define _subi0d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    getstatic [Ff]ield .* pennies I
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* pennies I
}

within test1
    NAME pennies--
    MATCH _subi0a  OR  _subi0b  OR  _subi0c  OR  _subi0d
done

# --------------------------------------------------

define _subf0a {
    getstatic [Ff]ield .* ants F
    dup OR SKIP
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    putstatic [Ff]ield .* ants F
}

define _subf0b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* ants F
    swap
    fsub
    putstatic [Ff]ield .* ants F
}

define _subf0c {
    getstatic [Ff]ield .* ants F
    dup OR SKIP
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    putstatic [Ff]ield .* ants F
}

define _subf0d {
    ldc [-]1[.]0 OR _intm1tofloat
    getstatic [Ff]ield .* ants F
    swap OR SKIP
    fadd
    putstatic [Ff]ield .* ants F
}

within test2
    NAME ants--
    MATCH _subf0a  OR  _subf0b  OR  _subf0c  OR  _subf0d
done

