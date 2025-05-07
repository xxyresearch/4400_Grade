
within first
  NAME float return
  MATCH freturn
done

within second
  NAME float return
  MATCH freturn
done

within third
  NAME float return
  MATCH freturn
done

within fourth
  NAME float return
  MATCH freturn
done

within fifth
  NAME float return
  MATCH freturn
done

within ninex
  NAME float return
  MATCH freturn
done

define seq {
  first
  second
  third
  fourth
  fifth
  ninex
  putfloat
}

within main
  NAME nested params
  MATCH seq

  NAME first()
  MATCH invokestatic [Mm]ethod fcall3 first [(][)]F

  NAME second()
  MATCH invokestatic [Mm]ethod fcall3 second [(][)]F

  NAME third()
  MATCH invokestatic [Mm]ethod fcall3 third [(][)]F

  NAME fourth()
  MATCH invokestatic [Mm]ethod fcall3 fourth [(][)]F

  NAME fifth()
  MATCH invokestatic [Mm]ethod fcall3 fifth [(][)]F

  NAME ninex()
  MATCH invokestatic [Mm]ethod fcall3 ninex [(]FFFFF[)]F

  NAME putfloat()
  MATCH invokestatic [Mm]ethod lib440 putfloat [(]F[)]V

  NAME putchar()
  MATCH invokestatic [Mm]ethod lib440 putchar [(]I[)]I
done
