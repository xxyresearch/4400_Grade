
define f1_1 {
  iload[ _]0
  iload[ _]1
  iconst_2 OR [bs]ipush 2 OR ldc2
  imul
  iadd
}

within func1
    NAME a+b*2
    MATCH f1_1
done

# ============================================

define f2_1 {
  iload[ _]0
  iload[ _]1
  iconst_2 OR [bs]ipush 2 OR ldc 2
  idiv
  iadd
}

within func2
    NAME a+b/2
    MATCH f2_1
done

# ============================================

define f3_1 {
  iconst_2 OR [bs]ipush 2 OR ldc 2
  iload[ _]0
  imul
  iload[ _]1
  iadd
}

within func3
    NAME 2*a+b
    MATCH f3_1
done

# ============================================

define f4_1 {
  sipush 888  OR  ldc 888
  iload[ _]0
  imul
  sipush 32749  OR  ldc 32749
  irem
}

within rand
    NAME 888*x%32749
    MATCH f4_1
done
