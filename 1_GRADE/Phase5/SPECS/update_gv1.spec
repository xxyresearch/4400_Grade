
define _test1 {
    getstatic [Ff]ield .* a I
    iload[ _]0
    isub
    dup OR SKIP
    putstatic [Ff]ield .* a I
}
define _test1s {
    iload[ _]0
    getstatic [Ff]ield .* a I
    swap
    isub
    dup OR SKIP
    putstatic [Ff]ield .* a I
}

within test1
    NAME a -= b
    MATCH _test1
done

# ----------------------------------------

define _test2 {
    getstatic [Ff]ield .* c F
    fload[ _]0
    swap OR SKIP
    fadd
    dup OR SKIP
    putstatic [Ff]ield .* c F
}

define _test2s {
    fload[ _]0
    getstatic [Ff]ield .* c F
    swap OR SKIP
    fadd
    dup OR SKIP
    putstatic [Ff]ield .* c F
}

within test2
    NAME c += d
    MATCH _test2
done

# ----------------------------------------

define _test3 {
    getstatic [Ff]ield .* b I
    iload[ _]0
    swap OR SKIP
    imul
    dup OR SKIP
    putstatic [Ff]ield .* b I
}

define _test3s {
    iload[ _]0
    getstatic [Ff]ield .* b I
    swap OR SKIP
    imul
    dup OR SKIP
    putstatic [Ff]ield .* b I
}

within test3
    NAME b *= a
    MATCH _test3
done

# ----------------------------------------

define _test4 {
    getstatic [Ff]ield .* d F
    fload[ _]0
    fdiv
    dup OR SKIP
    putstatic [Ff]ield .* d F
}
define _test4s {
    fload[ _]0
    getstatic [Ff]ield .* d F
    swap
    fdiv
    dup OR SKIP
    putstatic [Ff]ield .* d F
}

within test4
    NAME d /= c
    MATCH _test4 OR _test4s
done


