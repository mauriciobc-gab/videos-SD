# Design System — Soluções Digitais

Brand reference extracted from the Figma file **Branding Soluções Digitais** (`oUsCTvAbiRT4sZPrAvZyjx`) and consolidated from production patterns used across the RPA 2026 video series.

> **Purpose:** This document is the single source of truth for all video compositions in the Soluções Digitais series. Every new video should follow these specs to maintain visual consistency.

---

## 1. Brand Identity

**Product:** Soluções Digitais  
**Client:** DTI — Diretoria de Tecnologia e Inovação / Grupo Águia Branca  
**Logo mark:** SD hexagonal icon + two-line wordmark ("Soluções" bold / "Digitais" regular)

### Logo variants

| Variant | Background | Icon color | "Soluções" | "Digitais" |
|---|---|---|---|---|
| Azul fundo claro (horizontal) | `#ffffff` | `#0069b3` + `#1e3460` | `#0069b3` | `#1e3460` |
| Branco fundo escuro (horizontal) | `#1e3460` | white | `#fdfbf4` | `#fdfbf4` |
| Branco fundo gradiente (horizontal) | gradient (see §4) | white | `#fdfbf4` | `#fdfbf4` |
| Vertical fundo claro | `#ffffff` | `#1e3460` | `#1e3460` | `#1e3460` |
| Vertical fundo escuro | `#1e3460` | white | `#fdfbf4` | `#fdfbf4` |
| Vertical fundo gradiente | gradient (see §4) | white | `#fdfbf4` | `#fdfbf4` |

---

## 2. Colors

| Token | Hex / Value | Usage |
|---|---|---|
| `navy` | `#1e3460` | Primary dark background, wordmark dark |
| `navy-alt` | `#1d325d` | Alternative dark background (subtle variation for depth) |
| `blue` | `#0069b3` | Primary brand blue, icon primary color |
| `blue-accent` | `#0e6ac0` | Stats cards, data highlights, borders, glows |
| `cream` | `#fdfbf4` | Primary text on dark/gradient backgrounds |
| `cyan-glow` | `#86e5ff` | Highlight accents, lead paragraphs, emphasis text |
| `muted-text` | `#b6becf` | Subtitle text, secondary labels on dark slides |
| `black-65` | `rgba(0,0,0,0.65)` | Subtitle text on white slides (rarely used) |

### Opacity scale for cream text

| Opacity | Usage |
|---|---|
| `0.9` | Primary headlines, header labels |
| `0.85` | Body text, card labels, quad labels |
| `0.8` | Secondary labels, meta text |
| `0.7` | Subtitles, section headers, flow titles |

### Background gradient (Degrade-fundo)

```css
background: linear-gradient(164deg, #1e3460 15.4%, #0069b3 86.5%);
```

Used on: signature slide, logo variants with gradient background.

### Background overlay pattern

Almost every dark scene uses a consistent content overlay to improve text legibility over background graphics:

```css
.scene-content {
  background: rgba(30, 52, 96, 0.4);
}
```

---

## 3. Typography

**Primary typeface:** Satoshi Variable  
Source: `font-family: 'Satoshi Variable', sans-serif`

| Role | Weight | Notes |
|---|---|---|
| Display / big numbers | Black (900) | Stats numerals (e.g. "50", "10", "43", "R$ 899.000") |
| Headlines / wordmark "Soluções" | Bold (700) | Slide titles, logo wordmark first line |
| Subheadlines / emphasis | SemiBold (600) | Subtitles, secondary headlines |
| Body / wordmark "Digitais" | Regular (400) | Logo wordmark second line, card labels |
| Lead paragraphs / descriptions | Light (300) | Descriptive text, lead copy |

**Secondary typeface:** Cabin Bold  
Used for: DTI sub-label, section headers, meta labels  
`font-variation-settings: 'wdth' 100`

### Type scale (production slide dimensions 1920×1080)

