docker run -it \
  --volume $(pwd):/mnt/pwd:rw \
  --volume $(pwd)/secrets.json:/tmp/secrets.json:ro \
  ngenetzky/jatdb
