## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file solveCompoundInequalities.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_240 = Integer(240); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_136 = Integer(136); _sage_const_132 = Integer(132); _sage_const_138 = Integer(138); _sage_const_156 = Integer(156); _sage_const_173 = Integer(173); _sage_const_158 = Integer(158); _sage_const_219 = Integer(219); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_238 = Integer(238); _sage_const_162 = Integer(162); _sage_const_142 = Integer(142); _sage_const_225 = Integer(225); _sage_const_223 = Integer(223)## This file (solveCompoundInequalities.sagetex.sage) was *autogenerated* from solveCompoundInequalities.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveCompoundInequalities', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_30 
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
 
 ######## QUESTION 1 - Forces $(-\infty, a) \text{ or } (b, \infty)$ solution ##########
 coefficients1A = createCoefficientsHard()
 solution1A = createIntervalSolutionHard(coefficients1A, "less")
 while solution1A[_sage_const_1 ] == "Left":
     coefficients1A = createCoefficientsHard()
     solution1A = createIntervalSolutionHard(coefficients1A, "less")
 n1A0, n1A1, n1A2, n1A3, d1A0, d1A1, d1A2, d1A3 = coefficients1A
 displayLeftFactor1A = n1A0/d1A0+n1A1/d1A1*x
 displayRightFactor1A = n1A2/d1A2*x+n1A3/d1A3
 
 coefficients1B = createCoefficientsHard()
 solution1B = createIntervalSolutionHard(coefficients1B, "greater")
 while solution1B[_sage_const_1 ] == "Right":
     coefficients1B = createCoefficientsHard()
     solution1B = createIntervalSolutionHard(coefficients1B, "greater")
 n1B0, n1B1, n1B2, n1B3, d1B0, d1B1, d1B2, d1B3 = coefficients1B
 displayLeftFactor1B = n1B0/d1B0+n1B1/d1B1*x
 displayRightFactor1B = n1B2/d1B2*x+n1B3/d1B3
 
 
 ######## QUESTION 2 - Forces $(-\infty, a] \text{ or } [b, \infty)$ solution ##########
 coefficients2A = createCoefficientsHard()
 solution2A = createIntervalSolutionHard(coefficients2A, "leq")
 while solution2A[_sage_const_1 ] == "Left":
     coefficients2A = createCoefficientsHard()
     solution2A = createIntervalSolutionHard(coefficients2A, "leq")
 n2A0, n2A1, n2A2, n2A3, d2A0, d2A1, d2A2, d2A3 = coefficients2A
 displayLeftFactor2A = n2A0/d2A0+n2A1/d2A1*x
 displayRightFactor2A = n2A2/d2A2*x+n2A3/d2A3
 
 coefficients2B = createCoefficientsHard()
 solution2B = createIntervalSolutionHard(coefficients2B, "geq")
 while solution2B[_sage_const_1 ] == "Right":
     coefficients2B = createCoefficientsHard()
     solution2B = createIntervalSolutionHard(coefficients2B, "geq")
 n2B0, n2B1, n2B2, n2B3, d2B0, d2B1, d2B2, d2B3 = coefficients2B
 displayLeftFactor2B = n2B0/d2B0+n2B1/d2B1*x
 displayRightFactor2B = n2B2/d2B2*x+n2B3/d2B3
 
except:
 _st_.goboom(_sage_const_132 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_0 , latex(displayLeftFactor1A))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_1 , latex(displayRightFactor1A))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_2 , latex(displayLeftFactor1B))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_3 , latex(displayRightFactor1B))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_4 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_5 , latex(solution1A[_sage_const_0 ][_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_6 , latex(solution1B[_sage_const_0 ][_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_7 , latex(Infinity))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_8 , latex(displayLeftFactor2A))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_9 , latex(displayRightFactor2A))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_10 , latex(displayLeftFactor2B))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_11 , latex(displayRightFactor2B))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_158 
 _st_.inline(_sage_const_12 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_158 )
