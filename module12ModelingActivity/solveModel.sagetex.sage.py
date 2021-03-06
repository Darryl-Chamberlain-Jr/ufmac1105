## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file solveModel.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_32 = Integer(32); _sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_2 = Integer(2); _sage_const_10 = Integer(10); _sage_const_31 = Integer(31); _sage_const_15 = Integer(15); _sage_const_0p01 = RealNumber('0.01'); _sage_const_0 = Integer(0); _sage_const_46 = Integer(46); _sage_const_48 = Integer(48); _sage_const_3 = Integer(3); _sage_const_50 = Integer(50); _sage_const_52 = Integer(52); _sage_const_6 = Integer(6); _sage_const_7 = Integer(7); _sage_const_57 = Integer(57); _sage_const_101 = Integer(101); _sage_const_100 = Integer(100); _sage_const_1000 = Integer(1000); _sage_const_65 = Integer(65); _sage_const_67 = Integer(67); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_69 = Integer(69); _sage_const_11 = Integer(11); _sage_const_73 = Integer(73); _sage_const_26 = Integer(26); _sage_const_0p05 = RealNumber('0.05'); _sage_const_86 = Integer(86); _sage_const_89 = Integer(89); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_91 = Integer(91); _sage_const_96 = Integer(96); _sage_const_9p8 = RealNumber('9.8'); _sage_const_106 = Integer(106); _sage_const_109 = Integer(109); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_111 = Integer(111); _sage_const_19 = Integer(19); _sage_const_115 = Integer(115); _sage_const_0p5 = RealNumber('0.5'); _sage_const_5730 = Integer(5730); _sage_const_123 = Integer(123); _sage_const_126 = Integer(126); _sage_const_20 = Integer(20); _sage_const_128 = Integer(128); _sage_const_21 = Integer(21); _sage_const_133 = Integer(133); _sage_const_60 = Integer(60); _sage_const_145 = Integer(145); _sage_const_148 = Integer(148); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_24 = Integer(24); _sage_const_150 = Integer(150); _sage_const_25 = Integer(25); _sage_const_154 = Integer(154); _sage_const_1000000 = Integer(1000000); _sage_const_163 = Integer(163); _sage_const_165 = Integer(165); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_167 = Integer(167); _sage_const_29 = Integer(29)## This file (solveModel.sagetex.sage) was *autogenerated* from solveModel.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveModel', version='2019/11/14 v3.4', version_check=True)
_st_.current_tex_line = _sage_const_32 
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
 volumeA = solve(eqPartD6==concTotal*totalVolume*_sage_const_0p01 , v)[_sage_const_0 ].rhs()
 volumeB = eqPartA6(volumeA)
except:
 _st_.goboom(_sage_const_46 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_48 
 _st_.inline(_sage_const_0 , latex(concA))
except:
 _st_.goboom(_sage_const_48 )
try:
 _st_.current_tex_line = _sage_const_48 
 _st_.inline(_sage_const_1 , latex(concB))
except:
 _st_.goboom(_sage_const_48 )
try:
 _st_.current_tex_line = _sage_const_48 
 _st_.inline(_sage_const_2 , latex(totalVolume))
except:
 _st_.goboom(_sage_const_48 )
try:
 _st_.current_tex_line = _sage_const_48 
 _st_.inline(_sage_const_3 , latex(concTotal))
except:
 _st_.goboom(_sage_const_48 )
try:
 _st_.current_tex_line = _sage_const_50 
 _st_.inline(_sage_const_4 , latex(concA))
except:
 _st_.goboom(_sage_const_50 )
try:
 _st_.current_tex_line = _sage_const_50 
 _st_.inline(_sage_const_5 , latex(volumeA))
except:
 _st_.goboom(_sage_const_50 )
try:
 _st_.current_tex_line = _sage_const_52 
 _st_.inline(_sage_const_6 , latex(concB))
except:
 _st_.goboom(_sage_const_52 )
try:
 _st_.current_tex_line = _sage_const_52 
 _st_.inline(_sage_const_7 , latex(volumeB))
except:
 _st_.goboom(_sage_const_52 )
_st_.current_tex_line = _sage_const_57 
_st_.blockbegin()
try:
 t = var('t')
 halfLifeYears2 = ZZ.random_element(_sage_const_10 , _sage_const_101 )*ZZ.random_element(_sage_const_10 , _sage_const_101 )
 afterYears = halfLifeYears2 + ZZ.random_element(_sage_const_50 , _sage_const_101 )
 initialAmount2 = ZZ.random_element(_sage_const_100 , _sage_const_1000 )
 k2 = ln(_sage_const_1 /_sage_const_2 )/halfLifeYears2
 equation2 = initialAmount2*e**(k2*t)
 amountLeft = equation2(afterYears)
except:
 _st_.goboom(_sage_const_65 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_8 , latex(initialAmount2))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_9 , latex(halfLifeYears2))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_10 , latex(afterYears))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_69 
 _st_.inline(_sage_const_11 , latex(amountLeft))
except:
 _st_.goboom(_sage_const_69 )
