import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages

tests_require = ['pytest']

setup(
    name = "coima",
    version = "0.0.1",
    packages = find_packages(),
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

    cat file.txt
    "This is a {{variable}} in a {{string}}"

    from coima import Template
    Template({'variable':'word', 'string':'sentence'}, 'file.txt')

    Template.render()

    "This is a word in a sentence"

Syntax
-------
No Python or code blocks are allowed, this is basically a **dumb** templating 
engine.

Variables should be a one word or 2 words together with an underscore. These are
valid variables:

{{variable}}
{{variable_one}}

Invalid variables are left 'as is' and left in the final rendered template.

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

