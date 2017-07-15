from googlemaps import GoogleMaps
gmaps = GoogleMaps('AIzaSyCWM-KHA1VHucVMuAAR6VdolYR5CVY2khA')
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat, lng = gmaps.address_to_latlng(address)
print lat, lng