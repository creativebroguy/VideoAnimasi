---
name: ai-video-motion
description: Camera direction and motion prompt engineering for AI video generation tools including Kling AI, Runway Gen-3 Alpha, Minimax Hailuo, and Wan2.1. Focuses on dynamic pacing, realistic physics, and artifact-free camera movement.
argument-hint: "[image_context] [camera_move: push_in|orbit|tilt|pan|zoom] [motion_intensity: 3-6]"
---

# AI Video Motion & Camera Direction Skill

Dokumen ini adalah instruksi operasional untuk mengonversi gambar kunci statis (*Image-to-Video*) menjadi cuplikan video dinamis berdurasi 3 hingga 5 detik menggunakan **Kling AI**, **Runway Gen-3**, **Luma Dream Machine**, atau **Minimax**.

---

## 1. Aturan Emas Image-to-Video (I2V)

1. **Gambar adalah Pondasi:** Gambar statis menentukan 80% dari komposisi, pencahayaan, dan subjek. Prompt video **hanya boleh mendeskripsikan apa yang bergerak**.
2. **Jangan Ulangi Deskripsi Gambar:** 
   - ❌ *Buruk:* "A man with blue coat standing in a dark room and the camera pushes in"
   - ✅ *Benar:* "Slow cinematic camera push-in towards the subject. The subject slowly raises his head, eyes widening in shock. Subtle atmospheric dust motes float upwards."
3. **Motion Intensity Sweet Spot:**
   - Kling / Runway Motion Brush: Nilai **3 hingga 6** (skala 1-10).
   - Di atas nilai 7: Rawan terjadi *morphing*, distorsi tangan, atau deformasi anatomi.

---

## 2. Kosakata Gerakan Kamera (Camera Control Prompts)

Untuk menghasilkan retensi tinggi, gunakan pergerakan kamera aktif berikut:

### A. Dynamic Push-In (Zoom Dramatis):
```text
Fast cinematic camera push-in towards the subject's face, background rapidly compresses, shallow depth of field, dramatic motion blur on edges.
```

### B. Orbital Tracking (Mengelilingi Subjek):
```text
Smooth 45-degree orbital rotation shot around the protagonist, keeping the subject centered while background environment sweeps across frame.
```

### C. Low-Angle Tilt-Up (Membangun Rasa Kagum/Kengerian):
```text
Camera starts low near the wet ground and tilts upwards slowly to reveal the massive towering structure, volumetric fog drifting through frame.
```

### D. Drone Aerial Dive / Crane Shot:
```text
Downward crane shot descending rapidly through dark rain clouds, leveling out at eye level with the mysterious doorway.
```

---

## 3. Mengontrol Gerakan Karakter & Fisika Alami

Untuk membuat animasi terasa organik dan bukan sekadar filter 3D kaku:
- **Gerakan Mikro:**
  - *"Subtle breathing motion, eyes slowly blinking, wind gently blowing strands of hair and the edges of the cloak."*
- **Gerakan Elemen Atmosfer:**
  - *"Volumetric smoke billowing from the cracks, glowing embers drifting upwards in slow motion, water ripples expanding on the puddles."*
- **Aksi Cepat:**
  - *"The creature suddenly turns its head with unnatural speed, snapping into sharp focus, glowing eyes flaring with intense light."*

---

## 4. Format Output untuk Storyboard:
Setiap scene harus memberikan output dalam format siap salin:
- **Target Platform:** Kling AI v1.5 / Runway Gen-3 Alpha / Minimax
- **Motion Prompt:** [Deskripsi gerakan kamera + subjek]
- **Camera Settings:** [Pan / Tilt / Zoom / Speed]
- **Duration:** 3s atau 5s
