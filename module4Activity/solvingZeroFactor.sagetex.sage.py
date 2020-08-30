## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file solvingZeroFactor.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_33 = Integer(33); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_3 = Integer(3); _sage_const_7 = Integer(7); _sage_const_117 = Integer(117); _sage_const_122 = Integer(122); _sage_const_124 = Integer(124); _sage_const_126 = Integer(126); _sage_const_133 = Integer(133); _sage_const_135 = Integer(135); _sage_const_4 = Integer(4); _sage_const_137 = Integer(137); _sage_const_5 = Integer(5); _sage_const_144 = Integer(144); _sage_const_6 = Integer(6); _sage_const_146 = Integer(146); _sage_const_148 = Integer(148); _sage_const_8 = Integer(8); _sage_const_156 = Integer(156); _sage_const_9 = Integer(9); _sage_const_158 = Integer(158); _sage_const_10 = Integer(10); _sage_const_160 = Integer(160); _sage_const_11 = Integer(11); _sage_const_167 = Integer(167); _sage_const_12 = Integer(12); _sage_const_169 = Integer(169); _sage_const_13 = Integer(13); _sage_const_171 = Integer(171); _sage_const_14 = Integer(14); _sage_const_178 = Integer(178); _sage_const_15 = Integer(15); _sage_const_180 = Integer(180); _sage_const_16 = Integer(16); _sage_const_182 = Integer(182); _sage_const_17 = Integer(17)## This file (solvingZeroFactor.sagetex.sage) was *autogenerated* from solvingZeroFactor.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('solvingZeroFactor', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_33 
_st_.blockbegin()
try:
 x = var("x")
 
 ###########################
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def generateFactors(minimumPrime, maximumPrime, numberOfFactors):
     listPrimes = [p for p in range(minimumPrime, maximumPrime+_sage_const_1 ) if is_prime(p)]
     aFactors = [listPrimes[ZZ.random_element(_sage_const_0 , len(listPrimes))] for i in range(numberOfFactors)]
     cFactors = [listPrimes[ZZ.random_element(_sage_const_0 , len(listPrimes))] for i in range(numberOfFactors)]
     return [aFactors, cFactors]
 
 def generateSolution(minimum, maximum, numberOfFactors):
     factors = generateFactors(minimum, maximum, numberOfFactors)
     aFactors = factors[_sage_const_0 ]
     cFactors = factors[_sage_const_1 ]
     a = prod(aFactors)
     c = prod(cFactors)
     b = maybeMakeNegative(ZZ.random_element(minimum, maximum+_sage_const_1 ))
     d = maybeMakeNegative(ZZ.random_element(minimum, maximum+_sage_const_1 ))
     #This will guarantee that we always generate solutions with b < d
     if(b < d):
         return [a, b, c, d]
     else:
         return [c, d, a, b]
 
 def generateZeros(a, b, c, d):
     z0 = round(float(-b/a), _sage_const_3 )
     z1 = round(float(-d/c), _sage_const_3 )
     # Orders from small to large
     if z0 < z1:
         return [z0, z1]
     else:
         return [z1, z0]
 
 def generateProblem(solution):
     a, b, c, d = solution
     return [a*c, a*d + b*c, b*d]
 
 ############ END OF DEFINITIONS ###############
 numberOfFactors567 = _sage_const_1 
 minimum = _sage_const_2 
 maximum = _sage_const_7 
 
 ##### QUESTION 5 #####
 solution5 = generateSolution(minimum, maximum, numberOfFactors567)
 problem5 = generateProblem(solution5)
 generalForm5 = problem5[_sage_const_0 ] * x**_sage_const_2  + problem5[_sage_const_1 ] * x + problem5[_sage_const_2 ]
 zeros5 = generateZeros(solution5[_sage_const_0 ], solution5[_sage_const_1 ], solution5[_sage_const_2 ], solution5[_sage_const_3 ])
 
 ##### QUESTION 6 #####
 solution6 = generateSolution(minimum, maximum, numberOfFactors567)
 problem6 = generateProblem(solution6)
 generalForm6 = problem6[_sage_const_0 ] * x**_sage_const_2  + problem6[_sage_const_1 ] * x + problem6[_sage_const_2 ]
 zeros6 = generateZeros(solution6[_sage_const_0 ], solution6[_sage_const_1 ], solution6[_sage_const_2 ], solution6[_sage_const_3 ])
 
 ##### QUESTION 7 #####
 solution7 = generateSolution(minimum, maximum, numberOfFactors567)
 problem7 = generateProblem(solution7)
 generalForm7 = problem7[_sage_const_0 ] * x**_sage_const_2  + problem7[_sage_const_1 ] * x + problem7[_sage_const_2 ]
 zeros7 = generateZeros(solution7[_sage_const_0 ], solution7[_sage_const_1 ], solution7[_sage_const_2 ], solution7[_sage_const_3 ])
 
 ####
 numberOfFactors8910 = _sage_const_2 
 
 ##### Question 8 #####
 solution8 = generateSolution(minimum, maximum, numberOfFactors8910)
 problem8 = generateProblem(solution8)
 generalForm8 = problem8[_sage_const_0 ] * x**_sage_const_2  + problem8[_sage_const_1 ] * x + problem8[_sage_const_2 ]
 zeros8 = generateZeros(solution8[_sage_const_0 ], solution8[_sage_const_1 ], solution8[_sage_const_2 ], solution8[_sage_const_3 ])
 
 ##### Question 9 #####
 solution9 = generateSolution(minimum, maximum, numberOfFactors8910)
 problem9 = generateProblem(solution9)
 generalForm9 = problem9[_sage_const_0 ] * x**_sage_const_2  + problem9[_sage_const_1 ] * x + problem9[_sage_const_2 ]
 zeros9 = generateZeros(solution9[_sage_const_0 ], solution9[_sage_const_1 ], solution9[_sage_const_2 ], solution9[_sage_const_3 ])
 
 ##### Question 10 #####
 solution10 = generateSolution(minimum, maximum, numberOfFactors8910)
 problem10 = generateProblem(solution10)
 generalForm10 = problem10[_sage_const_0 ] * x**_sage_const_2  + problem10[_sage_const_1 ] * x + problem10[_sage_const_2 ]
 zeros10 = generateZeros(solution10[_sage_const_0 ], solution10[_sage_const_1 ], solution10[_sage_const_2 ], solution10[_sage_const_3 ])
