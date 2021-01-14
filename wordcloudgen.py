#!/usr/bin/env python3

from sys import argv, exit
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

class WordCloudMaker:
	def __init__(self, in_file, in_img, colormap, bg_color, width, height):
		self.in_file = in_file
		self.in_img = in_img
		self.colormap = colormap
		self.bg_color = bg_color
		self.width = width
		self.height = height

	def make_word_cloud(self):
		try:
			with open(self.in_file, 'r') as file:
				text = file.read()
		except:
			print(f"[*]Error: {self.in_file} not found.")

		if self.in_img != '':
			mask = np.array(Image.open(self.in_img))
		else:
			mask = None

		stopwords = STOPWORDS
		stopwords.update(['us', 'one', 'will', 'said', 'now', 'well',
			'man', 'may', 'little', 'say', 'must', 'way', 'long',
			'yet', 'mean', 'put', 'seem', 'asked', 'made', 'half', 
			'much', 'certainly', 'might', 'came'])

		word_cloud = WordCloud(max_words=500, relative_scaling=0.4, mask=mask,
			width=self.width, height=self.height, background_color=self.bg_color,
			stopwords=stopwords, margin=5, random_state=7, colormap=self.colormap).generate(text)

		colors = word_cloud.to_array()

		plt.figure()
		plt.imshow(colors, interpolation='bilinear')
		plt.axis('off')
		plt.show()

	def args_check(args_keys):
		args_values = [arg for arg in argv if argv.index(arg) % 2 == 0]
		for arg in args_values:
			if arg in args_keys:
				return True
		return False

	def help():
		print("""
Usage: {} -f <filename> [options]

Options:
  -i, image render for custom shapes.
  -cm, color for colormap, for more colors refer the link below
      https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
  -bg, background color for the word cloud.
  -wd, width of the word cloud.
  -ht, height of the word cloud.
""".format(argv[0]))


## End of class

def main():
	print("""


 __          __           _    _____ _                 _ 
 \ \        / /          | |  / ____| |               | |
  \ \  /\  / /__  _ __ __| | | |    | | ___  _   _  __| |
   \ \/  \/ / _ \| '__/ _` | | |    | |/ _ \| | | |/ _` |
    \  /\  / (_) | | | (_| | | |____| | (_) | |_| | (_| |
     \/  \/ \___/|_|  \__,_|  \_____|_|\___/ \__,_|\__,_|
                                                         
                                                         
""")
	if len(argv) > 1 and len(argv) < 14:
		args_keys = ['-f','-i', '-cm', '-bg', '-wd', '-ht']
		args_dict = {}
		in_args = [arg for arg in argv if argv.index(arg) % 2 != 0]
		if argv[1] in ['-h', '--help']:
			WordCloudMaker.help()
			exit(0)
		elif '-f' not in in_args:
			print("[*]Error: Please provide input file.")
			exit(1)
		elif len(argv) % 2 != 1 or WordCloudMaker.args_check(args_keys):
			print("[*]Error: Value not specified to the options.")
			WordCloudMaker.help()
			exit(1)
		else:
			for arg in in_args:
				if arg in args_keys:
					args_dict[arg] = argv[argv.index(arg) + 1]
					#print(args_dict)
				else:
					print("[*]Error: Invalid Arguments.")
					WordCloudMaker.help()
					exit(1)

		if '-wd' in args_dict:
			if args_dict['-wd'].isdigit():
				args_dict['-wd'] = int(args_dict['-wd'])
			else:
				print("[*]Error: width must be an integer.")
				exit(1)
		else:
			args_dict['-wd'] = 1000

		if '-ht' in args_dict:
			if args_dict['-ht'].isdigit():
				args_dict['-ht'] = int(args_dict['-ht'])
			else:
				print("[*]Error: height must be an integer.")
				exit(1)
		else:
			args_dict['-ht'] = 800

		if '-i' not in in_args:
			args_dict['-i'] = ''

		if '-cm' not in in_args:
			args_dict['-cm'] = 'Set2'

		if '-bg' not in in_args:
			args_dict['-bg'] = 'black'

		wc = WordCloudMaker(args_dict['-f'], args_dict['-i'], args_dict['-cm'], args_dict['-bg'], args_dict['-wd'], args_dict['-ht'])
		wc.make_word_cloud()
	else:
		print("Help:")
		print(f"  {argv[0]} --help")

if __name__ == "__main__":
	main()