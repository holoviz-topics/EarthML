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

## Smoke testing
Notebooks in examples are smoke tested using `nbsmoke` (list of ignored
notebooks are in tox.ini - grep for `nbsmoke_skip_run`). For this they
are run with the data stubs found in examples/data/.data_stubs. There is
a python command to replace entries in examples/data/catalog.yml with any
found in examples/data/.data_stubs/test_catalog.yml:

```bash
doit before_test
```

> **NOTE:** After running that command you will notice that your catalog.yml
> has changed. **DO NOT** check in that new catalog.

Now you have your fake catalog setup and can run all the tests like:

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

> This is kind of terrible, but if you want to generate just one example you
> can generate just the rst for that example. That would look like:
>
> ```
> nbsite generate-rst --org pyviz-topics --project-name earthml --offset 1 --nblink=top --skip '.*topics/.*,.*02.*,.*03.*,.*04.*,.*05.*,.*06.*'
> ```
> That will make just 01_ and the index notebooks. TODO: We should add a `nbsite --include` flag

### Step 2: evaluate notebooks
Next we will evaluate all the notebooks. This is the step that can take a while.
These notebooks will be under the doc dir and there are .json blobs that accompany them.

> #### Optional
> To get pre-evaluated versions of the notebooks you can checkout doc dir of the
> evaluated branch:
>
> ```bash
> git fetch https://github.com/pyviz-topics/earthml.git evaluated:refs/remotes/evaluated
> git checkout evaluated -- doc
> git reset HEAD
> ```
>
> Now you should have a lot of .ipynb and .json files in the doc dir. To avoid running
> all the notebooks you can just rm the notebook that you are interested in.
>
> ```bash
> rm doc/<path_to_your_evaluated_notebook>
> ```

To evaluate the notebooks run:

```bash
nbsite build --what=html --output=builtdocs
```

**NOTE**: Any notebook that exists in the doc dir will not be re-evaluated.

Now you should have a builtdocs dir with a lot of html in it. This is a
build artifact and should never be checked in anywhere by a human.

**NOTE:** 05_Machine_Learning.ipynb takes a long time to run, but if it takes more than
~10min you should kill the process and run the build command again.

### Step 3: run website locally

This step is optional, but if you want to inspect the website locally do:

```bash
cd builtdocs
python -m http.server
```

### Step 4: push *one* newly evaluated notebook

If you have made changes to a notebook, then you'll want to push a new evaluated
version to the `evaluated` branch. I think the easiest way to do this is to commit
the file on the branch you are on:

```bash
git add doc/<path_to_your_evaluated_notebook> -f
git commit -m "Adding my evalutated notebook"
```

Then checkout evaluated (making sure it's up to date) and put your evaluated
notebook onto that branch.

```bash
git checkout evaluated
git pull
git checkout <your-branch> doc/<path_to_your_evaluated_notebook>
git add doc/**/*.json
git commit -m "Adding my evalutated notebook"
git push
```

If you still care about your other branch check it out and do:

```bash
git reset HEAD~
```

---

## OR

---

### Step 4: push *all* newly evaluated notebooks

If you want to rebuild the whole evaluated branch and you have evaluated versions
of all the notebooks (you've done steps 1 and 2), the first step is deleting
the branch:

```
git branch -D evaluated
```

Then remove these lines from the .gitignore:

```yml
doc/**/*.ipynb
doc/**/*.json
```

Check in the new .gitignore

```bash
git add .gitignore
git commit -m "Updating gitignore to reflect this branch's different role"
```

Then add all your evaluated notebooks and force push the branch

```bash
git add doc
git commit -m "Updating all evaluated notebooks"
git push origin evaluated --force
```

### Step 5: tag a dev release

This step is optional.

First fetch all the tags and inspect them to get the next logical tag

```bash
git fetch --tags
git tag
```

Once you've figured out what your tag will be do:

```bash
git tag -a v0.1.3a2
git push --tags
```

A travis job will start that when done, will deploy the site to
https://pyviz-dev.github.io/EarthML

### Step 6: tag a release

First fetch all the tags and inspect them to get the next logical tag

```bash
git fetch --tags
git tag
```

Once you've figured out what your tag will be do:

```bash
git tag -a v0.1.3
git push --tags
```

A travis job will start that when done, will deploy the site to:
http://earthml.pyviz.org/
