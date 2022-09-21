import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

phone = phonenumbers.parse("+918630923246")

print(geocoder.description_for_number(phone, 'en'))
print(carrier.name_for_number(phone, 'en'))
print(timezone.time_zones_for_number(phone))