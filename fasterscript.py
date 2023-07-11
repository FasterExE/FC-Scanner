#!/usr/bin/python
# Author :  𓆩 𝐈𝐋𝐘𝐀𝐒𝐒 𓆪
# @faster_exe
#Account link https://t.me/faster_exe
# version : 1.1



import subprocess
import sys
import os


class SuperScanner:

	def __init__(self):
		self.lines = []
		self.filename = ""

	def printCredits(self):
		print("""
        _______ __   __   __ ______ _______ _______
       /__  __// /  / /  / // __  // _____// _____/
        / /   / /  / /__/ // /_/ // /____ / /____
       / /   / /  /__  __// __  //____  //____  /
    __/ /__ / /____ / /  / / / /_____/ /_____/ /
   /______//______//_/  /_/ /_//______//______/
	                                                                              
		""")

		print("   Happy Scanning Script by:  𓆩 𝐈𝐋𝐘𝐀𝐒𝐒 𓆪 ")
		print("            @FasterExE  @RAYANDIAG            	")   
		print("      https://t.me/FasterExE   	")  


	def getFilename(self):
		self.filename = sys.argv[1]

	def loadIP(self):
		with open(self.filename) as f:
			self.lines = [line.rstrip('\n') for line in f]
		print(f"\n\nThere are {len(self.lines)} in {self.filename} \n\n")

	def executeCommands(self):
		target = ""
		targeted = ""
		
		
		if len(sys.argv) >= 4: 
			if sys.argv[3] == "target":
				target = "--target cloudflare.net"
				targeted = "target"
			elif sys.argv[3] == "target2":
				target = "--target amir5.tk"
				targeted = "target2"
			else:
				pass
		for ip in self.lines:
			print(f"cdn-ssl {ip} {targeted}")
			os.system(f"bugscanner-go scan cdn-ssl -c {ip} {target} -t700 -o Ilyass_files/scanned_{sys.argv[1]}")
			
	def executeCommands2(self):
		os.system(f"bugscanner-go scan direct -f {sys.argv[1]} -o Ilyass_files/scanned_{sys.argv[1]}")
	def run(self):
		self.printCredits()
		self.getFilename()
		self.loadIP()
		if sys.argv[2] == "cdn":
			self.executeCommands()
		elif sys.argv[2] == "direct":
			self.executeCommands2()
			
		print("All Commands has been run successfully!")


if __name__ == "__main__":
	scan = SuperScanner()
	scan.run()


