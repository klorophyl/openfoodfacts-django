# Open Food Facts client for your Python applications and scripts
![Open Food Facts](https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-178x150.png)
===================================

## What is Open Food Facts?
### A food products database

Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.

### Made by everyone

Open Food Facts is a non-profit association of volunteers.
1800+ contributors like you have added 43 000+ products from 150 countries using our Android, iPhone or Windows Phone app or their camera to scan barcodes and upload pictures of products and their labels.

### For everyone

Data about food is of public interest and has to be open. The complete database is published as open data and can be reused by anyone and for any use. Check-out the cool reuses or make your own!
- <https://world.openfoodfacts.org>

**Status**
===

[![Project Status](http://opensource.box.com/badges/active.svg)](http://opensource.box.com/badges)


## Installation

Pip doesn't support git-backed dependency in a git-backed package. You'll have to install openfoodfacts-python manually.

```
sudo pip install git+https://github.com/openfoodfacts/openfoodfacts-python#egg=openfoodfacts==0.1
sudo pip install git+https://github.com/klorophyl/openfoodfacts-django#egg=off_django==0.4
```

or:

```
git clone https://github.com/klorophyl/openfoodfacts-django
cd openfoodfacts-django
sudo python setup.py install
```

### Dependencies

`off_django` was developped under Python 3

Installing` off_django` will install [openfoodfacts-python](https://github.com/openfoodfacts/openfoodfacts-python) as a dependency and use it as an API connector, check this repo for advanced API usage.

## Docs

### Django settings

1) add off_django to your INSTALLED_APPS :

```
INSTALLED_APPS = (
    ...,
    "off_django",
)
```

2) add `OFF_TMP_FOLDER_PATH` to your settings, it is the path to a folder in which off_django can download Open Food Facts DB dump (~1.5Go). It will be removed once it has been loaded in your local DB.

```
OFF_TMP_FOLDER_PATH = 'my/path/to/off/tmp/folder'
```

3) if needed, build a custom Open Food Facts food product model by inheriting from AbstractOFFFood [(see definition)](off_django/models.py) and add `OFF_MODEL` to your settings :

```
OFF_MODEL = 'your_custom_off_app.YOUR_CUSTOM_OFF_MODEL'
```

You can then override the `parse_api_fields` method to add your custom fields to the dict returned

```
from off_django.models import AbstractOFFFood

class MyCustomOFFFood(AbstractOFFFood):

    my_custom_field = models.IntegerField(default=None, null=True)
    ...

    @classmethod
    def parse_api_fields(cls, data):
        treated_fields = super(MyCustomOFFFood, cls).parse_api_fields(data)
        treated_fields['my_custom_field'] = my_custom_value
        return treated_fields
```

__

openfoodfacts-django has [predefined models](off_django/models.py) for Open Food Facts objects, bear in mind that it is best practice to create a separated database under [ODbL](https://opendatacommons.org/licenses/odbl/). Do not forget to update your [DATABASES settings](https://docs.djangoproject.com/en/2.0/ref/settings/#databases) accordingly, and also to create a new [django router](https://docs.djangoproject.com/en/2.0/topics/db/multi-db/#database-routers) for the database.

Pro tip: create a django CRON job thanks to [django-crontabs](https://github.com/kraiz/django-crontab) to update your database daily, Open Food Facts dumps are released nightly. To do just that, use :

```
from off_django.db import DumpManager

dump_manager = DumpManager()
objects = dump_manager.load_last_dump()  # will load last open food facts dump (~1.5Go) in your database
```


## Facets

These models have been implemented to represent OFF product facets :

```
OFFAdditive, OFFAllergen, OFFBrand, OFFCategory, OFFCountry, OFFIngredient, OFFLanguage,
OFFPackaging, OFFPackagingCode, OFFPurchasePlace, OFFStore, OFFTrace, OFFState
```

They inherit all from `AbstractOFFFacet` abstract model.
To populate your local database with a dump from OFF, use :

```
from off_django.models import AbstractOFFFacet
AbstractOFFFacet.fetch_all_facets()
```

You can alternatively populate only one kind of facet with the following method :

```
from off_django.models import OFFAdditive
OFFAdditive.update_with_off_db()
```


## Posting products

Use `OFFApiConnector` object to post products via OFF API.

```
from off_django.api import OFFApiConnector

off_food = OFFFood(...)
connector = OFFApiConnector(username=YOUR_USERNAME, password=YOUR_PASSWORD)
connector.post_product(off_food)
```

It will guess the country for you if you don't fill the field in OFFFood.

__Warning__ this will fail silently if username/password is not known by OFF, see [OFF API docs](https://en.wiki.openfoodfacts.org/API/Write)


## Uploading images

Use `OFFApiConnector` object to upload your images to OFF.
img_field must be in `['front', 'ingredients', 'nutrition', 'other']`

```
from off_django.api import OFFApiConnector

connector = OFFApiConnector(username=YOUR_USERNAME, password=YOUR_PASSWORD)

with open(path_to_file, "r") as img_file:
    connector.upload_image(barcode, img_file, img_field="front")
```

__Warning__ this will fail silently, see [OFF API docs](https://en.wiki.openfoodfacts.org/API/Write)

## Contributing

The project is initially started by [Gabriel Samain](https://github.com/klorophyl)


Copyright 2018 Open Food Facts
