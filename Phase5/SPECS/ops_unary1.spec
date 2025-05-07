
define _test1 {
  iconst_2 OR [bs]ipush 2 OR LDC 2
  ineg
}
within test1
  NAME -2
  MATCH _test1
done

define _test2 {
  iload[_ ]0
  ineg
}
within test2
  NAME -param
  MATCH _test2
done

within test3
  NAME -local
  MATCH _test2
done

define _test4 {
  invokestatic .* seven
  ineg
}

within test4
  NAME -func
  MATCH _test4
done

define _test5 {
  iload[_ ]0
  ineg
  ineg
}

within test5
  NAME double -
  MATCH _test5
done

define _neg16 {
  [bs]ipush 16 OR ldc 16
  ineg
}

define _neg46 {
  [bs]ipush 46 OR ldc 46
  ineg
}

define _dneg47 {
  [bs]ipush 47 OR ldc 47
  ineg
  ineg
}

within main
  NAME -16
  MATCH _neg16

  NAME -46
  MATCH _neg46

  NAME - - 47
  MATCH _dneg47
done
