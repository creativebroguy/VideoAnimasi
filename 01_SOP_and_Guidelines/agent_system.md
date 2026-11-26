# 🤖 Sistem Agen AI Studio (Subagents Roster)

Sistem ini menggunakan 4 Subagent terspesialisasi yang dipimpin oleh 1 Orchestrator (Antigravity):

---

## 1. `script-hook-specialist`
- **Fokus:** Naskah & Viral Retention Architect.
- **Tugas:**
  - Merancang Hook 0-3 detik (Curiosity Gap / Visual Shock).
  - Menulis naskah padat 30-45 detik (65-85 kata).
  - Menerapkan formula *Seamless Loop* (ending video menyambung ke hook pembuka).

---

## 2. `visual-director`
- **Fokus:** Visual Consistency & Master Style (Midjourney / Flux.1).
- **Tugas:**
  - Merancang Master Style visual (tone warna, cinematic lighting, art style).
  - Menghasilkan image prompt rasio vertical `--ar 9:16`.
  - Menjaga konsistensi wajah, pakaian, dan setting antar-adegan.

---

## 3. `motion-director`
- **Fokus:** Image-to-Video Animation (Kling AI, Runway Gen-3, Luma, Minimax).
- **Tugas:**
  - Membuat prompt pergerakan dinamis per adegan (1.5 - 2.5 detik per beat).
  - Mengontrol camera movement (push-in, orbit, tilt, pan).
  - Menjaga gerakan karakter tetap natural tanpa deformasi anatomi.

---

## 4. `audio-post-specialist`
- **Fokus:** Sound Design & Post-Production Blueprint.
- **Tugas:**
  - Konfigurasi Voiceover ElevenLabs (karakter suara, pacing, intonasi emosional).
  - Mapping Sound Effects (SFX risers, sub-bass impacts, whooshes).
  - Panduan editing CapCut: Safe zone subtitle (menghindari UI YouTube Shorts), typography, dan BGM mixing.

---

## 🔄 Alur Produksi Otomatis

```
[User Brief]
     │
     ▼
[Orchestrator]
     │
     ├──► 1. script-hook-specialist (Buat Naskah & Hook)
     │
     ├──► 2. visual-director (Generate Prompt Midjourney/Flux)
     │
     ├──► 3. motion-director (Generate Prompt Video Kling/Runway)
     │
     └──► 4. audio-post-specialist (Setup ElevenLabs + SFX + CapCut)
     │
     ▼
[Production Sheet Lengkap di folder 03_Projects/]
```
