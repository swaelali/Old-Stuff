from googlemaps import GoogleMaps
gmaps = GoogleMaps('<replace_with_your_key>')
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat, lng = gmaps.address_to_latlng(address)
print lat, lng
