## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file solveLinearEquations.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_32 = Integer(32); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_16 = Integer(16); _sage_const_6 = Integer(6); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_106 = Integer(106); _sage_const_111 = Integer(111); _sage_const_3 = Integer(3); _sage_const_113 = Integer(113); _sage_const_116 = Integer(116); _sage_const_123 = Integer(123); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_125 = Integer(125); _sage_const_10 = Integer(10); _sage_const_128 = Integer(128); _sage_const_11 = Integer(11); _sage_const_135 = Integer(135); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_137 = Integer(137); _sage_const_140 = Integer(140); _sage_const_17 = Integer(17); _sage_const_146 = Integer(146); _sage_const_257 = Integer(257); _sage_const_262 = Integer(262); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_268 = Integer(268); _sage_const_24 = Integer(24); _sage_const_273 = Integer(273); _sage_const_25 = Integer(25); _sage_const_275 = Integer(275); _sage_const_26 = Integer(26); _sage_const_277 = Integer(277); _sage_const_27 = Integer(27); _sage_const_284 = Integer(284); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_30 = Integer(30); _sage_const_31 = Integer(31); _sage_const_33 = Integer(33); _sage_const_286 = Integer(286); _sage_const_34 = Integer(34); _sage_const_291 = Integer(291); _sage_const_35 = Integer(35); _sage_const_293 = Integer(293); _sage_const_36 = Integer(36); _sage_const_295 = Integer(295); _sage_const_37 = Integer(37); _sage_const_302 = Integer(302); _sage_const_38 = Integer(38); _sage_const_39 = Integer(39); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_304 = Integer(304); _sage_const_44 = Integer(44); _sage_const_309 = Integer(309); _sage_const_45 = Integer(45); _sage_const_311 = Integer(311); _sage_const_46 = Integer(46); _sage_const_313 = Integer(313); _sage_const_47 = Integer(47)## This file (solveLinearEquations.sagetex.sage) was *autogenerated* from solveLinearEquations.tex with sagetex.sty version 2019/01/09 v3.2.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveLinearEquations', version='2019/01/09 v3.2', version_check=True)
_st_.current_tex_line = _sage_const_32 
_st_.blockbegin()
try:
 # SOLVES BASIC LINEAR EQUATIONS OF THE FORM
     # b0 * (b1 + b2 * x) = b3 ( x * b4 - b5)
 
 x = var('x')
 
 ###################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def generateBlocks():
     listNaturals = range(_sage_const_2 , _sage_const_16 )
     n0, n1, n2, n3, n4, n5 = sample(listNaturals, _sage_const_6 )
     b0 = Integer(-n0)
     b1 = Integer(maybeMakeNegative(n1))
     b2 = Integer(maybeMakeNegative(n2))
     b3 = Integer(-n3)
     b4 = Integer(maybeMakeNegative(n4))
     b5 = Integer(maybeMakeNegative(n5))
     # Begin checking for one solution
     OneSolutionCheck = b0*b2 - b3*b4
     # Makes sure there is exactly one solution
     while (OneSolutionCheck == _sage_const_0 ):
         listNaturals = range(_sage_const_2 , _sage_const_16 )
         n0, n1, n2, n3, n4, n5 = sample(listNaturals, _sage_const_6 )
         b0 = Integer(-n0)
         b1 = Integer(maybeMakeNegative(n1))
         b2 = Integer(maybeMakeNegative(n2))
         b3 = Integer(-n3)
         b4 = Integer(maybeMakeNegative(n4))
         b5 = Integer(maybeMakeNegative(n5))
         # Begin checking for one solution
         OneSolutionCheck = b0*b2 - b3*b4
     blocks = [b0, b1, b2, b3, b4, b5]
     return blocks
 
 #b0 * (b1 + b2 * x) =  b3 ( x * b4 - b5)
 def generateSolution(blocks):
     a, b, c, d, e, f = blocks
     basicLinearEquation = a * (b + c * x) - d * ( x * e - f)
     solution = float(solve(basicLinearEquation, x)[_sage_const_0 ].rhs())
     return solution
 
 def generateFeedback(blocks):
     a, b, c, d, e, f = blocks
     basicLinearEquation = a * (b - c * x) - d * ( x * e + f)
     feedback = float(solve(basicLinearEquation, x)[_sage_const_0 ].rhs())
     return feedback
 
 ######### END OF DEFINITIONS ##########
 
 ##### QUESTION 1 #####
 blocks1 = generateBlocks()
 answer1 = generateSolution(blocks1)
 feedback1 = generateFeedback(blocks1)
 displayEquationLeft1 = blocks1[_sage_const_1 ]+blocks1[_sage_const_2 ]*x
 displayEquationRight1 = blocks1[_sage_const_4 ]*x-blocks1[_sage_const_5 ]
 
 ##### QUESTION 2 #####
 blocks2 = generateBlocks()
 answer2 = generateSolution(blocks2)
 feedback2 = generateFeedback(blocks2)
 displayEquationLeft2 = blocks2[_sage_const_1 ]+blocks2[_sage_const_2 ]*x
 displayEquationRight2 = blocks2[_sage_const_4 ]*x-blocks2[_sage_const_5 ]
 
 ##### QUESTION 3 #####
 blocks3 = generateBlocks()
 answer3 = generateSolution(blocks3)
 feedback3 = generateFeedback(blocks3)
 displayEquationLeft3 = blocks3[_sage_const_1 ]+blocks3[_sage_const_2 ]*x
 displayEquationRight3 = blocks3[_sage_const_4 ]*x-blocks3[_sage_const_5 ]
 
