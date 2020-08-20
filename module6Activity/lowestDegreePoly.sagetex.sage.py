## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file lowestDegreePoly.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_290 = Integer(290); _sage_const_294 = Integer(294); _sage_const_116 = Integer(116); _sage_const_296 = Integer(296); _sage_const_114 = Integer(114); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_98 = Integer(98); _sage_const_104 = Integer(104); _sage_const_106 = Integer(106); _sage_const_248 = Integer(248); _sage_const_246 = Integer(246); _sage_const_240 = Integer(240); _sage_const_66 = Integer(66); _sage_const_67 = Integer(67); _sage_const_64 = Integer(64); _sage_const_65 = Integer(65); _sage_const_62 = Integer(62); _sage_const_63 = Integer(63); _sage_const_60 = Integer(60); _sage_const_61 = Integer(61); _sage_const_138 = Integer(138); _sage_const_68 = Integer(68); _sage_const_69 = Integer(69); _sage_const_251 = Integer(251); _sage_const_45 = Integer(45); _sage_const_75 = Integer(75); _sage_const_74 = Integer(74); _sage_const_77 = Integer(77); _sage_const_76 = Integer(76); _sage_const_126 = Integer(126); _sage_const_70 = Integer(70); _sage_const_124 = Integer(124); _sage_const_72 = Integer(72); _sage_const_78 = Integer(78); _sage_const_260 = Integer(260); _sage_const_262 = Integer(262); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_205 = Integer(205); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_276 = Integer(276); _sage_const_274 = Integer(274); _sage_const_59 = Integer(59); _sage_const_58 = Integer(58); _sage_const_57 = Integer(57); _sage_const_56 = Integer(56); _sage_const_55 = Integer(55); _sage_const_54 = Integer(54); _sage_const_53 = Integer(53); _sage_const_52 = Integer(52); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_73 = Integer(73); _sage_const_140 = Integer(140); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_71 = Integer(71); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_283 = Integer(283); _sage_const_285 = Integer(285)## This file (lowestDegreePoly.sagetex.sage) was *autogenerated* from lowestDegreePoly.tex with sagetex.sty version 2019/01/09 v3.2.
import sagetex
_st_ = sagetex.SageTeXProcessor('lowestDegreePoly', version='2019/01/09 v3.2', version_check=True)
_st_.current_tex_line = _sage_const_30 
_st_.blockbegin()
try:
 def maybeMakeNegative(natural):
     integer = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 ) * natural
     return integer
 
 def generateFactorEasy():
     a = _sage_const_1 
     b = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_6 ))
     return [a, b]
 
 def generateFactorHard():
     a = ZZ.random_element(_sage_const_1 , _sage_const_4 )
     b = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_6 ))
     while gcd(a, b) > _sage_const_1 :
         a = ZZ.random_element(_sage_const_1 , _sage_const_4 )
         b = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_6 ))
     return [a, b]
 
 def generateAllFactorsEasy():
     factor1 = generateFactorEasy()
     factor2 = generateFactorEasy()
     factor3 = generateFactorEasy()
     return [factor1, factor2, factor3]
 
 def generateAllFactorsHard():
     factor1 = generateFactorHard()
     factor2 = generateFactorHard()
     factor3 = generateFactorHard()
     return [factor1, factor2, factor3]
 
 def generateZeros(factor1, factor2, factor3):
     zero1 = factor1[_sage_const_1 ]/factor1[_sage_const_0 ]
     zero2 = factor2[_sage_const_1 ]/factor2[_sage_const_0 ]
     zero3 = factor3[_sage_const_1 ]/factor3[_sage_const_0 ]
     return [zero1, zero2, zero3]
 
 def generatePolynomial(factor1, factor2, factor3):
     f10, f11 = factor1
     f20, f21 = factor2
     f30, f31 = factor3
     #
     a = f10*f20*f30
     b = -f11*f20*f30 - f10*f21*f30 - f10*f20*f31
     c = f11*f20*f31 + f10*f21*f31 + f11*f21*f30
     d = -f11*f21*f31
     #
     coefficients = [a, b, c, d]
     return coefficients
 
 ##### QUESTION 13 #####
 factor131, factor132, factor133 = generateAllFactorsEasy()
 zero131, zero132, zero133 = generateZeros(factor131, factor132, factor133)
 coefficients13 = generatePolynomial(factor131, factor132, factor133)
 
 ##### QUESTION 14 #####
 factor141, factor142, factor143 = generateAllFactorsEasy()
 zero141, zero142, zero143 = generateZeros(factor141, factor142, factor143)
 coefficients14 = generatePolynomial(factor141, factor142, factor143)
 
 ##### QUESTION 15 #####
 factor151, factor152, factor153 = generateAllFactorsHard()
 zero151, zero152, zero153 = generateZeros(factor151, factor152, factor153)
 coefficients15 = generatePolynomial(factor151, factor152, factor153)
 
 ##### QUESTION 16 #####
 factor161, factor162, factor163 = generateAllFactorsHard()
 zero161, zero162, zero163 = generateZeros(factor161, factor162, factor163)
 coefficients16 = generatePolynomial(factor161, factor162, factor163)
