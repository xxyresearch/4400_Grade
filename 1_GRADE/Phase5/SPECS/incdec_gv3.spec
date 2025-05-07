
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
    getstatic [Ff]ield .* i I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    dup OR SKIP
    putstatic [Ff]ield .* i I
}

define _subi0b {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* i I
    swap
    isub
    dup OR SKIP
    putstatic [Ff]ield .* i I
}

define _subi0c {
    getstatic [Ff]ield .* i I
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    swap OR SKIP
    iadd
    dup OR SKIP
    putstatic [Ff]ield .* i I
}

define _subi0d {
    iconst_m1 OR [bs]ipush -1 OR ldc -1
    getstatic [Ff]ield .* i I
    swap OR SKIP
    iadd
    dup OR SKIP
    putstatic [Ff]ield .* i I
}

within test1
    NAME --i
    MATCH _subi0a  OR  _subi0b  OR  _subi0c  OR  _subi0d
done

# --------------------------------------------------

define _subf0a {
    getstatic [Ff]ield .* z F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fsub
    dup OR SKIP
    putstatic [Ff]ield .* z F
}

define _subf0b {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* z F
    swap
    fsub
    dup OR SKIP
    putstatic [Ff]ield .* z F
}

define _subf0c {
    getstatic [Ff]ield .* z F
    ldc [-]1[.]0 OR _intm1tofloat
    swap OR SKIP
    fadd
    dup OR SKIP
    putstatic [Ff]ield .* z F
}

define _subf0d {
    ldc [-]1[.]0 OR _intm1tofloat
    getstatic [Ff]ield .* z F
    swap OR SKIP
    fadd
    dup OR SKIP
    putstatic [Ff]ield .* z F
}

within test2
    NAME --z
    MATCH _subf0a  OR  _subf0b  OR  _subf0c  OR  _subf0d
done

