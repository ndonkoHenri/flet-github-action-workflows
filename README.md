# flet-github-action-workflows

GitHub Action Workflows to ease the packaging of your [Flet](https://flet.dev) apps.
Flet is a cross-platform framework, i.e., from a single codebase you can target multiple platforms: 
Android (`aab`, `apk`), iOS (`ipa`), Linux, macOS, Windows, and Web.

Feel free to reuse them and customize to your specific usecases and needs.

## What is in this repo

## What is in this repo

| File                                                                                                                 | Purpose                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`.github/workflows/all-builds.yml`](.github/workflows/all-builds.yml)                                               | Builds for Linux, macOS, Windows, AAB, APK, IPA, and Web.<br>More details [here](https://docs.flet.dev/publish/#github-actions).                                                                                          |
| [`.github/workflows/web-build-and-github-pages-deploy.yml`](.github/workflows/web-build-and-github-pages-deploy.yml) | Builds the web app and deploys it to GitHub Pages.<br><br>Uses:<br>• `--base-url ${GITHUB_REPOSITORY#*/}` (repository name as base URL)<br>• `--route-url-strategy hash` (recommended for static hosts like GitHub Pages) |
| [`pyproject.toml`](pyproject.toml)                                                                                   | Example Flet project configuration                                                                                                                                                                                        |
| [`src/main.py`](src/main.py)                                                                                         | Example Flet app to test the workflows                                                                                                                                                                                    |


**Quick start:**
1. Copy the workflow(s) you need into your own repository under `.github/workflows/`.
2. Push to GitHub or run manually from the Actions tab of your repository.

## Common customization points

- Triggers: adjust `push`, `pull_request`, and `workflow_dispatch` for your flow.
- Matrix targets: remove entries you do not need from `all-builds.yml`.
- Versioning: [`BUILD_NUMBER`](https://docs.flet.dev/publish/#build-number), [`BUILD_VERSION` ](https://docs.flet.dev/publish/#build-version).
- Python/tooling:
  - `UV_PYTHON` - the Python version to use
  - [`FLET_CLI_NO_RICH_OUTPUT`](https://docs.flet.dev/reference/environment-variables/#flet_cli_skip_flutter_doctor) - disables console rich output
  - [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8) - enables UTF-8 encoding for Python. Useful in Windows builds.
- Build commands: customize `flet build ...` flags to match your app requirements.

## Notes

- The workflows run with `--verbose` to make `flet build` troubleshooting easier.
- Linux desktop builds need extra system packages, already handled in `all-builds.yml`.
- You can define app metadata (like `BUILD_NUMBER` and `BUILD_VERSION`) in the `pyproject.toml` if preferred. ([docs](https://docs.flet.dev/publish/#versioning))

## Resources

- [Flet publishing guide](https://docs.flet.dev/publish)
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [My YouTube video tutorial](https://youtu.be/ObO-D2TD_wo)

## Contributing

Contributions are welcome.
Open an issue or PR with improvements, fixes, or suggestions.
