# Application Logic for Location Finder application

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def get_location(phone_number):
    """Return the location of the phone number."""
    phone_number = phonenumbers.parse(phone_number)
    return geocoder.description_for_number(phone_number, "en")

def get_carrier(phone_number):
    """Return the carrier of the phone number."""
    phone_number = phonenumbers.parse(phone_number)
    return carrier.name_for_number(phone_number, "en")


def get_cords(phone_number):
    """Return the coordinates of the phone number."""
    phone_number = phonenumbers.parse(phone_number)
    return geocoder.description_for_number(phone_number, "en")


if __name__ == "__main__":
    # Test the logic functions
    print(get_location("+256752541359"))
    print(get_carrier("+256752541359"))