import urllib.request as request
import urllib.parse as parse
import json

main_url = "http://dontpad.com/"

def write(page, content):
	url = main_url + page
	data = parse.urlencode({"text" : content})
	data = data.encode("utf-8")
	req = request.Request(url, data)
	with request.urlopen(req) as response:
		timestamp = response.read()
	return timestamp

def read_raw(page):
	with request.urlopen(main_url + page + ".body.json?lastUpdate=0") as response:
		html = response.read()
	return html

def read(page):
	return json.loads(read_raw(page).decode())

if __name__ == "__main__":
	print("==> POST:", write(":", "ohohohohoho ahahahahaha ohohohohoho ahahahaha trolololololololololololololololooool"))
	print(read(":"))