| Element | Size | Weight | Tracking | Notes |
|---|---|---|---|---|
| Hero counter | 160px | 900 | −0.03em | Big number reveals (e.g. R$ 899.000) |
| Keyword / impact word | 80–120px | 900 | −0.03em | Kinetic opener keywords |
| Section title | 128px | 700 | −6.4px | Large slide titles (rare) |
| Slide headline | 96px | 700 | −0.02em | Primary headlines |
| Sub-headline | 72px | 900 | −0.02em | Phrase lines, closing words |
| Stats unit label | 48px | 400 | — | Unit labels ("/semana", "/mês") |
| Section header | 48px | 700 | — | Card section titles |
| Subtitle / description | 36px | 400–700 | 0.1em | Subtitles, typewriter lines |
| Lead paragraph | 32px | 300 | — | Descriptive lead copy |
| Flow title / meta | 24px | 700 | 0.25em | Uppercase meta labels |
| Card label | 24px | 400 | — | Quad card descriptions |
| Metric label | 20px | 400 | 0.1em | Uppercase metric descriptions |
| Logo wordmark | ~59px | 700/400 | — | "Soluções" / "Digitais" |
| Logo wordmark (small) | 32px | — | +4.48–8.8px | Compact wordmark |
| DTI sub-label | ~13px | 700 | — | "Diretoria de Tecnologia e Inovação" |

### Letter-spacing guidelines

| Context | Value |
|---|---|
| Tight headlines | −0.03em to −0.02em |
| Body / neutral | 0 |
| Uppercase labels | +0.05em to +0.3em |
| Wide meta labels | +0.15em to +0.3em |

---

## 4. Common Layout Patterns

### 4.1 Scene wrapper

Every composition follows this base structure:

```css
#scene-id {
  width: 1920px;
  height: 1080px;
  overflow: hidden;
  background: #1e3460;
  font-family: "Satoshi Variable", sans-serif;
  color: #fdfbf4;
  position: relative;
}
```

### 4.2 Scene content overlay

```css
.scene-content {
  width: 100%;
  height: 100%;
  padding: 80px 120px;   /* or 80px 140px, 80px */
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 40px;
  background: rgba(30, 52, 96, 0.4);
}
```

### 4.3 Background graphics

| Pattern | Usage | Opacity |
|---|---|---|
| Grid lines (SVG pattern) | Tech/data scenes | 0.12 |
| Hex pattern (SVG) | Process/flow scenes | 0.08 |
| Geo lines (SVG lines) | Strategic/pillar scenes | 0.1–0.3 |
| Particles (circles + lines) | Kinetic openers | 0.2–0.7 |
| Photo + gradient overlay | Closing slides | photo 0.5, gradient multiply |
| SD watermark (large icon) | Closing slides | 0.08, `mix-blend-mode: soft-light` |

### 4.4 Corner accents

Decorative corner brackets used on opener scenes:

```css
.corner-accent {
  position: absolute;
  width: 80px;
  height: 80px;
  border: 2px solid rgba(253, 251, 244, 0.2);
}
.corner-tl { top: 40px; left: 40px; border-right: none; border-bottom: none; }
.corner-tr { top: 40px; right: 40px; border-left: none; border-bottom: none; }
.corner-bl { bottom: 40px; left: 40px; border-right: none; border-top: none; }
.corner-br { bottom: 40px; right: 40px; border-left: none; border-top: none; }
```

### 4.5 Text legibility helpers

For text placed over complex backgrounds, use inline-block backgrounds:

```css
.text-highlight {
  background: rgba(30, 52, 96, 0.85);
  padding: 8px 24px;
  border-radius: 8px;
  display: inline-block;
}
```

---

## 5. UI Components

### 5.1 Metric card

Used for single-stat displays with icon:

```css
.metric-card {
  width: 340px;
  background: rgba(14, 106, 192, 0.12);
  border: 1px solid rgba(14, 106, 192, 0.35);
  border-radius: 20px;
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}
.metric-value {
  font-size: 56px;
  font-weight: 900;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}
.metric-label {
  font-size: 20px;
  font-weight: 400;
  color: rgba(253, 251, 244, 0.85);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
```

### 5.2 Quad card (impact grid)

Used for 2×2 or multi-quadrant layouts:

```css
.quad {
  border-radius: 24px;
  padding: 48px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(14, 106, 192, 0.25);
  background: rgba(14, 106, 192, 0.08);
}
.quad-highlight {
  border-color: rgba(14, 106, 192, 0.6);
  background: rgba(14, 106, 192, 0.15);
}
.quad-value {
  font-size: 72px;
  font-weight: 900;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}
.quad-label {
  font-size: 24px;
  font-weight: 400;
  color: rgba(253, 251, 244, 0.8);
}
```

