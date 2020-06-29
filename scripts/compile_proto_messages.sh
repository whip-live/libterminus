#!/usr/bin/env bash

# Exit on error. Append "|| true" if you expect an error.
set -o errexit
# Exit on error inside any functions or subshells.
set -o errtrace
# Do not allow use of undefined vars. Use ${VAR:-} to use an undefined VAR
set -o nounset
# Catch the error in case mysqldump fails (but gzip succeeds) in `mysqldump |gzip`
set -o pipefail

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROTOC=${PROTOC:-"protoc"}

SRC_DIR="${__dir}/../messages"
DST_DIR="${__dir}/../"

echo "Generate proto implementations:"
$PROTOC -I=$SRC_DIR --python_out=$DST_DIR \
	$SRC_DIR/terminus/proto/core.proto \
	$SRC_DIR/terminus/proto/device_data.proto

echo "Completed with success"
