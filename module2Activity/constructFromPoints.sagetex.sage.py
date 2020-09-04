## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file constructFromPoints.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_32 = Integer(32); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_9 = Integer(9); _sage_const_0 = Integer(0); _sage_const_79 = Integer(79); _sage_const_83 = Integer(83); _sage_const_3 = Integer(3); _sage_const_85 = Integer(85); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_94 = Integer(94); _sage_const_6 = Integer(6); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_96 = Integer(96); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_101 = Integer(101); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_103 = Integer(103); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_108 = Integer(108); _sage_const_160 = Integer(160); _sage_const_167 = Integer(167); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_169 = Integer(169); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_179 = Integer(179); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_181 = Integer(181); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_187 = Integer(187); _sage_const_30 = Integer(30); _sage_const_31 = Integer(31); _sage_const_33 = Integer(33); _sage_const_189 = Integer(189); _sage_const_34 = Integer(34); _sage_const_35 = Integer(35); _sage_const_198 = Integer(198); _sage_const_36 = Integer(36); _sage_const_37 = Integer(37); _sage_const_38 = Integer(38); _sage_const_39 = Integer(39); _sage_const_200 = Integer(200); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41)## This file (constructFromPoints.sagetex.sage) was *autogenerated* from constructFromPoints.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('constructFromPoints', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_32 
_st_.blockbegin()
try:
 x = var('x')
 
 #################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def generatePoints():
     pointOne = [maybeMakeNegative(ZZ.random_element(_sage_const_2 ,_sage_const_9 )), maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))]
     pointTwo = [maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 )), maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))]
     # Makes sure coordinates are distinct and not a vertical/horizontal line
     while (pointOne[_sage_const_0 ]==pointTwo[_sage_const_0 ] or pointOne[_sage_const_1 ]==pointTwo[_sage_const_1 ]):
         pointOne = [maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 )), maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))]
         pointTwo = [maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 )), maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))]
     return [pointOne, pointTwo]
 
 def generateSolution(problem):
     pointOne, pointTwo = problem
     numerator = pointTwo[_sage_const_1 ]-pointOne[_sage_const_1 ]
     denominator = pointTwo[_sage_const_0 ]-pointOne[_sage_const_0 ]
     slope = float(numerator/denominator)
     yInt = float(pointTwo[_sage_const_1 ]-slope*pointTwo[_sage_const_0 ])
     slope = slope
     #print "Slope %s and y-Intercept %s" %(slope, yInt)
     return [slope, yInt]
 
 ######## END OF DEFINITIONS #########
 
 ##### QUESTION 1 #####
 points1 = generatePoints()
 pointOne1, pointTwo1 = points1
 solution1 = generateSolution(points1)
 equation1 = solution1[_sage_const_0 ]*x + solution1[_sage_const_1 ]
 
 ##### QUESTION 2 #####
 points2 = generatePoints()
 pointOne2, pointTwo2 = points2
 solution2 = generateSolution(points2)
 equation2 = solution2[_sage_const_0 ]*x + solution2[_sage_const_1 ]
 
 ##### QUESTION 3 #####
 points3 = generatePoints()
 pointOne3, pointTwo3 = points3
 solution3 = generateSolution(points3)
 equation3 = solution3[_sage_const_0 ]*x + solution3[_sage_const_1 ]
