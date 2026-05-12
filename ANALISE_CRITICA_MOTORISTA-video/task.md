# ANALISE_CRITICA_MOTORISTA — Task Log

## Design Context

### Users
C-level and senior leadership at Grupo Águia Branca — a large Brazilian transportation group. They watch this in a meeting or presentation context: projected screen, limited attention, high stakes. They need to feel *convinced*, not informed. They are not reading slides; they are receiving an argument. Every second must justify itself.

### Brand Personality
**Moderno · Informativo · Institucional**

The brand speaks with authority, not enthusiasm. It doesn't shout — it states. The product (driver cognitive fitness platform) is serious infrastructure for a safety-critical operation. The tone is confident, measured, and precise. Think Volvo Safety meets Apple product keynote: the product IS the hero, the technology IS the argument.

### Aesthetic Direction
**Reference**: Apple product presentations + modern tech startup design language.  
What this means concretely: purposeful whitespace, type doing the heavy lifting, deliberate contrast, smooth and choreographed motion with no ambient "decoration." Clarity as luxury.

**Anti-reference (inferred)**: Generic Brazilian corporate slide decks (clip-art icons, rainbow gradients, busy layouts). Also explicitly avoid the "AI slop" palette — no cyan-on-dark neon glow aesthetics, no purple-to-blue gradients trying to look "futuristic."

**Theme**: Dark-background-first. Navy `#1e3460` base, blue `#0069b3` primary, `#86e5ff` as a *rare* accent (not everywhere), cream `#fdfbf4` text. The palette already has the Apple-like restraint — don't pollute it.

**Typography**: Satoshi Variable is the workhorse — it has the clean geometric confidence of SF Pro without copying it. Cabin Bold for meta labels only. Never mix in system fonts or fallbacks.

### Design Principles

1. **Clarity is the product** — if something doesn't help the viewer understand faster or feel the argument more strongly, remove it. No decorative complexity.

2. **Type at video scale** — headlines should be physically large enough to register from a projected screen across a conference room. 64px minimum for any content that matters; 40px is the floor for supporting text.

3. **Motion reveals, never decorates** — every GSAP tween should answer "what is the viewer supposed to notice right now?" Entrances sync to voiceover beats. No ambient loop tweens except the final hold.

4. **The phone mockup is the product hero** — in scenes 03–08, the mockup is a persistent prop, not a decoration. It must stay stable, never flicker or re-enter. The content on the right changes; the device does not.

5. **Institutional authority through restraint** — avoid anything that reads "startup pitch deck." Fewer elements, more deliberate spacing, heavier type weights. The composition should look expensive, not busy.

### Active Composition Rules (ANALISE_CRITICA_MOTORISTA-video)

- **Scenes 03–08**: Phone mockup persists across crossfade transitions. Do NOT re-animate it on enter.
- **All transitions C3→C4, C4→C5, C5→C6, C6→C7, C7→C8**: Crossfade only — never slide or zoom.
- **Demo video**: `assets/demo-analise-critica-motorista.mp4` must be re-encoded with dense keyframes (`ffmpeg -i input.mp4 -c:v libx264 -r 30 -g 30 -keyint_min 30 -movflags +faststart output.mp4`) before final render to avoid seek failures.
- **`<br>` is forbidden** in composition content — use `<div>` or `<span>` with flex layout.
- **Bar animations**: Use `scaleX` with `transform-origin: left center`, never animate `width`.
- **Final scene (cena-09) only**: `gsap.to` fading to `opacity: 0` is permitted — that's the only allowed exit tween.
