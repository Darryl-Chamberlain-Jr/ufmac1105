## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file convertSlopeInterceptStandard.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_33 = Integer(33); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_9 = Integer(9); _sage_const_0 = Integer(0); _sage_const_86 = Integer(86); _sage_const_92 = Integer(92); _sage_const_94 = Integer(94); _sage_const_3 = Integer(3); _sage_const_101 = Integer(101); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_103 = Integer(103); _sage_const_6 = Integer(6); _sage_const_7 = Integer(7); _sage_const_110 = Integer(110); _sage_const_8 = Integer(8); _sage_const_116 = Integer(116); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_123 = Integer(123); _sage_const_12 = Integer(12); _sage_const_129 = Integer(129); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15)## This file (convertSlopeInterceptStandard.sagetex.sage) was *autogenerated* from convertSlopeInterceptStandard.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('convertSlopeInterceptStandard', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_33 
_st_.blockbegin()
try:
 x = var('x')
 y = var('y')
 
 #################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def standardToSlopeInt():
     A = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     B = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     C = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     while gcd(A, B) > _sage_const_1  or gcd(A, C) > _sage_const_1 :
         A = ZZ.random_element(_sage_const_2 , _sage_const_9 )
         B = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         C = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     slope = float(-A/B)
     yInt = float(C/B)
     return [A, B, C, slope, yInt]
 
 def sloptIntToStandard():
     mNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     mDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     yIntNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     yIntDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     while gcd(mNum, mDenom) > _sage_const_1  or gcd(yIntNum, yIntDenom) > _sage_const_1  or mDenom == yIntDenom:
         mNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         mDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
         yIntNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         yIntDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     slope = mNum/mDenom
     yInt = yIntNum/yIntDenom
     lcmConstant = (mDenom*yIntDenom/gcd(mDenom, yIntDenom))
     if mNum < _sage_const_0 :
         A = -mNum*lcmConstant/mDenom
         B = lcmConstant
         C = yIntNum*lcmConstant/yIntDenom
     else:
         A = mNum*lcmConstant/mDenom
         B = -lcmConstant
         C = -yIntNum*lcmConstant/yIntDenom
     return [A, B, C, slope, yInt]
 ###############
 A1, B1, C1, slope1, yInt1 = standardToSlopeInt()
 equationXY1 = A1*x + B1*y
 A2, B2, C2, slope2, yInt2 = standardToSlopeInt()
 equationXY2 = A2*x + B2*y
 A3, B3, C3, slope3, yInt3 = sloptIntToStandard()
 equationSlopeInt3 = slope3*x + yInt3
 A4, B4, C4, slope4, yInt4 = sloptIntToStandard()
 equationSlopeInt4 = slope4*x + yInt4
except:
 _st_.goboom(_sage_const_86 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_0 , latex(equationXY1))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_92 
 _st_.inline(_sage_const_1 , latex(C1))
except:
 _st_.goboom(_sage_const_92 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.inline(_sage_const_2 , latex(slope1))
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.inline(_sage_const_3 , latex(yInt1))
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_4 , latex(equationXY2))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_5 , latex(C2))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_6 , latex(slope2))
except:
 _st_.goboom(_sage_const_103 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_7 , latex(yInt2))
except:
 _st_.goboom(_sage_const_103 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_8 , latex(equationSlopeInt3))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_9 , latex(A3))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_10 , latex(B3))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_11 , latex(C3))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_12 , latex(equationSlopeInt4))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_13 , latex(A4))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_14 , latex(B4))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_15 , latex(C4))
except:
 _st_.goboom(_sage_const_129 )
_st_.endofdoc()

