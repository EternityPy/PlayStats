# PlayStats
A python package to fetch details of apps on Google Play such as ratings, vendor,last updated and much more.


pip install playstats

```python

from playstats.appstat import AppStat
app=AppStat('com.google.android.gms')
app.vendor()
app.last_updated()
app.rating()
app.all_ratings()
```
