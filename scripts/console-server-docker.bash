#!/bin/bash

SCRIPTDIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)"

console_server_docker(){
  local args=$@
  local name="jatdb_server"

  docker exec -it \
    "${name}" \
    /bin/sh
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Bash Strict Mode
    set -eu -o pipefail

    # set -x
    console_server_docker "$@"
fi