try:
 _st_.current_tex_line = _sage_const_158 
 _st_.inline(_sage_const_13 , latex(solution2A[_sage_const_0 ][_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_158 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_14 , latex(solution2B[_sage_const_0 ][_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_15 , latex(Infinity))
except:
 _st_.goboom(_sage_const_162 )
_st_.current_tex_line = _sage_const_173 
_st_.blockbegin()
try:
 x = var('x')
 ############
 def createAllCoefficientsAndEndpoints():
     coefficients = [_sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 ]
     coefficients[_sage_const_0 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     coefficients[_sage_const_1 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     coefficients[_sage_const_3 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     coefficients[_sage_const_4 ] = ZZ.random_element(_sage_const_3 , _sage_const_9 )
     coefficients[_sage_const_5 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     coefficients[_sage_const_6 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     # Need 1, 4, and 6 set before 2
     coefficients[_sage_const_2 ] = max(coefficients[_sage_const_1 ], coefficients[_sage_const_6 ])*coefficients[_sage_const_4 ] + ZZ.random_element(_sage_const_2 , _sage_const_5 )
     # This flips the inequalities
     smallerEndpoint = float((-coefficients[_sage_const_0 ]*coefficients[_sage_const_4 ] + coefficients[_sage_const_3 ]) / (coefficients[_sage_const_1 ]*coefficients[_sage_const_4 ] - coefficients[_sage_const_2 ]))
     largerEndpoint = float((coefficients[_sage_const_4 ]*coefficients[_sage_const_5 ] - coefficients[_sage_const_3 ]) / (coefficients[_sage_const_2 ] - coefficients[_sage_const_4 ] * coefficients[_sage_const_6 ]))
     #####
     # Makes sure we get a solution interval
     while  (largerEndpoint < smallerEndpoint) or (largerEndpoint == smallerEndpoint):
         coefficients[_sage_const_0 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
         coefficients[_sage_const_1 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
         coefficients[_sage_const_3 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
         coefficients[_sage_const_4 ] = ZZ.random_element(_sage_const_3 , _sage_const_9 )
         coefficients[_sage_const_5 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
         coefficients[_sage_const_6 ] = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
         # Need 1, 4, and 6 set before 2
         coefficients[_sage_const_2 ] = max(coefficients[_sage_const_1 ], coefficients[_sage_const_6 ])*coefficients[_sage_const_4 ] + ZZ.random_element(_sage_const_2 , _sage_const_5 )
         # This flips the inequalities
         smallerEndpoint = float((-coefficients[_sage_const_0 ]*coefficients[_sage_const_4 ] + coefficients[_sage_const_3 ]) / (coefficients[_sage_const_1 ]*coefficients[_sage_const_4 ] - coefficients[_sage_const_2 ]))
         largerEndpoint = float((coefficients[_sage_const_4 ]*coefficients[_sage_const_5 ] - coefficients[_sage_const_3 ]) / (coefficients[_sage_const_2 ] - coefficients[_sage_const_4 ] * coefficients[_sage_const_6 ]))
     #####
     a, b, c, d, e, f, g = coefficients
     return [coefficients, smallerEndpoint, largerEndpoint]
 
 def constructInequalitiesToDisplay(coefficients):
     c0, c1, c2, c3, c4, c5, c6 = coefficients
     andInequalityLeft = c0 + c1*x
     andInequalityMiddle = (c2*x + c3)/c4
     andInequalityRight = c5 + c6*x
     return [andInequalityLeft, andInequalityMiddle, andInequalityRight]
 ##############
 coefficients3, smallerEndpoint3, largerEndpoint3 = createAllCoefficientsAndEndpoints()
 andInequalityLeft3, andInequalityMiddle3, andInequalityRight3 = constructInequalitiesToDisplay(coefficients3)
 
 coefficients4, smallerEndpoint4, largerEndpoint4 = createAllCoefficientsAndEndpoints()
 andInequalityLeft4, andInequalityMiddle4, andInequalityRight4 = constructInequalitiesToDisplay(coefficients4)
except:
 _st_.goboom(_sage_const_219 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_16 , latex(andInequalityLeft3))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_17 , latex(andInequalityMiddle3))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_18 , latex(andInequalityRight3))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_225 
 _st_.inline(_sage_const_19 , latex(smallerEndpoint3))
except:
 _st_.goboom(_sage_const_225 )
try:
 _st_.current_tex_line = _sage_const_225 
 _st_.inline(_sage_const_20 , latex(largerEndpoint3))
except:
 _st_.goboom(_sage_const_225 )
try:
 _st_.current_tex_line = _sage_const_238 
 _st_.inline(_sage_const_21 , latex(andInequalityLeft4))
except:
 _st_.goboom(_sage_const_238 )
try:
 _st_.current_tex_line = _sage_const_238 
 _st_.inline(_sage_const_22 , latex(andInequalityMiddle4))
except:
 _st_.goboom(_sage_const_238 )
try:
 _st_.current_tex_line = _sage_const_238 
 _st_.inline(_sage_const_23 , latex(andInequalityRight4))
except:
 _st_.goboom(_sage_const_238 )
try:
 _st_.current_tex_line = _sage_const_240 
 _st_.inline(_sage_const_24 , latex(smallerEndpoint4))
except:
 _st_.goboom(_sage_const_240 )
try:
 _st_.current_tex_line = _sage_const_240 
 _st_.inline(_sage_const_25 , latex(largerEndpoint4))
except:
 _st_.goboom(_sage_const_240 )
_st_.endofdoc()
