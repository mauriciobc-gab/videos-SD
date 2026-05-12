#!/usr/bin/env python3
"""
ElevenLabs TTS helper for HyperFrames voiceovers.

Usage:
  python3 tts-elevenlabs.py "Your script here" --output narration.wav
  python3 tts-elevenlabs.py script.txt --output narration.wav
  python3 tts-elevenlabs.py --list-voices

Requires ELEVENLABS_API_KEY in .env (or as env var).
"""

import argparse
import os
import sys
from pathlib import Path

def load_env():
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

def get_api_key():
    key = os.environ.get("ELEVENLABS_API_KEY", "")
    if not key or key == "your_api_key_here":
        print("Error: ELEVENLABS_API_KEY not set. Edit .env and replace the placeholder.", file=sys.stderr)
        sys.exit(1)
    return key

def list_voices(client):
    voices = client.voices.get_all()
    print(f"{'Name':<30} {'Voice ID':<25} {'Category'}")
    print("-" * 70)
    for v in voices.voices:
        category = getattr(v, "category", "—") or "—"
        print(f"{v.name:<30} {v.voice_id:<25} {category}")

def main():
    parser = argparse.ArgumentParser(description="Generate voiceover with ElevenLabs API")
    parser.add_argument("input", nargs="?", help="Text to speak, or path to a .txt file")
    parser.add_argument("-o", "--output", default="narration.mp3", help="Output .mp3 file (default: narration.mp3)")
    parser.add_argument("-v", "--voice", default="9YV3DUwCgm6KWiUxKhxc", help="Voice name or ID (default: Gambeta, PT-BR professional)")
    parser.add_argument("-m", "--model", default="eleven_multilingual_v2", help="Model ID (default: eleven_multilingual_v2)")
    parser.add_argument("--stability", type=float, default=0.5, help="Voice stability 0.0-1.0 (default: 0.5)")
    parser.add_argument("--similarity", type=float, default=0.75, help="Similarity boost 0.0-1.0 (default: 0.75)")
    parser.add_argument("--style", type=float, default=0.0, help="Style exaggeration 0.0-1.0 (default: 0.0)")
    parser.add_argument("--list-voices", action="store_true", help="List available voices and exit")
    parser.add_argument("--project", default=None, help="Project slug (e.g. rpa-video). Scopes assets/ paths to assets/<project>/ to avoid cross-project filename collisions.")
    args = parser.parse_args()

    # Inject project subfolder into assets/ paths so files from different projects
    # never share the same flat namespace and overwrite each other.
    if args.project:
        project = args.project.strip("/")
        def _scope(p):
            """Rewrite 'assets/foo' -> 'assets/<project>/foo' if not already scoped."""
            parts = Path(p).parts
            if parts and parts[0] == "assets" and (len(parts) < 2 or parts[1] != project):
                return str(Path("assets") / project / Path(*parts[1:]))
            return p
        if args.input:
            args.input = _scope(args.input)
        args.output = _scope(args.output)

    load_env()
    api_key = get_api_key()

    from elevenlabs.client import ElevenLabs

    client = ElevenLabs(api_key=api_key)

    if args.list_voices:
        list_voices(client)
        return

    if not args.input:
        parser.error("INPUT is required (text or .txt file path)")

    # Resolve input text
    input_path = Path(args.input)
    if input_path.suffix == ".txt" and input_path.exists():
        text = input_path.read_text(encoding="utf-8").strip()
        print(f"Reading script from {input_path} ({len(text)} chars)")
    else:
        text = args.input

    if not text:
        print("Error: empty script.", file=sys.stderr)
        sys.exit(1)

    # Resolve voice (name → ID lookup, or pass ID directly)
    voice_param = args.voice

    print(f"Generating speech → {args.output}  [voice: {voice_param}, model: {args.model}]")

    audio = client.text_to_speech.convert(
        voice_id=voice_param,
        text=text,
        model_id=args.model,
        voice_settings={
            "stability": args.stability,
            "similarity_boost": args.similarity,
            "style": args.style,
            "use_speaker_boost": True,
        },
        output_format="mp3_44100_128",
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    print(f"Saved: {output_path.resolve()}")

if __name__ == "__main__":
    main()
