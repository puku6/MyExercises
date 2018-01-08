try:
	from setuptools import setup
except ImportError:
	from distutuls.core import setup
	
config = {
	'description': 'My Project',
	'autor': 'Kimberly B.',
	'url': 'URL to get it at',
	'download_url': 'Where to download',
	'author_email': 'My email',
	'version': '0.1' ,
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
	}
	
	setup(**config)