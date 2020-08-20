## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file solveLinearInequalities.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_285 = Integer(285); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_298 = Integer(298); _sage_const_18 = Integer(18); _sage_const_130 = Integer(130); _sage_const_113 = Integer(113); _sage_const_110 = Integer(110); _sage_const_115 = Integer(115); _sage_const_156 = Integer(156); _sage_const_154 = Integer(154); _sage_const_311 = Integer(311); _sage_const_313 = Integer(313); _sage_const_274 = Integer(274); _sage_const_272 = Integer(272); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_32 = Integer(32); _sage_const_166 = Integer(166); _sage_const_128 = Integer(128); _sage_const_287 = Integer(287); _sage_const_269 = Integer(269); _sage_const_141 = Integer(141); _sage_const_143 = Integer(143); _sage_const_300 = Integer(300)## This file (solveLinearInequalities.sagetex.sage) was *autogenerated* from solveLinearInequalities.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveLinearInequalities', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_32 
_st_.blockbegin()
try:
 x = var('x')
 ##################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def createCoefficientsEasy():
     coefficients = [_sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 ]
     while (coefficients[_sage_const_1 ] == coefficients[_sage_const_2 ]):
         coefficients[_sage_const_0 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
         coefficients[_sage_const_1 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
         coefficients[_sage_const_2 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
         coefficients[_sage_const_3 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
     return coefficients
 
 def createIntervalSolutionEasy(coefficients, direction):
     a, b, c, d = coefficients
     equation = (a+b*x) - (c*x+d)
     endpoint = round(float(solve(equation, x)[_sage_const_0 ].rhs()), _sage_const_3 )
     nearEndpoint = endpoint - _sage_const_1 
     checkNearby = float( float(a)+float(b)*nearEndpoint - (float(c)*nearEndpoint+float(d)) )
     # Checks direction of inequality
     if direction == "less" or direction == "leq":
         if (checkNearby < _sage_const_0 ):
             interval = [-oo, endpoint]
             whichSideFloat = "Right"
         else:
             interval = [endpoint, oo]
             whichSideFloat = "Left"
     elif direction == "greater" or direction == "geq":
         if (checkNearby > _sage_const_0 ):
             interval = [-oo, endpoint]
             whichSideFloat = "Right"
         else:
             interval = [endpoint, oo]
             whichSideFloat = "Left"
     else:
         interval = [_sage_const_0 , _sage_const_0 ]
         whichSideFloat = "Neither"
     return [interval, whichSideFloat]
 ######### QUESTION 3 - FORCED $[, \infty)$ Solution #########
 coefficients3 = createCoefficientsEasy()
 solution3 = createIntervalSolutionEasy(coefficients3, "leq")
 while solution3[_sage_const_1 ] == "Right":
     coefficients3 = createCoefficientsEasy()
     solution3 = createIntervalSolutionEasy(coefficients3, "leq")
 displayLeftFactor3 = coefficients3[_sage_const_0 ] + coefficients3[_sage_const_1 ] * x
 displayRightFactor3 = coefficients3[_sage_const_2 ] * x + coefficients3[_sage_const_3 ]
 
 ######### QUESTION 4 - FORCED $(-\infty, ]$ Solution #########
 coefficients4 = createCoefficientsEasy()
 solution4 = createIntervalSolutionEasy(coefficients4, "geq")
 while solution4[_sage_const_1 ] == "Left":
     coefficients4 = createCoefficientsEasy()
     solution4 = createIntervalSolutionEasy(coefficients4, "geq")
 displayLeftFactor4 = coefficients4[_sage_const_0 ] + coefficients4[_sage_const_1 ] * x
 displayRightFactor4 = coefficients4[_sage_const_2 ] * x + coefficients4[_sage_const_3 ]
 
 ######### QUESTION 5 - FORCED $(-\infty, )$ Solution #########
 coefficients5 = createCoefficientsEasy()
 solution5 = createIntervalSolutionEasy(coefficients5, "less")
 while solution5[_sage_const_1 ] == "Left":
     coefficients5 = createCoefficientsEasy()
     solution5 = createIntervalSolutionEasy(coefficients5, "less")
 displayLeftFactor5 = coefficients5[_sage_const_0 ] + coefficients5[_sage_const_1 ] * x
 displayRightFactor5 = coefficients5[_sage_const_2 ] * x + coefficients5[_sage_const_3 ]
 
 ######### QUESTION 6 - FORCED $(, \infty)$ Solution #########
 direction6 = "greater"
 coefficients6 = createCoefficientsEasy()
 solution6 = createIntervalSolutionEasy(coefficients6, "greater")
 while solution6[_sage_const_1 ] == "Right":
     coefficients6 = createCoefficientsEasy()
     solution6 = createIntervalSolutionEasy(coefficients6, "greater")
 displayLeftFactor6 = coefficients6[_sage_const_0 ] + coefficients6[_sage_const_1 ] * x
 displayRightFactor6 = coefficients6[_sage_const_2 ] * x + coefficients6[_sage_const_3 ]
except:
 _st_.goboom(_sage_const_110 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_0 , latex(displayLeftFactor3))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_1 , latex(displayRightFactor3))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_115 
 _st_.inline(_sage_const_2 , latex(solution3[_sage_const_0 ][_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_115 )
try:
 _st_.current_tex_line = _sage_const_115 
 _st_.inline(_sage_const_3 , latex(Infinity))
except:
 _st_.goboom(_sage_const_115 )
try:
 _st_.current_tex_line = _sage_const_128 
 _st_.inline(_sage_const_4 , latex(displayLeftFactor4))
except:
 _st_.goboom(_sage_const_128 )
try:
 _st_.current_tex_line = _sage_const_128 
 _st_.inline(_sage_const_5 , latex(displayRightFactor4))
except:
 _st_.goboom(_sage_const_128 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_6 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_7 , latex(solution4[_sage_const_0 ][_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_8 , latex(displayLeftFactor5))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_9 , latex(displayRightFactor5))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_143 
 _st_.inline(_sage_const_10 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_143 )
try:
 _st_.current_tex_line = _sage_const_143 
 _st_.inline(_sage_const_11 , latex(solution5[_sage_const_0 ][_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_143 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_12 , latex(displayLeftFactor6))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_13 , latex(displayRightFactor6))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_14 , latex(solution6[_sage_const_0 ][_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_15 , latex(Infinity))
except:
 _st_.goboom(_sage_const_156 )
_st_.current_tex_line = _sage_const_166 
_st_.blockbegin()
try:
 import random
 x = var('x')
 ##################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def createNumerators():
     numerators = [_sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 ]
     numerators[_sage_const_0 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
     numerators[_sage_const_1 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
     numerators[_sage_const_2 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
     numerators[_sage_const_3 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_11 ))
     return numerators
 
 def createDenominators():
     listOfDenominators= range(_sage_const_2 , _sage_const_10 )
     a, b, c, d = random.sample(listOfDenominators, _sage_const_4 )
     return [Integer(a), Integer(b), Integer(c), Integer(d)]
 
 def createCoefficientsHard():
     n0, n1, n2, n3 = createNumerators()
     d0, d1, d2, d3 = createDenominators()
     left = (n0/d0)+(n1/d1)*x
     right = (n2/d2)*x+(n3/d3)
     oneSolutionCheck = (n1/d1) - (n2/d2)
     while oneSolutionCheck == _sage_const_0 :
         n0, n1, n2, n3 = createNumerators()
         d0, d1, d2, d3 = createDenominators()
         left = (n0/d0)+(n1/d1)*x
         right = (n2/d2)*x+(n3/d3)
         oneSolutionCheck = (n1/d1) - (n2/d2)
     return [n0, n1, n2, n3, d0, d1, d2, d3]
 
 def createIntervalSolutionHard(coefficients, direction):
     n0, n1, n2, n3, d0, d1, d2, d3 = coefficients
     left = (n0/d0)+(n1/d1)*x
     right = (n2/d2)*x+(n3/d3)
     # Checks which direction the interval points
     endpoint = round(float(solve(left-right, x)[_sage_const_0 ].rhs() ), _sage_const_3 )
     nearEndpoint = endpoint - _sage_const_1 
     checkNearby = float(float(n0/d0)+float(n1/d1)*nearEndpoint - (float(n2/d2)*nearEndpoint+float(n3/d3)))
     if direction == "leq" or direction == "less":
         if (checkNearby < _sage_const_0 ):
             interval = [-oo, endpoint]
             whichSideFloat = "Right"
         else:
             interval = [endpoint, oo]
             whichSideFloat = "Left"
     elif direction == "geq" or direction == "greater":
         if (checkNearby > _sage_const_0 ):
             interval = [-oo, endpoint]
             whichSideFloat = "Right"
         else:
             interval = [endpoint, oo]
             whichSideFloat = "Left"
     else:
         interval = [_sage_const_0 , _sage_const_0 ]
         whichSideFloat = "Neither"
     return [interval, whichSideFloat]
 
 ######## QUESTION 7 - Forces $(a, \infty)$ solution ##########
 coefficients7 = createCoefficientsHard()
 solution7 = createIntervalSolutionHard(coefficients7, "less")
 while solution7[_sage_const_1 ] == "Right":
     coefficients7 = createCoefficientsHard()
     solution7 = createIntervalSolutionHard(coefficients7, "less")
 n70, n71, n72, n73, d70, d71, d72, d73 = coefficients7
 displayLeftFactor7 = n70/d70+n71/d71*x
 displayRightFactor7 = n72/d72*x+n73/d73
 
 ######## QUESTION 8 - Forces $(a, \infty)$ solution ##########
 coefficients8 = createCoefficientsHard()
 solution8 = createIntervalSolutionHard(coefficients8, "greater")
 while solution8[_sage_const_1 ] == "Right":
     coefficients8 = createCoefficientsHard()
     solution8 = createIntervalSolutionHard(coefficients8, "greater")
 n80, n81, n82, n83, d80, d81, d82, d83 = coefficients8
 displayLeftFactor8 = n80/d80+n81/d81*x
 displayRightFactor8 = n82/d82*x+n83/d83
 
 ######## QUESTION 9 - Forces $(-\infty, a)$ solution ##########
 coefficients9 = createCoefficientsHard()
 solution9 = createIntervalSolutionHard(coefficients9, "leq")
 while solution9[_sage_const_1 ] == "Left":
     coefficients9 = createCoefficientsHard()
     solution9 = createIntervalSolutionHard(coefficients9, "leq")
 n90, n91, n92, n93, d90, d91, d92, d93 = coefficients9
 displayLeftFactor9 = n90/d90+n91/d91*x
 displayRightFactor9 = n92/d92*x+n93/d93
 
 ######## QUESTION 10 - Forces $(-\infty, a)$ solution ##########
 coefficients10 = createCoefficientsHard()
 solution10 = createIntervalSolutionHard(coefficients10, "geq")
 while solution10[_sage_const_1 ] == "Left":
     coefficients10 = createCoefficientsHard()
     solution10 = createIntervalSolutionHard(coefficients10, "geq")
 n100, n101, n102, n103, d100, d101, d102, d103 = coefficients10
 displayLeftFactor10 = n100/d100+n101/d101*x
 displayRightFactor10 = n102/d102*x+n103/d103
 
except:
 _st_.goboom(_sage_const_269 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_272 
 _st_.inline(_sage_const_16 , latex(displayLeftFactor7))
except:
 _st_.goboom(_sage_const_272 )
try:
 _st_.current_tex_line = _sage_const_272 
 _st_.inline(_sage_const_17 , latex(displayRightFactor7))
except:
 _st_.goboom(_sage_const_272 )
try:
 _st_.current_tex_line = _sage_const_274 
 _st_.inline(_sage_const_18 , latex(solution7[_sage_const_0 ][_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_274 )
try:
 _st_.current_tex_line = _sage_const_274 
 _st_.inline(_sage_const_19 , latex(Infinity))
except:
 _st_.goboom(_sage_const_274 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_20 , latex(displayLeftFactor8))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_21 , latex(displayRightFactor8))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_287 
 _st_.inline(_sage_const_22 , latex(solution8[_sage_const_0 ][_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_287 )
try:
 _st_.current_tex_line = _sage_const_287 
 _st_.inline(_sage_const_23 , latex(Infinity))
except:
 _st_.goboom(_sage_const_287 )
try:
 _st_.current_tex_line = _sage_const_298 
 _st_.inline(_sage_const_24 , latex(displayLeftFactor9))
except:
 _st_.goboom(_sage_const_298 )
try:
 _st_.current_tex_line = _sage_const_298 
 _st_.inline(_sage_const_25 , latex(displayRightFactor9))
except:
 _st_.goboom(_sage_const_298 )
try:
 _st_.current_tex_line = _sage_const_300 
 _st_.inline(_sage_const_26 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_300 )
try:
 _st_.current_tex_line = _sage_const_300 
 _st_.inline(_sage_const_27 , latex(solution9[_sage_const_0 ][_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_300 )
try:
 _st_.current_tex_line = _sage_const_311 
 _st_.inline(_sage_const_28 , latex(displayLeftFactor10))
except:
 _st_.goboom(_sage_const_311 )
try:
 _st_.current_tex_line = _sage_const_311 
 _st_.inline(_sage_const_29 , latex(displayRightFactor10))
except:
 _st_.goboom(_sage_const_311 )
try:
 _st_.current_tex_line = _sage_const_313 
 _st_.inline(_sage_const_30 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_313 )
try:
 _st_.current_tex_line = _sage_const_313 
 _st_.inline(_sage_const_31 , latex(solution10[_sage_const_0 ][_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_313 )
_st_.endofdoc()

