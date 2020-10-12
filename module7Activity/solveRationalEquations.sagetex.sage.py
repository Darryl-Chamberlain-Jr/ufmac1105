## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file solveRationalEquations.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_31 = Integer(31); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_3 = Integer(3); _sage_const_7 = Integer(7); _sage_const_9 = Integer(9); _sage_const_4 = Integer(4); _sage_const_144 = Integer(144); _sage_const_150 = Integer(150); _sage_const_161 = Integer(161); _sage_const_5 = Integer(5); _sage_const_163 = Integer(163); _sage_const_6 = Integer(6); _sage_const_172 = Integer(172); _sage_const_8 = Integer(8); _sage_const_183 = Integer(183); _sage_const_10 = Integer(10); _sage_const_185 = Integer(185); _sage_const_11 = Integer(11); _sage_const_194 = Integer(194); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_196 = Integer(196); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15)## This file (solveRationalEquations.sagetex.sage) was *autogenerated* from solveRationalEquations.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveRationalEquations', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_31 
_st_.blockbegin()
try:
 x = var("x")
 
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def generateTermsLinearSolutions(numberOfSolutions):
     if (numberOfSolutions==_sage_const_0 ):
         mask = ZZ.random_element(_sage_const_3 , _sage_const_7 )
         a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 )) * mask
         d = -_sage_const_1 
         f = _sage_const_1 
         e = a
         b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 )) * mask
         c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 )) * mask
         solution = _sage_const_0 
     else:
         a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         d = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         e = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         f = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         makeSolutionExist = (-f*a +e + d*c*f)/(-d*f*b)
         #
         while (makeSolutionExist==_sage_const_0 ):
             a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
             b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
             c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
             d = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
             e = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
             f = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
             makeSolutionExist = (-f*a +e + d*c*f)/(-d*f*b)
         solution = (-f*a +e + d*c*f)/(-d*f*b)
     leftTerm = (a/(b*x+c)) - d
     rightTermNum = e
     rightTermDenom = f*(b*x+c)
     return [leftTerm, rightTermNum, rightTermDenom, solution]
 
 def generateCoefficientsQuadraticSolutions(numberOfSolutions):
     #
     a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     d = -ZZ.random_element(_sage_const_2 , _sage_const_7 )
     e = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     f = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     g = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
     discrim = (a*g-e*b)**_sage_const_2  - _sage_const_4 *(a*f+d)*(-e*c)
     leadingCoefficient = a*f+d
 
    #
     if (numberOfSolutions == _sage_const_0 ):
         while (leadingCoefficient == _sage_const_0  or discrim > _sage_const_0  or discrim == _sage_const_0 ):
             a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             d = -ZZ.random_element(_sage_const_2 , _sage_const_7 )
             e = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             f = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             g = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             discrim = (a*g-e*b)**_sage_const_2  - _sage_const_4 *(a*f+d)*(-e*c)
             leadingCoefficient = a*f+d
         solution = [_sage_const_0 , _sage_const_0 ]
     elif (numberOfSolutions == _sage_const_1 ):
         while (leadingCoefficient==_sage_const_0  or discrim != _sage_const_0 ):
             a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             d = -ZZ.random_element(_sage_const_2 , _sage_const_7 )
             e = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             f = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             g = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             discrim = (a*g-e*b)**_sage_const_2  - _sage_const_4 *(a*f+d)*(-e*c)
             leadingCoefficient = a*f+d
         quadraticEquation = (a*x)/(b*x+c) + (d*x**_sage_const_2 )/(b*f*x**_sage_const_2  + (b*g+c*f)*x+c*g) - e/(f*x+g)
         singleSolution = solve(quadraticEquation == _sage_const_0 , x)[_sage_const_0 ].rhs()
         solution = [singleSolution, _sage_const_0 ]
     else:
         while (leadingCoefficient==_sage_const_0  or discrim < _sage_const_0  or discrim == _sage_const_0 ):
             a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             d = -ZZ.random_element(_sage_const_2 , _sage_const_7 )
             e = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             f = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             g = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_7 ))
             discrim = (a*g-e*b)**_sage_const_2  - _sage_const_4 *(a*f+d)*(-e*c)
             leadingCoefficient = a*f+d
         quadraticEquation = (a*x)/(b*x+c) + (d*x**_sage_const_2 )/(b*f*x**_sage_const_2  + (b*g+c*f)*x+c*g) - e/(f*x+g)
         rawSolutions = solve(quadraticEquation == _sage_const_0 , x)
         solution1 = rawSolutions[_sage_const_0 ].rhs()
         solution2 = rawSolutions[_sage_const_1 ].rhs()
         solution = sorted([solution1, solution2])
     firstTerm = (a*x)/(b*x+c)
     secondTerm = (d*x**_sage_const_2 )/(b*f*x**_sage_const_2  + (b*g+c*f)*x+c*g)
     thirdTerm = e/(f*x+g)
     return [firstTerm, secondTerm, thirdTerm, solution]
 ##########
 leftTerm1, rightTerm1Num, rightTerm1Denom, solution1 = generateTermsLinearSolutions(_sage_const_0 )
 leftTerm2, rightTerm2Num, rightTerm2Denom, solution2 = generateTermsLinearSolutions(_sage_const_1 )
 #
 firstTerm3, secondTerm3, thirdTerm3, solution3TEMP = generateCoefficientsQuadraticSolutions(_sage_const_0 )
 leftTerm3 = firstTerm3 + secondTerm3
 #
 firstTerm4, secondTerm4, thirdTerm4, solution4TEMP = generateCoefficientsQuadraticSolutions(_sage_const_1 )
 leftTerm4 = firstTerm4 + secondTerm4
 solution4 = solution4TEMP[_sage_const_0 ]
 #
 firstTerm5, secondTerm5, thirdTerm5, solution5TEMP = generateCoefficientsQuadraticSolutions(_sage_const_2 )
 leftTerm5 = firstTerm5 + secondTerm5
 solution5a, solution5b = sorted([solution5TEMP[_sage_const_0 ], solution5TEMP[_sage_const_1 ]])