Optional glow line accent:

```css
.glow-line {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: #0e6ac0;
  box-shadow: 0 0 30px #0e6ac0;
  transform: scaleX(0);
  transform-origin: left center;
}
```

### 5.3 Flow node

Used for process flow diagrams:

```css
.flow-node {
  width: 120px;
  height: 120px;
  border-radius: 20px;
  background: rgba(14, 106, 192, 0.2);
  border: 2px solid rgba(14, 106, 192, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
.flow-arrow {
  font-size: 48px;
  font-weight: 900;
  color: #fdfbf4;
}
```

### 5.4 Pillar item

Used for numbered strategic pillars:

```css
.pillar {
  font-size: 56px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1.2;
  padding: 18px 48px;
  border-left: 6px solid #0e6ac0;
  background: rgba(30, 52, 96, 0.85);
  width: 100%;
  max-width: 900px;
}
.pillar-num {
  display: inline-block;
  width: 64px;
  font-weight: 900;
  color: #0e6ac0;
}
```

### 5.5 Tag

Used for keyword clusters:

```css
.tag {
  font-size: 22px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 14px 28px;
  border: 2px solid rgba(253, 251, 244, 0.3);
  border-radius: 8px;
  background: rgba(30, 52, 96, 0.85);
}
```

### 5.6 Shock ring

Used for emphasis moments around big numbers:

```css
.shock-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 600px;
  border-radius: 50%;
  border: 2px solid rgba(14, 106, 192, 0.4);
  pointer-events: none;
}
```

### 5.7 Formula card

Used for equation-style displays:

```css
.formula-card {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 50px;
  padding: 23px 40px;
  border-radius: 16px;
  border: 1px solid rgba(12, 104, 190, 0.5);
  background: rgba(24, 96, 168, 0.05);
  font-size: 32px;
  font-weight: 400;
  letter-spacing: 0.96px;
  color: #b6becf;
  text-align: center;
  white-space: nowrap;
}
```

---

## 6. Slide Templates

### 6.1 Kinetic Title Opener (`cena-01`)

**Purpose:** High-energy intro with floating keywords that resolve into the title.

**Structure:**
- Background: Navy (`#1e3460`) + grid pattern (0.12 opacity) + particles
- Corner accents (4 corners)
- 3 floating keywords (left, center, right): 80–120px, weight 900, uppercase
- Main title: 72px, weight 900, with subtitle (36px, weight 600)
- Meta label at bottom: 18px Cabin, uppercase, wide tracking

**Animation pattern:**
1. Keywords slide in from varied directions (`expo.out`)
2. Keywords exit upward (`power2.in`)
3. Title scales in from 0.85 (`power3.out`)
4. Subtle breath animation on title (`sine.inOut`)

---

### 6.2 Data Visualization / Split Screen (`cena-02`)

**Purpose:** Present data alongside narrative content with a photo sidebar.

**Structure:**
- Left column (~1048px): Title (96px), subtitle (48px), lead paragraph (32px, `#86e5ff`), formula card, impact block
- Right column (~589px): Full-height photo with dark overlay
- Background: `#1d325d` or navy

**Animation pattern:**
- Title slides up (`power3.out`)
- Photo scales in (`power3.out`)
- Formula card pops (`back.out(1.2)`)
- Elements stagger by ~0.15s

---

### 6.3 Process Flow with Metrics (`cena-03`)

**Purpose:** Show a step-by-step process with end metrics.

**Structure:**
- Background: Navy + hex pattern overlay
- Header label: 24px Cabin, uppercase, wide tracking
- Flow chain: 4 nodes (120×120px) with arrows between
- Process label: 64px, weight 900
- Metrics row: 3 metric cards

**Animation pattern:**
- Header drops in (`power3.out`)
- Flow nodes stagger with `back.out(1.6)`
- Process label pops (`expo.out`)
- Cards pop with `back.out(1.4)` and stagger 1.0s
- Ambient pulse on cards (`sine.inOut`, yoyo)

---

### 6.4 Impact Grid (`cena-04`)

**Purpose:** Showcase multiple deliverables in a 2×2 grid.

