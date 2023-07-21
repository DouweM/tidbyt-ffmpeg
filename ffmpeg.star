load("render.star", "render")
load("pixlib/file.star", "file")
load("pixlib/const.star", "const")

def main(config):
  SOURCE_URL = config.get("source_url")
  snapshot = file.exec("snapshot.py", {"source_url": SOURCE_URL})

  return render.Root(
    render.Box(
      child=render.Image(src=snapshot, height=const.HEIGHT)
    )
  )

# TODO: get_schema
