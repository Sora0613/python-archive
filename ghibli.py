import os
import pprint
import time
import requests
import urllib.error
import urllib.request
import os.path

works_text_box = input("[NOTICE]どの作品の画像をダウンロードするのか入力してください。(例：http://www.ghibli.jp/works/kazetachinu/ なら kazetachinu の部分を入力)：")
dir_text_box = input("[NOTICE]保存するディレクトリを指定してください。(例：/Users/UserName/Documents)：")

if os.path.isdir(dir_text_box) == False:
	os.mkdir(dir_text_box)

def download_file(url, dst_path):
	try:
		with urllib.request.urlopen(url) as web_file:
			data = web_file.read()
			with open(dst_path, mode='wb') as local_file:
				local_file.write(data)
	except urllib.error.URLError as e:
		print(e)

def download_file_to_dir(url, dst_dir):
	download_file(url, os.path.join(dst_dir, os.path.basename(url)))

url_list = ["http://www.ghibli.jp/gallery/"+ works_text_box +"{:03}.jpg".format(i) for i in range(51)]


for url in url_list:
	print("[NOTICE]Downloading")
	print(url)
	download_file_to_dir(url, dir_text_box)
	#time.sleep(2)
