
define _test1 {
  ldc [+]?1[.]25
  fneg
}
within test1
  NAME -1.25
  MATCH _test1
done

define _test2 {
  fload[_ ]0
  fneg
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
  fneg
}

within test4
  NAME -func
  MATCH _test4
done

define _test5 {
  fload[_ ]0
  fneg
  fneg
}

within test5
  NAME double -
  MATCH _test5
done

define _neg25 {
  ldc [+]?2[.]5
  fneg
}

define _neg775 {
  ldc [+]?7[.]75
  fneg
}

define _dneg8875 {
  ldc [+]?8[.]875
  fneg
  fneg
}

within main
  NAME -2.5
  MATCH _neg25

  NAME -7.75
  MATCH _neg775

  NAME - - 8.875
  MATCH _dneg8875
done
