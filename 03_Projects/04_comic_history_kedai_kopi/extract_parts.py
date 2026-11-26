import json, os, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi

SRC_DIR = "04_Assets/images"
OUT_DIR = "03_Projects/04_comic_history_kedai_kopi/parts"
os.makedirs(OUT_DIR, exist_ok=True)

def key(img):
    a = np.asarray(img).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    d = g - np.maximum(r, b)
    lo, hi = 20.0, 60.0
    t = np.clip((d - lo) / (hi - lo), 0, 1)
    alpha = 1 - t * t * (3 - 2 * t)
    # despill
    spill = np.clip((d - 4) / 40.0, 0, 1)
    g2 = g - spill * np.maximum(d - 4, 0)
    out = np.dstack([r, g2, b, alpha * 255]).clip(0, 255).astype(np.uint8)
    return out, alpha

def paper_edge(crop, px=5):
    """Leave a margin of cream card around the piece with subtle paper grain."""
    a = crop[..., 3].astype(np.float32) / 255
    core = a > 0.4
    rim = ndi.binary_dilation(core, iterations=px)
    rim = ndi.binary_closing(rim, iterations=3)
    rimf = ndi.gaussian_filter(rim.astype(np.float32), 0.8)
    h, w = a.shape
    rng = np.random.default_rng(h * 7 + w)
    n = ndi.gaussian_filter(rng.standard_normal((h, w)), 1.2) * 8
    card = np.dstack([241 + n, 233 + n, 214 + n * 0.9]).clip(0, 255)
    rgb = crop[..., :3].astype(np.float32)
    edge = np.clip(ndi.gaussian_filter(core.astype(np.float32), 1.5) - a, 0, 1)[..., None]
    out_rgb = rgb * a[..., None] + card * (1 - a[..., None])
    out_rgb = out_rgb * (1 - 0.25 * edge)
    out_a = np.maximum(a, rimf)
    return np.dstack([out_rgb, out_a * 255]).clip(0, 255).astype(np.uint8)

def process_sheet(sheet_path, prefix):
    img = Image.open(sheet_path).convert('RGB')
    rgba, alpha = key(img)
    solid = alpha > 0.5
    solid = ndi.binary_opening(solid, iterations=2)
    grown = ndi.binary_dilation(solid, iterations=4)
    lab, n = ndi.label(grown)
    objs = ndi.find_objects(lab)
    
    parts = []
    dbg = Image.fromarray(rgba).convert('RGB')
    dr = ImageDraw.Draw(dbg)
    
    # filter tiny specs
    valid_objs = []
    for i, sl in enumerate(objs):
        area = int((lab[sl] == i + 1).sum())
        if area > 2000:
            valid_objs.append((i, sl, area))
            
    # Sort left to right, top to bottom
    valid_objs.sort(key=lambda item: (item[1][0].start // 100, item[1][1].start))
    
    for k, (i, sl, area) in enumerate(valid_objs):
        ys, xs = sl
        pad = 12
        y0, y1 = max(ys.start - pad, 0), min(ys.stop + pad, img.height)
        x0, x1 = max(xs.start - pad, 0), min(xs.stop + pad, img.width)
        m = (lab[y0:y1, x0:x1] == i + 1)
        crop = rgba[y0:y1, x0:x1].copy()
        crop[..., 3] = (crop[..., 3] * m).astype(np.uint8)
        crop = paper_edge(crop)
        
        part_filename = f"{prefix}_{k}.png"
        Image.fromarray(crop).save(os.path.join(OUT_DIR, part_filename))
        parts.append({'id': k, 'file': part_filename, 'x': x0, 'y': y0, 'w': x1 - x0, 'h': y1 - y0, 'area': area})
        dr.rectangle([x0, y0, x1, y1], outline=(255, 0, 255), width=2)
        dr.text((x0 + 4, y0 + 4), str(k), fill=(255, 0, 255))
        
    dbg.save(os.path.join(OUT_DIR, f"{prefix}_debug.jpg"), quality=90)
    print(f"Extracted {len(parts)} parts for {prefix}")
    return parts

if __name__ == "__main__":
    if os.path.exists("04_Assets/images/barista_sheet.jpg"):
        res = process_sheet("04_Assets/images/barista_sheet.jpg", "barista")
        with open(os.path.join(OUT_DIR, "barista_parts.json"), "w") as f:
            json.dump(res, f, indent=2)

if os.path.exists("04_Assets/images/coffee_props_sheet.jpg"):
    res2 = process_sheet("04_Assets/images/coffee_props_sheet.jpg", "props")
    with open(os.path.join(OUT_DIR, "props_parts.json"), "w") as f:
        json.dump(res2, f, indent=2)
