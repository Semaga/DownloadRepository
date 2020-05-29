import os

def MakeClone(url):
	linkFromGit = url
	comandInstalFromGit = 'git clone '
	NameOfNewDir = url.split('/')[-1]
	try:
		os.system(comandInstalFromGit+linkFromGit)
		print("\n\tRepository {}  was download".format(NameOfNewDir))
	except OSError:
		print("\n\tThe repository is already in this directory.")

def InstallReq(NameOfNewDir):
	comandInstalLibr = 'pip3 install -r requirements.txt'
	HomeDir = os.getcwd()
	print("\n\tRuning install dependencies")
	try:
		os.chdir(NameOfNewDir)
		os.system(comandInstalLibr)
	except OSError:
		print("\tFile with dependencies's info not found.")
	except Exception:
		print("The dependencies was installed early.")
	print("\nThe dependencies was install.")
	os.chdir(HomeDir)

def main():
	url = "https://github.com/ArthurG/Kijiji-Repost-Headless"
	NameOfNewDir = url.split('/')[-1]
	MakeClone(url)
	InstallReq(NameOfNewDir)

	
if __name__ == "__main__":
	main()