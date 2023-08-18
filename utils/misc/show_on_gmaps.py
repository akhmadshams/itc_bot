
URL = "http://maps.google.com/maps?q={lat},{lon}"


def show(lat, lon):
    return URL.format(lat=lat, lon=lon)


# bu funksiya kartadan markaz turgan joyni aniqlash uchun