import re

# Write a function that, for that data in device1 and device2
# 1. captures mDisplayInfo data using regular expressions
# 2. stores the data as numbers in a dictionary with the keys
# 'width', 'height' and 'refresh_rate'
# 3. prints the information in the dictionary along with whether or not the
# display is HD (e.g. resolution >= 1920x1080)
def extract_display_info(file):
	# pattern = re.compile(r'([0-9]?[0-9]{3})x([0-9]?[0-9]{3}):(\w+)')
	# matches = pattern.finditer(file)
	matches = re.findall(r'([0-9]?[0-9]{3})x([0-9]?[0-9]{3}):(\d+)', file)[0]
	# print(matches)
	my_dict = {
		'width': int(matches[0]),
		'height': int(matches[1]),
		'refresh_rate': int(matches[2]),
	}
	print(my_dict)
	
	if my_dict['width'] >= 1920 and my_dict['height'] >= 1080:
		print('display is HD')

	return my_dict


device1 = """
mDisplayController:
	mWifiDisplayOnSetting=false
	mWifiP2pEnabled=true
	mWfdEnabled=false
	mWfdEnabling=false
	mNetworkInfo=[type: WIFI_P2P[] - WIFI_P2P, state: UNKNOWN/IDLE, reason: (unspecified), extra: (none), roaming: false, failover: false, isAvailable: true]
	mScanRequested=false
	mDisplayInfo=800x600:30Hz
	"""
extract_display_info(device1)

device2 = """
mDisplayController:
	mWfdEnabled=false
	mWfdEnabling=false
	mDisplayInfo=1920x1080:120Hz
	mNetworkInfo=[type: WIFI_P2P[] - WIFI_P2P, state: UNKNOWN/IDLE, reason: (unspecified), extra: (none), roaming: false, failover: false, isAvailable: true]
	mScanRequested=false
	"""
extract_display_info(device2)