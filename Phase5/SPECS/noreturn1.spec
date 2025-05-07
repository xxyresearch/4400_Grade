
within voidfunc
    NAME added return
    MATCH return
done

within floatfunc
    NAME has freturn
    MATCH freturn
    NAME no added return
    OMIT ^return
done
