
define init {
    aload_0
    invokespecial Method java/lang/Object <init>
    return
}

define mainseq {
    invokestatic Method minimal main [(][)]I
    invokestatic Method java/lang/System exit [(]I[)]V
}

within <init>
    NAME init
    MATCH init
done

within main
    NAME call C main
    MATCH invokestatic Method minimal main [(][)]I

    NAME exit status
    MATCH invokestatic Method java/lang/System exit [(]I[)]V

    NAME sequence
    MATCH mainseq
done
