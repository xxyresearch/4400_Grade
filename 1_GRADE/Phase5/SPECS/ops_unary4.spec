
define _test1 {
  ldc [+]?1[.]23
  f2i
}
within test1
  NAME (int) 1.23
  MATCH _test1
done

define _test2 {
  fload[_ ]0
  f2i
}
within test2
  NAME (int) param
  MATCH _test2
done

define _test3 {
  invokestatic .* pi
  f2i
}

within test3
  NAME (int) func
  MATCH _test3
done

within test4
  NAME (int) local
  MATCH _test2
done

define _test5 {
  fload[_ ]0
  ldc [+]?0[.]6
  fsub
  f2i
}

within test5
  NAME (int) expr
  MATCH _test5
done

