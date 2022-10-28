# REST-photo-manager
REST app for photos managing

## Instalation:

Run the following command in your terminal:

Clone repository using SSH key:

```
git@github.com:Daniken94/REST-photo-manager.git
```
or download 'zip'.

## Requirements:

Python is required !!!


You can install all app from requirements.txt by using command:

```
pip install -r requirements.txt
```
## Database:

Install PostgreSQL and fill settings with your data


```
DATABASES = {
     'default': {
     'ENGINE': 'django.db.backends.postgresql',
     'NAME': 'name of your db',
     'USER': 'your name',
     'PASSWORD': 'your password',
     'HOST': 'localhost'
      }
  }
```

After that create your database.

## Hardcode path:

Change hardcoded path toy your directory in files:
- script.py


```
55 line   file = os.path.abspath('/your path/REST-photo-manager/photo_manager/app/fixtures/photos.json')

90 line   patch_raw = "/your path/REST-photo-manager/photo_manager/"
91 line   patch_photo = "/your path/REST-photo-manager/photo_manager/media/photos/"
92 line   patch_photo_png = "/your path/REST-photo-manager/photo_manager/media/photos_png/"

117 line  dir = '/your path/REST-photo-manager/photo_manager/media/photos_png'
```


## Commands:

Run

```
python manage.py runserver
```

to start app.

Run

```
python script.py
```

to download data from external API