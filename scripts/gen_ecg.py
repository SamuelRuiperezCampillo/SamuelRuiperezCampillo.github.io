#!/usr/bin/env python3
"""Generate the denoising-ECG divider SVG markup for blox/ecg-divider.

A synthetic ECG (sum-of-Gaussians P-QRS-T template) rides under additive
band-limited noise whose amplitude decays left to right, so the trace
"resolves" into a clean rhythm — a nod to denoising-VAE work.
Outputs two SVGs: desktop (900x60, 4 beats) and mobile (440x60, 2 beats).
"""
import math
import random

H = 60
BASE = 38.0  # baseline y

# Beat template, px offsets within one beat (period-independent)
WAVES = [  # (mu, sigma, amp)  amp>0 = upward deflection
    (37.0, 7.0, 5.5),    # P
    (78.0, 2.2, -4.0),   # Q
    (84.0, 3.0, 22.0),   # R
    (90.5, 2.4, -6.0),   # S
    (130.0, 13.0, 7.0),  # T
]
QRS_WIN = (71.0, 99.0)  # QRS highlight window within beat


def ecg(x, starts):
    y = 0.0
    for s in starts:
        t = x - s
        if -20 < t < 180:
            for mu, sig, amp in WAVES:
                y += amp * math.exp(-((t - mu) ** 2) / (2 * sig * sig))
    return y


def make_noise(rng, n_components=26):
    comps = []
    for _ in range(n_components):
        lam = rng.uniform(5.0, 70.0)
        comps.append((lam, rng.uniform(0, 2 * math.pi), math.sqrt(lam / 70.0)))
    norm = math.sqrt(sum(a * a for _, _, a in comps) / 2)
    return [(l, p, a / norm) for l, p, a in comps]


def noise_val(comps, x):
    return sum(a * math.sin(2 * math.pi * x / l + p) for l, p, a in comps)


def build(width, starts, env_scale, env_reach, rng, dx=1.2):
    comps = make_noise(rng)
    pts = []
    x = 0.0
    while x <= width + 1e-6:
        env = env_scale * max(0.0, 1.0 - x / env_reach) ** 1.6
        n = env * (0.75 * noise_val(comps, x) + 0.5 * rng.uniform(-1, 1))
        y = BASE - ecg(x, starts) + n
        y = min(max(y, 2.0), H - 2.0)
        pts.append((min(x, width), y))
        x += dx
    d = "M%.1f %.1f" % pts[0] + "".join("L%.1f %.1f" % p for p in pts[1:])
    return d


def svg(width, starts, env_scale, env_reach, uid, cls, seed):
    rng = random.Random(seed)
    d = build(width, starts, env_scale, env_reach, rng)
    rects = "".join(
        '<rect x="%.1f" y="0" width="%.1f" height="%d" fill="#fff"/>'
        % (s + QRS_WIN[0], QRS_WIN[1] - QRS_WIN[0], H)
        for s in starts
    )
    return (
        '<svg class="hb-ecg %s" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false">'
        '<defs>'
        '<path id="%s-p" d="%s" pathLength="1000"/>'
        '<mask id="%s-m" maskUnits="userSpaceOnUse" x="0" y="0" width="%d" height="%d">%s</mask>'
        "</defs>"
        '<use href="#%s-p" class="hb-ecg-base"/>'
        '<use href="#%s-p" class="hb-ecg-qrs" mask="url(#%s-m)"/>'
        "</svg>"
    ) % (cls, width, H, uid, d, uid, width, H, rects, uid, uid, uid)


desktop = svg(900, [12.0, 234.0, 456.0, 678.0], 6.5, 650.0, "hbecg-d", "hb-ecg-desktop", 7)
mobile = svg(440, [15.0, 235.0], 5.5, 300.0, "hbecg-m", "hb-ecg-mobile", 11)

print(desktop)
print("@@SPLIT@@")
print(mobile)
