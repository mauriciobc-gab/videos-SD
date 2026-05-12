# HyperFrames Composition Project — ANALISE_CRITICA_MOTORISTA-video

## Skills — USE THESE FIRST

**Always invoke the relevant skill before writing or modifying compositions.** Skills encode framework-specific patterns (e.g., `window.__timelines` registration, `data-*` attribute semantics, shader-compatible CSS rules) that are NOT in generic web docs. Skipping them produces broken compositions.

| Skill | Command | When to use |
|---|---|---|
| **hyperframes** | `/hyperframes` | Creating or editing HTML compositions, captions, TTS, audio-reactive animation, marker highlights |
| **hyperframes-cli** | `/hyperframes-cli` | CLI commands: lint, preview, render, transcribe, tts |
| **hyperframes-registry** | `/hyperframes-registry` | Installing blocks and components via `hyperframes add` |
| **website-to-hyperframes** | `/website-to-hyperframes` | Capturing a URL and turning it into a video |
| **gsap** | `/gsap` | GSAP animations — tweens, timelines, easing, performance |

## Commands

```bash
npm run dev          # preview in browser (studio editor)
npm run check        # lint + validate + inspect — ALWAYS run before finishing
npm run render       # render to MP4
npm run publish      # publish and get a shareable link
npx hyperframes docs <topic>  # reference docs in terminal
```

## Project Structure

- `index.html` — main composition (root timeline)
- `compositions/` — sub-compositions referenced via `data-composition-src`
- `assets/` — media files (video, audio, images)
- `meta.json` — project metadata (id, name)
- `transcript.json` — whisper word-level transcript (if generated)

## Linting — Always Run After Changes

After creating or editing any `.html` composition, run the full check before considering the task complete:

```bash
npm run check
```

Fix all errors before presenting the result.

## Key Rules

1. Every timed element needs `data-start`, `data-duration`, and `data-track-index`
2. Visible timed elements **must** have `class="clip"` — the framework uses this for visibility control
3. GSAP timelines must be paused and registered on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
4. Videos use `muted` with a separate `<audio>` element for the audio track
5. Sub-compositions use `data-composition-src="compositions/file.html"`
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches

## Documentation

Full docs: https://hyperframes.heygen.com/introduction

Machine-readable index for AI tools: https://hyperframes.heygen.com/llms.txt
