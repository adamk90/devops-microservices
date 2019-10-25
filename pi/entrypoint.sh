#!/bin/bash

/consul agent --retry-join consul --data-dir=/tmp/x --config-file=/pi.json > /dev/null &

exec "$@"
