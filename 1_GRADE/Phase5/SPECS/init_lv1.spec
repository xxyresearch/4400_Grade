
define _test1 {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    istore[_ ]0
}

define _test2 {
    fconst_2 OR ldc [+]?2[.]0
    fstore[_ ]0
}

define _test3 {
    bipush 67
    istore[_ ]0
}

within thing1
    NAME int a=1
    MATCH _test1
done

within thing2
    NAME float b=2.0
    MATCH _test2
done

within thing3
    NAME char c='C'
    MATCH _test3
done