except:
 _st_.goboom(_sage_const_98 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_0 , latex(zero131))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_1 , latex(zero132))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_2 , latex(zero133))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_106 
 _st_.inline(_sage_const_3 , latex(coefficients13[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_106 )
try:
 _st_.current_tex_line = _sage_const_106 
 _st_.inline(_sage_const_4 , latex(coefficients13[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_106 )
try:
 _st_.current_tex_line = _sage_const_106 
 _st_.inline(_sage_const_5 , latex(coefficients13[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_106 )
try:
 _st_.current_tex_line = _sage_const_106 
 _st_.inline(_sage_const_6 , latex(coefficients13[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_106 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_7 , latex(zero141))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_8 , latex(zero142))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_9 , latex(zero143))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_10 , latex(coefficients14[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_11 , latex(coefficients14[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_12 , latex(coefficients14[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_13 , latex(coefficients14[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.inline(_sage_const_14 , latex(zero151))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.inline(_sage_const_15 , latex(zero152))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.inline(_sage_const_16 , latex(zero153))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_17 , latex(coefficients15[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_18 , latex(coefficients15[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_19 , latex(coefficients15[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_20 , latex(coefficients15[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_21 , latex(zero161))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_22 , latex(zero162))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_23 , latex(zero163))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_24 , latex(coefficients16[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_25 , latex(coefficients16[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_26 , latex(coefficients16[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_27 , latex(coefficients16[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_140 )
_st_.current_tex_line = _sage_const_205 
_st_.blockbegin()
try:
 def constructLowestDegreePolyIrrational(b):
     a = ZZ.random_element(_sage_const_2 , _sage_const_8 )
     n = ZZ.random_element(-_sage_const_5 , _sage_const_5 )
     d = ZZ.random_element(_sage_const_2 , _sage_const_8 )
     while gcd(abs(n), d) > _sage_const_1  or n == _sage_const_0 :
         n = ZZ.random_element(-_sage_const_5 , _sage_const_5 )
         d = ZZ.random_element(_sage_const_2 , _sage_const_8 )
     coefficients = [d, -_sage_const_2 *b*d-n, _sage_const_2 *b*n + b**_sage_const_2 *d - a*d, -b**_sage_const_2 *n+a*n]
     zeros = [b, sqrt(a), n/d]
     return [coefficients, zeros]
 
 def constructLowestDegreePolyComplex(a):
     b = ZZ.random_element(_sage_const_2 , _sage_const_8 )
     n = ZZ.random_element(-_sage_const_5 , _sage_const_5 )
     d = ZZ.random_element(_sage_const_2 , _sage_const_8 )
     while gcd(abs(n), d) > _sage_const_1  or n == _sage_const_0 :
         n = ZZ.random_element(-_sage_const_5 , _sage_const_5 )
         d = ZZ.random_element(_sage_const_2 , _sage_const_8 )
     coefficients = [d, -n-_sage_const_2 *a*d, _sage_const_2 *a*n+a**_sage_const_2 *d+b**_sage_const_2 *d, -a**_sage_const_2 *n-b**_sage_const_2 *n]
     zeros = [a, b, n/d]
     hintValues = [n, d]
     return [coefficients, zeros, hintValues]
 #
 irrationalB = ZZ.random_element(_sage_const_2 , _sage_const_6 )
 complexA = ZZ.random_element(_sage_const_2 , _sage_const_6 )
 #
 # Q6 - Irrational Roots with b=0
 coefficientsQ6, zerosQ6 = constructLowestDegreePolyIrrational(_sage_const_0 )
 # Q7 - Irrational Roots with b neq 0
 coefficientsQ7, zerosQ7 = constructLowestDegreePolyIrrational(irrationalB)
 # Q8 - Complex Roots with a=0
 coefficientsQ8, zerosQ8, hintValuesQ8 = constructLowestDegreePolyComplex(_sage_const_0 )
 # Q9 - Complex Roots with a neq 0
 coefficientsQ9, zerosQ9, hintValuesQ9 = constructLowestDegreePolyComplex(complexA)
except:
 _st_.goboom(_sage_const_240 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_246 
 _st_.inline(_sage_const_28 , latex(zerosQ6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_246 )
try:
 _st_.current_tex_line = _sage_const_246 
 _st_.inline(_sage_const_29 , latex(zerosQ6[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_246 )
try:
 _st_.current_tex_line = _sage_const_248 
 _st_.inline(_sage_const_30 , latex(coefficientsQ6[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_248 )
try:
 _st_.current_tex_line = _sage_const_248 
 _st_.inline(_sage_const_31 , latex(coefficientsQ6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_248 )
try:
 _st_.current_tex_line = _sage_const_248 
 _st_.inline(_sage_const_32 , latex(coefficientsQ6[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_248 )
try:
 _st_.current_tex_line = _sage_const_248 
 _st_.inline(_sage_const_33 , latex(coefficientsQ6[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_248 )
try:
 _st_.current_tex_line = _sage_const_251 
 _st_.inline(_sage_const_34 , latex(zerosQ6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_251 )
try:
 _st_.current_tex_line = _sage_const_251 
 _st_.inline(_sage_const_35 , latex(zerosQ6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_251 )
try:
 _st_.current_tex_line = _sage_const_251 
 _st_.inline(_sage_const_36 , latex(zerosQ6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_251 )
try:
 _st_.current_tex_line = _sage_const_251 
 _st_.inline(_sage_const_37 , latex(zerosQ6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_251 )
try:
 _st_.current_tex_line = _sage_const_260 
 _st_.inline(_sage_const_38 , latex(zerosQ7[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_260 )
try:
 _st_.current_tex_line = _sage_const_260 
 _st_.inline(_sage_const_39 , latex(zerosQ7[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_260 )
try:
 _st_.current_tex_line = _sage_const_260 
 _st_.inline(_sage_const_40 , latex(zerosQ7[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_260 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_41 , latex(coefficientsQ7[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_42 , latex(coefficientsQ7[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_43 , latex(coefficientsQ7[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_44 , latex(coefficientsQ7[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_274 
 _st_.inline(_sage_const_45 , latex(zerosQ8[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_274 )
try:
 _st_.current_tex_line = _sage_const_274 
 _st_.inline(_sage_const_46 , latex(zerosQ8[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_274 )
try:
 _st_.current_tex_line = _sage_const_276 
 _st_.inline(_sage_const_47 , latex(coefficientsQ8[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_276 )
try:
 _st_.current_tex_line = _sage_const_276 
 _st_.inline(_sage_const_48 , latex(coefficientsQ8[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_276 )
try:
 _st_.current_tex_line = _sage_const_276 
 _st_.inline(_sage_const_49 , latex(coefficientsQ8[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_276 )
try:
 _st_.current_tex_line = _sage_const_276 
 _st_.inline(_sage_const_50 , latex(coefficientsQ8[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_276 )
try:
 _st_.current_tex_line = _sage_const_283 
 _st_.inline(_sage_const_51 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_283 )
try:
 _st_.current_tex_line = _sage_const_283 
 _st_.inline(_sage_const_52 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_283 )
try:
 _st_.current_tex_line = _sage_const_283 
 _st_.inline(_sage_const_53 , latex(zerosQ9[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_283 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_54 , latex(coefficientsQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_55 , latex(coefficientsQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_56 , latex(coefficientsQ9[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_57 , latex(coefficientsQ9[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_290 
 _st_.inline(_sage_const_58 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_290 )
try:
 _st_.current_tex_line = _sage_const_290 
 _st_.inline(_sage_const_59 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_290 )
try:
 _st_.current_tex_line = _sage_const_290 
 _st_.inline(_sage_const_60 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_290 )
try:
 _st_.current_tex_line = _sage_const_290 
 _st_.inline(_sage_const_61 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_290 )
try:
 _st_.current_tex_line = _sage_const_290 
 _st_.inline(_sage_const_62 , latex(hintValuesQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_290 )
try:
 _st_.current_tex_line = _sage_const_290 
 _st_.inline(_sage_const_63 , latex(hintValuesQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_290 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_64 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_65 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_66 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_67 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_68 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_69 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_70 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_71 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_72 , latex(hintValuesQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.inline(_sage_const_73 , latex(hintValuesQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_296 
 _st_.inline(_sage_const_74 , latex(_sage_const_2 *zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_296 )
try:
 _st_.current_tex_line = _sage_const_296 
 _st_.inline(_sage_const_75 , latex(zerosQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_296 )
try:
 _st_.current_tex_line = _sage_const_296 
 _st_.inline(_sage_const_76 , latex(zerosQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_296 )
try:
 _st_.current_tex_line = _sage_const_296 
 _st_.inline(_sage_const_77 , latex(hintValuesQ9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_296 )
try:
 _st_.current_tex_line = _sage_const_296 
 _st_.inline(_sage_const_78 , latex(hintValuesQ9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_296 )
_st_.endofdoc()

