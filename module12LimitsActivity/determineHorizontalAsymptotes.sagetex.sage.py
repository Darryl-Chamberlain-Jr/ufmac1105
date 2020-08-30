## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file determineHorizontalAsymptotes.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_99 = Integer(99); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_3 = Integer(3); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_255 = Integer(255); _sage_const_261 = Integer(261); _sage_const_263 = Integer(263); _sage_const_270 = Integer(270); _sage_const_279 = Integer(279); _sage_const_281 = Integer(281); _sage_const_7 = Integer(7); _sage_const_288 = Integer(288); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9)## This file (determineHorizontalAsymptotes.sagetex.sage) was *autogenerated* from determineHorizontalAsymptotes.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('determineHorizontalAsymptotes', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_99 
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
     a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_4 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     while gcd(abs(a), abs(b)) > _sage_const_1 :
         a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_4 ))
         b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     rationalFactor = a*x + b
     return [rationalFactor, a]
 
 def makeIrrationalQuadratic():
     a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     c = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     discrim = b**_sage_const_2  - _sage_const_4 *a*c
     integerType = type(_sage_const_2 )
     while type(sqrt(discrim)) == integerType:
         a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         c = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         discrim = b**_sage_const_2  - _sage_const_4 *a*c
     solution0 = (-b + sqrt(discrim))/_sage_const_2 *a
     solution1 = (-b - sqrt(discrim))/_sage_const_2 *a
     smallerSolution, largerSolution = sorted([solution0, solution1])
     quadratic = a*x**_sage_const_2  + b*x + c
     return [quadratic, smallerSolution, largerSolution]
 
 def makeComplexQuadratic():
     a0 = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_4 ))
     b0 = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     complex0 = a0 + b0*i
     complex1 = a0 - b0*i
     quadratic = x**_sage_const_2  - (a0**_sage_const_2  + b0**_sage_const_2 )
     return [quadratic, complex0, complex1]
 
 def createPolyDegree1to4(degree):
     if degree == _sage_const_1 :
         poly, deadZero1 = makeRationalFactor()
         leadingCoefficient = derivative(poly, x)/factorial(degree)
     elif degree == _sage_const_2 :
         factor2a, deadZero2a = makeRationalFactor()
         factor2b, deadZero2b = makeRationalFactor()
         poly = factor2a * factor2b
         leadingCoefficient = derivative(derivative(poly, x), x)/factorial(degree)
     elif degree == _sage_const_3 :
         factor3a, deadZero3a = makeRationalFactor()
         factor3b, deadZero3b = makeRationalFactor()
         factor3c, deadZero3c = makeRationalFactor()
         poly = factor3a * factor3b * factor3c
         leadingCoefficient = derivative(derivative(derivative(poly, x), x), x)/factorial(degree)
     elif degree == _sage_const_4 :
         factor4a, deadZero4a = makeRationalFactor()
         factor4b, deadZero4b = makeRationalFactor()
         factor4c, deadZero4c = makeRationalFactor()
         factor4d, deadZero4d = makeRationalFactor()
         poly = factor4a * factor4b * factor4c * factor4d
         leadingCoefficient = derivative(derivative(derivative(derivative(poly, x), x), x), x)/factorial(degree)
     else:
         poly = _sage_const_0 
         leadingCoefficient = _sage_const_0 
     return [poly, leadingCoefficient]
 
 def horizontalAsymptote():
     chooseType = ZZ.random_element(_sage_const_2 )
     if chooseType == _sage_const_0 :
         degreeDenom = ZZ.random_element(_sage_const_2 , _sage_const_5 )
         degreeNum = ZZ.random_element(_sage_const_1 , degreeDenom)
         polyNumerator, coeffNumerator = createPolyDegree1to4(degreeNum)
         polyDenominator, coeffDenominator = createPolyDegree1to4(degreeDenom)
         horizontalAsymptote = _sage_const_0 
     elif chooseType == _sage_const_1 :
         degreeNumAndDenom = ZZ.random_element(_sage_const_1 , _sage_const_5 )
         polyNumerator, coeffNumerator = createPolyDegree1to4(degreeNumAndDenom)
         polyDenominator, coeffDenominator = createPolyDegree1to4(degreeNumAndDenom)
         horizontalAsymptote = coeffNumerator/coeffDenominator
     else:
         polyNumerator = _sage_const_0 
         polyDenominator = _sage_const_0 
         horizontalAsymptote = _sage_const_0 
     return [polyNumerator, polyDenominator, horizontalAsymptote]
 
 def obliqueAsymptote(z0, missingOrNot):
     a0 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
     b0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     a1 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
     b1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     z1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     r = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     #
     numeratorPoly = (a0*a1*z0)*x**_sage_const_3  + (-a0*a1*z1 + a0*b1*z0 + a1*b0*z0)*x**_sage_const_2 + (-a0*b1*z1 - a1*b0*z1 + b0*b1*z0)*x + (-b0*b1*z1 + r)
     numCo1 = a0*a1*z0
     numCo2 = -a0*a1*z1 + a0*b1*z0 + a1*b0*z0
     numCo3 = -a0*b1*z1 - a1*b0*z1 + b0*b1*z0
     numCo4 = -b0*b1*z1 + r
     #
     denominator = z0 * x - z1
     quotient = (a0*a1)*x**_sage_const_2  + (a0*b1+a1*b0)*x + b0*b1
     remainder = r
     #
     if missingOrNot == "notMissing":
         while (numCo1==_sage_const_0  or numCo2==_sage_const_0  or numCo3==_sage_const_0  or numCo4==_sage_const_0 ):
             a0 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             a1 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             z1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             r = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             #
             numeratorPoly = (a0*a1*z0)*x**_sage_const_3  + (-a0*a1*z1 + a0*b1*z0 + a1*b0*z0)*x**_sage_const_2 + (-a0*b1*z1 - a1*b0*z1 + b0*b1*z0)*x + (-b0*b1*z1 + r)
             numCo1 = a0*a1*z0
             numCo2 = -a0*a1*z1 + a0*b1*z0 + a1*b0*z0
             numCo3 = -a0*b1*z1 - a1*b0*z1 + b0*b1
             numCo4 = -b0*b1*z1 + r
             denominator = z0*x - z1
             quotient = (a0*a1)*x**_sage_const_2  + (a0*b1+a1*b0)*x + b0*b1
             remainder = r
             #
     else:
         index =  _sage_const_0 
         while (abs(numCo1)>_sage_const_0  and abs(numCo2)>_sage_const_0  and abs(numCo3)>_sage_const_0  and abs(numCo4)>_sage_const_0 ):
             a0 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             a1 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             z1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             r = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             #
             numeratorPoly = (a0*a1*z0)*x**_sage_const_3  + (-a0*a1*z1 + a0*b1*z0 + a1*b0*z0)*x**_sage_const_2 + (-a0*b1*z1 - a1*b0*z1 + b0*b1*z0)*x + (-b0*b1*z1 + r)
             numCo1 = a0*a1*z0
             numCo2 = -a0*a1*z1 + a0*b1*z0 + a1*b0*z0
             numCo3 = -a0*b1*z1 - a1*b0*z1 + b0*b1
             numCo4 = -b0*b1*z1 + r
             denominator = z0*x - z1
             quotient = (a0*a1)*x**_sage_const_2  + (a0*b1+a1*b0)*x + b0*b1
             remainder = r
             index =  index + _sage_const_1 
             #
     return [numeratorPoly, denominator, quotient, remainder]
 #####
 polyNum1, polyDenom1, horAsy1 = horizontalAsymptote()
 polyNum2, polyDenom2, horAsy2 = horizontalAsymptote()
 #
 choices = ["missing", "notMissing"]
 polyNum3, polyDenom3, obliqueAsy3, deadRemainder3 = obliqueAsymptote(_sage_const_1 , choices[ZZ.random_element(_sage_const_2 )])
 polyNum4, polyDenom4, obliqueAsy4, deadRemainder4 = obliqueAsymptote(ZZ.random_element(_sage_const_2 , _sage_const_6 ), choices[ZZ.random_element(_sage_const_2 )])
