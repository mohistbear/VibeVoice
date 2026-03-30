#!/usr/bin/env bash
# VibeVoice 社区版 (mohistbear fork) — Gradio，默认简体中文界面 + 7862 端口（与 FaceFusion/ASR 错开）
# 依赖：Gradio 5.x 需 Python ≥3.10。建议在仓库根目录执行：
#   /opt/homebrew/bin/python3.11 -m venv .venv
#   .venv/bin/pip install -U pip && .venv/bin/pip install -e .
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$SCRIPT_DIR"

export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8

if [ -x "$ROOT/.venv/bin/python3" ]; then
  PY="$ROOT/.venv/bin/python3"
elif [ -x "$ROOT/.venv/bin/python" ]; then
  PY="$ROOT/.venv/bin/python"
else
  echo "未找到 $ROOT/.venv。请在 VibeVoice-cc 根目录用 Python 3.10+ 创建环境，例如:" >&2
  echo "  /opt/homebrew/bin/python3.11 -m venv .venv" >&2
  echo "  .venv/bin/pip install -U pip && .venv/bin/pip install -e ." >&2
  exit 1
fi

exec "$PY" gradio_demo.py \
  --zh \
  --model_path "${MODEL_PATH:-vibevoice/VibeVoice-1.5B}" \
  --device "${MODEL_DEVICE:-mps}" \
  --port "${GRADIO_PORT:-7862}" \
  --server_name "${GRADIO_SERVER_NAME:-0.0.0.0}" \
  "$@"