except:
 _st_.goboom(_sage_const_106 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_111 
 _st_.inline(_sage_const_0 , latex(blocks1[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_111 )
try:
 _st_.current_tex_line = _sage_const_111 
 _st_.inline(_sage_const_1 , latex(displayEquationLeft1))
except:
 _st_.goboom(_sage_const_111 )
try:
 _st_.current_tex_line = _sage_const_111 
 _st_.inline(_sage_const_2 , latex(blocks1[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_111 )
try:
 _st_.current_tex_line = _sage_const_111 
 _st_.inline(_sage_const_3 , latex(displayEquationRight1))
except:
 _st_.goboom(_sage_const_111 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_4 , latex(answer1))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_5 , latex(feedback1))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_6 , latex(blocks2[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_7 , latex(displayEquationLeft2))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_8 , latex(blocks2[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_9 , latex(displayEquationRight2))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_10 , latex(answer2))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_128 
 _st_.inline(_sage_const_11 , latex(feedback2))
except:
 _st_.goboom(_sage_const_128 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_12 , latex(blocks3[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_13 , latex(displayEquationLeft3))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_14 , latex(blocks3[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_15 , latex(displayEquationRight3))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_137 
 _st_.inline(_sage_const_16 , latex(answer3))
except:
 _st_.goboom(_sage_const_137 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_17 , latex(feedback3))
except:
 _st_.goboom(_sage_const_140 )
_st_.current_tex_line = _sage_const_146 
_st_.blockbegin()
try:
 # Type 2 - Solve Advanced linear equations (fractions)
 #(coefficients[0]*x + numerators[0])/denominators[0]
     # - (coefficients[1]*x+numerators[1])/denominators[1]
     # = (coefficients[2]*x+numerators[2])/denominators[2]
 
 x = var('x')
 ###################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 #No restrictions on coefficients or numerators
 def createThreeRandomIntegers():
     a = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     c = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     return [a, b, c]
 
 def createThreeDistinctRandomNaturals():
     possibleNaturals= range(_sage_const_2 ,_sage_const_7 )
     n1, n2, n3 = sample(possibleNaturals, _sage_const_3 )
     naturals = [Integer(n1), Integer(n2), Integer(n3)]
     return naturals
 
 def createThreeDistinctRandomIntegers():
     a, b, c = sample(range(_sage_const_3 , _sage_const_8 ), _sage_const_3 )
     return [Integer(maybeMakeNegative(a)), Integer(maybeMakeNegative(b)), Integer(maybeMakeNegative(c))]
 
 def createViableConstants():
     a, b, c = createThreeRandomIntegers()
     d, e, f = createThreeRandomIntegers()
     g, h, i = createThreeDistinctRandomNaturals()
     # Check that there is exactly one solution to the linear equation
     OneSolutionCheck = (a/g) - (b/h) - (c/i)
     while (OneSolutionCheck == _sage_const_0 ):
         a, b, c = createThreeRandomIntegers()
         d, e, f = createThreeRandomIntegers()
         g, h, i = createThreeDistinctRandomNaturals()
         OneSolutionCheck = (a/g) - (b/h) - (c/i)
     return [a, b, c, d, e, f, g, h, i]
 
 def createSolution(constants):
     a, b, c, d, e, f, g, h, i = constants
     equationBlockOne = (a*x+d)/g
     equationBlockTwo = (b*x+e)/h
     equationBlockThree = (c*x+f)/i
     toSolve = equationBlockOne - equationBlockTwo - equationBlockThree
     solution = round(float(solve(toSolve, x)[_sage_const_0 ].rhs()), _sage_const_3 )
     return solution
 
 def generateFeedback1(constants):
     a, b, c, d, e, f, g, h, i = constants
     equationBlockOne = (a*x+d)/g
     equationBlockTwo = (b*x-e)/h
     equationBlockThree = (c*x+f)/i
     toSolve = equationBlockOne - equationBlockTwo - equationBlockThree
     feedback = round(float(solve(toSolve, x)[_sage_const_0 ].rhs()), _sage_const_3 )
     return feedback
 
 def generateFeedback2(constants):
     a, b, c, d, e, f, g, h, i = constants
     equationBlockOne = (a*x)/g + d
     equationBlockTwo = (b*x)/h + e
     equationBlockThree = (c*x)/i + f
     toSolve = equationBlockOne - equationBlockTwo - equationBlockThree
     feedback = round(float(solve(toSolve, x)[_sage_const_0 ].rhs()), _sage_const_3 )
     return feedback
 
 def generateFeedback3(constants):
     a, b, c, d, e, f, g, h, i = constants
     equationBlockOne = (a*x)/g + d
     equationBlockTwo = (b*x)/h - e
     equationBlockThree = (c*x)/i + f
     toSolve = equationBlockOne - equationBlockTwo - equationBlockThree
     feedback = round(float(solve(toSolve, x)[_sage_const_0 ].rhs()), _sage_const_3 )
     return feedback
 
 
 ######## END OF DEFINITIONS ###########
 
 ##### QUESTION 4 #####
 constants4 = createViableConstants()
 displayNumeratorA4 = constants4[_sage_const_0 ] * x + constants4[_sage_const_3 ]
 displayNumeratorB4 = constants4[_sage_const_1 ] * x + constants4[_sage_const_4 ]
 displayNumeratorC4 = constants4[_sage_const_2 ] * x + constants4[_sage_const_5 ]
 answer4 = createSolution(constants4)
 feedback41 = generateFeedback1(constants4)
 feedback42 = generateFeedback2(constants4)
 feedback43 = generateFeedback3(constants4)
 
 ##### QUESTION 5 #####
 constants5 = createViableConstants()
 displayNumeratorA5 = constants5[_sage_const_0 ] * x + constants5[_sage_const_3 ]
 displayNumeratorB5 = constants5[_sage_const_1 ] * x + constants5[_sage_const_4 ]
 displayNumeratorC5 = constants5[_sage_const_2 ] * x + constants5[_sage_const_5 ]
 answer5 = createSolution(constants5)
 feedback51 = generateFeedback1(constants5)
 feedback52 = generateFeedback2(constants5)
 feedback53 = generateFeedback3(constants5)
 
 ##### QUESTION 6 #####
 constants6 = createViableConstants()
 displayNumeratorA6 = constants6[_sage_const_0 ] * x + constants6[_sage_const_3 ]
 displayNumeratorB6 = constants6[_sage_const_1 ] * x + constants6[_sage_const_4 ]
 displayNumeratorC6 = constants6[_sage_const_2 ] * x + constants6[_sage_const_5 ]
 answer6 = createSolution(constants6)
 feedback61 = generateFeedback1(constants6)
 feedback62 = generateFeedback2(constants6)
 feedback63 = generateFeedback3(constants6)
except:
 _st_.goboom(_sage_const_257 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_18 , latex(displayNumeratorA4))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_19 , latex(constants4[_sage_const_6 ]))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_20 , latex(displayNumeratorB4))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_21 , latex(constants4[_sage_const_7 ]))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_22 , latex(displayNumeratorC4))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_262 
 _st_.inline(_sage_const_23 , latex(constants4[_sage_const_8 ]))
except:
 _st_.goboom(_sage_const_262 )
try:
 _st_.current_tex_line = _sage_const_268 
 _st_.inline(_sage_const_24 , latex(answer4))
except:
 _st_.goboom(_sage_const_268 )
try:
 _st_.current_tex_line = _sage_const_273 
 _st_.inline(_sage_const_25 , latex(feedback41))
except:
 _st_.goboom(_sage_const_273 )
try:
 _st_.current_tex_line = _sage_const_275 
 _st_.inline(_sage_const_26 , latex(feedback42))
except:
 _st_.goboom(_sage_const_275 )
try:
 _st_.current_tex_line = _sage_const_277 
 _st_.inline(_sage_const_27 , latex(feedback43))
except:
 _st_.goboom(_sage_const_277 )
try:
 _st_.current_tex_line = _sage_const_284 
 _st_.inline(_sage_const_28 , latex(displayNumeratorA5))
except:
 _st_.goboom(_sage_const_284 )
try:
 _st_.current_tex_line = _sage_const_284 
 _st_.inline(_sage_const_29 , latex(constants5[_sage_const_6 ]))
except:
 _st_.goboom(_sage_const_284 )
try:
 _st_.current_tex_line = _sage_const_284 
 _st_.inline(_sage_const_30 , latex(displayNumeratorB5))
except:
 _st_.goboom(_sage_const_284 )
try:
 _st_.current_tex_line = _sage_const_284 
 _st_.inline(_sage_const_31 , latex(constants5[_sage_const_7 ]))
except:
 _st_.goboom(_sage_const_284 )
try:
 _st_.current_tex_line = _sage_const_284 
 _st_.inline(_sage_const_32 , latex(displayNumeratorC5))
except:
 _st_.goboom(_sage_const_284 )
try:
 _st_.current_tex_line = _sage_const_284 
 _st_.inline(_sage_const_33 , latex(constants5[_sage_const_8 ]))
except:
 _st_.goboom(_sage_const_284 )
try:
 _st_.current_tex_line = _sage_const_286 
 _st_.inline(_sage_const_34 , latex(answer5))
except:
 _st_.goboom(_sage_const_286 )
try:
 _st_.current_tex_line = _sage_const_291 
 _st_.inline(_sage_const_35 , latex(feedback51))
except:
 _st_.goboom(_sage_const_291 )
try:
 _st_.current_tex_line = _sage_const_293 
 _st_.inline(_sage_const_36 , latex(feedback52))
except:
 _st_.goboom(_sage_const_293 )
try:
 _st_.current_tex_line = _sage_const_295 
 _st_.inline(_sage_const_37 , latex(feedback53))
except:
 _st_.goboom(_sage_const_295 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_38 , latex(displayNumeratorA6))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_39 , latex(constants6[_sage_const_6 ]))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_40 , latex(displayNumeratorB6))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_41 , latex(constants6[_sage_const_7 ]))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_42 , latex(displayNumeratorC6))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_43 , latex(constants6[_sage_const_8 ]))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_304 
 _st_.inline(_sage_const_44 , latex(answer6))
except:
 _st_.goboom(_sage_const_304 )
try:
 _st_.current_tex_line = _sage_const_309 
 _st_.inline(_sage_const_45 , latex(feedback61))
except:
 _st_.goboom(_sage_const_309 )
try:
 _st_.current_tex_line = _sage_const_311 
 _st_.inline(_sage_const_46 , latex(feedback62))
except:
 _st_.goboom(_sage_const_311 )
try:
 _st_.current_tex_line = _sage_const_313 
 _st_.inline(_sage_const_47 , latex(feedback63))
except:
 _st_.goboom(_sage_const_313 )
_st_.endofdoc()
