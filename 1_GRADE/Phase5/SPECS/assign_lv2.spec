
define _test1 {
    iload[_ ]0
    dup OR SKIP
    istore[_ ]1
}

define _test2 {
    fload[_ ]0
    dup OR SKIP
    fstore[_ ]1
}

within thing1
    NAME int b=a
    MATCH _test1
done

within thing2
    NAME float z=x
    MATCH _test2
done
