# HyperFrames Video Production Workspace

Multi-project workspace for **Soluções Digitais** (DTI / Grupo Águia Branca) corporate motion-graphics videos built with [HyperFrames](https://hyperframes.heygen.com/introduction).

## Projects

| Directory | Description | Scenes |
|---|---|---|
| `RPA-video/` | RPA results 2025/2026 — ~2:44 runtime | cena-01 → cena-07 |
| `ANALISE_CRITICA_MOTORISTA-video/` | Análise Crítica Motorista — 9 scenes | cena-01 → cena-09 |
| `ANALISE_CRITICA_IMPLANTACAO/` | Análise Crítica Implantação — 9 scenes | cena-01 → cena-09 |
| `ANALISE_CRITICA_RESULTADOS/` | Análise Crítica Resultados — 2 scenes | cena-intro, cena-outro |

Each project has its own `AGENTS.md` (HyperFrames rules) and `CLAUDE.md` (composition rules). **Read both before editing any composition.**

## Skills — Load Before Compositing

Skills are in `skills/` and `.agents/skills/`. Always invoke the relevant skill before writing or modifying HTML compositions — they encode non-obvious framework patterns that generic web docs won't cover.

| Skill | Trigger | Source |
|---|---|---|---|
| `/hyperframes` | Creating/editing compositions, captions, audio-reactive visuals, transitions | `heygen-com/hyperframes` |
| `/hyperframes-cli` | lint, preview, render, transcribe, tts CLI commands | `heygen-com/hyperframes` |
| `/hyperframes-registry` | `hyperframes add` — install blocks/components | `heygen-com/hyperframes` |
| `/gsap` | GSAP animations in compositions | `heygen-com/hyperframes` |
| `/website-to-hyperframes` | Capture a URL → video | `heygen-com/hyperframes` |
| `/remotion-to-hyperframes` | Port Remotion (React) code to HyperFrames | `heygen-com/hyperframes` |
| `/text-to-speech` | ElevenLabs TTS voiceover generation | `elevenlabs/skills` |

## Commands

Run HyperFrames commands from **inside the project directory**:

```bash
cd RPA-video   # or ANALISE_CRITICA_MOTORISTA-video/
npx hyperframes preview      # open studio in browser
npx hyperframes render       # render to MP4
npx hyperframes lint         # validate — fix all errors before finishing
npx hyperframes lint --verbose
npx hyperframes docs <topic> # local reference docs (no network)
```

## TTS Voiceover Generation

Run from **project root** (`videos-gab/`). The `--project` flag is **mandatory** to avoid overwriting another project's audio:

```bash
python3 tts-elevenlabs.py assets/<project>/locucao-cena-XX.txt \
  --output assets/<project>/voice-cena-XX.mp3 \
  --project <project>
```

After generating, copy to the project's `assets/` folder:

```bash
cp assets/rpa-video/voice-cena-0{1..7}.mp3 RPA-video/assets/
```

Requires `ELEVENLABS_API_KEY` in `.env`. Default voice: `Gambeta` (PT-BR).

## Asset Organization

```
assets/                        # Shared — source of truth
  brand/                       # SVG logos and brand assets
  DESIGN.MD                    # Brand design system — read for colors/typography
  rpa-video/                   # VO scripts + generated MP3s for RPA-video
  analise-critica-motorista/   # VO scripts + generated MP3s for Análise Crítica Motorista
  analise-critica-implantacao/ # VO scripts + generated MP3s + media for Análise Crítica Implantação

<ProjectDir>/assets/           # Deployed assets used at render time (copy from above)
```

**Never edit files in `<ProjectDir>/assets/` directly** — they are copies. Edit the source in the top-level `assets/<project>/` subfolder and re-copy.

## Installed Skills

Skills are installed in `.agents/skills/` (canonical source). Other `.xxx/` AI agent config directories are symlinks and ignored by git. Run `hyperframes add <skill>` to install new ones.

Installed skills (from `skills-lock.json`):
- `gsap` — from `heygen-com/hyperframes`
- `hyperframes` — from `heygen-com/hyperframes`
- `hyperframes-cli` — from `heygen-com/hyperframes`
- `hyperframes-registry` — from `heygen-com/hyperframes`
- `remotion-to-hyperframes` — from `heygen-com/hyperframes`
- `text-to-speech` — from `elevenlabs/skills`
- `website-to-hyperframes` — from `heygen-com/hyperframes`

## Brand Design System

Full spec: [assets/DESIGN.MD](assets/DESIGN.MD)

Quick reference:
- Navy `#1e3460` — dark backgrounds
- Blue `#0069b3` — primary brand blue
- Cream `#fdfbf4` — text on dark
- Gradient: `linear-gradient(164deg, #1e3460 15.4%, #0069b3 86.5%)`
- Canvas: **1920 × 1080 px**
- Fonts: Satoshi Variable (display/headlines/body) + Cabin Bold (DTI sub-label only)
- Motion defaults: fade + `y: 20→0`, `duration: 0.6s`, `ease: power2.out`

## Key Constraints

- Run `npx hyperframes lint` after every composition edit; fix all errors before finishing.
- No dynamic JS: `Date.now()`, `Math.random()`, network fetches are **forbidden** in compositions.
- Asset paths in compositions are relative to the project directory (e.g., `../assets/voice-cena-01.mp3` — note `../`).
- Each composition must register its GSAP timeline on `window.__timelines["composition-id"]` (paused).
