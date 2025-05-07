
within test3
    NAME String literal
    MATCH ldc ['"]Hello

    NAME Java to C
    MATCH invokestatic [Mm]ethod lib440 java2c

    NAME Function call
    MATCH invokestatic [Mm]ethod .* test1 [(][\[]C[)]V
done

within test4
    NAME String literal
    MATCH ldc ['"]world!

    NAME Java to C
    MATCH invokestatic [Mm]ethod lib440 java2c

    NAME Function call
    MATCH invokestatic [Mm]ethod .* test2 [(]I[\[]C[)]C
done