except:
 _st_.goboom(_sage_const_144 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_0 , latex(leftTerm1))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_1 , latex(rightTerm1Num))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_2 , latex(rightTerm1Denom))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_3 , latex(leftTerm2))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_4 , latex(rightTerm2Num))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_5 , latex(rightTerm2Denom))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_163 
 _st_.inline(_sage_const_6 , latex(solution2))
except:
 _st_.goboom(_sage_const_163 )
try:
 _st_.current_tex_line = _sage_const_172 
 _st_.inline(_sage_const_7 , latex(leftTerm3))
except:
 _st_.goboom(_sage_const_172 )
try:
 _st_.current_tex_line = _sage_const_172 
 _st_.inline(_sage_const_8 , latex(thirdTerm3))
except:
 _st_.goboom(_sage_const_172 )
try:
 _st_.current_tex_line = _sage_const_183 
 _st_.inline(_sage_const_9 , latex(leftTerm4))
except:
 _st_.goboom(_sage_const_183 )
try:
 _st_.current_tex_line = _sage_const_183 
 _st_.inline(_sage_const_10 , latex(thirdTerm4))
except:
 _st_.goboom(_sage_const_183 )
try:
 _st_.current_tex_line = _sage_const_185 
 _st_.inline(_sage_const_11 , latex(solution4))
except:
 _st_.goboom(_sage_const_185 )
try:
 _st_.current_tex_line = _sage_const_194 
 _st_.inline(_sage_const_12 , latex(leftTerm5))
except:
 _st_.goboom(_sage_const_194 )
try:
 _st_.current_tex_line = _sage_const_194 
 _st_.inline(_sage_const_13 , latex(thirdTerm5))
except:
 _st_.goboom(_sage_const_194 )
try:
 _st_.current_tex_line = _sage_const_196 
 _st_.inline(_sage_const_14 , latex(solution5a))
except:
 _st_.goboom(_sage_const_196 )
try:
 _st_.current_tex_line = _sage_const_196 
 _st_.inline(_sage_const_15 , latex(solution5b))
except:
 _st_.goboom(_sage_const_196 )
_st_.endofdoc()

