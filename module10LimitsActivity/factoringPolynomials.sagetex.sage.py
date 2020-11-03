## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file factoringPolynomials.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_31 = Integer(31); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_0 = Integer(0); _sage_const_109 = Integer(109); _sage_const_115 = Integer(115); _sage_const_117 = Integer(117); _sage_const_3 = Integer(3); _sage_const_122 = Integer(122); _sage_const_5 = Integer(5); _sage_const_129 = Integer(129); _sage_const_7 = Integer(7); _sage_const_131 = Integer(131); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_140 = Integer(140); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_147 = Integer(147); _sage_const_16 = Integer(16); _sage_const_149 = Integer(149); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_154 = Integer(154); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_161 = Integer(161); _sage_const_23 = Integer(23); _sage_const_163 = Integer(163); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_26 = Integer(26); _sage_const_168 = Integer(168); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_175 = Integer(175); _sage_const_30 = Integer(30); _sage_const_177 = Integer(177); _sage_const_32 = Integer(32); _sage_const_182 = Integer(182); _sage_const_33 = Integer(33); _sage_const_34 = Integer(34); _sage_const_35 = Integer(35); _sage_const_189 = Integer(189); _sage_const_36 = Integer(36); _sage_const_191 = Integer(191); _sage_const_37 = Integer(37); _sage_const_38 = Integer(38); _sage_const_196 = Integer(196); _sage_const_39 = Integer(39); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41)## This file (factoringPolynomials.sagetex.sage) was *autogenerated* from factoringPolynomials.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('factoringPolynomials', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_31 
_st_.blockbegin()
try:
 R, x = QQ['x'].objgen()
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def makeIntegerFactor():
     zero = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     integerFactor = x - zero
     return [integerFactor, zero]
 
 def makeRationalFactor():
     a = ZZ.random_element(_sage_const_1 , _sage_const_4 )
     b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     while gcd(abs(a), abs(b)) > _sage_const_1 :
         a = ZZ.random_element(_sage_const_1 , _sage_const_4 )
         b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     rationalFactor = a*x + b
     return [rationalFactor, -b/a]
 
 def makeIrrationalQuadratic():
     a = ZZ.random_element(_sage_const_1 , _sage_const_6 )
     b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     c = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     discrim = b**_sage_const_2  - _sage_const_4 *a*c
     integerType = type(_sage_const_2 )
     while type(sqrt(discrim)) == integerType or _sage_const_0  > discrim:
         a = ZZ.random_element(_sage_const_1 , _sage_const_6 )
         b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         c = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         discrim = b**_sage_const_2  - _sage_const_4 *a*c
     solution0 = (-b + sqrt(discrim))/(_sage_const_2 *a)
     solution1 = (-b - sqrt(discrim))/(_sage_const_2 *a)
     smallerSolution, largerSolution = sorted([solution0, solution1])
     quadratic = a*x**_sage_const_2  + b*x + c
     return [quadratic, smallerSolution, largerSolution]
 
 def makeComplexQuadratic():
     a0 = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_4 ))
     b0 = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     complex0 = a0 + b0*i
     complex1 = a0 - b0*i
     quadratic = x**_sage_const_2  -_sage_const_2 *a0*x + (a0**_sage_const_2  + b0**_sage_const_2 )
     return [quadratic, complex0, complex1]
 ######################
 factor1a, zeroTemp1a = makeIntegerFactor()
 factor1b, zeroTemp1b = makeIntegerFactor()
 factor1c, zeroTemp1c = makeIntegerFactor()
 polynomial1 = factor1a * factor1b * factor1c
 zero1a, zero1b, zero1c = sorted([zeroTemp1a, zeroTemp1b, zeroTemp1c])
 
 factor2a, zeroTemp2a = makeIntegerFactor()
 factor2b, zeroTemp2b = makeIntegerFactor()
 factor2c, zeroTemp2c = makeIntegerFactor()
 factor2d, zeroTemp2d = makeIntegerFactor()
 polynomial2 = factor2a * factor2b * factor2c * factor2d
 zero2a, zero2b, zero2c, zero2d = sorted([zeroTemp2a, zeroTemp2b, zeroTemp2c, zeroTemp2d])
 
 factor3a, zeroTemp3a = makeIntegerFactor()
 factor3b, zeroTemp3b = makeRationalFactor()
 factor3c, zeroTemp3c = makeRationalFactor()
 polynomial3 = factor3a * factor3b * factor3c
 zero3a, zero3b, zero3c = sorted([zeroTemp3a, zeroTemp3b, zeroTemp3c])
 
 factor4a, zeroTemp4a = makeRationalFactor()
 factor4b, zeroTemp4b = makeRationalFactor()
 factor4c, zeroTemp4c = makeRationalFactor()
 polynomial4 = factor4a * factor4b * factor4c
 zero4a, zero4b, zero4c = sorted([zeroTemp4a, zeroTemp4b, zeroTemp4c])
 
 factor5a, zeroTemp5a = makeIntegerFactor()
 factor5b, zeroTemp5b, zeroTemp5c = makeIrrationalQuadratic()
 zero5a, zero5b, zero5c = sorted([zeroTemp5a, zeroTemp5b, zeroTemp5c])
 polynomial5 = factor5a * factor5b
 
 factor6a, zero6a = makeIntegerFactor()
 factor6b, zero6b, zero6c = makeComplexQuadratic()
 polynomial6 = factor6a * factor6b
