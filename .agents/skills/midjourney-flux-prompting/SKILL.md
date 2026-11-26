---
name: midjourney-flux-prompting
description: Expert prompt engineering framework for Midjourney v6.1 and FLUX.1. Specializes in 9:16 vertical compositions, cinematic lighting, photorealism, master style anchors, and character consistency for AI video animations.
argument-hint: "[scene_description] [style: dark_fantasy|hyperreal_scifi|3d_pixar|horror] [aspect_ratio: 9:16]"
---

# Midjourney v6 & FLUX.1 Master Prompting Skill

Dokumen ini adalah standar prompt engineering untuk menghasilkan gambar statis berkualitas tinggi dengan konsistensi karakter dan estetika sinematik, siap dijadikan bahan *Image-to-Video*.

---

## 1. Anatomi Master Prompt Midjourney v6.1

```text
[Subject & Action], [Environment & Background], [Lighting & Atmosphere], [Camera Angle & Lens], [Art Style & Engine Render], [Parameters]
```

### Parameter Wajib untuk YouTube Shorts:
- `--ar 9:16` : Rasio vertikal layar penuh smartphone.
- `--v 6.1` : Menggunakan model terbaru Midjourney untuk ketajaman tekstur dan anatomi tangan/wajah yang akurat.
- `--style raw` : Mengurangi interpretasi artistik berlebihan dari Midjourney, memberikan hasil lebih natural/fotorealistik.
- `--c 5` to `--c 10` : Chaos rendah untuk menjaga stabilitas scene.

---

## 2. Master Style Presets (Pilih Salah Satu untuk Seluruh Episode)

### A. Dark Fantasy / Mythological Mystery:
```text
hyperrealistic 8k, dark fantasy aesthetic, ominous volumetric lighting, chiaroscuro, heavy fog, moody shadows, cinematic film grain, color graded with desaturated emerald and gold, Unreal Engine 5 render, shot on 35mm Arri Alexa --ar 9:16 --v 6.1 --style raw
```

### B. Hyper-Realistic Sci-Fi / Anomaly:
```text
photorealistic cinematic still, NASA documentary footage style, cold anamorphic lens flare, deep space shadows, ultra-detailed metallic textures, harsh directional sunlight, 70mm IMAX framing, volumetric dust motes, realistic physics --ar 9:16 --v 6.1 --style raw
```

### C. Stylized 3D Animation (Pixar / Disney Hyper-Detailed):
```text
Pixar and DreamWorks animation style, 3D character design, subsurface scattering on skin, rich vibrant subsurface lighting, Octane render, glossy textures, expressive wide eyes, soft ambient occlusion, 8k resolution, ray tracing --ar 9:16 --v 6.1
```

---

## 3. Terminologi Lensa & Kamera (Menghindari Angle Monoton)

Setiap scene dalam storyboard **harus** memiliki angle kamera berbeda untuk menjaga variasi visual:

1. **Extreme Close-Up (ECU):** `Extreme macro shot of character's dilated eye reflecting a glowing red portal, fine skin pores, hyper-detailed iris`
2. **Low-Angle Hero Shot:** `Dramatic low-angle worm's-eye shot looking up at an imposing towering giant stone monolith, vast cloudy sky`
3. **Dutch Angle (Menegangkan):** `Dutch tilt angle shot of an abandoned futuristic laboratory corridor, flickering warning lights, tilted perspective`
4. **Cinematic Tracking Wide Shot:** `Wide establishing shot of a lone wanderer in a glowing bioluminescent forest, fog crawling on the ground`

---

## 4. Teknik Menjaga Konsistensi Karakter (Character Consistency)

Untuk menjaga wajah dan kostum karakter tetap sama di seluruh adegan:
1. **Gunakan Karakter Descriptor Unik:**
   - Bukan sekadar: *"a man"*
   - Tapi: *"a 35-year-old weathered Scandinavian sailor with a distinctive jagged scar across his left eyebrow, short silver-grey buzzcut, wearing a frayed dark-navy wool coat"*
2. **Gunakan Character Reference Midjourney (`--cref`):**
   - Buat satu gambar master karakter terlebih dahulu (front facing neutral expression).
   - Dapatkan URL gambar tersebut, lalu tambahkan `--cref <URL_GAMBAR> --cw 80` di setiap prompt adegan berikutnya.
3. **Gunakan Seed yang Sama:**
   - Tambahkan `--seed 12345` pada adegan-adegan yang berurutan.
