## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file solveRadicalLeadLinearEquation.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_34 = Integer(34); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_10 = Integer(10); _sage_const_0 = Integer(0); _sage_const_3 = Integer(3); _sage_const_108 = Integer(108); _sage_const_114 = Integer(114); _sage_const_116 = Integer(116); _sage_const_118 = Integer(118); _sage_const_130 = Integer(130); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_132 = Integer(132); _sage_const_6 = Integer(6); _sage_const_142 = Integer(142); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_144 = Integer(144); _sage_const_9 = Integer(9); _sage_const_154 = Integer(154); _sage_const_11 = Integer(11); _sage_const_156 = Integer(156); _sage_const_12 = Integer(12); _sage_const_158 = Integer(158); _sage_const_13 = Integer(13)## This file (solveRadicalLeadLinearEquation.sagetex.sage) was *autogenerated* from solveRadicalLeadLinearEquation.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveRadicalLeadLinearEquation', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_34 
_st_.blockbegin()
try:
 def createSingleSolutionLinearFactors():
     a = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     b = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     c = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     d = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     factorA = a*x + b
     factorB = c*x + d
     answerList = solve(factorA-factorB==_sage_const_0 , x)
     while len(answerList)==_sage_const_0  or b==d:
         a = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
         b = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
         c = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
         d = (-_sage_const_1 )**(ZZ.random_element(_sage_const_2 ))*(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
         factorA = a*x + b
         factorB = c*x + d
         answerList = solve(factorA-factorB==_sage_const_0 , x)
     return [a, b, c, d]
 
 a9, b9, c9, d9 = createSingleSolutionLinearFactors()
 factor9A = a9*x + b9
 factor9B = c9*x + d9
 answer9 = round(float(solve(factor9A-factor9B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
 checkFactorAGreater9 = factor9A(answer9)
 checkFactorBGreater9 = factor9B(answer9)
 while (checkFactorAGreater9 < _sage_const_0  or checkFactorBGreater9 < _sage_const_0 ):
     a9, b9, c9, d9 = createSingleSolutionLinearFactors()
     factor9A = a9*x + b9
     factor9B = c9*x + d9
     answer9 = round(float(solve(factor9A-factor9B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
     checkFactorAGreater9 = factor9A(answer9)
     checkFactorBGreater9 = factor9B(answer9)
 
 a10, b10, c10, d10 = createSingleSolutionLinearFactors()
 factor10A = a10*x + b10
 factor10B = c10*x + d10
 answer10 = round(float(solve(factor10A-factor10B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
 checkFactorAGreater10 = factor10A(answer10)
 checkFactorBGreater10 = factor10B(answer10)
 while (checkFactorAGreater10 < _sage_const_0  or checkFactorBGreater10 < _sage_const_0 ):
     a10, b10, c10, d10 = createSingleSolutionLinearFactors()
     factor10A = a10*x + b10
     factor10B = c10*x + d10
     answer10 = round(float(solve(factor10A-factor10B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
     checkFactorAGreater10 = factor10A(answer10)
     checkFactorBGreater10 = factor10B(answer10)
 
 a11, b11, c11, d11 = createSingleSolutionLinearFactors()
 factor11A = a11*x + b11
 factor11B = c11*x + d11
 answer11 = round(float(solve(factor11A-factor11B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
 checkFactorAGreater11 = factor11A(answer11)
 checkFactorBGreater11 = factor11B(answer11)
 while (checkFactorAGreater11 > _sage_const_0  and checkFactorBGreater11 > _sage_const_0 ):
     a11, b11, c11, d11 = createSingleSolutionLinearFactors()
     factor11A = a11*x + b11
     factor11B = c11*x + d11
     answer11 = round(float(solve(factor11A-factor11B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
     checkFactorAGreater11 = factor11A(answer11)
     checkFactorBGreater11 = factor11B(answer11)
 
 a12, b12, c12, d12 = createSingleSolutionLinearFactors()
 factor12A = a12*x + b12
 factor12B = c12*x + d12
 answer12 = round(float(solve(factor12A-factor12B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
 checkFactorAGreater12 = factor12A(answer12)
 checkFactorBGreater12 = factor12B(answer12)
 while (checkFactorAGreater12 > _sage_const_0  and checkFactorBGreater12 > _sage_const_0 ):
     a12, b12, c12, d12 = createSingleSolutionLinearFactors()
     factor12A = a12*x + b12
     factor12B = c12*x + d12
     answer12 = round(float(solve(factor12A-factor12B==_sage_const_0 , x)[_sage_const_0 ].rhs()), _sage_const_3 )
     checkFactorAGreater12 = factor12A(answer12)
     checkFactorBGreater12 = factor12B(answer12)
except:
 _st_.goboom(_sage_const_108 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_0 , latex(factor9A))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_1 , latex(factor9B))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_2 , latex(answer9))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_3 , latex(answer9))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_4 , latex(factor11A))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_5 , latex(factor11B))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_6 , latex(answer11))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_7 , latex(factor12A))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_8 , latex(factor12B))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_9 , latex(answer12))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_10 , latex(factor10A))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_11 , latex(factor10B))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_12 , latex(answer10))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_158 
 _st_.inline(_sage_const_13 , latex(answer10))
except:
 _st_.goboom(_sage_const_158 )
_st_.endofdoc()