except:
 _st_.goboom(_sage_const_255 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_261 
 _st_.inline(_sage_const_0 , latex(polyNum1))
except:
 _st_.goboom(_sage_const_261 )
try:
 _st_.current_tex_line = _sage_const_261 
 _st_.inline(_sage_const_1 , latex(polyDenom1))
except:
 _st_.goboom(_sage_const_261 )
try:
 _st_.current_tex_line = _sage_const_263 
 _st_.inline(_sage_const_2 , latex(horAsy1))
except:
 _st_.goboom(_sage_const_263 )
try:
 _st_.current_tex_line = _sage_const_270 
 _st_.inline(_sage_const_3 , latex(polyNum3))
except:
 _st_.goboom(_sage_const_270 )
try:
 _st_.current_tex_line = _sage_const_270 
 _st_.inline(_sage_const_4 , latex(polyDenom3))
except:
 _st_.goboom(_sage_const_270 )
try:
 _st_.current_tex_line = _sage_const_279 
 _st_.inline(_sage_const_5 , latex(polyNum2))
except:
 _st_.goboom(_sage_const_279 )
try:
 _st_.current_tex_line = _sage_const_279 
 _st_.inline(_sage_const_6 , latex(polyDenom2))
except:
 _st_.goboom(_sage_const_279 )
try:
 _st_.current_tex_line = _sage_const_281 
 _st_.inline(_sage_const_7 , latex(horAsy2))
except:
 _st_.goboom(_sage_const_281 )
try:
 _st_.current_tex_line = _sage_const_288 
 _st_.inline(_sage_const_8 , latex(polyNum4))
except:
 _st_.goboom(_sage_const_288 )
try:
 _st_.current_tex_line = _sage_const_288 
 _st_.inline(_sage_const_9 , latex(polyDenom4))
except:
 _st_.goboom(_sage_const_288 )
_st_.endofdoc()
