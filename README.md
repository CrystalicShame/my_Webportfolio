# Andre Cavota Web Portfolio

Flet web portfolio for Computer Programming I.

## Project Layout

- `src/main.py` - the deployable Flet app
- `src/assets/` - images, icons, and `Video_Contribution.mp4`
- `main.py` - local compatibility launcher

## Run Locally

```powershell
.\.venv\Scripts\flet.exe run --web
```

Or run the compatibility launcher:

```powershell
.\.venv\Scripts\python.exe main.py
```

## Build For Web

For GitHub Pages, replace `YOUR_REPO_NAME` with the repository name:

```powershell
.\.venv\Scripts\flet.exe build web --yes --base-url /YOUR_REPO_NAME/ --route-url-strategy hash
```

Test the build locally:

```powershell
.\.venv\Scripts\flet.exe serve build\web
```

## Deploy

This repo includes a GitHub Actions workflow for GitHub Pages. In GitHub, open
`Settings -> Pages` and set the deployment source to `GitHub Actions`, then push
to the `main` branch.
