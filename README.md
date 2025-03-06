# flet-github-action-workflows

A collection of useful GitHub Action Workflows to ease the building of [Flet](https://flet.dev) applications.

Feel free to adapt all the workflows in this repo to your own projects: [flet.dev/publish](https://flet.dev/publish)

## Video Tutorial

Watch this video I made to get started: https://youtu.be/ObO-D2TD_wo ⬇️

[![YouTube](http://i.ytimg.com/vi/ObO-D2TD_wo/hqdefault.jpg)](https://www.youtube.com/watch?v=ObO-D2TD_wo)

## File Structure

As you might know, Flet is a cross-platform framework. This means, from a single codebase you can target multiple platforms: Android (AAB, APK), iOS (IPA), Linux, macOS, Windows, and Web.

The repository contains the following workflows (located in the [`.github/workflows`](.github/workflows) directory):


| File Name                                                                                        | Builds                                                                          | Runs on                                     |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------|
| [aab-build.yml](.github/workflows/aab-build.yml)                                                 | Android App Bundle (AAB)                                                        | ubuntu-latest                               |
| [apk-build.yml](.github/workflows/apk-build.yml)                                                 | Android Application Package (APK)                                               | ubuntu-latest                               |
| [desktop-and-mobile-builds.yml](.github/workflows/desktop-and-mobile-builds.yml)                 | desktop [linux, macOS, windows] and mobile [Android (AAB, APK), iOS (IPA)] apps | ubuntu-latest, macos-latest, windows-latest |
| [desktop-build.yml](.github/workflows/desktop-builds.yml)                                        | desktop [Linux, macOS, windows] apps                                            | ubuntu-latest, macos-latest, windows-latest |
| [ipa-build.yml](.github/workflows/ipa-build.yml)                                                 | iOS Package App Store (IPA)                                                     | macos-latest                                |
| [linux-build.yml](.github/workflows/linux-build.yml)                                             | linux app                                                                       | ubuntu-latest                               |
| [macos-build.yml](.github/workflows/macos-build.yml)                                             | macOS app                                                                       | macos-latest                                |
| [mobile-builds.yml](.github/workflows/mobile-builds.yml)                                         | mobile [Android (AAB, APK), iOS (IPA)] apps                                     | ubuntu-latest, macos-latest                 |
| [web-build-and-github-pages-deploy.yml](.github/workflows/web-build-and-github-pages-deploy.yml) | static web app and deploys it to GitHub Pages                                   | ubuntu-latest                               |
| [windows-build.yml](.github/workflows/windows-build.yml)                                         | windows app                                                                     | windows-latest                              |

## GitHub Actions 

All the workflows in this repository are based on [GitHub Actions](https://github.com/features/actions). 
Read it's [documentation](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) to get started. Understanding the syntax will be very useful if you want to customize the workflows to suit your specific needs.

The following actions from the [GitHub marketplace](https://github.com/marketplace?type=actions) are used in one or more of the workflows in this repository:

- [actions/checkout](https://github.com/marketplace/actions/checkout): checks-out your repository for use in the workflow
- [actions/configure-pages](https://github.com/marketplace/actions/configure-pages): configures the GitHub Pages action for web deployment
- [actions/deploy-page](https://github.com/marketplace/actions/deploy-pages): deploys your static site to GitHub Pages
- [actions/setup-python](https://github.com/marketplace/actions/setup-python): sets up a Python environment
- [actions/setup-java](https://github.com/marketplace/actions/setup-java-jdk): sets up Java JDK
- [actions/upload-artifact](https://github.com/marketplace/actions/upload-a-build-artifact): uploads a build artifact for a workflow run
- [subosito/flutter-action](https://github.com/marketplace/actions/flutter-action): sets up a Flutter environment

See their respective documentation for more information on how to further customize their execution.

Thanks to their creators!

## Usage
- Choose the workflow that suits your needs. For example, if you are building an Linux app, you can choose the [linux-build.yml](.github/workflows/linux-build.yml) workflow.
- Copy the content of the chosen workflow file.
- Create a new file in your repository under the `.github/workflows` directory and paste the copied content into it.
- Modify the file as needed. For example, you might want to change the event that triggers the workflow, the name of the workflow, the name of the job, etc. It's up to you.
- Name the file to your liking, but make sure it ends with `.yml` extension, else it won't be recognized as a workflow file.
- Commit the changes and push them to your repository.
- Go to the Actions tab in your repository. If you haven't modified the file, you should see the workflow running, as a result of a push to `main`/`master` branch. Else, you can trigger it manually by clicking on the `Run workflow` button.

## Example

This repo has a branch named [`example`](https://github.com/ndonkoHenri/flet-github-action-workflows/tree/example) which contains a simple example application which gets built using some of the workflows in this repo.

See the [Actions tab](https://github.com/ndonkoHenri/flet-github-action-workflows/actions) of this repository to see the workflows in action.

## For Your Information (FYI)

- Customize the build command for your specific needs. Docs: [flet.dev/publish](https://flet.dev/publish)
- `BUILD_NUMBER` and `BUILD_VERSION` are used for [versioning](https://flet.dev/docs/publish#versioning). If you instead prefer defining them in your `pyproject.toml`, feel free to remove them from the workflow.
- Only `flet-cli` needs to be installed when building a Flet app. The version to be installed is specified by the `FLET_CLI_VERSION` environment variable.
- All workflows are based on the `FLUTTER_VERSION` and `PYTHON_VERSION` environment variables.
- `PYTHONUTF8` is set to `1`, ensuring that the build outputs are decoded in UTF-8. (useful on Windows)
- `FLET_CLI_NO_RICH_OUTPUT` and `UV_NO_PROGRESS` (effective only when using uv) are set to `1` to reduce rich & live output from the build output.
- You might find the below in some of the workflows:
  - `workflow_dispatch`: used to trigger the workflow manually from the Actions tab
  - `flutter config --no-analytics`: disables Flutter analytics
- The below error occured on Linux when `flutter doctor` was run:
    ```
    [✗] Linux toolchain - develop for Linux desktop
        ✗ ninja is required for Linux development.
          It is likely available from your distribution (e.g.: apt install ninja-build), or can be downloaded from https://github.com/ninja-build/ninja/releases
        ✗ GTK 3.0 development libraries are required for Linux development.
          They are likely available from your distribution (e.g.: apt install libgtk-3-dev)
    ```
    
    A step named `Patch for linux build` was added to the linux-related jobs/workflows which resolves this issue by installing the required dependencies.
- The build commands are run in verbose mode (`--verbose`) to provide detailed information about the build process. This is very useful when you need to report an issue on the [Flet repo](https://github.com/flet-dev/flet).

## Contribution

You can contribute by adding more workflows, improving the existing ones, or reporting issues you encounter.

**Improvements ideas:**
- Add a step for releasing the built artifacts to the GitHub releases
- It will be nice if we could take advantage of caching to speed up the builds

