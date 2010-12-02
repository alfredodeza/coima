import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup

tests_require = ['pytest']

setup(
    name = "coima",
    version = "0.0.1",
    packages = ['coima'],
    include_package_data=True,
    package_data = {
        '': ['distribute_setup.py'],
        },

    # metadata 
    author = "Alfredo Deza",
    author_email = "alfredodeza [at] gmail [dot] com",
    description = "Extremely plain and simple template engine for text files",
    long_description = """\
 Small template engine that replaces variables via dictionary values::

    line = "This is a {{variable}} in a {{string}}"

    coima({'variable':'word', 'string':'sentence'}, line)

    "This is a word in a sentence"

 """,

   classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
      ],

    license = "MIT",
    keywords = "WSGI stats requests context development",
    url = "http://github.com/alfredodeza/coima",   

)

