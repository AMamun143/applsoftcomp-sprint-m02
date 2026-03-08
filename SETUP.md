# Setup

Notes I used to push this project to my GitHub and to reproduce the figures.

## Pushing to my repo

I added my GitHub repo as a remote and pushed:

```bash
git remote add myrepo https://github.com/AMamun143/applsoftcomp-sprint-m02.git
git push myrepo master
git push myrepo --all
```

If I need to point origin at my repo instead:

```bash
git remote set-url origin https://github.com/AMamun143/applsoftcomp-sprint-m02.git
git push origin master
git push origin --all
```

If the remote already had commits (e.g. a README), I used `--force` once: `git push myrepo master --force`. I only do that when I know I'm overwriting the remote.

## Reproducing the figures

I run the pipeline from the project root. Either:

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run `./run.sh`, or
- Use a venv:
  ```bash
  python3 -m venv .venv
  .venv/bin/pip install pandas matplotlib seaborn scikit-learn
  ./run.sh
  ```
  The script uses `.venv/bin/python` when uv is not installed.
