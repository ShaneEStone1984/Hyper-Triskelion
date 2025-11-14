
# Hyper-Triskelion v2 — Feedback-Coupled 4D Parametric Simulator
# Author: Shane Edward Stone
# License: CC-BY-4.0

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (needed for 3D)

N_T      = 2000
N_THETA  = 400
R0       = 1.0
TFUTURE_BASE = 2.0
TFUTURE_AMP  = 0.5
EPS_AMP      = 0.1
NOISE_EPS    = 0.01
W_SPLIT      = 2.0

def t_future(t):
    return TFUTURE_BASE + TFUTURE_AMP * np.sin(2.0 * np.pi * t)

def delta_t(t):
    return t_future(t) - t

def epsilon_theta_t(theta, t, rng=None):
    base = EPS_AMP * np.sin(3.0 * theta + 2.0 * np.pi * t)
    if rng is None or NOISE_EPS <= 0.0:
        return base
    noise = NOISE_EPS * rng.normal(size=theta.shape)
    return base + noise

def hyper_triskelion_arm(theta, t, phi, rng=None):
    dt = delta_t(t)
    eps = epsilon_theta_t(theta, t, rng=rng)
    r = R0 + dt * np.cos(theta) * (1.0 + eps)
    phase = theta + phi + np.sin(dt)
    x = r * np.cos(phase)
    y = r * np.sin(phase)
    z = dt * np.sin(theta) + np.cos(theta / 2.0)
    w = dt * np.sin(theta / 2.0) + np.cos(W_SPLIT * theta / 2.0)
    return x, y, z, w

def simulate_hyper_triskelion(n_t=N_T, n_theta=N_THETA, seed=42):
    rng = np.random.default_rng(seed)
    thetas = np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)
    ts = np.linspace(0.0, 1.0, n_t)
    phis = [0.0, 2.0 * np.pi / 3.0, 4.0 * np.pi / 3.0]
    coords_4d = []
    for phi in phis:
        x_arr = np.zeros((n_t, n_theta))
        y_arr = np.zeros((n_t, n_theta))
        z_arr = np.zeros((n_t, n_theta))
        w_arr = np.zeros((n_t, n_theta))
        for i, t in enumerate(ts):
            x, y, z, w = hyper_triskelion_arm(thetas, t, phi, rng=rng)
            x_arr[i, :] = x
            y_arr[i, :] = y
            z_arr[i, :] = z
            w_arr[i, :] = w
        coords_4d.append({"x": x_arr,"y": y_arr,"z": z_arr,"w": w_arr,"phi": phi})
    return coords_4d, ts, thetas

def plot_snapshot(coords_4d, ts, step=None):
    if step is None:
        step = len(ts) // 2
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    colors = ["tab:orange", "tab:blue", "tab:green"]
    for arm_idx, (arm, c) in enumerate(zip(coords_4d, colors)):
        x = arm["x"][step, :]
        y = arm["y"][step, :]
        z = arm["z"][step, :]
        ax.plot(x, y, z, c=c, lw=1.0, label=f"arm {arm_idx}")
    ax.set_title(f"Hyper-Triskelion v2 snapshot at t ≈ {ts[step]:.3f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    coords_4d, ts, thetas = simulate_hyper_triskelion()
    plot_snapshot(coords_4d, ts, step=len(ts) // 2)