**Structure:**
- Background: Navy
- Section title at top-center: 18px Cabin, uppercase
- 2×2 grid of quad cards (gap: 24px)
- Each card: icon (72px), header (18px uppercase), value (72px), label (24px)
- Optional `.quad-highlight` for emphasis
- Optional glow line at top of card

**Animation pattern:**
- Header fades in
- Quadrants scale in one by one (`power3.out`, stagger 6.0s)
- Glow lines draw left-to-right (`power2.out`)
- Values pop (`expo.out`)
- Ambient glow on highlight quadrant

---

### 6.5 Big Number Highlight (`cena-05`)

**Purpose:** Dramatic reveal of a single key metric.

**Structure:**
- Background: Navy
- Shock rings (2 concentric circles)
- Big counter: 160px, weight 900
- Typewriter subtitle: 36px, uppercase
- Tags row: 3 tags centered

**Animation pattern:**
- Shock rings expand from center (`power3.out`) then fade
- Counter counts up from 0 using GSAP proxy (`power2.out`, 2.5s)
- Subtitle types character-by-character
- Tags pop staggered (`back.out(1.6)`)
- Counter breath hold (`sine.inOut`)

---

### 6.6 Strategic Pillars (`cena-06`)

**Purpose:** List strategic principles with a circular motif.

**Structure:**
- Background: Navy + geo line overlay
- Header: 20px Cabin, uppercase
- 5 pillar items stacked vertically
- Circular word ring (optional): 4 words orbiting a center circle

**Animation pattern:**
- Header fades in
- Pillars slide from left staggered (`power3.out`)
- Ring scales in (`back.out(1.2)`)
- Ring words pop (`back.out(1.6)`)
- Pillars fade as ring takes focus
- Ring rotates ambiently

---

### 6.7 Closing / Signature (`cena-07`)

**Purpose:** Brand close-out with tagline and logos.

**Structure:**
- Layers (bottom → top):
  1. `background: #1e3460`
  2. Tech/circuit photography at `opacity: 0.5`
  3. Gradient overlay (`mix-blend-mode: multiply`)
  4. SD symbol watermark, large, centered, `mix-blend-mode: soft-light`
  5. Vignette (`box-shadow: inset 0 0 120px rgba(0,0,0,0.3)`)
  6. Tagline words (5 lines): 72px, weight 900, uppercase
  7. Logo group: SD icon + "Soluções Digitais" wordmark (~59px)
  8. Co-logos: DTI + Grupo Águia Branca side-by-side

**Animation pattern:**
- Words slam in one by one with varied eases (`expo.out`, `power3.out`, `back.out(1.4)`)
- Highlight words glow pulse (`sine.inOut`)
- Logo group fades in (`power2.out`)
- Final fade to dark (only on final scene)

**Positioning:**
- Main logo group: centered
- Co-logos: centered below, gap 21px

---

## 7. Motion & Animation Guidelines

### 7.1 Entrance presets

| Pattern | Properties | Duration | Ease |
|---|---|---|---|
| Fade up | `y: 20→0`, `opacity: 0→1` | 0.6s | `power2.out` |
| Slide left | `x: -120→0`, `opacity: 0→1` | 1.0s | `power3.out` |
| Scale pop | `scale: 0.85→1.0`, `opacity: 0→1` | 1.2s | `back.out(1.4)` |
| Dramatic drop | `y: 40→0`, `scale: 0.95→1` | 0.8s | `expo.out` |
| Back pop | `scale: 0.9→1`, `opacity: 0→1` | 0.7s | `back.out(1.6)` |

### 7.2 Exit presets

| Pattern | Properties | Duration | Ease |
|---|---|---|---|
| Fade up out | `opacity: 1→0`, `y: 0→-40` | 0.6s | `power2.in` |
| Fade right | `opacity: 1→0.15`, `x: 0→60` | 1.0s | `power2.in` |

### 7.3 Ambient motion

| Pattern | Properties | Duration | Ease |
|---|---|---|---|
| Breath | `scale: 1→1.02→1` or `scale: 1→1.03→1` | 1.5s | `sine.inOut`, yoyo, repeat |
| Glow pulse | `box-shadow` intensity change | 1.2–2.0s | `sine.inOut`, yoyo, repeat |
| Rotation | `rotation: 0→360` | 7s | `none` |

