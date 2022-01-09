from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver
import requests
import os, sys, time
import time as t
import socket
import random
from random import randrange
import threading
import random
import getpass
import re
import urllib.request
import os
import sys
import pickle
from subprocess import call

#mydirectory = os.getcwd() #grabbing current directory
#os.system("export PATH=$PATH:" + mydirectory) #used for geckodriver
os.system("cls") #clear panel

CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\33[92m'
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

global syn
def header():
	print(CRED+'''
	    _  _   _ _       _    _ _       
	   /_\| | | | |_ ___| |  (_) |_____ 
	  / _ \ |_| |  _/ _ \ |__| | / / -_)
	 /_/ \_\___/ \__\___/____|_|_\_\___| v1
	''')
	print(CRED+"[+] Autoliker based on hashtags for Instagram")
	print(CRED+"[-] Developed by underscores#0001")
	print(WHITE+"-------------------------------------------------------"+YELLOW)

firefoxOptions = Options()
#firefoxOptions.add_argument("-headless")
#firefoxOptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0")
browser = webdriver.Firefox(executable_path="C:\\xampp\\htdocs\\geckodriver.exe", options=firefoxOptions)

def save_cookie(driver):
    with open("cookie", 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver):
     with open("cookie", 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             #print(cookie)
             driver.add_cookie(cookie)

def login():
	try:
		username = input("[+] Enter username: ")
		#password = getpass.getpass('[-] Enter password (Hidden): ')
		password = input('[-] Enter password (Hidden): ')
		print("")
		print(CGREEN+"[+] Signing in..."+WHITE)

		browser.get("http://www.instagram.com")

		time.sleep(5)

		usern = browser.find_element_by_name("username")
		usern.send_keys(username)

		passw = browser.find_element_by_name("password")
		passw.send_keys(password)
		time.sleep(2)


		log_c1 = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
		log_c1.click()
		time.sleep(4)

		try:
			ele = browser.find_element_by_xpath("//*[@id='slfErrorAlert']");
			if "The username you entered doesn't belong to an account. Please check your username and try again." in ele.text:
				print(CRED + "[-] Username entered does not belong to an account!")
				time.sleep(7)
				os.system("cls")
				login()
			else:
				if "Sorry, your password was incorrect. Please double-check your password." in ele.text:
					print(CRED + "[-] Invalid Login... please try again!")
					time.sleep(7)
					os.system("cls")
					login()
				else:
					if "Please wait a few minutes before you try again." in ele.text:
						print(CRED + "[-] Rate limited, delaying 3 minutes and then please try again!")
						time.sleep(200)
						os.system("cls")
						login()
					else:
						if "We couldn't connect to Instagram. Make sure you're connected to the internet and try again." in ele.text:
							print(CRED + "[-] Instagram returned 'Could Not Connect' message,  delaying 1 minute and then please try again!")
							time.sleep(60)
							os.system("cls")
							login()
						else:
							return "Y"
		except Exception as e:
			return "Y"
	except:
		print(CRED + "[?] Something unexpected happened...")

#def nextpage():

def like(hashtag, skip, times):
	try:
		browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
		time.sleep(2)
		print(YELLOW + "[+] Loading Images... Please wait.")
		print("")
	except Exception as e:
		print(CRED + "[!] Could not load page correctly, trying again in 30 seconds...")
		time.sleep(30)
		browser.close()
	
	try:
		clickpicture = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]") #Clicks first picture
		clickpicture.click()
		time.sleep(1)

		skip1 = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/div/button").click() #Skips first picture
		time.sleep(1)
	except:
		print(CRED + "[!] Could not grab the first image, reload script")

	# Skips first 8 images
	if skip == "1":
		skip1 = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/div/button").click() #Skips first picture
		time.sleep(1)
		for x in range(8): #Skipping next 8 pictures
			skip2 = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/div[2]/button").click() #Skips the rest of the top posts
			time.sleep(1)
	else:
		pass

	likessent = 1

	while True:

		if likessent >= times:
			print("[-] Using new hashtag")
			break
		else:
			pass

		continuelike = False
		try:
			alreadyliked = browser.find_element_by_css_selector(".fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)").get_attribute("aria-label")
			liked = alreadyliked
		except:
			pass

		try:
			alreadyliked = browser.find_element_by_css_selector(".fr66n > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)").get_attribute("aria-label")
			liked = alreadyliked
		except:
			pass

		if "Unlike" in liked:
			print(CRED+ "[-] Already liked, skipping")
			nextpage = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/div[2]/button").click() #Next Page
			time.sleep(1)
		else:
			continuelike = True

		if continuelike == True:
			try:
				like = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click() #Click Like
				time.sleep(1)
				
				try:
					nextpage = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/div[2]/button/div").click() #Next Page
				except:
					pass
				
				try:
					nextpage = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/div[2]/button").click() #Next Page
				except:
					pass

				randomnumber = random.randint(10,30)
				print(CGREEN + "[-] Like sent (" + str(likessent) + "/" + str(times) + ") | Delay: " + str(randomnumber) + " sec")
				likessent += 1
				time.sleep(randomnumber) #Sleeping for 10-30 seconds each picture
			except Exception as e:
				print(CRED + "[!] Issue with liking the post/going to next page: " + str(e))
				time.sleep(30)
		else:
			pass

def main():
	header()
	prompt = input("[+] Login? Y/N: ")
	prompt = "n"
	if prompt == "Y" or prompt == "y":
		loginstatus = login()
		if loginstatus == "Y":
			print(CGREEN + "[-] Login successful!\n")
			save_cookie(browser)
			pass
		else:
			print(CRED + "[-] Login failed. Relaunch program")
	else:
		pass

	browser.get("https://www.instagram.com/")
	load_cookie(browser)
	hashtag = input(CGREEN + "[+] Enter hashtag: ")
	times = input(CGREEN + "[+] Likes per hashtag: ")
	#hashtag = "c7"
	#times = 30
	like(hashtag, "0", int(times))

main()

browser.quit()
