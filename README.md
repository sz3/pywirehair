[![Build Status](https://github.com/sz3/pywirehair/workflows/ci/badge.svg)](https://github.com/sz3/pywirehair/actions?query=workflow%3Aci)
[![Coverage Status](https://coveralls.io/repos/github/sz3/pywirehair/badge.svg?branch=master)](https://coveralls.io/github/sz3/pywirehair?branch=master)

## pywirehair

A python wrapper for the [wirehair](https://github.com/catid/wirehair) forward error correction C library. wirehair is included as a git subtree.

I'll probably put some wheels in pypi sooner or later. In the meantime:

```
python setup.py build
python setup.py install
```

or maybe:
`pip install https://github.com/sz3/pywirehair/archive/master.zip`

## Usage

```
from pywirehair import encoder, decoder

data = b'0123456789' * 10
enc = encoder(data, 40)
a = enc.encode(0)

dec = decoder(len(data), 40)
dec.decode(0, a)

for i in range(2,4):  # skip 1 for fun
    print(i)
    a = enc.encode(i)
    print(dec.decode(i, a))
```

decoder.decode() will return `None` if there is more work to do, or the decoded value if all is well. Error cases are not incredibly well handled at the moment, but should explode in predictable and obvious ways.

