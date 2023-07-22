# Tidbyt + FFmpeg

[Tidbyt](https://tidbyt.com/) app that shows a snapshot of a video stream using [FFmpeg](https://ffmpeg.org/).

Example using "SMPTE Color Bars With Timestamp" from [RTSP.stream](https://rtsp.stream/):

![Screenshot](screenshot.webp)

---

Note that this app **cannot be installed from Tidbyt's smartphone app** as it uses features that (for security reasons) are not supported in [community apps](https://tidbyt.dev/docs/publish/community-apps) that run on Tidbyt's official app server.
(Your Tidbyt does not run apps directly; it depends on a server to periodically run apps and push the resulting images to the device.)

Specifically, this app uses [Pixlib](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib), the unofficial standard library for [Pixlet](https://github.com/tidbyt/pixlet) (the Tidbyt app development framework), similar to how [Starlib](https://github.com/qri-io/starlib) is the unofficial standard library for [Starlark](https://github.com/google/starlark-go) (the Python-like language Tidbyt app are written in).
It also uses [Python packages](./requirements.txt) and depends on [FFmpeg](https://ffmpeg.org/).

These features are enabled by [`tap-pixlet`](https://github.com/DouweM/tap-pixlet), an unofficial Tidbyt app runner that extends Pixlet with the Pixlib standard library and advanced abilities like reading local (image) files, reaching local network resources, and running Python scripts and packages.

To render this app to your Tidbyt or a WebP image file, follow the instructions below.
They use `tap-pixlet` to run the app, [`target-tidbyt`](https://github.com/DouweM/target-tidbyt) and [`target-webp`](https://github.com/DouweM/target-tidbyt) to push the resulting image to your Tidbyt or a WebP image file, and [Meltano](https://github.com/meltano/meltano) to tie these components together.
You can use these same components to set up your own Tidbyt app server for apps like this one, that are too advanced for the official community app server.

## Installation

1. Install [FFmpeg](https://ffmpeg.org/):

    - On macOS:

      ```bash
      brew install ffmpeg
      ```

    - [Other operating systems](https://ffmpeg.org/download.html)

1. Install [Pixlet](https://github.com/tidbyt/pixlet):

    - On macOS:

      ```bash
      brew install tidbyt/tidbyt/pixlet
      ```

    - [Other operating systems](https://tidbyt.dev/docs/build/installing-pixlet)

1. Install [Meltano](https://github.com/meltano/meltano):

   - With `pip`:

      ```bash
      pip install meltano
      ```

   - [Other installation methods](https://docs.meltano.com/getting-started/installation)

1. Clone this repository and enter the new directory:

    ```bash
    git clone https://github.com/DouweM/tidbyt-ffmpeg.git
    cd tidbyt-ffmpeg
    ```

1. Install [`tap-pixlet`](https://github.com/DouweM/tap-pixlet), [`target-tidbyt`](https://github.com/DouweM/target-tidbyt), and [`target-webp`](https://github.com/DouweM/target-tidbyt) using Meltano:

    ```bash
    meltano install
    ```

## Configuration

1. Create your own `.env` configuration file from the sample:

   ```bash
   cp .env.sample .env
   ```

1. Find your video stream URL. It needs to be supported by [FFmpeg](https://ffmpeg.org/), but most video streams are.

1. Update `.env` with your configuration:

   ```bash
   FFMPEG_SOURCE_URL="<video stream URL>"
   ```

## Usage

### Render app to a WebP image file

The image will be created at `output/ffmpeg/<timestamp>.webp`.
The exact path is also printed in the command output.

#### Regular size (64x32)

```bash
meltano run webp
```

#### Magnified 8 times (512x256)

```bash
TAP_PIXLET_MAGNIFICATION=8 meltano run webp
```

### Render app to your Tidbyt

#### Configure your Tidbyt

1. If you haven't already, create your own `.env` configuration file from the sample:

   ```bash
   cp .env.sample .env
   ```

1. Find your Device ID and your API Token in the Tidbyt smartphone app under Settings > General > Get API Key.

1. Update `.env` with your configuration:

   ```bash
   TIDBYT_DEVICE_ID="<device ID>"
   TIDBYT_TOKEN="<token>"
   ```

#### Send to foreground

The app will immediately show up on your Tidbyt.
This is useful during development.

```bash
TAP_PIXLET_BACKGROUND=false meltano run tidbyt
```

#### Send to background

The app will be added to the Tidbyt app rotation.
This is useful when you're running this command on a schedule, to make sure that the app will be up to date the next time it comes up in the app rotation.

```bash
meltano run tidbyt
```