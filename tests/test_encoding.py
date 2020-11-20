from base64 import b64encode, b64decode
from unittest import TestCase

from pywirehair import encoder, decoder

SAMPLES_A=[
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5',
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OQ==',
    b'0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz80YO1p4rY7vznNRGDtaeK2O785zU',
]

SAMPLES_B=[
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5',
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OQ==',
    b'0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz80YO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zU',
]


class EncoderTest(TestCase):
    def test_encode(self):
        data = b'0123456789' * 10
        enc = encoder(data, 60)

        self.assertEqual(b64encode(enc.encode(0)), SAMPLES_A[0])
        self.assertEqual(b64encode(enc.encode(1)), SAMPLES_A[1])
        self.assertEqual(b64encode(enc.encode(2)), SAMPLES_A[2])

    def test_decode(self):
        expected = b'0123456789' * 10
        dec = decoder(len(expected), 60)

        self.assertEqual(None, dec.decode(0, b64decode(SAMPLES_A[0])))
        self.assertEqual(expected, dec.decode(2, b64decode(SAMPLES_A[2])))
