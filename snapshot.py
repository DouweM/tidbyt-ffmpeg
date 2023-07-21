import sys
import json
import tempfile
from ffmpeg import FFmpeg

config = json.loads(sys.argv[1])
source_url = config["source_url"]

with tempfile.NamedTemporaryFile(mode="w+b", prefix="snapshot.", suffix=".jpg") as temp_file:
    filename = temp_file.name

    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(source_url)
        .output(
            filename,
            {
                "frames:v": "1",
                "f": "image2",
                "filter:v": "scale='min(64,iw)':'min(32,ih)':force_original_aspect_ratio=increase,crop=64:32"
            }
        )
    )
    ffmpeg.execute()

    snapshot = temp_file.read()

sys.stdout.buffer.write(snapshot)
