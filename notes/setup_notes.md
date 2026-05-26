# BigQuery Data Quality Agent - Setup Notes

## Python Environment

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Git Workflow

Check status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "your message"
```

Push to GitHub:

```bash
git push
```

## Google Cloud CLI

Verify installation:

```bash
gcloud --version
```

Login:

```bash
gcloud auth login
```

List projects:

```bash
gcloud projects list
```

## Python Interpreter Debugging

If `python` does not use the virtual environment correctly, run commands with the venv Python directly:

```bash
.venv/bin/python -m pip list
.venv/bin/python src/query_runner.py

Then run:

```bash
git status