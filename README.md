# flet-github-action-workflows

GitHub Action Workflows to ease the packaging of your [Flet](https://flet.dev) apps.
Flet is a cross-platform framework, i.e., from a single codebase you can target multiple platforms: 
Android (`aab`, `apk`), iOS (`ipa`), Linux, macOS, Windows, and Web.

Feel free to reuse them and customize to your specific usecases and needs.

## What is in this repo

| File                                                                                                                 | Purpose                                                                  |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [`.github/workflows/all-builds.yml`](.github/workflows/all-builds.yml)                                               | Builds for Linux, macOS, Windows, AAB, APK, IPA, and Web in one workflow |
| [`.github/workflows/web-build-and-github-pages-deploy.yml`](.github/workflows/web-build-and-github-pages-deploy.yml) | Builds for Web and deploys to GitHub Pages                               |
| [`pyproject.toml`](pyproject.toml)                                                                                   | Example Flet project configuration                                       |
| [`src/main.py`](src/main.py)                                                                                         | Example Flet app to test the workflows                                   |

## Quick start

1. Copy the workflow(s) you need into your own repository under `.github/workflows/`.
2. Ensure your project has a valid `pyproject.toml` and Flet app source.
3. Push to GitHub or run manually from the [Actions](/actions) tab.

## Workflow details

### `all-builds.yml`

- Uses `uv` as package manager/installer.
- Uses a matrix strategy to build: `linux`, `macos`, `windows`, `aab`, `apk`, `ipa`, `web`.
- Uploads one artifact per target with the pattern `<target>-build-artifact`.
- Includes a Linux dependency installation step only when needed for Linux desktop builds.
- Supports manual runs via `workflow_dispatch`.

### `web-build-and-github-pages-deploy.yml`

- Builds the web app with:
  - `--base-url ${GITHUB_REPOSITORY#*/}`: which sets the base URL to the repository name.
  - `--route-url-strategy hash`: which uses the hash URL strategy; useful when deploying to static hosts without SPA support, like GitHub Pages.
- Uploads the web output as a Pages artifact.
- Deploys only on push to the `main` branch.
- Supports manual runs via `workflow_dispatch`.

## Common customization points

- Triggers: adjust `push`, `pull_request`, and `workflow_dispatch` for your flow.
- Matrix targets: remove entries you do not need from `all-builds.yml`.
- Versioning:
  - `BUILD_NUMBER`
  - `BUILD_VERSION`
- Python/tooling:
  - `UV_PYTHON`
  - `FLET_CLI_NO_RICH_OUTPUT`
  - `PYTHONUTF8`
- Build commands: customize `flet build ...` flags to match your app requirements.

## Notes

- The workflows run with `--verbose` to make troubleshooting easier.
- Linux desktop builds need extra system packages, already handled in `all-builds.yml`.
- You can define app/version metadata in `pyproject.toml` if preferred. ([docs](https://docs.flet.dev/publish/#versioning))

## Resources

- [Flet publishing guide](https://docs.flet.dev/publish)
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [My YouTube video tutorial](https://youtu.be/ObO-D2TD_wo)

## Contributing

Contributions are welcome and appreciated! 😄 

Please open an issue or PR if you have any feedback or suggestions.
