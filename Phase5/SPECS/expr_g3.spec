
within print4
    NAME read x
    MATCH getstatic Field expr_g3 x F

    NAME read y
    MATCH getstatic Field expr_g3 y F

    NAME read z
    MATCH getstatic Field expr_g3 z F
done

define wra1 {
    8[.]486
    putstatic Field expr_g3 x F
}
define wra1dp {
    8[.]486
    dup
    putstatic Field expr_g3 x F
    pop
}

define wrb1 {
    10[.]05
    putstatic Field expr_g3 y F
}
define wrb1dp {
    10[.]05
    dup
    putstatic Field expr_g3 y F
    pop
}

define wrc1 {
    10[.]4
    putstatic Field expr_g3 z F
}
define wrc1dp {
    10[.]4
    dup
    putstatic Field expr_g3 z F
    pop
}

define wra2 {
    10[.]54
    putstatic Field expr_g3 x F
}
define wra2dp {
    10[.]54
    dup
    putstatic Field expr_g3 x F
    pop
}

define wrb2 {
    5[.]66
    putstatic Field expr_g3 y F
}
define wrb2dp {
    5[.]66
    dup
    putstatic Field expr_g3 y F
    pop
}

define wrc2 {
    9[.]33
    putstatic Field expr_g3 z F
}
define wrc2dp {
    9[.]33
    dup
    putstatic Field expr_g3 z F
    pop
}

within main
    NAME write x
    MATCH wra1 OR wra1dp

    NAME write x
    MATCH wra2 OR wra2dp

    NAME write y
    MATCH wrb1 OR wrb1dp

    NAME write y
    MATCH wrb2 OR wrb2dp

    NAME write z
    MATCH wrc1 OR wrc1dp

    NAME write z
    MATCH wrc2 OR wrc2dp
done
