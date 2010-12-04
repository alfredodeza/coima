Small, easy and dumb
--------------------

Small template engine that replaces variables via dictionary values::

    cat file.txt
    "This is a {{variable}} in a {{string}}"

    from coima import Template
    t = Template({'variable':'word', 'string':'sentence'}, 'file.txt')

    t.render()

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

pip install coima
-----------------


