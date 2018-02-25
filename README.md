# PlayStats
> Fetches details of packages on Google Play.

It is a python package to fetch details of apps on Google Play such as ratings, vendor,last updated, content rating and much more.


## Installation

Install using pip:

```sh
pip install playstats
```

## Usage example


```python

>>> from playstats.appstat import AppStat
>>> app=AppStat('com.whatsapp')
>>> app.vendor()
'WhatsApp Inc.'
>>> app.title()
'WhatsApp Messenger'
>>> app.rating()
4.4
>>> app.genre()
'Communication'
>>> app.version()
'Varies with device'
>>> app.content_rating()
'Rated for 3+'
>>> app.keyword_rank('whats app instant messenger')
2
```



## Meta

Apoorva Pandey – apoorvapandey365@gmail.com

Distributed under the BSD license.

[https://github.com/apoorvaeternity](https://github.com/apoorvaeternity)

## Contributing

1. Fork it (<https://github.com/EternityPy/PlayStats/>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

