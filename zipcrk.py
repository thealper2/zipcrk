import zipfile
import argparse
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

def zip_pass(wordlist="", zipfile="", verbose=False):
	is_found = False
	try:
		with open(wordlist, 'rb') as file:
			for password in file.readlines():
					password = password.strip()
					try:
						with zipfile.ZipFile(zipfile) as zip:
                                                        zip.extractall(pwd=password)
                                                        print(f'{Fore.GREEN}[+] Password found: ', password.decode('utf-8'), '{Fore.RESET}')
							is_found = True
                                                        exit()
					except:
                                                if verbose == True:
                                                        print(f'{Fore.RED}[-] Password failed:', password.decode('utf-8'), '{Fore.RESET}')
                                                pass
		if is_found == False:
			print(f'{Fore.RED}[!] Password not found in {wordlist}{Fore.RESET}')

	except Exception as e:
		print(f'[!] Error: {e}')


argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('--wordlist', type=str, required=True, help='')
argument_parser.add_argument('--zipfile', type=str, required=True, help='')
argument_parser.add_argument('--verbose', action='store_true', required=False, help='')
arg = argument_parser.parse_args()

if (arg.wordlist and arg.zipfile and not arg.verbose):
	zip_pass(wordlist=arg.wordlist, zipfile=arg.zipfile, verbose=False)

elif (arg.wordlist and arg.zipfile and arg.verbose):
	zip_pass(wordlist=arg.wordlist, zipfile=arg.zipfile, verbose=True)


