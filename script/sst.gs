function main(args)
'reinit'
* get argument
*file = 'sst_monthly_201809.nc'

file = subwrd(args,1);
path_source = '/home/datin/Documents/Cloud97242/OTOMASI_SST/sst_indonesia_daily_nc/'file
path_target = '/home/datin/Documents/Cloud97242/OTOMASI_SST/sst_indonesia_png/'file
'sdfopen 'path_source
'set gxout shaded'
*'set gxout shaded2'
'set mpdset hires'
'set clevs -20 21 22 23 24 25 26 27 28 29 30'
*'set ccols 16 17 18 19 20 21 22 23 24 25'
'd sst'
'/home/datin/Documents/Cloud97242/OTOMASI_SST/script/cbarn'
'draw title 'file' (C)'
'printim 'path_target'.png white'
