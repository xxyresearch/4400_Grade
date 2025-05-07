
define _test1_0 {
    aload[ _]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    caload
}

define _test1_1 {
    aload[ _]1
    iconst_3 OR [bs]ipush 3 OR ldc 3
    caload
}

define _test1_0s {
    iconst_3 OR [bs]ipush 3 OR ldc 3
    aload[ _]0
    swap
    caload
}

define _test1_1s {
    iconst_3 OR [bs]ipush 3 OR ldc 3
    aload[ _]1
    swap
    caload
}

within test1
    NAME A[3]
    MATCH _test1_0 OR _test1_1 OR _test1_0s OR _test1_1s
done

# ----------------------------------------------------

define _test2 {
    aload[ _]1
    iconst_2 OR [bs]ipush 2 OR ldc 2
    iaload
}

define _test2s {
    iconst_2 OR [bs]ipush 2 OR ldc 2
    aload[ _]1
    swap
    iaload
}

within test2
    NAME A[2]
    MATCH _test2 OR _test2s
done

# ----------------------------------------------------

define _test3 {
    aload[ _]1
    iload_0
    faload
}

define _test3s {
    iload_0
    aload[ _]1
    swap
    faload
}

within test3
    NAME F[i]
    MATCH _test3 OR _test3s
done

