from base64 import b64encode, b64decode
from os import urandom
from unittest import TestCase

from pywirehair import encoder, decoder

SAMPLES_A = [
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5',
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OQ==',
    b'0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz80YO1p4rY7vznNRGDtaeK2O785zU',
]

SAMPLES_B = [
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5',  # noqa
    b'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OQ==',  # noqa
    b'0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz89AQHd0Hx8oKM/PQEB3dB8fKCjPz0BAd3QfHygoz80YO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zURg7Wnitju/Oc1EYO1p4rY7vznNRGDtaeK2O785zU',  # noqa
]


class EncoderTest(TestCase):
    def test_encode(self):
        data = b'0123456789' * 10
        enc = encoder(data, 60)

        self.assertEqual(b64encode(enc.encode(0)), SAMPLES_A[0])
        self.assertEqual(b64encode(enc.encode(1)), SAMPLES_A[1])
        self.assertEqual(b64encode(enc.encode(2)), SAMPLES_A[2])

    def test_encode_bigger(self):
        data = b'0123456789' * 100
        enc = encoder(data, 600)

        self.assertEqual(b64encode(enc.encode(0)), SAMPLES_B[0])
        self.assertEqual(b64encode(enc.encode(1)), SAMPLES_B[1])
        self.assertEqual(b64encode(enc.encode(2)), SAMPLES_B[2])

    def test_decode(self):
        expected = b'0123456789' * 10
        dec = decoder(len(expected), 60)

        self.assertEqual(None, dec.decode(0, b64decode(SAMPLES_A[0])))
        self.assertEqual(expected, dec.decode(2, b64decode(SAMPLES_A[2])))

        # this shouldn't explode! The decoder will cache the decoded result.
        self.assertEqual(expected, dec.decode(1, b64decode(SAMPLES_A[1])))

    def test_decode_bigger(self):
        expected = b'0123456789' * 100
        dec = decoder(len(expected), 600)

        self.assertEqual(None, dec.decode(0, b64decode(SAMPLES_B[0])))
        self.assertEqual(expected, dec.decode(2, b64decode(SAMPLES_B[2])))

    def test_roundtrip(self):
        data = b'' + urandom(21234)

        enc = encoder(data, 1300)
        dec = decoder(len(data), 1300)

        for i in range(30):
            if i % 4 == 0:  # fake data loss
                continue
            fountain_bytes = enc.encode(i)
            res = dec.decode(i, fountain_bytes)
            if res is not None:
                break
        self.assertEqual(res, data)
        self.assertEqual(22, i)
