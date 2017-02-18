# pelican-ghp

This is the source for my [Github Pages static site](ixjlyons.github.io)
generated with [Pelican][pelican].


## Setup

Clone the repository:

```bash
git clone git@github.com:ixjlyons/pelican-ghp.git
cd pelican-ghp
```

Pull in the submodule for [pelican-plugins][]:

```bash
git submodule init
git submodule update
```

Now create a virtual environment and install the dependencies, which are:

* [pelican][]
* [markdown][]
* [ghp-import][]

These are included in `requirements.txt`, the following should work:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Build

The Makefile generated by `pelican-quickstart` is included here, with some
modifications. It provides a `devserver` target which sets up processes for
automatically regenerating the site when files in `content/` change and serving
the `output/` directory on localhost.

I prefer the more manual approach with no "background" processes that I would
probably forget about. Generate the site manually:

```bash
make html
```

Then set up a terminal to serve the site locally:

```bash
make serve
```

Point the browser of choice to `locahost:8000` to see the result (note: the
port can be changed -- see the `Makefile`). Now, when changing content, issue
another `make html` and reload the site in the browser.


## Do it Live

This site is set up as a personal site for my GitHub profile, so there is
a separate repository holding the contents of the website (as opposed to
a project page, where the content exists only in a `gh-pages` branch). This is
done by pushing the `gh-pages` branch to that separate repository.

To deploy the site to GitHub Pages:

```bash
make github
```

You can optionally specify a commit message (note: this is not the commit
message that shows up on the `master` branch of this repository -- those
commits are separate):

```bash
make github MSG="\"Commit message for GHP\""
```


## Updating the Plugins

It is probably not necessary to update the plugins with every commit, but it
is likely a good idea to keep it reasonably up to date. Sometimes [pelican][]
introduces breaking changes.

```bash
git submodule update --remote
```


[pelican]: http://blog.getpelican.com/
[markdown]: https://pythonhosted.org/Markdown/
[pelican-plugins]: https://github.com/getpelican/pelican-plugins
[ghp-import]: https://github.com/davisp/ghp-import
