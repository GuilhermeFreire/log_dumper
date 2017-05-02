from mss import mss
from PIL import Image
import base64
from io import BytesIO

def grab():
	all_monitors = []
	with mss() as sct:
		monitors = sct.enum_display_monitors()
		for num, monitor in enumerate(monitors[1:], 1):
			sct.get_pixels(monitor)
			img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
			buffered = BytesIO()
			img.save(buffered, format="JPEG")
			img_str = base64.b64encode(buffered.getvalue())
			all_monitors.append(img_str)
	return all_monitors