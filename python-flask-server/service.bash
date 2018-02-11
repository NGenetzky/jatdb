
PN="jatdb-server"
PV="0.0.1"

# GITROOT="${GITROOT-$(readlink -f ./$(git rev-parse --show-cdup))}"
DOCKER_USER='ngenetzky'

get_tag(){
  echo "$DOCKER_USER/$PN:$PV"
}

build() {
  docker build \
    -t $"$(get_tag)" \
    .
}

run() {
  docker run \
    --name "${PN}" \
    -p 80:80 \
    -v "$(pwd)/data:/data:rw" \
    "$(get_tag)"
}

main(){
  local action="${1?}"
  case $action in
    kill) docker kill "${PN}" ;;
    rm) docker rm "${PN}" ;;
    build) build ;;
    run) run ;;
    *) echo "Unrecognized action ($1)" ;;
  esac
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Bash Strict Mode
    set -eu -o pipefail
    set -x
    main "$@"
fi
