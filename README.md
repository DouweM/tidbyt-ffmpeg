# Tidbyt + FFmpeg

[Tidbyt](https://tidbyt.com/) app that shows a snapshot of a video stream using [FFmpeg](https://ffmpeg.org/).

Example using "SMPTE Color Bars With Timestamp" from [RTSP.stream](https://rtsp.stream/):

![Screenshot](screenshot.webp)


## Installation

This app is not available through Tidbyt's mobile app as it uses features that (for security reasons) are not supported in [community apps](https://tidbyt.dev/docs/publish/community-apps) that run on Tidbyt's official app server.

Instead, it needs to be run using [Pixbyt](https://pixbyt.dev), a self-hosted Tidbyt app server for advanced apps.

### 1. Set up Pixbyt

1. [Create your own Pixbyt repo](https://github.com/DouweM/pixbyt#1-create-your-own-pixbyt-repo)
2. [Configure your Tidbyt](https://github.com/DouweM/pixbyt#2-configure-your-tidbyt)

### 2. Install the app

1. Add this repo as a submodule under `apps`:

    ```bash
    git submodule add https://github.com/DouweM/tidbyt-ffmpeg.git apps/ffmpeg
    ```

1. Add an update schedule to `apps.yml` under `schedules:`:

    ```yaml
    schedules:
    # ...
    - name: ffmpeg
      interval: '*/5 * * * *' # Every 5 minutes
      job: ffmpeg
    ```

## Configuration

1. Find your video stream URL. It needs to be supported by [FFmpeg](https://ffmpeg.org/), but most video streams are.

1. Update `.env` with your configuration:

   ```bash
   FFMPEG_SOURCE_URL="<video stream URL>"
   ```

## Usage

Build and launch your Pixbyt app server:

1. [Build the app server](https://github.com/DouweM/pixbyt#4-build-the-app-server)
1. [Launch the app server](https://github.com/DouweM/pixbyt#5-launch-the-app-server)
