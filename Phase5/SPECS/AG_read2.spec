
define _test1 {
    getstatic [fF]ield .* CA [\[]C
    iload[_ ]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
    caload
}

define _test1s {
    iload[_ ]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
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
    getstatic [fF]ield .* IA [\[]I
    iload[_ ]2
    iaload
    iaload
}

define _test2s {
    iload[_ ]2
    getstatic [fF]ield .* IA [\[]I
    swap
    iaload
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
    invokestatic .* the_index
    faload
}

define _test3s {
    invokestatic .* the_index
    getstatic [fF]ield .* FA [\[]F
    swap
    faload
}

within test3
    NAME F[i]
    MATCH _test3 OR _test3s
done

