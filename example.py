import tinysong as ts
import os
import sys


def program():
	limit = 8
	#limit = int(raw_input("Enter the number of results to display: "))
	print(sys.platform + "\n")
	query = raw_input("Enter a search query: ")
	ret=ts.api_call(query, 3, limit)
	if ret == []:
		print("No match found!")
	else:
		print("\nMatch found!\n")
		numb_results = len(ret)
		print(numb_results)
		for x in range(0, numb_results):
			print("  Result: " + str(x + 1))
			print("-------------------------------------------")
			print("| Song: " + ts.get_title(ret, x))
			print("| Artist: " + ts.get_artist(ret, x))
			print("| Album: " + ts.get_album(ret, x))
			print("| Url: " + ts.get_url(ret, x))
			print("-------------------------------------------\n")
		open_url = str(raw_input("\nDo you want to open a link one of these songs? [Y/N] "))
		if open_url.lower() == "y":
			choice = int(raw_input("Please enter the number you want to open: "))
			if choice <= numb_results:
				#We need to open the url differently between OS's
				if sys.platform[:6] == "darwin":
					os.system("open " + ts.get_url(ret, choice - 1))
				elif sys.platform[:3] == "win":
					os.system("start " + ts.get_url(ret, choice - 1))
				elif sys.platform[:5] == "linux":
					os.system("firefox " + ts.get_url(ret, choice - 1))
				else:
					print("Unsupported platform: Cannot open URL...")
			else:
				print("Invalid answer: Doing nothing...")
	ans = str(raw_input("\nDo you want to search again? [Y/N] "))
	if ans.lower() == "y":
		program()


if __name__ == "__main__":
	program()
