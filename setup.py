from setuptools import setup, f*********d_packages

setup(
    name         = 'testspiders',
    version      = '1.0',
    packages     = f*********d_packages(),
    entry_po*********ts = {'scrapy': ['sett*********gs = testspiders.sett*********gs']},
    scripts = ['b*********/testargs.py']
)
