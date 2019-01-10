Site is built with nbsite; see https://pyviz.github.io/nbsite for
details and instructions.

## General tips
Look at .travis.yml in the root dir to get the latest idea on how the
build should be run. This README will tend to get out of date.

## Setup
To create a new environment with a name of your choosing, do:

```bash
conda env create -f environment.yml -n <name>
```

If you want to also have the testing and doc building requirements:

```bash
conda env update -f environment-dev.yml -n <name>
```

> **SHORTCUT:** `doit env_create`

## Smoke testing
Notebooks in examples are smoke tested using `nbsmoke` (list of ignored
notebooks are in tox.ini - grep for `nbsmoke_skip_run`). For this they
are run with the data stubs found in examples/data/.data_stubs. There is
a python command to replace entries in examples/data/catalog.yml with any
found in examples/data/.data_stubs/test_catalog.yml:

```bash
doit small_data_setup
```

> **NOTE:** After running that command you will notice that your catalog.yml
> has changed. **DO NOT** check in that new catalog.

Now you have your fake catalog set up and can run all the tests like:

```bash
pytest --nbsmoke-run -k ".ipynb"
```

### Common Patterns

- Run one test: `pytest --nbsmoke-run -k ".ipynb" -k "Walker_Lake" --ignore-nbsmoke-skip`

## Building the website
The source material for the website is mostly in notebooks under examples.
There are also some .rst files in this doc dir. To build the site we use
`nbsite`.

### Step 1: generate .rst files
First we generate .rst files for all the notebooks. To do this run:

```bash
nbsite generate-rst --org pyviz-topics --project-name earthml --offset 1 --nblink=top
```

This will generate a bunch of .rst files in the doc dir. They won't show up if
you do `git status` because they aren't tracked and are being actively ignored.
To clean them out I recommend you run `git clean -xfdi doc`. But be careful.

> This is kind of terrible, but if you want to run just one example you
> can generate just the rst for that example. That would look like:
>
> ```
> nbsite generate-rst --org pyviz-topics --project-name earthml --offset 1 --nblink=top --skip '.*topics/.*,.*02.*,.*03.*,.*04.*,.*05.*,.*06.*'
> ```
> That will make just 01_ and the index notebooks.
>
> **TODO:** We should add a `nbsite --include` flag

### Step 2: evaluate notebooks
Next we will evaluate all the notebooks, which for sites that have many notebooks or computation-intensive notebooks can take a long time. The evaluated notebooks will be under the doc dir and there are .json blobs that accompany them.

> #### Optional
> Some notebooks have evaluated versions checked in to master as git-lfs files.
> These notebooks will be skipped by default. You can rm the notebook(s) that you
> want to re-evaluate. For example:
>
> ```bash
> rm doc/topics/Heat_and_Trees.ipynb
> ```

To run the notebooks do:

```bash
nbsite build --what=html --output=builtdocs
```

**NOTE**: Any notebook that exists in the doc dir will not be re-evaluated.

Now you should have a builtdocs dir with a lot of html in it. This is a
build artifact and should never be checked in anywhere by a human.

### Step 3: serve website locally [Optional]

This step is optional, but if you want to inspect the website locally do:

```bash
doit serve_website
```

### Step 4: add a new evaluated version of a notebook

If you have made changes to a topics notebook, then you will want to check in
a new evaluated version. To do this make sure you have
[git-lfs](https://git-lfs.github.com/) installed, then do:

```bash
git add doc/<path_to_your_evaluated_notebook>
git commit -m "Adding my evaluated notebook"
git push
```

Make a PR and merge it to master.

### Step 5: tag a release

First fetch all the tags and inspect them to get the next logical tag:

```bash
git fetch --tags
git tag
```

> #### Optional - tag a dev release
> Tag a dev release like:
>
> ```bash
> git tag -a v0.1.3a2
> git push --tags
> ```
>
> A Travis job will start that (if completed successfully) will deploy the site to
> https://pyviz-dev.github.io/EarthML

Tag a full release like so:

```bash
git tag -a v0.1.3
git push --tags
```

A Travis job will start that (if completed successfully) will deploy the site to
http://earthml.pyviz.org/
