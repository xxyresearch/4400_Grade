
define _test1 {
  [bs]ipush 9 OR ldc 9
  i2f
}
within test1
  NAME (float) 9
  MATCH _test1
done

define _test2 {
  iload[_ ]0
  i2f
}
within test2
  NAME (float) param
  MATCH _test2
done

define _test3 {
  invokestatic .* seven
  i2f
}

within test3
  NAME (float) func
  MATCH _test3
done

within test4
  NAME (float) local
  MATCH _test2
done

define _test5 {
  [bs]ipush 55 OR ldc 55
  iload[_ ]0
  isub
  i2f
}

within test5
  NAME (float) expr
  MATCH _test5
done