_st_.current_tex_line = _sage_const_73 
_st_.blockbegin()
try:
 x = var("x")
 fixedCost1 = ZZ.random_element(_sage_const_10 , _sage_const_26 )*_sage_const_1000 
 productionCost1 = round(ZZ.random_element(_sage_const_1 , _sage_const_4 )*_sage_const_0p05 , _sage_const_2 )
 sellingPoint1 = round(productionCost1*ZZ.random_element(_sage_const_2 , _sage_const_5 ), _sage_const_2 )
 costs1 = productionCost1*x + fixedCost1
 profits1 = sellingPoint1*x
 revenue1 = profits1 - costs1
 exactBreakEven = solve(revenue1==_sage_const_0 , x)[_sage_const_0 ].rhs()
 if exactBreakEven > round(exactBreakEven, _sage_const_0 ):
     breakEven = round(exactBreakEven, _sage_const_0 ) + _sage_const_1 
 else:
     breakEven = round(exactBreakEven, _sage_const_0 )
except:
 _st_.goboom(_sage_const_86 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_12 , latex(fixedCost1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_13 , latex(productionCost1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_14 , latex(sellingPoint1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_15 , latex(breakEven))
except:
 _st_.goboom(_sage_const_91 )
_st_.current_tex_line = _sage_const_96 
_st_.blockbegin()
try:
 k1 = (_sage_const_4 *pi**_sage_const_2 ) / (_sage_const_9p8 )
 a1 = ZZ.random_element(_sage_const_3 , _sage_const_9 )
 saturnA = a1 - ZZ.random_element(_sage_const_1 , _sage_const_3 )
 while (saturnA > a1):
     a1 = ZZ.random_element(_sage_const_3 , _sage_const_9 )
     saturnA = a1 - ZZ.random_element(_sage_const_1 , _sage_const_3 )
 T1 = round(k1*sqrt(a1**_sage_const_3 )*_sage_const_12 , _sage_const_2 )
 saturnMonths = round(k1*sqrt(saturnA**_sage_const_3 )*_sage_const_12 , _sage_const_2 )
 
except:
 _st_.goboom(_sage_const_106 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_16 , latex(a1))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_17 , latex(T1))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_18 , latex(saturnMonths))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_111 
 _st_.inline(_sage_const_19 , latex(saturnA))
except:
 _st_.goboom(_sage_const_111 )
_st_.current_tex_line = _sage_const_115 
_st_.blockbegin()
try:
 t = var('t')
 r = var('r')
 k3 = ln(_sage_const_0p5 )/_sage_const_5730 
 equation3A = e**(t*k3)
 equation3B = ln(r)/k3
 percent3 = ZZ.random_element(_sage_const_1 , _sage_const_101 )
 old3 = round(equation3B(percent3*_sage_const_0p01 ), _sage_const_0 )
except:
 _st_.goboom(_sage_const_123 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_20 , latex(percent3))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_128 
 _st_.inline(_sage_const_21 , latex(old3))
except:
 _st_.goboom(_sage_const_128 )
_st_.current_tex_line = _sage_const_133 
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
 distanceOfficers = ZZ.random_element(_sage_const_2 , _sage_const_5 )
 timeOfficers = solve(partC3 == distanceOfficers, m)[_sage_const_0 ].rhs()
except:
 _st_.goboom(_sage_const_145 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_148 
 _st_.inline(_sage_const_22 , latex(officerAspeed3))
except:
 _st_.goboom(_sage_const_148 )
try:
 _st_.current_tex_line = _sage_const_148 
 _st_.inline(_sage_const_23 , latex(officerBspeed3))
except:
 _st_.goboom(_sage_const_148 )
try:
 _st_.current_tex_line = _sage_const_148 
 _st_.inline(_sage_const_24 , latex(distanceOfficers))
except:
 _st_.goboom(_sage_const_148 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_25 , latex(timeOfficers))
except:
 _st_.goboom(_sage_const_150 )
_st_.current_tex_line = _sage_const_154 
_st_.blockbegin()
try:
 t = var('t')
 rateList1 = ["doubles", "triples", "quadruples"]
 choose1 = ZZ.random_element(_sage_const_0 , _sage_const_3 )
 rate1 = rateList1[choose1]
 initialBacteria1 = ZZ.random_element(_sage_const_1 , _sage_const_9 )*_sage_const_100 
 bacteriaPopulation1 = initialBacteria1 * (choose1 + _sage_const_2 )**(t)
 hugeBacteriaPopulation = ZZ.random_element(_sage_const_1 , _sage_const_9 )
 timeToHugePopulation = solve(bacteriaPopulation1 == hugeBacteriaPopulation*_sage_const_1000000 , t)[_sage_const_0 ].rhs()
except:
 _st_.goboom(_sage_const_163 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_165 
 _st_.inline(_sage_const_26 , latex(rate1))
except:
 _st_.goboom(_sage_const_165 )
try:
 _st_.current_tex_line = _sage_const_165 
 _st_.inline(_sage_const_27 , latex(initialBacteria1))
except:
 _st_.goboom(_sage_const_165 )
try:
 _st_.current_tex_line = _sage_const_165 
 _st_.inline(_sage_const_28 , latex(hugeBacteriaPopulation))
except:
 _st_.goboom(_sage_const_165 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_29 , latex(timeToHugePopulation))
except:
 _st_.goboom(_sage_const_167 )
_st_.endofdoc()

