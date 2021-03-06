'sdfopen ../uwnd850_indonesia_daily_nc/uwnd850_indonesia_20181017.nc'
'define u = uwnd'
'sdfopen ../vwnd850_indonesia_daily_nc/vwnd850_indonesia_20181017.nc'
'set dfile 2'
'define v = vwnd'
'define u85=u*2.0'
'define v85=v*2.0'
'define wind=sqrt(u85*u85+v85*v85)'
'set grads off'
'set grid off'
'set mpdset hires'
'set csmooth on'
'set gxout shaded'
'd wind'
'cbarn'
'set gxout stream'
'set strmden 4'
'd u;v'
'draw xlab Bujur'
'draw ylab Lintang'
'draw title Angin 850 mb bulan September 2018'
'printim anginSeptember2018.gif x1600 y1200 white'
