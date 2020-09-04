## -*- encoding: utf-8 -*-
## This file (solveRadicalLeadLinearEquation.sagetex.sage) was *autogenerated* from solveRadicalLeadLinearEquation.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveRadicalLeadLinearEquation', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = 32
_st_.blockbegin()
try:
 def createSingleSolutionLinearFactors():
     a = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     b = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     c = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     d = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     factorA = a*x + b
     factorB = c*x + d
     answerList = solve(factorA-factorB==0, x)
     while len(answerList)==0 or b==d:
         a = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
         b = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
         c = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
         d = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
         factorA = a*x + b
         factorB = c*x + d
         answerList = solve(factorA-factorB==0, x)
     return [a, b, c, d]
 
 a9, b9, c9, d9 = createSingleSolutionLinearFactors()
 factor9A = a9*x + b9
 factor9B = c9*x + d9
 answer9 = round(float(solve(factor9A-factor9B==0, x)[0].rhs()), 3)
 checkFactorAGreater9 = factor9A(answer9)
 checkFactorBGreater9 = factor9B(answer9)
 while (checkFactorAGreater9 < 0 or checkFactorBGreater9 < 0):
     a9, b9, c9, d9 = createSingleSolutionLinearFactors()
     factor9A = a9*x + b9
     factor9B = c9*x + d9
     answer9 = round(float(solve(factor9A-factor9B==0, x)[0].rhs()), 3)
     checkFactorAGreater9 = factor9A(answer9)
     checkFactorBGreater9 = factor9B(answer9)
 
 a10, b10, c10, d10 = createSingleSolutionLinearFactors()
 factor10A = a10*x + b10
 factor10B = c10*x + d10
 answer10 = round(float(solve(factor10A-factor10B==0, x)[0].rhs()), 3)
 checkFactorAGreater10 = factor10A(answer10)
 checkFactorBGreater10 = factor10B(answer10)
 while (checkFactorAGreater10 < 0 or checkFactorBGreater10 < 0):
     a10, b10, c10, d10 = createSingleSolutionLinearFactors()
     factor10A = a10*x + b10
     factor10B = c10*x + d10
     answer10 = round(float(solve(factor10A-factor10B==0, x)[0].rhs()), 3)
     checkFactorAGreater10 = factor10A(answer10)
     checkFactorBGreater10 = factor10B(answer10)
 
 a11, b11, c11, d11 = createSingleSolutionLinearFactors()
 factor11A = a11*x + b11
 factor11B = c11*x + d11
 answer11 = round(float(solve(factor11A-factor11B==0, x)[0].rhs()), 3)
 checkFactorAGreater11 = factor11A(answer11)
 checkFactorBGreater11 = factor11B(answer11)
 while (checkFactorAGreater11 > 0 and checkFactorBGreater11 > 0):
     a11, b11, c11, d11 = createSingleSolutionLinearFactors()
     factor11A = a11*x + b11
     factor11B = c11*x + d11
     answer11 = round(float(solve(factor11A-factor11B==0, x)[0].rhs()), 3)
     checkFactorAGreater11 = factor11A(answer11)
     checkFactorBGreater11 = factor11B(answer11)
 
 a12, b12, c12, d12 = createSingleSolutionLinearFactors()
 factor12A = a12*x + b12
 factor12B = c12*x + d12
 answer12 = round(float(solve(factor12A-factor12B==0, x)[0].rhs()), 3)
 checkFactorAGreater12 = factor12A(answer12)
 checkFactorBGreater12 = factor12B(answer12)
 while (checkFactorAGreater12 > 0 and checkFactorBGreater12 > 0):
     a12, b12, c12, d12 = createSingleSolutionLinearFactors()
     factor12A = a12*x + b12
     factor12B = c12*x + d12
     answer12 = round(float(solve(factor12A-factor12B==0, x)[0].rhs()), 3)
     checkFactorAGreater12 = factor12A(answer12)
     checkFactorBGreater12 = factor12B(answer12)
except:
 _st_.goboom(106)
_st_.blockend()
try:
 _st_.current_tex_line = 112
 _st_.inline(0, latex(factor9A))
except:
 _st_.goboom(112)
try:
 _st_.current_tex_line = 112
 _st_.inline(1, latex(factor9B))
except:
 _st_.goboom(112)
try:
 _st_.current_tex_line = 114
 _st_.inline(2, latex(answer9))
except:
 _st_.goboom(114)
try:
 _st_.current_tex_line = 116
 _st_.inline(3, latex(answer9))
except:
 _st_.goboom(116)
try:
 _st_.current_tex_line = 128
 _st_.inline(4, latex(factor11A))
except:
 _st_.goboom(128)
try:
 _st_.current_tex_line = 128
 _st_.inline(5, latex(factor11B))
except:
 _st_.goboom(128)
try:
 _st_.current_tex_line = 130
 _st_.inline(6, latex(answer11))
except:
 _st_.goboom(130)
try:
 _st_.current_tex_line = 140
 _st_.inline(7, latex(factor12A))
except:
 _st_.goboom(140)
try:
 _st_.current_tex_line = 140
 _st_.inline(8, latex(factor12B))
except:
 _st_.goboom(140)
try:
 _st_.current_tex_line = 142
 _st_.inline(9, latex(answer12))
except:
 _st_.goboom(142)
try:
 _st_.current_tex_line = 152
 _st_.inline(10, latex(factor10A))
except:
 _st_.goboom(152)
try:
 _st_.current_tex_line = 152
 _st_.inline(11, latex(factor10B))
except:
 _st_.goboom(152)
try:
 _st_.current_tex_line = 154
 _st_.inline(12, latex(answer10))
except:
 _st_.goboom(154)
try:
 _st_.current_tex_line = 156
 _st_.inline(13, latex(answer10))
except:
 _st_.goboom(156)
_st_.endofdoc()
