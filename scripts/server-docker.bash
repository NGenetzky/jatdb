#!/bin/bash

SCRIPTDIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)"
readonly SERVER_DIR="$(readlink -f ${SCRIPTDIR}/../python-flask-server)"

server_open(){
  xdg-open 'http://0.0.0.0:8080/ui/#/'
}

server_help(){
cat << EOF
Server will be runnning at "0.0.0.0:8080".

Try it out!

xdg-open 'http://0.0.0.0:8080/ui/#/'

EOF
}

server_docker(){
  local args=$@
  local tag="jatdb_server"

  docker build \
    -t "${tag}" \
    "${SERVER_DIR}"

  server_help
  docker run \
    --rm \
    -p "8080:8080" \
    --name jatdb_server \
    "${tag}" \
    $@
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Bash Strict Mode
    set -eu -o pipefail

    # set -x
    server_docker "$@"
fi

