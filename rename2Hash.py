# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import argparse

hashType = "sha256"

def hash(file, method):
	if not os.path.isdir(file):
		f = open(file, 'rb')
		sum = ""
		if method == "sha1":
			sum = hashlib.sha1(f.read()).hexdigest()
		elif method == "sha224":
			sum = hashlib.sha224(f.read()).hexdigest()
		elif method == "sha256":
			sum = hashlib.sha256(f.read()).hexdigest()
		elif method == "sha384":
			sum = hashlib.sha384(f.read()).hexdigest()
		elif method == "sha512":
			sum = hashlib.sha512(f.read()).hexdigest()
		elif method == "md5":
			sum = hashlib.md5(f.read()).hexdigest()
		f.close()
		return sum
	else:
		return "dir"

def renameFiles (path):
	unsorted = os.listdir(path)
	filelist = sorted(unsorted, key=len)
	for file in filelist:
		if not file == "rename2Hash.py":
			sum = hash(path + "\\" + file, hashType)
			try:
				print("Trying to rename: " + file)
				if os.path.isfile(path + "\\" + sum):                   # 如果文件名已经存在
					print("file " + sum + " already exists")
					if file != (sum):
						print("Removing: " + file + " because it is a duplicate")
						os.remove(path + "\\" + file)
				elif sum != "dir":                                      # 非文件夹
					os.rename(path + "\\" + file, path + "\\" + sum)
					print(file + ' --> ' + sum)
				else:                                                   # 如果到了这里说明非文件夹且指定文件不存在
					renameFiles(path + "\\" + file)
			except Exception as e:
				print("Error displaying file name.")
		print("")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='you need to input hash type and directory path')
	parser.add_argument("--type", type = str, help = "hash type, like md5 sha256, default is sha256")
	parser.add_argument("--dir", type = str, required = True, help = "Directory path")                 #必要参数
	args = parser.parse_args()
	if args.type != None:
		hashType = args.type
	renameFiles(args.dir)

