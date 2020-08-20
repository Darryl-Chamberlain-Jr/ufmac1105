## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file solveExp.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_32 = Integer(32); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_7 = Integer(7); _sage_const_0 = Integer(0); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_112 = Integer(112); _sage_const_118 = Integer(118); _sage_const_120 = Integer(120); _sage_const_127 = Integer(127); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_8 = Integer(8); _sage_const_129 = Integer(129); _sage_const_9 = Integer(9); _sage_const_136 = Integer(136); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_138 = Integer(138); _sage_const_14 = Integer(14); _sage_const_145 = Integer(145); _sage_const_15 = Integer(15); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_147 = Integer(147); _sage_const_19 = Integer(19); _sage_const_154 = Integer(154); _sage_const_213 = Integer(213); _sage_const_219 = Integer(219); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_221 = Integer(221); _sage_const_24 = Integer(24); _sage_const_228 = Integer(228); _sage_const_25 = Integer(25); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_230 = Integer(230); _sage_const_29 = Integer(29); _sage_const_237 = Integer(237); _sage_const_30 = Integer(30); _sage_const_31 = Integer(31); _sage_const_33 = Integer(33); _sage_const_239 = Integer(239); _sage_const_34 = Integer(34)## This file (solveExp.sagetex.sage) was *autogenerated* from solveExp.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveExp', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_32 
_st_.blockbegin()
try:
 x = var("x")
 
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def generateFactor():
     a0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     a1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     factor = a0*x + a1
     return factor
 
 #####
 factor5a = generateFactor()
 factor5b = generateFactor()
 base5 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 #
 while len(solve(factor5a - factor5b == _sage_const_0 , x)) == _sage_const_0 :
     factor5a = generateFactor()
     factor5b = generateFactor()
     base5 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 #
 solution5 = round(float( solve(factor5a - factor5b == _sage_const_0 , x)[_sage_const_0 ].rhs() ), _sage_const_3 )
 #####
 #####
 factor6a = generateFactor()
 factor6b = generateFactor()
 preBase6 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 k6 = ZZ.random_element(_sage_const_2 , _sage_const_4 )
 base6a = preBase6**k6
 base6b = preBase6
 #
 while len(solve(k6*factor6a - factor6b == _sage_const_0 , x)) == _sage_const_0 :
     factor6a = generateFactor()
     factor6b = generateFactor()
     preBase6 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
     k6 = ZZ.random_element(_sage_const_2 , _sage_const_4 )
     base6a = preBase6**k6
     base6b = preBase6
 #
 solution6 = round(float( solve(k6*factor6a - factor6b == _sage_const_0 , x)[_sage_const_0 ].rhs() ), _sage_const_3 )
 #####
 #####
 factor7a = generateFactor()
 factor7b = generateFactor()
 preBase7 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 k7 = -ZZ.random_element(_sage_const_2 , _sage_const_4 )
 base7a = preBase7**k7
 base7b = preBase7
 #
 while len(solve(k7*factor7a - factor7b == _sage_const_0 , x)) == _sage_const_0 :
     factor7a = generateFactor()
     factor7b = generateFactor()
     preBase7 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
     k7 = -ZZ.random_element(_sage_const_2 , _sage_const_4 )
     base7a = preBase7**k7
     base7b = preBase7
 #
 solution7 = round(float( solve(k7*factor7a - factor7b == _sage_const_0 , x)[_sage_const_0 ].rhs() ), _sage_const_3 )
 #####
 #####
 factor8a = generateFactor()
 factor8b = generateFactor()
 preBase8 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 k8a = ZZ.random_element(_sage_const_2 , _sage_const_4 )
 k8b = k8a + ZZ.random_element(_sage_const_1 , _sage_const_2 )
 base8a = preBase8**k8a
 base8b = preBase8**k8b
 #
 while len(solve(k8a*factor8a - k8b*factor8b == _sage_const_0 , x)) == _sage_const_0 :
     factor8a = generateFactor()
     factor8b = generateFactor()
     preBase8 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
     k8a = ZZ.random_element(_sage_const_2 , _sage_const_4 )
     k8b = k8a + ZZ.random_element(_sage_const_1 , _sage_const_2 )
     base8a = preBase8**k8a
     base8b = preBase8**k8b
 #
 solution8 = round(float( solve(k8a*factor8a - k8b*factor8b == _sage_const_0 , x)[_sage_const_0 ].rhs() ), _sage_const_3 )
except:
 _st_.goboom(_sage_const_112 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_0 , latex(base5))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_1 , latex(factor5a))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_2 , latex(base5))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_3 , latex(factor5b))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_4 , latex(solution5))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_5 , latex(base6a))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_6 , latex(factor6a))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_7 , latex(base6b))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_8 , latex(factor6b))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_9 , latex(solution6))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_10 , latex(base7a))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_11 , latex(factor7a))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_12 , latex(base7b))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_13 , latex(factor7b))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_14 , latex(solution7))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_15 , latex(base8a))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_16 , latex(factor8a))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_17 , latex(base8b))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_18 , latex(factor8b))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_147 
 _st_.inline(_sage_const_19 , latex(solution8))
