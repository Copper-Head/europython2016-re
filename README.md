# Re-Discovering Python's Regular Expressions
Here you will find the source of the slides for my EuroPython 2016 presentation
about Python's `re` module.

This is my first attempt at using [Reveal.js](http://lab.hakim.se/reveal-js),
so I haven't quite figured out how to **cleanly** export the slides as pdf.
Currently to view them you have to serve them locally. I will add a github page
for them soon.

## Serving Locally
This setup was a quick way to get things running for me personally, so it is
**not** robust.
First, make sure you have the following:

- you are using Python3
- you installed the dependencies from `requirements.txt`

Once that's done, in the root directory of this repo run:
```
python mgr.py serve
```
If this doesn't show any errors, you should be able to view the slides at
`http://localhost:8000`

To change the port on which to serve, see `mgr.py`
