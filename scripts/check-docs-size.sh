#!/usr/bin/env sh
# Fails if any docs .md file is larger than 4096 bytes or not linked from README.md.
set -eu
MAX=4096
status=0
for f in README.md $(find org projects plan meta tasks -type f -name '*.md' | sort); do
  size=$(wc -c < "$f" | tr -d ' ')
  if [ "$size" -gt "$MAX" ]; then
    echo "TOO BIG: $f ($size bytes > $MAX)"; status=1
  fi
  if [ "$f" != "README.md" ] && ! grep -q "($f)" README.md; then
    echo "NOT IN INDEX: $f"; status=1
  fi
done
[ "$status" -eq 0 ] && echo "docs OK"
exit "$status"
