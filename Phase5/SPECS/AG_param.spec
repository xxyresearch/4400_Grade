
define _test1C_a {
    aload[ _]0
    iconst_0 OR [bs]ipush 0 OR ldc 0
    caload
}
define _test1C_b {
    iconst_0 OR [bs]ipush 0 OR ldc 0
    aload[ _]0
    swap
    caload
}

within test1C
    NAME read char[]
    MATCH _test1C_a OR _test1C_b
done

# ------------------------------------------------------------

define _test2C {
    aload[ _]1
    invokestatic [Mm]ethod .* test1C [(][\[]C[)]V
}

within test2C
    NAME read+pass char[]
    MATCH _test2C
done

# ------------------------------------------------------------

define _test3C {
    getstatic [Ff]ield .* Carray [\[]C
    invokestatic [Mm]ethod .* test2C [(]I[\[]C[)]V
}

within test3C
    NAME pass char[]
    MATCH _test3C
done

# ======================================================================

define _test1I_a {
    aload[ _]0
    iconst_0 OR [bs]ipush 0 OR ldc 0
    iaload
}
define _test1I_b {
    iconst_0 OR [bs]ipush 0 OR ldc 0
    aload[ _]0
    swap
    iaload
}

within test1I
    NAME read char[]
    MATCH _test1I_a OR _test1I_b
done

# ------------------------------------------------------------

define _test2I {
    aload[ _]1
    invokestatic [Mm]ethod .* test1I [(][\[]I[)]I
}

within test2I
    NAME read+pass char[]
    MATCH _test2I
done

# ------------------------------------------------------------

define _test3I {
    getstatic [Ff]ield .* Iarray [\[]I
    invokestatic [Mm]ethod .* test2I [(]I[\[]I[)]V
}

within test3I
    NAME pass char[]
    MATCH _test3I
done

# ======================================================================

define _test1F_a {
    aload[ _]0
    iconst_0 OR [bs]ipush 0 OR ldc 0
    faload
}
define _test1F_b {
    iconst_0 OR [bs]ipush 0 OR ldc 0
    aload[ _]0
    swap
    faload
}

within test1F
    NAME read char[]
    MATCH _test1F_a OR _test1F_b
done

# ------------------------------------------------------------

define _test2F {
    aload[ _]1
    invokestatic [Mm]ethod .* test1F [(][\[]F[)]V
}

within test2F
    NAME read+pass char[]
    MATCH _test2F
done

# ------------------------------------------------------------

define _test3F {
    getstatic [Ff]ield .* Farray [\[]F
    invokestatic [Mm]ethod .* test2F [(]I[\[]F[)]V
}

within test3F
    NAME pass char[]
    MATCH _test3F
done

