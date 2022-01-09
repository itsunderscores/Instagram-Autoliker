## Instagram Liker by Hashtag
Version: **1.0**<br>
Last Update: **01/08/2022**<br>
<hr>

Likes images automatically based on the hashtag you want.<br>
I've only tested this on Windows, so it may display weird on Linux. I dunno.

If it is your first time using the program, you must select "Y" when it asks you to login. Once you have done this, you do not have to do this as it will reuse the cookies.

You must place the Selenium Driver in the same folder as the program. You must also set the driver in the script.
```
browser = webdriver.Firefox(executable_path="C:\\xampp\\htdocs\\geckodriver.exe", options=firefoxOptions)
```

## Selenium Driver Download
```
https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz.asc
https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip
```

## Installation
```sh
git clone https://github.com/itsunderscores/Instagram-Autoliker
cd Instagram-Autoliker
pip install -r requirements.txt
python instagram.py
```