except:
 _st_.goboom(_sage_const_79 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_0 , latex(pointOne1[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_1 , latex(pointOne1[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_2 , latex(pointTwo1[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_3 , latex(pointTwo1[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_85 
 _st_.inline(_sage_const_4 , latex(solution1[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_85 )
try:
 _st_.current_tex_line = _sage_const_85 
 _st_.inline(_sage_const_5 , latex(solution1[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_85 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.inline(_sage_const_6 , latex(pointOne2[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.inline(_sage_const_7 , latex(pointOne2[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.inline(_sage_const_8 , latex(pointTwo2[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.inline(_sage_const_9 , latex(pointTwo2[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_10 , latex(solution2[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_11 , latex(solution2[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_12 , latex(pointOne3[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_13 , latex(pointOne3[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_14 , latex(pointTwo3[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_15 , latex(pointTwo3[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_16 , latex(solution3[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_103 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_17 , latex(solution3[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_103 )
_st_.current_tex_line = _sage_const_108 
_st_.blockbegin()
try:
 x, y = var('x, y')
 
 #################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def generateProblemAndSolution(lineType):
     if lineType == _sage_const_0 :
         point = [maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_11 )), maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_11 ))]
         aCoeff = ZZ.random_element(_sage_const_3 , _sage_const_10 )
         bCoeff = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_10 ))
         cCoeff = ZZ.random_element(_sage_const_3 , _sage_const_16 )
         # Slope and y-intercept
         slope = float(-aCoeff/bCoeff)
         yInt = float(point[_sage_const_1 ]-slope*point[_sage_const_0 ])
         return [[slope, yInt], point, [aCoeff, bCoeff, cCoeff]]
     else:
         point = [maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_11 )), maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_11 ))]
         aCoeff = ZZ.random_element(_sage_const_3 , _sage_const_10 )
         bCoeff = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_10 ))
         cCoeff = ZZ.random_element(_sage_const_3 , _sage_const_16 )
         # Slope and y-intercept
         slope = float(bCoeff/aCoeff)
         yInt = float(point[_sage_const_1 ]-slope*point[_sage_const_0 ])
         return [[slope, yInt], point, [aCoeff, bCoeff, cCoeff]]
 
 ################# QUESTION 4 - Parallel #####################
 solution4, point4, coefficients4 = generateProblemAndSolution(_sage_const_0 )
 aCoeff4, bCoeff4, cCoeff4 = coefficients4
 standardForm4 = aCoeff4 * x + bCoeff4 * y
 pointSlopeForm4 = solution4[_sage_const_0 ]*x + solution4[_sage_const_1 ]
 
 ################# QUESTION 5 - Parallel #####################
 solution5, point5, coefficients5 = generateProblemAndSolution(_sage_const_0 )
 aCoeff5, bCoeff5, cCoeff5 = coefficients5
 standardForm5 = aCoeff5 * x + bCoeff5 * y
 pointSlopeForm5 = solution5[_sage_const_0 ]*x + solution5[_sage_const_1 ]
 
 ################# QUESTION 6 - Perpendicular #####################
 solution6, point6, coefficients6 = generateProblemAndSolution(_sage_const_1 )
 aCoeff6, bCoeff6, cCoeff6 = coefficients6
 standardForm6 = aCoeff6 * x + bCoeff6 * y
 pointSlopeForm6 = solution6[_sage_const_0 ]*x + solution6[_sage_const_1 ]
 
 ################# QUESTION 7 - Perpendicular #####################
 solution7, point7, coefficients7 = generateProblemAndSolution(_sage_const_1 )
 aCoeff7, bCoeff7, cCoeff7 = coefficients7
 standardForm7 = aCoeff7 * x + bCoeff7 * y
 pointSlopeForm7 = solution7[_sage_const_0 ]*x + solution7[_sage_const_1 ]
except:
 _st_.goboom(_sage_const_160 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_18 , latex(standardForm4))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_19 , latex(cCoeff4))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_20 , latex(point4[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_21 , latex(point4[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_169 
 _st_.inline(_sage_const_22 , latex(solution4[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_169 )
try:
 _st_.current_tex_line = _sage_const_169 
 _st_.inline(_sage_const_23 , latex(solution4[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_169 )
try:
 _st_.current_tex_line = _sage_const_179 
 _st_.inline(_sage_const_24 , latex(standardForm5))
except:
 _st_.goboom(_sage_const_179 )
try:
 _st_.current_tex_line = _sage_const_179 
 _st_.inline(_sage_const_25 , latex(cCoeff5))
except:
 _st_.goboom(_sage_const_179 )
try:
 _st_.current_tex_line = _sage_const_179 
 _st_.inline(_sage_const_26 , latex(point5[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_179 )
try:
 _st_.current_tex_line = _sage_const_179 
 _st_.inline(_sage_const_27 , latex(point5[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_179 )
try:
 _st_.current_tex_line = _sage_const_181 
 _st_.inline(_sage_const_28 , latex(solution5[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_181 )
try:
 _st_.current_tex_line = _sage_const_181 
 _st_.inline(_sage_const_29 , latex(solution5[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_181 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_30 , latex(standardForm6))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_31 , latex(cCoeff6))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_32 , latex(point6[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_33 , latex(point6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_189 
 _st_.inline(_sage_const_34 , latex(solution6[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_189 )
try:
 _st_.current_tex_line = _sage_const_189 
 _st_.inline(_sage_const_35 , latex(solution6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_189 )
try:
 _st_.current_tex_line = _sage_const_198 
 _st_.inline(_sage_const_36 , latex(standardForm7))
except:
 _st_.goboom(_sage_const_198 )
try:
 _st_.current_tex_line = _sage_const_198 
 _st_.inline(_sage_const_37 , latex(cCoeff7))
except:
 _st_.goboom(_sage_const_198 )
try:
 _st_.current_tex_line = _sage_const_198 
 _st_.inline(_sage_const_38 , latex(point7[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_198 )
try:
 _st_.current_tex_line = _sage_const_198 
 _st_.inline(_sage_const_39 , latex(point7[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_198 )
try:
 _st_.current_tex_line = _sage_const_200 
 _st_.inline(_sage_const_40 , latex(solution7[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_200 )
try:
 _st_.current_tex_line = _sage_const_200 
 _st_.inline(_sage_const_41 , latex(solution7[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_200 )
_st_.endofdoc()

