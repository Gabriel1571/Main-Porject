import fractal
pixels = fracta;.mandelbrot(448, 256)
import reprlib
reprlib.repr(pixels)
'[[31, 31, 31, 31, 31, 31, ...],
 [31, 31, 31, 31, 31, 31, 31, 31, ...], 
 [31, 31, 31, 31, 31, 31, ...], [31, 31, 31,
  31, 31, 31, 31, 31, 31, ...], ...]'
  import bmp
  bmp.write_grayscale("madel.bmp", pixels)