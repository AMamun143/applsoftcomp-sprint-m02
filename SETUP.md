# Setup: Push to your GitHub repository

This project was completed for the M02 Sprint. To push to your own GitHub repo:

1. Add your repo as a remote (if not already added):
   ```bash
   git remote add myrepo https://github.com/AMamun143/applsoftcomp-sprint-m02.git
   ```

2. Push `master` to your repo:
   ```bash
   git push myrepo master
   ```

3. If your repo already has content (e.g., a README), you may need to force-push once:
   ```bash
   git push myrepo master --force
   ```
   Use with care.

## Reproducing figures

- **With uv:** Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run `./run.sh`.
- **With Python venv:** From project root:
  ```bash
  python3 -m venv .venv
  .venv/bin/pip install pandas matplotlib seaborn scikit-learn
  ./run.sh
  ```
  The script uses `.venv/bin/python` when `uv` is not available.
