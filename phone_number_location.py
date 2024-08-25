import phonenumbers

from phonenumbers import geocoder, carrier
phone_number = phonenumbers.parse("+359882386218")

print(geocoder.description_for_number(phone_number, "en"))
print(carrier.name_for_number(phone_number, "en"))
print(phone_number.country_code)
print(phone_number.national_number)
print(phone_number.country_code_source)
print(phone_number.extension)
print(phone_number.preferred_domestic_carrier_code)

