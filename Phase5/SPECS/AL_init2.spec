
define _test1 {
    [bs]ipush 10 OR ldc 10
    newarray char
    astore[_ ]1
}

define _test2 {
    [bs]ipush 15 OR ldc 15
    newarray int
    astore[_ ]2
}

define _test3 {
    [bs]ipush 22 OR ldc 22
    newarray float
    astore[_ ]3
}

within test1
    NAME char[10]
    MATCH _test1
done

within test2
    NAME int[15]
    MATCH _test2
done

within test3
    NAME float[22]
    MATCH _test3
done

