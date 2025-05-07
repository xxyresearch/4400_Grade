
define _test1 {
    iload[_ ]0
    dup OR SKIP
    putstatic [Ff]ield .* b I
}

define _test2 {
    fload[_ ]0
    dup OR SKIP
    putstatic [Ff]ield .* z F
}

within thing1
    NAME int b=a
    MATCH _test1
done

within thing2
    NAME float z=x
    MATCH _test2
done
