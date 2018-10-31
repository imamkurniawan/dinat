import requests, wget, os
from bs4 import BeautifulSoup

def getTid():
        ## Fungsi untuk mengambil variabel DB_tid
        ## url_1 adalah halaman awal tempat memilih data apakah data akat di subset
        url_1 = 'https://www.esrl.noaa.gov/psd/cgi-bin/db_search/DBSearch.pl?Dataset=NOAA+High-resolution+Blended+Analysis&Variable=Sea+Surface+Temperature&group=0&submit=Search'
        page = requests.get(url_1)
        soup = BeautifulSoup(page.content,'html.parser')
        # print (soup.prettify)

        ## variabel tid_s untuk menampung semua link yg ada
        tid_s = []
        for links in soup.find_all('a'):
                tid_s.append(links.get('href'))
                
        ## variabel link tempat menampunk url untuk make plot or subset daily mean
        link = (tid_s[47]) #56
        # print (link)

        ## var menampung char pada link yang dipisahkan oleh karakter '&'
        var = link.split('&')
        
        ## var2 berisi key DB_tid dan value nya
        var2 = (var[3])
        # print (var2)
        
        chars = var2.split('=')
        # print (chars)
        DB_tid = chars[1]
        # print (DB_tid)
        return (DB_tid)

def inisisasi(DB_tid):
	## Fungsi untuk mengecek data terakhir yang sudah tersedia dan mengatur penamaan outfile
	## url_2 adalah halaman memilih parameter data sst exp: waktu, dll
        url_2 = 'https://www.esrl.noaa.gov/psd/cgi-bin/DataAccess.pl?DB_dataset=NOAA+High-resolution+Blended+Analysis&DB_variable=Sea+Surface+Temperature&DB_statistic=Mean&DB_tid='+DB_tid+'&DB_did=132&DB_vid=2423'
        page = requests.get(url_2)
	#print (page.content)
        soup = BeautifulSoup(page.content,'html.parser')
	
	## Inisiasi variabel global untuk dibaca diluar fungsi
        global end_year, end_month, end_day, filename
	
	## Set scrapping Range: Start - End Data
        td = soup.find_all('td')
        start_year = (td[2].get_text())
        start_month = (td[3].get_text())
        start_day = (td[4].get_text())
        end_year = (td[11].get_text())
        end_month = (td[12].get_text())
        end_day = (td[13].get_text())

	## Atur bulan menggunakan angka untuk keperluan penamaan file
        month_number = {
		"Jan":"01",
		"Feb":"02",
		"Mar":"03",
		"Apr":"04",
		"May":"05",
		"Jun":"06",
		"Jul":"07",
		"Aug":"08",
		"Sep":"09",
		"Oct":"10",
		"Nov":"11",
		"Dec":"12"
		}
        bln = month_number[end_month]

	## Atur tanggal menjadi tetap 2 digit
        day = 00
        if len(end_day)==1:
                day = "0"+end_day
        else:
                day = end_day

        ## Format penamaan file output
        filename = 'sst_indonesia_'+end_year+bln+day+'.nc'

def ftp_nc(end_year, end_month, end_day, path, filename, tid):
	## Fungsi untuk download ftp NetCDF file
	## url_3 adalah request halaman download ftp setelah melakukan set variabel data nc (Proses subset)

	## Set batas area grid 
	lat_begin = '20S'
	lat_end = '20N'
	lon_begin = '90E'
	lon_end = '150E'

	url_3 = 'https://www.esrl.noaa.gov/psd/cgi-bin/GrADS.pl?dataset=NOAA+High-resolution+Blended+Analysis&DB_did=132&file=%2FDatasets%2Fnoaa.oisst.v2.highres%2Fsst.day.mean.1981.nc+sst.day.mean.%25y4.nc+13562&variable=sst&DB_vid=2423&DB_tid='+tid+'&units=degC&longstat=Mean&DB_statistic=Mean&stat=&lat-begin='+lat_begin+'&lat-end='+lat_end+'&lon-begin='+lon_begin+'&lon-end='+lon_end+'&dim0=time&year_begin='+end_year+'&mon_begin='+end_month+'&day_begin='+end_day+'&year_end='+end_year+'&mon_end='+end_month+'&day_end='+end_day+'&X=lon&Y=lat&output=file&bckgrnd=black&use_color=on&fill=lines&cint=&range1=&range2=&scale=100&maskf=%2FDatasets%2Fnoaa.oisst.v2.highres%2Flsmask.oisst.v2.nc&maskv=Land-sea+mask&submit=Create+Plot+or+Subset+of+Data'
	
	page = requests.get(url_3)
	soup = BeautifulSoup(page.content,'html.parser')
	ftp = []
	for link in soup.find_all('a'):
		ftp.append(link.get('href'))
	download_link = (ftp[43])
	print (download_link)
	wget.download(download_link, out=path+filename)

def drawGrads(filename):
        os.system("grads -lbcx '/home/datin/Documents/Cloud97242/OTOMASI_SST/script/sst.gs "+filename+"'")

if __name__ == '__main__':
        ##
        # getTid() # untuk ngetes ajah
        DB_tid = getTid()
        print ('DB_tid : '+DB_tid)
        
        inisisasi(DB_tid)
        print ('Out Filename : '+filename)

	## Set lokasi penyimpanan data NetCDF
        path = '/home/datin/Documents/Cloud97242/OTOMASI_SST/sst_indonesia_daily_nc/'

        ftp_nc(end_year, end_month, end_day, path, filename, DB_tid)

        # filename = 'sst_indonesia_20181026.nc'
        # ftp_nc('2018','Oct','26',path,filename, DB_tid)

        drawGrads(filename)