except:
 _st_.goboom(_sage_const_117 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_0 , latex(generalForm5))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.inline(_sage_const_1 , latex(zeros5[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_2 , latex(zeros5[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_133 
 _st_.inline(_sage_const_3 , latex(generalForm6))
except:
 _st_.goboom(_sage_const_133 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_4 , latex(zeros6[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_137 
 _st_.inline(_sage_const_5 , latex(zeros6[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_137 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_6 , latex(generalForm7))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_146 
 _st_.inline(_sage_const_7 , latex(zeros7[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_146 )
try:
 _st_.current_tex_line = _sage_const_148 
 _st_.inline(_sage_const_8 , latex(zeros7[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_148 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_9 , latex(generalForm8))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_158 
 _st_.inline(_sage_const_10 , latex(zeros8[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_158 )
try:
 _st_.current_tex_line = _sage_const_160 
 _st_.inline(_sage_const_11 , latex(zeros8[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_160 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_12 , latex(generalForm9))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_169 
 _st_.inline(_sage_const_13 , latex(zeros9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_169 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_14 , latex(zeros9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_178 
 _st_.inline(_sage_const_15 , latex(generalForm10))
except:
 _st_.goboom(_sage_const_178 )
try:
 _st_.current_tex_line = _sage_const_180 
 _st_.inline(_sage_const_16 , latex(zeros10[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_180 )
try:
 _st_.current_tex_line = _sage_const_182 
 _st_.inline(_sage_const_17 , latex(zeros10[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_182 )
_st_.endofdoc()
