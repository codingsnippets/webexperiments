__author__ = 'Kevin'
import pyximport; pyximport.install()
import subprocess

with open("C:\Users\Kevin\Desktop\packages.txt") as f:
    for line in f:
        package = line.split("=")[0]
        subprocess.call('pip install -U %s' % package, shell=True)
