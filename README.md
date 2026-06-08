# backend-cloud

Django backend server 2 for RoboMunch Task 2.

## Endpoints

```text
POST /get/resolution
```

Both endpoints accept:

```json
{
  "image": "data:image/png;base64,..."
}
```

`/get/resolution` returns image dimensions.

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py runserver 0.0.0.0:8001
```

For Docker:

```powershell
docker compose up --build
```

## Demo Docker Logs

When the mobile app sends a request to backend server 2, show the cloud VM terminal:

```bash
docker logs -f backend-cloud
```

or, if using compose:

```bash
docker compose logs -f backend-cloud
```

The logs include lines like:

```text
resolution request received: width=512 height=232
```

## GitHub Secrets For CD

Set these repository secrets:

```text
VM_HOST
VM_USER
VM_SSH_KEY
VM_APP_DIR
VM_PORT
```

The CD workflow SSHes into the VM, pulls this repo, rebuilds the Docker container, and restarts it.

## Workflows

- `CI`: installs dependencies, runs Ruff linting, and runs Django tests.
- `Semantic Version`: creates `vX.Y.Z` tags from conventional commits on `main`.
- `CD`: deploys tagged versions to the cloud VM with Docker.
