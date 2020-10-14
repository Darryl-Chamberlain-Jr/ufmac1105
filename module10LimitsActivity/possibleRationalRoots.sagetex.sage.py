## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file possibleRationalRoots.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_76 = Integer(76); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_7 = Integer(7); _sage_const_11 = Integer(11); _sage_const_88 = Integer(88); _sage_const_93 = Integer(93); _sage_const_0 = Integer(0); _sage_const_95 = Integer(95); _sage_const_1 = Integer(1); _sage_const_101 = Integer(101); _sage_const_4 = Integer(4); _sage_const_103 = Integer(103); _sage_const_111 = Integer(111); _sage_const_9 = Integer(9); _sage_const_25 = Integer(25); _sage_const_49 = Integer(49); _sage_const_121 = Integer(121); _sage_const_117 = Integer(117); _sage_const_122 = Integer(122); _sage_const_6 = Integer(6); _sage_const_124 = Integer(124); _sage_const_8 = Integer(8); _sage_const_130 = Integer(130); _sage_const_132 = Integer(132); _sage_const_10 = Integer(10)## This file (possibleRationalRoots.sagetex.sage) was *autogenerated* from possibleRationalRoots.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('possibleRationalRoots', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_76 
_st_.blockbegin()
try:
 listSomePrimes = [_sage_const_2 , _sage_const_3 , _sage_const_5 , _sage_const_7 , _sage_const_11 ]
 divisor0, divisor1 = sample(listSomePrimes, _sage_const_2 )
 notPerfectSquare = divisor0 * divisor1
 if divisor1 > divisor0:
     smallerDivisor = divisor0
     largerDivisor = divisor1
 else:
     smallerDivisor = divisor1
     largerDivisor = divisor0
 solution1a = float(-sqrt(notPerfectSquare))
 solution1b = float(sqrt(notPerfectSquare))
except:
 _st_.goboom(_sage_const_88 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_93 
 _st_.inline(_sage_const_0 , latex(notPerfectSquare))
except:
 _st_.goboom(_sage_const_93 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_1 , latex(smallerDivisor))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_2 , latex(largerDivisor))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_3 , latex(notPerfectSquare))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_4 , latex(solution1a))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_5 , latex(solution1b))
except:
 _st_.goboom(_sage_const_103 )
_st_.current_tex_line = _sage_const_111 
_st_.blockbegin()
try:
 listPerfectSquares = [_sage_const_4 , _sage_const_9 , _sage_const_25 , _sage_const_49 , _sage_const_121 ]
 perfectSquare = sample(listPerfectSquares, _sage_const_1 )[_sage_const_0 ]
 otherDivisor = sqrt(perfectSquare)
 smallerRoot = -sqrt(perfectSquare)*i
 largerRoot = sqrt(perfectSquare)*i
except:
 _st_.goboom(_sage_const_117 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_6 , latex(perfectSquare))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.inline(_sage_const_7 , latex(otherDivisor))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.inline(_sage_const_8 , latex(perfectSquare))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_9 , latex(smallerRoot))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_10 , latex(largerRoot))
except:
 _st_.goboom(_sage_const_132 )
_st_.endofdoc()

