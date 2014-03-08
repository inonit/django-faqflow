import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-faqflow',
    version='0.2a',
    packages=['faqflow'],
    include_package_data=True,
    license='MIT License',
    description='An FAQ support app',
    long_description=README.rst,
    url='https://github.com/inonit/django-faqflow',
    author='Eirik Krogstad',
    author_email='eirikkr@gmail.com',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Framework :: Django",
    ],
)