except:
 _st_.goboom(_sage_const_109 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_115 
 _st_.inline(_sage_const_0 , latex(polynomial1))
except:
 _st_.goboom(_sage_const_115 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_1 , latex(factor1a))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_2 , latex(factor1b))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_3 , latex(factor1c))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_4 , latex(zero1a))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_5 , latex(zero1b))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_6 , latex(zero1c))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_7 , latex(polynomial2))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_131 
 _st_.inline(_sage_const_8 , latex(factor2a))
except:
 _st_.goboom(_sage_const_131 )
try:
 _st_.current_tex_line = _sage_const_131 
 _st_.inline(_sage_const_9 , latex(factor2b))
except:
 _st_.goboom(_sage_const_131 )
try:
 _st_.current_tex_line = _sage_const_131 
 _st_.inline(_sage_const_10 , latex(factor2c))
except:
 _st_.goboom(_sage_const_131 )
try:
 _st_.current_tex_line = _sage_const_131 
 _st_.inline(_sage_const_11 , latex(factor2d))
except:
 _st_.goboom(_sage_const_131 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_12 , latex(zero2a))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_13 , latex(zero2b))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_14 , latex(zero2c))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_15 , latex(zero2d))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_147 
 _st_.inline(_sage_const_16 , latex(polynomial3))
except:
 _st_.goboom(_sage_const_147 )
try:
 _st_.current_tex_line = _sage_const_149 
 _st_.inline(_sage_const_17 , latex(factor3a))
except:
 _st_.goboom(_sage_const_149 )
try:
 _st_.current_tex_line = _sage_const_149 
 _st_.inline(_sage_const_18 , latex(factor3b))
except:
 _st_.goboom(_sage_const_149 )
try:
 _st_.current_tex_line = _sage_const_149 
 _st_.inline(_sage_const_19 , latex(factor3c))
except:
 _st_.goboom(_sage_const_149 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_20 , latex(zero3a))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_21 , latex(zero3b))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_22 , latex(zero3c))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_23 , latex(polynomial4))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_163 
 _st_.inline(_sage_const_24 , latex(factor4a))
except:
 _st_.goboom(_sage_const_163 )
try:
 _st_.current_tex_line = _sage_const_163 
 _st_.inline(_sage_const_25 , latex(factor4b))
except:
 _st_.goboom(_sage_const_163 )
try:
 _st_.current_tex_line = _sage_const_163 
 _st_.inline(_sage_const_26 , latex(factor4c))
except:
 _st_.goboom(_sage_const_163 )
try:
 _st_.current_tex_line = _sage_const_168 
 _st_.inline(_sage_const_27 , latex(zero4a))
except:
 _st_.goboom(_sage_const_168 )
try:
 _st_.current_tex_line = _sage_const_168 
 _st_.inline(_sage_const_28 , latex(zero4b))
except:
 _st_.goboom(_sage_const_168 )
try:
 _st_.current_tex_line = _sage_const_168 
 _st_.inline(_sage_const_29 , latex(zero4c))
except:
 _st_.goboom(_sage_const_168 )
try:
 _st_.current_tex_line = _sage_const_175 
 _st_.inline(_sage_const_30 , latex(polynomial5))
except:
 _st_.goboom(_sage_const_175 )
try:
 _st_.current_tex_line = _sage_const_177 
 _st_.inline(_sage_const_31 , latex(factor5a))
except:
 _st_.goboom(_sage_const_177 )
try:
 _st_.current_tex_line = _sage_const_177 
 _st_.inline(_sage_const_32 , latex(factor5b))
except:
 _st_.goboom(_sage_const_177 )
try:
 _st_.current_tex_line = _sage_const_182 
 _st_.inline(_sage_const_33 , latex(zero5a))
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.current_tex_line = _sage_const_182 
 _st_.inline(_sage_const_34 , latex(zero5b))
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.current_tex_line = _sage_const_182 
 _st_.inline(_sage_const_35 , latex(zero5c))
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.current_tex_line = _sage_const_189 
 _st_.inline(_sage_const_36 , latex(polynomial6))
except:
 _st_.goboom(_sage_const_189 )
try:
 _st_.current_tex_line = _sage_const_191 
 _st_.inline(_sage_const_37 , latex(factor6a))
except:
 _st_.goboom(_sage_const_191 )
try:
 _st_.current_tex_line = _sage_const_191 
 _st_.inline(_sage_const_38 , latex(factor6b))
except:
 _st_.goboom(_sage_const_191 )
try:
 _st_.current_tex_line = _sage_const_196 
 _st_.inline(_sage_const_39 , latex(zero6a))
except:
 _st_.goboom(_sage_const_196 )
try:
 _st_.current_tex_line = _sage_const_196 
 _st_.inline(_sage_const_40 , latex(zero6b))
except:
 _st_.goboom(_sage_const_196 )
try:
 _st_.current_tex_line = _sage_const_196 
 _st_.inline(_sage_const_41 , latex(zero6c))
except:
 _st_.goboom(_sage_const_196 )
_st_.endofdoc()

