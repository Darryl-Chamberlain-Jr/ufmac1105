## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file constructCorrectModel.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_37 = Integer(37); _sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_2 = Integer(2); _sage_const_10 = Integer(10); _sage_const_31 = Integer(31); _sage_const_15 = Integer(15); _sage_const_0p01 = RealNumber('0.01'); _sage_const_49 = Integer(49); _sage_const_51 = Integer(51); _sage_const_0 = Integer(0); _sage_const_3 = Integer(3); _sage_const_6 = Integer(6); _sage_const_53 = Integer(53); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_58 = Integer(58); _sage_const_100 = Integer(100); _sage_const_1001 = Integer(1001); _sage_const_1000 = Integer(1000); _sage_const_64 = Integer(64); _sage_const_66 = Integer(66); _sage_const_9 = Integer(9); _sage_const_68 = Integer(68); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_72 = Integer(72); _sage_const_26 = Integer(26); _sage_const_0p05 = RealNumber('0.05'); _sage_const_80 = Integer(80); _sage_const_83 = Integer(83); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_85 = Integer(85); _sage_const_16 = Integer(16); _sage_const_90 = Integer(90); _sage_const_9p8 = RealNumber('9.8'); _sage_const_96 = Integer(96); _sage_const_99 = Integer(99); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_101 = Integer(101); _sage_const_19 = Integer(19); _sage_const_105 = Integer(105); _sage_const_0p5 = RealNumber('0.5'); _sage_const_5730 = Integer(5730); _sage_const_113 = Integer(113); _sage_const_118 = Integer(118); _sage_const_20 = Integer(20); _sage_const_123 = Integer(123); _sage_const_60 = Integer(60); _sage_const_133 = Integer(133); _sage_const_136 = Integer(136); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_138 = Integer(138); _sage_const_23 = Integer(23); _sage_const_142 = Integer(142); _sage_const_150 = Integer(150); _sage_const_152 = Integer(152); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_154 = Integer(154); _sage_const_27 = Integer(27)## This file (constructCorrectModel.sagetex.sage) was *autogenerated* from constructCorrectModel.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('constructCorrectModel', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_37 
_st_.blockbegin()
try:
 v = var('v')
 concA = ZZ.random_element(_sage_const_1 , _sage_const_4 )*_sage_const_5 
 concB = ZZ.random_element(_sage_const_2 , _sage_const_5 )*_sage_const_10 
 concTotal = ZZ.random_element(_sage_const_10 , _sage_const_31 )
 while concTotal < concA or concTotal > concB:
     concTotal = ZZ.random_element(_sage_const_10 , _sage_const_31 )
 totalVolume = ZZ.random_element(_sage_const_5 , _sage_const_15 )
 eqPartA6 = totalVolume - v
 eqPartB6 = concA * _sage_const_0p01  * v
 eqPartC6 = concB * _sage_const_0p01  * eqPartA6
 eqPartD6 = eqPartB6 + eqPartC6
except:
 _st_.goboom(_sage_const_49 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_51 
 _st_.inline(_sage_const_0 , latex(concA))
except:
 _st_.goboom(_sage_const_51 )
try:
 _st_.current_tex_line = _sage_const_51 
 _st_.inline(_sage_const_1 , latex(concB))
except:
 _st_.goboom(_sage_const_51 )
try:
 _st_.current_tex_line = _sage_const_51 
 _st_.inline(_sage_const_2 , latex(totalVolume))
except:
 _st_.goboom(_sage_const_51 )
try:
 _st_.current_tex_line = _sage_const_51 
 _st_.inline(_sage_const_3 , latex(concTotal))
except:
 _st_.goboom(_sage_const_51 )
try:
 _st_.current_tex_line = _sage_const_51 
 _st_.inline(_sage_const_4 , latex(concTotal))
except:
 _st_.goboom(_sage_const_51 )
try:
 _st_.current_tex_line = _sage_const_51 
 _st_.inline(_sage_const_5 , latex(concTotal))
except:
 _st_.goboom(_sage_const_51 )
try:
 _st_.current_tex_line = _sage_const_51 
 _st_.inline(_sage_const_6 , latex(concA))
except:
 _st_.goboom(_sage_const_51 )
try:
 _st_.current_tex_line = _sage_const_53 
 _st_.inline(_sage_const_7 , latex(concTotal))
except:
 _st_.goboom(_sage_const_53 )
try:
 _st_.current_tex_line = _sage_const_53 
 _st_.inline(_sage_const_8 , latex(eqPartD6))
except:
 _st_.goboom(_sage_const_53 )
_st_.current_tex_line = _sage_const_58 
_st_.blockbegin()
try:
 t = var('t')
 halfLifeYears2 = ZZ.random_element(_sage_const_100 , _sage_const_1001 )*ZZ.random_element(_sage_const_100 , _sage_const_1001 )
 initialAmount2 = ZZ.random_element(_sage_const_100 , _sage_const_1000 )
 k2 = -ln(_sage_const_2 )/halfLifeYears2
 equation2 = initialAmount2*e**(k2*t)
except:
 _st_.goboom(_sage_const_64 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_66 
 _st_.inline(_sage_const_9 , latex(initialAmount2))
except:
 _st_.goboom(_sage_const_66 )
try:
 _st_.current_tex_line = _sage_const_66 
 _st_.inline(_sage_const_10 , latex(halfLifeYears2))
except:
 _st_.goboom(_sage_const_66 )
try:
 _st_.current_tex_line = _sage_const_68 
 _st_.inline(_sage_const_11 , latex(initialAmount2))
except:
 _st_.goboom(_sage_const_68 )
try:
 _st_.current_tex_line = _sage_const_68 
 _st_.inline(_sage_const_12 , latex(k2))
except:
 _st_.goboom(_sage_const_68 )
_st_.current_tex_line = _sage_const_72 
_st_.blockbegin()
try:
 x = var("x")
 fixedCost1 = ZZ.random_element(_sage_const_10 , _sage_const_26 )*_sage_const_1000 
 productionCost1 = round(ZZ.random_element(_sage_const_1 , _sage_const_4 )*_sage_const_0p05 , _sage_const_2 )
 sellingPoint1 = round(productionCost1*ZZ.random_element(_sage_const_1 , _sage_const_4 ), _sage_const_2 )
 costs1 = productionCost1*x + fixedCost1
 profits1 = sellingPoint1*x
 revenue1 = profits1 - costs1
except:
 _st_.goboom(_sage_const_80 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_13 , latex(fixedCost1))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_14 , latex(productionCost1))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_15 , latex(sellingPoint1))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_85 
 _st_.inline(_sage_const_16 , latex(revenue1))
