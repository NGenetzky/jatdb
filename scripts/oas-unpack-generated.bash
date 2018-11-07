#!/bin/bash

SCRIPTDIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)"
readonly OAS_DIR="$(readlink -f ${SCRIPTDIR}/../oas)"

oas_unpack_generated(){
  local zipfile="${1?}"

  local s="${OAS_DIR}/default"
  case "${zipfile}" in
    *html2-client-generated.zip)
      local s="${OAS_DIR}/html2"
      ;;
    *python-client-generated.zip)
      local s="${OAS_DIR}/python-client"
      ;;
    *python-flask-server-generated.zip)
      local s="${OAS_DIR}/python-flask-server"
      ;;
    *swagger-yaml-client-generated.zip)
      local s="${OAS_DIR}/api"
      ;;
    *)
      return 1
      ;;
  esac

  rm -r "${s}"
  unzip -d "${s}" "${zipfile}"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Bash Strict Mode
    set -eu -o pipefail

    # set -x
    oas_unpack_generated "$@"
fi

