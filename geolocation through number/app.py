import phonenumbers
from test import a

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
ch_nmber = phonenumbers.parse(a, "CH")
print(geocoder.description_for_number(ch_nmber, "ru"))
