import os
from pyproc import *
procOpts(nprocess=2)
FID('/Users/pipapa/Downloads/Julia-2021_0819/2')
CREATE('/Users/pipapa/Downloads/Julia-2021_0819/2/RRM1_HSQC_35C_pH6p8_HSQC.nv')
acqOrder('21')
acqarray(0,0)
fixdsp(True)
skip(0,0)
label('1H','15N')
acqsize(0,0)
tdsize(0,0)
sf('SFO1,1','SFO1,2')
sw('SW_h,1','SW_h,2')
ref('','N')
DIM(1)
TDCOMB(dim=2,coef='echo-antiecho-r')
TDSS()
SB()
ZF()
FT()
PHASE(ph0=67.5,ph1=0.0,dimag=False)
EXTRACT()
DIM(2)
LP()
SB(c=0.5)
ZF()
FT(negateImag=True)
PHASE(ph0=0.0,ph1=0.0)
run()