except:
 _st_.goboom(_sage_const_85 )
_st_.current_tex_line = _sage_const_90 
_st_.blockbegin()
try:
 k = var('k')
 a = var('a')
 k4 = round((_sage_const_4 *pi**_sage_const_2 ) / (_sage_const_9p8 ), _sage_const_3 )
 a4 = ZZ.random_element(_sage_const_3 , _sage_const_9 )
 T4 = round(k4*sqrt(a4**_sage_const_3 )*_sage_const_12 , _sage_const_2 )
except:
 _st_.goboom(_sage_const_96 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_17 , latex(a4))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_18 , latex(T4))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_19 , latex(k4))
except:
 _st_.goboom(_sage_const_101 )
_st_.current_tex_line = _sage_const_105 
_st_.blockbegin()
try:
 t = var('t')
 r = var('r')
 k5 = ln(_sage_const_0p5 )/_sage_const_5730 
 equation5A = e**(t*k5)
 equation5B = ln(r)/k5
 percent5 = ZZ.random_element(_sage_const_1 , _sage_const_101 )
 old5 = round(equation5B(percent5*_sage_const_0p01 ), _sage_const_0 )
except:
 _st_.goboom(_sage_const_113 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_20 , latex(_sage_const_1 /k5))
except:
 _st_.goboom(_sage_const_118 )
_st_.current_tex_line = _sage_const_123 
_st_.blockbegin()
try:
 m = var('m')
 officerAspeed3 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 officerBspeed3 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 while officerAspeed3 == officerBspeed3:
     officerAspeed3 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
     officerBspeed3 = ZZ.random_element(_sage_const_2 , _sage_const_7 )
 partA3 = officerAspeed3/_sage_const_60  * m
 partB3 = officerAspeed3/_sage_const_60  * m + officerBspeed3/_sage_const_60  * m
 partC3 = sqrt((officerAspeed3/_sage_const_60 )**_sage_const_2  + (officerBspeed3/_sage_const_60 )**_sage_const_2 )*m
except:
 _st_.goboom(_sage_const_133 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_21 , latex(officerAspeed3))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_22 , latex(officerBspeed3))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_23 , latex(partC3))
except:
 _st_.goboom(_sage_const_138 )
_st_.current_tex_line = _sage_const_142 
_st_.blockbegin()
try:
 t = var('t')
 rateList1 = ["doubles", "triples", "quadruples"]
 choose8 = ZZ.random_element(_sage_const_0 , _sage_const_3 )
 rate8 = rateList1[choose8]
 initialBacteria8 = ZZ.random_element(_sage_const_1 , _sage_const_9 )*_sage_const_100 
 k8 = ln(choose8+_sage_const_2 )
 bacteriaPopulation8 = initialBacteria8 * (choose8 + _sage_const_2 )**(k8*t)
except:
 _st_.goboom(_sage_const_150 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_24 , latex(rate8))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_25 , latex(initialBacteria8))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_26 , latex(initialBacteria8))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_27 , latex(choose8+_sage_const_2 ))
except:
 _st_.goboom(_sage_const_154 )
_st_.endofdoc()
