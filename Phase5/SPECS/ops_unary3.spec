
define _test1 {
  bipush 72
  invokestatic .* putchar
}
within test1
  NAME (char) literal
  MATCH _test1
done

define _test2 {
  iload[_ ]0
  invokestatic .* putchar
}
within test2
  NAME (char) param
  MATCH _test2
done

define _test3 {
  invokestatic .* LFUNC
  invokestatic .* putchar
}

within test3
  NAME (char) func
  MATCH _test3
done

within test4
  NAME (char) local
  MATCH _test2
done

define _test5 {
  iload[_ ]0
  bipush 32
  iadd
}

within test5
  NAME (char) expr
  MATCH _test5
done

