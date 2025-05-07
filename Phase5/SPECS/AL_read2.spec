
define _test1 {
    aload[ _]1
    iload[ _]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
    caload
}

define _test1s {
    iload[ _]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
    aload[ _]1
    swap
    caload
}

within test1
    NAME A[i-3]
    MATCH _test1 OR _test1s
done

# ----------------------------------------------------

define _test2 {
    aload[ _]3
    aload[ _]3
    iload[ _]2
    iaload
    iaload
}

define _test2s {
    iload[ _]2
    aload[ _]3
    swap
    iaload
    aload[ _]3
    swap
    iaload
}

within test2
    NAME A[A[j]]
    MATCH _test2 OR _test2s
done

# ----------------------------------------------------

define _test3 {
    aload[ _]0
    invokestatic .* the_index
    faload
}

define _test3s {
    invokestatic .* the_index
    aload[ _]0
    swap
    faload
}

within test3
    NAME F[func()]
    MATCH _test3 OR _test3s
done

