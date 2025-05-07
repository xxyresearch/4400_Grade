
define _test1 {
    getstatic [fF]ield .* CA [\[]C
    iconst_3 OR [bs]ipush 3 OR ldc 3
    caload
}

define _test1s {
    iconst_3 OR [bs]ipush 3 OR ldc 3
    getstatic [fF]ield .* CA [\[]C
    swap
    caload
}

within test1
    NAME A[3]
    MATCH _test1 OR _test1s
done

# ----------------------------------------------------

define _test2 {
    getstatic [fF]ield .* IA [\[]I
    iconst_2 OR [bs]ipush 2 OR ldc 2
    iaload
}

define _test2s {
    iconst_2 OR [bs]ipush 2 OR ldc 2
    getstatic [fF]ield .* IA [\[]I
    swap
    iaload
}

within test2
    NAME A[2]
    MATCH _test2 OR _test2s
done

# ----------------------------------------------------

define _test3 {
    getstatic [fF]ield .* FA [\[]F
    iload_0
    faload
}

define _test3s {
    iload_0
    getstatic [fF]ield .* FA [\[]F
    swap
    faload
}

within test3
    NAME F[i]
    MATCH _test3 OR _test3s
done

