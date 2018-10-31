##istSpecificFile
import glob, os, sys, datetime, imageio

path = "/home/datin/Documents/Cloud97242/OTOMASI_SST/sst_indonesia_png/"
x = glob.glob(path+"sst_indonesia_201809*.png")
## Sortir berdasarkan nama file
x.sort()
for nama in x:
	print (nama)
	
def create_gif(x, duration):
	images = []
	for filename in x:
		print(filename)
		images.append(imageio.imread(filename))
	output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
	out_path = "/home/datin/Documents/Cloud97242/OTOMASI_SST/temp/"+output_file
	imageio.mimsave(out_path, images, duration=duration)

if __name__ == "__main__":
	duration = 0.50
	create_gif(x, duration)
