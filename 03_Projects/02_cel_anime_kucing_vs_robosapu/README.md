# 🎬 Proyek Animasi: OYEN VS ROBO-VAC 1988 (80s Cel Anime)

Proyek ini dibuat dan dirender langsung di komputer lokal menggunakan **HyperFrames Engine** dan **Lemo-Opuscar** (`cel-anime-80s`).

---

## 📁 Struktur Berkas:
* **`video_project/index.html`**: Master komposisi vertikal 9:16 (HTML5/SVG/GSAP) lengkap dengan lapisan cel anime, backlit glow 透過光, dan overlay scanlines VHS CRT.
* **`oyen_vs_robosapu.mp4`**: File video hasil render akhir 1080×1920 (Shorts Ready).
* **`TREATMENT.md`**: Dokumen penyutradaraan gaya OVA 1988.
* **`production_sheet.md`**: Breakdown storyboard per adegan.
* **`script.md`**: Naskah voiceover loop.

---

## ⚡ Perintah Menjalankan:

### 1. Live Preview di Browser:
```bash
cd "03_Projects/02_cel_anime_kucing_vs_robosapu/video_project"
hyperframes preview
```

### 2. Render Ulang ke MP4:
```bash
cd "03_Projects/02_cel_anime_kucing_vs_robosapu/video_project"
hyperframes render -o "../oyen_vs_robosapu.mp4" --fps 30
```
