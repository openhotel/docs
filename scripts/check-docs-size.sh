#!/usr/bin/env sh
# Fails if any docs .md file is larger than 4096 bytes or not linked from its index.
# Index: ideas/** -> ideas/README.md, everything else -> README.md.
set -eu
MAX=4096
status=0
for f in README.md $(find org projects ideas meta tasks -type f -name '*.md' | sort); do
  size=$(wc -c < "$f" | tr -d ' ')
  if [ "$size" -gt "$MAX" ]; then
    echo "TOO BIG: $f ($size bytes > $MAX)"; status=1
  fi
  case "$f" in
    README.md|ideas/README.md) ;;
    ideas/*) grep -q "(${f#ideas/})" ideas/README.md || { echo "NOT IN ideas/README.md: $f"; status=1; } ;;
    *) grep -q "($f)" README.md || { echo "NOT IN README.md: $f"; status=1; } ;;
  esac
done
[ "$status" -eq 0 ] && echo "docs OK"
exit "$status"
