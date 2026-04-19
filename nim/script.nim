import os, strutils, algorithm

let input = paramStr(1)

echo "[Nim] upper: ", input.toUpperAscii()
echo "[Nim] reversed: ", join(reversed(input), "")
echo "[Nim] length: ", input.len