### 7.4 Special effects

| Effect | Technique |
|---|---|
| Count-up counter | GSAP proxy object + `onUpdate` with `Math.floor(val).toLocaleString("pt-BR")` |
| Typewriter | Split text to chars, `tl.call()` to append each char with 0.06s stagger |
| Glow line draw | `scaleX: 0→1` with `transform-origin: left center` |
| Shock ring | Scale from 0 + fade out to 1.6×–1.8× |

### 7.5 Stagger defaults

| Context | Stagger |
|---|---|
| Cards / pills | 0.15–0.4s |
| Flow nodes | 0.4s |
| Pillars | 1.0s |
| Quadrants | 6.0s (long hold per item) |
| Tags | 0.4s |

---

## 8. Transitions

The root timeline (`index.html`) handles scene transitions. Use these transition types:

| Transition | Effect | Duration | Use case |
|---|---|---|---|
| Crossfade | `autoAlpha` + `blur` crossfade | 0.3–0.5s | Default, most scene changes |
| Glitch | Rapid `skewX` oscillation + scale + blur | 0.3s | High-energy cuts |
| Zoom | Old scene zooms out (1.8×), new zooms in (0.6×→1) | 0.4s | Dramatic perspective shifts |
| Slide | Directional slide out + slide in with blur | 0.4s | Vertical/horizontal movement |

**Transition helper functions** (defined in `index.html`):

- `crossfadeTransition(oldId, newId, T, dur)`
- `glitchTransition(oldId, newId, T, dur)`
- `zoomTransition(oldId, newId, T, dur)`
- `slideTransition(oldId, newId, T, dur, dir)` — dir: `"left"`, `"right"`, `"up"`, `"down"`

> **Rule:** Only the final scene may fade to dark (`opacity: 0.3`). All other scenes maintain full brightness through transitions.

---

## 9. Brand Assets

All files are saved under `assets/brand/`.

| Asset | File | Format |
|---|---|---|
| SD icon — white (vertical) | `brand/icon-sd-white-vertical.svg` | SVG |
| SD icon — white (horizontal, dark bg) | `brand/icon-sd-white-horizontal-dark.svg` | SVG |
| SD icon — blue/navy (horizontal, light bg) | `brand/icon-sd-blue-horizontal-light.svg` | SVG |
| SD icon — navy vertical (light bg) | `brand/icon-sd-navy-vertical-light.svg` | SVG |
| SD icon — white vertical (dark bg) | `brand/icon-sd-white-vertical-dark.svg` | SVG |
| SD icon — blue/navy vertical (gradient) | `brand/icon-sd-blue-vertical-gradient.svg` | SVG |
| SD icon — white horizontal (gradient) | `brand/icon-sd-white-horizontal-gradient.svg` | SVG |
| Background photo (tech/circuit) | `brand/bg-tech-circuit.png` | PNG (895 KB) |
| DTI logo | `brand/logo-dti.svg` | SVG |
| Grupo Águia Branca logo | `brand/logo-aguia-branca.svg` | SVG |

### Font files (self-hosted)

| Font | File | Format |
|---|---|---|
| Satoshi Variable | `fonts/Satoshi-Variable.woff2` | woff2 (variable, 300–900) |
| Cabin Bold | `fonts/Cabin-Bold.woff` | woff |

> Figma source: `oUsCTvAbiRT4sZPrAvZyjx` — nodes `251:104`, `280:2`, `16:84`

---

## 10. HyperFrames Production Notes

When building compositions for this design system within HyperFrames:

1. **Base canvas:** 1920×1080 px
2. **Timeline registration:**
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
3. **Deterministic logic only:** No `Date.now()`, `Math.random()`, or network fetches
4. **Asset paths:** Relative to `RPA-video/` directory (e.g., `../assets/brand/icon.svg`)
5. **Font loading:** Define `@font-face` in root `index.html` `<style>` block
6. **Audio:** Use separate `<audio>` elements per scene, `data-start`/`data-duration`/`data-track-index`
7. **Always lint:** Run `npx hyperframes lint` after editing any composition

---

*Last updated: 2026-05-04 — consolidated from RPA 2026 production patterns.*
