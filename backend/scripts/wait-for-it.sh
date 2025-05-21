#!/usr/bin/env bash
# Use: ./wait-for-it.sh host:port -- command_to_run_after

hostport=$1
shift
cmd="$@"

host=$(echo "$hostport" | cut -d: -f1)
port=$(echo "$hostport" | cut -d: -f2)

until nc -z "$host" "$port"; do
  echo "Waiting for $host:$port..."
  sleep 2
done

exec $cmd
