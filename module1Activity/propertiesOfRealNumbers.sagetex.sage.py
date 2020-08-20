## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file propertiesOfRealNumbers.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_59 = Integer(59); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_0 = Integer(0); _sage_const_21 = Integer(21); _sage_const_6 = Integer(6); _sage_const_100 = Integer(100); _sage_const_122 = Integer(122); _sage_const_125 = Integer(125); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_127 = Integer(127); _sage_const_130 = Integer(130); _sage_const_7 = Integer(7); _sage_const_135 = Integer(135); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_137 = Integer(137); _sage_const_14 = Integer(14); _sage_const_139 = Integer(139); _sage_const_15 = Integer(15); _sage_const_144 = Integer(144); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_146 = Integer(146); _sage_const_22 = Integer(22); _sage_const_148 = Integer(148); _sage_const_23 = Integer(23)## This file (propertiesOfRealNumbers.sagetex.sage) was *autogenerated* from propertiesOfRealNumbers.tex with sagetex.sty version 2019/01/09 v3.2.
import sagetex
_st_ = sagetex.SageTeXProcessor('propertiesOfRealNumbers', version='2019/01/09 v3.2', version_check=True)
_st_.current_tex_line = _sage_const_59 
_st_.blockbegin()
try:
 # Order of Operations Question
 def generateSolution1(constants):
     c0, c1, c2, c3, c4, c5 = constants
     solution = float((c0 - ((c1/c2) * c3)) - (c4 * c5 ))
     return solution
 
 def generateDistractor1(constants):
     c0, c1, c2, c3, c4, c5 = constants
     distractor = float(c0 - (c1/(c2 * c3)) - (c4 * c5 ))
     return distractor
 
 def generateSolution2(constants):
     c0, c1, c2, c3, c4, c5 = constants
     solution = float(c0 - c1 - c2 + c3 - c4 + c5 )
     return solution
 
 def generateDistractor2(constants):
     c0, c1, c2, c3, c4, c5 = constants
     distractor = float(c0 - c1 - (c2 + c3) - (c4 + c5) )
     return distractor
 
 def generateSolution3(constants):
     c0, c1, c2, c3, c4, c5 = constants
     solution = float((c0/c1) - c2 + (c3/c4) + c5 )
     return solution
 
 def generateDistractor3(constants):
     c0, c1, c2, c3, c4, c5 = constants
     distractor = float( (c0/c1) - ( (c2 + (c3/c4) ) + c5) )
     return distractor
 
 def generateSolutionAndDistractor(structureType, constants):
     if structureType==_sage_const_1 :
         return [generateSolution1(constants), generateDistractor1(constants)]
     elif structureType==_sage_const_2 :
         return [generateSolution2(constants), generateDistractor2(constants)]
     elif structureType==_sage_const_3 :
         return [generateSolution3(constants), generateDistractor3(constants)]
     else:
         return [_sage_const_0 , _sage_const_0 ]
 
 def createProblem(structureType):
     # Array of 6 distinct integers
     constants = sample(list(range(_sage_const_2 , _sage_const_21 )), _sage_const_6 )
     solution, distractor = generateSolutionAndDistractor(structureType, constants)
     # CHECKS if doing the question wrong will still give the correct solution.
     index = _sage_const_0 
     while solution == distractor:
         constants = sample(list(range(_sage_const_2 , _sage_const_21 )), _sage_const_6 )
         solution, distractor = generateSolutionAndDistractor(structureType, constants)
         # Makes sure we don't get stuck in an infinite loop
         index += _sage_const_1 
         if (index > _sage_const_100 ):
             break
     return [constants, solution, distractor]
 
 ########## END OF DEFINITIONS ###########
 
 constants1, solution1, distractor1 = createProblem(_sage_const_1 )
 constants2, solution2, distractor2 = createProblem(_sage_const_2 )
 constants3, solution3, distractor3 = createProblem(_sage_const_3 )
 
except:
 _st_.goboom(_sage_const_122 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_0 , latex(constants1[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_1 , latex(constants1[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_2 , latex(constants1[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_3 , latex(constants1[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_4 , latex(constants1[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_5 , latex(constants1[_sage_const_5 ]))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_6 , latex(solution1))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_7 , latex(distractor1))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_8 , latex(constants2[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_9 , latex(constants2[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_10 , latex(constants2[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_11 , latex(constants2[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_12 , latex(constants2[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_13 , latex(constants2[_sage_const_5 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_137 
 _st_.inline(_sage_const_14 , latex(solution2))
except:
 _st_.goboom(_sage_const_137 )
try:
 _st_.current_tex_line = _sage_const_139 
 _st_.inline(_sage_const_15 , latex(distractor2))
except:
 _st_.goboom(_sage_const_139 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_16 , latex(constants3[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_17 , latex(constants3[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_18 , latex(constants3[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_19 , latex(constants3[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_20 , latex(constants3[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_21 , latex(constants3[_sage_const_5 ]))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_146 
 _st_.inline(_sage_const_22 , latex(solution3))
except:
 _st_.goboom(_sage_const_146 )
try:
 _st_.current_tex_line = _sage_const_148 
 _st_.inline(_sage_const_23 , latex(distractor3))
except:
 _st_.goboom(_sage_const_148 )
_st_.endofdoc()

