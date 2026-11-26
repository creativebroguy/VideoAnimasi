---
name: hyperframes-remotion-video
description: Programmatic video production and post-production skill using HyperFrames (HTML/CSS/GSAP) and Remotion (React). Handles dynamic vertical 9:16 layout, kinetic subtitles, audio mixing, safe zone compliance, and automated rendering.
argument-hint: "[tool: hyperframes|remotion] [layout: vertical_9_16] [action: scaffold|caption|render]"
---

# HyperFrames & Remotion Post-Production Skill

Dokumen ini memandu pembuatan dan perakitan video otomatis (code-to-video) untuk YouTube Shorts menggunakan **HyperFrames** (HTML + CSS + GSAP) dan **Remotion** (React).

---

## 1. Safe Zone YouTube Shorts (1080 x 1920)

Layout vertikal memiliki area terlarang (*restricted UI areas*) yang tidak boleh ditutupi oleh teks penting atau subjek utama:

- **Top Safe Margin:** 120px (untuk header & search).
- **Bottom Dead Zone:** 420px dari bawah (area judul Shorts, nama channel, dan tombol subscribe).
- **Right Dead Zone:** 180px dari kanan (tombol Like, Comment, Share, dan Audio remix).
- **Subtitles Sweet Spot:** Berada pada koordinat Y antara **50% hingga 65%** dari tinggi layar (di area dada subjek).

---

## 2. HyperFrames Production Workflow (HTML/CSS/GSAP)

HyperFrames adalah framework rendering deterministik berbasis HTML/CSS/GSAP yang sangat ramah terhadap AI coding agent.

### Setup Proyek Baru (Vertical Shorts):
```bash
npx hyperframes init shorts-project --skip-skills
```

### Aturan Utama HyperFrames:
1. Elemen berdurasi wajib memiliki attribute: `class="clip"`, `data-start="0"`, dan `data-duration="3"`.
2. Format resolusi vertikal diatur di `index.html`: `width="1080"` dan `height="1920"`.
3. Gunakan GSAP timeline untuk animasi transisi antar-adegan:
```javascript
const tl = gsap.timeline({ paused: true });
tl.fromTo("#scene1", { scale: 1 }, { scale: 1.08, duration: 2.5, ease: "power1.inOut" });
window.__timelines["scene-1"] = tl;
```
4. Subtitle dibuat dinamis per kata menggunakan highlight warna kuning (`#FFE600`) atau hijau neon (`#00FF88`).

---

## 3. Remotion Workflow (React Video)

Untuk merakit komposisi video berbasis React:
```tsx
import { Composition, Sequence, Video, Audio, staticFile } from 'remotion';

export const ShortsVideo = () => {
  return (
    <Composition
      id="ShortsEpisode"
      component={MainTimeline}
      durationInFrames={30 * 35} // 35 detik @ 30fps = 1050 frames
      fps={30}
      width={1080}
      height={1920}
    />
  );
};
```

---

## 4. Standar Mixing Audio (Desibel / dB Standard):
- **Voiceover (VO):** `-3 dB` s.d. `-6 dB` (kompresi tebal, jernih di atas frekuensi lain).
- **Sound Effects (SFX / Impacts):** `-8 dB` s.d. `-12 dB` (punchy saat transisi visual).
- **Background Music (BGM):** `-20 dB` s.d. `-26 dB` (tidak boleh menenggelamkan artikulasi kata narasi).