except:
 _st_.goboom(_sage_const_147 )
_st_.current_tex_line = _sage_const_154 
_st_.blockbegin()
try:
 x = var("x")
 
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def generateFactor():
     a0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     a1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     factor = a0*x + a1
     return factor
 
 def generateRelativelyPrimeBases():
     b0 = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     b1 = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     while gcd(b0, b1) > _sage_const_1 :
         b0 = ZZ.random_element(_sage_const_2 , _sage_const_9 )
         b1 = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     return [b0, b1]
 ##########
 factor9a = generateFactor()
 factor9b = generateFactor()
 base9a, base9b = generateRelativelyPrimeBases()
 #
 while len(solve(factor9a * ln(base9a) - factor9b * ln(base9b) == _sage_const_0 , x)) == _sage_const_0 :
     factor9a = generateFactor()
     factor9b = generateFactor()
     base9a, base9b = generateRelativelyPrimeBases()
 #
 solution9 = round(float( solve(factor9a * ln(base9a) - factor9b * ln(base9b) == _sage_const_0 , x)[_sage_const_0 ].rhs() ), _sage_const_3 )
 #####
 #####
 factor10a = generateFactor()
 factor10b = generateFactor()
 base10a = generateRelativelyPrimeBases()[_sage_const_0 ] ** ZZ.random_element(_sage_const_2 , _sage_const_4 )
 base10b = generateRelativelyPrimeBases()[_sage_const_1 ] ** ZZ.random_element(_sage_const_2 , _sage_const_4 )
 #
 while len(solve(factor10a * ln(base10a) - factor10b * ln(base10b) == _sage_const_0 , x)) == _sage_const_0 :
     factor10a = generateFactor()
     factor10b = generateFactor()
     base10a = generateRelativelyPrimeBases()[_sage_const_0 ] ** ZZ.random_element(_sage_const_2 , _sage_const_4 )
     base10b = generateRelativelyPrimeBases()[_sage_const_1 ] ** ZZ.random_element(_sage_const_2 , _sage_const_4 )
 #
 solution10 = round(float( solve(factor10a * ln(base10a) - factor10b * ln(base10b) == _sage_const_0 , x)[_sage_const_0 ].rhs() ), _sage_const_3 )
 #####
 #####
 factor11a = generateFactor()
 factor11b = generateFactor()
 base11a = generateRelativelyPrimeBases()[_sage_const_0 ] ** ZZ.random_element(_sage_const_2 , _sage_const_4 )
 base11b = generateRelativelyPrimeBases()[_sage_const_1 ] ** - ZZ.random_element(_sage_const_2 , _sage_const_4 )
 #
 while len(solve(factor11a * ln(base11a) - factor11b * ln(base11b) == _sage_const_0 , x)) == _sage_const_0 :
     factor11a = generateFactor()
     factor11b = generateFactor()
     base11a = generateRelativelyPrimeBases()[_sage_const_0 ] ** ZZ.random_element(_sage_const_2 , _sage_const_4 )
     base11b = generateRelativelyPrimeBases()[_sage_const_1 ] ** - ZZ.random_element(_sage_const_2 , _sage_const_4 )
 #
 solution11 = round(float( solve(factor11a * ln(base11a) - factor11b * ln(base11b) == _sage_const_0 , x)[_sage_const_0 ].rhs() ), _sage_const_3 )
except:
 _st_.goboom(_sage_const_213 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_219 
 _st_.inline(_sage_const_20 , latex(base9a))
except:
 _st_.goboom(_sage_const_219 )
try:
 _st_.current_tex_line = _sage_const_219 
 _st_.inline(_sage_const_21 , latex(factor9a))
except:
 _st_.goboom(_sage_const_219 )
try:
 _st_.current_tex_line = _sage_const_219 
 _st_.inline(_sage_const_22 , latex(base9b))
except:
 _st_.goboom(_sage_const_219 )
try:
 _st_.current_tex_line = _sage_const_219 
 _st_.inline(_sage_const_23 , latex(factor9b))
except:
 _st_.goboom(_sage_const_219 )
try:
 _st_.current_tex_line = _sage_const_221 
 _st_.inline(_sage_const_24 , latex(solution9))
except:
 _st_.goboom(_sage_const_221 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_25 , latex(base10a))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_26 , latex(factor10a))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_27 , latex(base10b))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_28 , latex(factor10b))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_230 
 _st_.inline(_sage_const_29 , latex(solution10))
except:
 _st_.goboom(_sage_const_230 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_30 , latex(base11a))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_31 , latex(factor11a))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_32 , latex(base11b))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_33 , latex(factor11b))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_239 
 _st_.inline(_sage_const_34 , latex(solution11))
except:
 _st_.goboom(_sage_const_239 )
_st_.endofdoc()

