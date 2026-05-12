# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a HyperFrames video production workspace for **Soluções Digitais** (DTI / Grupo Águia Branca). It contains a corporate motion-graphics video about RPA results for 2025/2026 (~2:44 total runtime).

## Commands

### HyperFrames (run from inside `RPA-video/`)

```bash
cd RPA-video
npx hyperframes preview          # open studio editor in browser
npx hyperframes render           # render to MP4
npx hyperframes lint             # validate all compositions
npx hyperframes lint --verbose   # include info-level findings
npx hyperframes docs <topic>     # local reference docs (no network)
```

Topics for `docs`: `data-attributes`, `gsap`, `compositions`, `rendering`, `examples`, `troubleshooting`

### TTS voiceover generation (run from project root)

```bash
# Generate from inline text
python3 tts-elevenlabs.py "Script text here" --output assets/<project>/voice-cena-XX.mp3 --project <project>

# Generate from a .txt file
python3 tts-elevenlabs.py assets/<project>/locucao-cena-XX.txt --output assets/<project>/voice-cena-XX.mp3 --project <project>

# List available voices
python3 tts-elevenlabs.py --list-voices
```

Requires `ELEVENLABS_API_KEY` set in `.env`. Default voice: `Gambeta` (9YV3DUwCgm6KWiUxKhxc, PT-BR professional), model: `eleven_multilingual_v2`.

**`--project` flag is mandatory.** Each project has its own subfolder under `assets/` (e.g. `rpa-video`, `analise-critica-motorista`). Omitting it risks overwriting another project's audio files since all voiceovers share the same `voice-cena-XX.mp3` naming scheme.

After generating, copy the `.mp3` files to the project's own `assets/` folder:
```bash
cp assets/rpa-video/voice-cena-0{1..7}.mp3 RPA-video/assets/
```

## Architecture

```
videos-gab/
├── assets/                            # Shared media — scoped by project subfolder
│   ├── brand/                         # SVG logos and brand image assets
│   ├── DESIGN.MD                      # Brand design system (colors, typography, layout specs)
│   ├── rpa-video/                     # Source-of-truth audio + scripts for RPA-video
│   │   ├── locucao-cena-01..07.txt    # VO scripts
│   │   └── voice-cena-01..07.mp3      # Generated audio (copy to RPA-video/assets/)
│   └── analise-critica-motorista/     # Source-of-truth audio + scripts for ANALISE project
│       ├── locucao-cena-01..09.txt
│       └── voice-cena-01..09.mp3
├── RPA-video/                         # HyperFrames project
│   ├── index.html                     # Root timeline, stitches scenes via data-composition-src
│   ├── assets/                        # Deployed audio used at render time (copied from assets/rpa-video/)
│   ├── compositions/                  # One HTML file per scene (cena-01 through cena-07)
│   ├── fonts/                         # Satoshi Variable + Cabin Bold (woff/woff2, self-hosted)
│   ├── hyperframes.json               # Project config (registry, path mappings)
│   ├── meta.json                      # Project ID and name
│   └── CLAUDE.md                      # HyperFrames-specific composition rules — READ THIS FIRST
├── ANALISE_CRITICA_MOTORISTA-video/   # HyperFrames project
│   └── …
├── skills/                            # Locally installed HyperFrames skills
├── tts-elevenlabs.py                  # ElevenLabs TTS helper script
└── .env                               # API keys (ELEVENLABS_API_KEY)
```

### Scene timeline (`RPA-video/index.html`)

| ID  | File                         | Start (s) | Duration (s) | Content               |
|-----|------------------------------|-----------|--------------|-----------------------|
| c1  | cena-01-abertura.html        | 0         | 10.3         | Kinetic title opener  |
| c2  | cena-02-dataviz.html         | 10.3      | 40.95        | Bar chart / KPIs      |
| c3  | cena-03-rh.html              | 51.25     | 36.72        | RH Metadados case     |
| c4  | cena-04-grid.html            | 87.97     | 35.19        | 4-quadrant impact grid|
| c5  | cena-05-highlight.html       | 123.16    | 15.22        | R$899k highlight      |
| c6  | cena-06-pilares.html         | 138.38    | 20.14        | 5 strategic pillars   |
| c7  | cena-07-fim.html             | 158.55    | 5.75         | Closing / logo        |

## Brand Design System (see `assets/DESIGN.MD` for full spec)

**Colors:**
- Navy `#1e3460` — primary dark background
- Blue `#0069b3` — primary brand blue
- Blue-accent `#0e6ac0` — stat cards / highlights
- Cream `#fdfbf4` — text on dark backgrounds
- Background gradient: `linear-gradient(164deg, #1e3460 15.4%, #0069b3 86.5%)`

**Typography (self-hosted fonts in `RPA-video/fonts/`):**
- Satoshi Variable — display (900), headlines (700), body (400)
- Cabin Bold — DTI sub-label only

**Canvas:** 1920 × 1080 px

**Motion defaults:**
- Entrance: fade + `y: 20→0`, `duration: 0.6s`, `ease: power2.out`
- Logo: scale `0.85→1.0` + fade, `ease: back.out(1.4)`
- Slide transitions: opacity crossfade, `0.4s`

## Key Constraints

- Always run `npx hyperframes lint` after editing any `.html` composition; fix all errors before finishing.
- Asset paths in compositions are relative to the `RPA-video/` directory (e.g., `../assets/voice-cena-01.mp3`).
- No dynamic JS inside compositions (`Date.now()`, `Math.random()`, network fetches are forbidden by the renderer).
- Voiceover `.mp3` files live in `assets/`; corresponding scripts in `assets/locucao-cena-XX.txt`.
