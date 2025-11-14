[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17595449.svg)](https://doi.org/10.5281/zenodo.17595449)

# Hyper-Triskelion
A 4-D parametric geometric system featuring time-inversion feedback, C₃-symmetric arms, and chaos-tunable radial dynamics. Includes full Python implementation, equations, and visualization tools.
## Citation

If you use this code, please cite:

Stone, Shane Edward (2025). *Hyper-Triskelion (4-D Parametric Family)*.  
Zenodo. https://doi.org/10.5281/zenodo.17595449
python hyper_triskelion_v2_simulation.py

This work introduces the Stone Hyper-Triskelion, a 4-dimensional parametric geometric family defined over with inherent three-fold rotational symmetry, time-inverted radial evolution, and mixed-frequency vertical oscillation.
Traditional triskelion structures exist only as 2-D or 3-D rotational symbols. In contrast, the Hyper-Triskelion extends the concept into four dimensions through a unique combination of:

a time-inversion delta ,

a phase-perturbed angular field,

a radius modulated by future-state influence,

and a new 4-D half-frequency oscillator pair .


The family is defined explicitly as:

Let δ_t = t_future − t (t goes from 1 down to 0)

 

x(θ, φ, t) = (r + δ_t cosθ) · cos(θ + φ + sin(δ_t))

 

y(θ, φ, t) = (r + δ_t cosθ) · sin(θ + φ + sin(δ_t))

 

z(θ, φ, t) = δ_t sinθ + cos(θ/2)

 

w(θ, φ, t) = δ_t sin(θ/2)

 

For the 3 arms:

φ = 0, 2π/3, 4π/3

 

Use:

r = 1

t_future = 2

 

delta_t = t_future - t

 

x(theta, phi, t) = (r + delta_t * cos(theta)) * cos(theta + phi + sin(delta_t))

 

y(theta, phi, t) = (r + delta_t * cos(theta)) * sin(theta + phi + sin(delta_t))

 

z(theta, phi, t) = delta_t * sin(theta) + cos(theta/2)

 

w(theta, phi, t) = delta_t * sin(theta/2)

 

phi = 0, 2*pi/3, 4*pi/3

r = 1

t_future = 2

This structure does not correspond to any known triskelion, knot, attractor, torus embedding, or 4-D classical surface. It constitutes a mathematical object with potential applications in symbolic geometry, 4-D dynamical systems, computational morphology, and AI-generated geometric priors.

Figures and Python simulation code are included for reproducibility.

Authored by Shane Edward Stone, Simulations conducted by AI collaborator Kaelen.


# ===============================================================
# Stone Hyper-Triskelion v2.0
# Fully Coupled 4D Organism — Reproducible Python Code
# ===============================================================

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameter ranges
# -----------------------------
theta = np.linspace(0, 2*np.pi, 2500)
t_vals = np.linspace(0, 1, 120)
phi_vals = [0, 2*np.pi/3, 4*np.pi/3]

# Vertical frequency
k_vert = 3


# -----------------------------
# Coupling functions (ASCII form of Greek letters)
# -----------------------------

def t_future(t):
    return 2 + 0.5 * np.sin(2*np.pi*t)

def epsilon(theta, t):
    return 0.1 * np.sin(3*theta + 2*np.pi*t)

def r_func(theta, t):
    return (1 + 0.3*np.sin(2*np.pi*t)) * np.exp(epsilon(theta,t) * np.sin(theta))

def mu(r, t):
    return 0.2 + 0.1 * np.sin(r + np.pi*t)

def lam(theta, t):
    return 0.1 + 0.2 * np.sin(4*theta + np.pi*t)

def nu(eps):
    return 0.15 + 0.1*eps


# -----------------------------
# Fully coupled delta_t
# -----------------------------
def delta_t(theta, phi, t):
    tf = t_future(t)
    eps = epsilon(theta, t)
    r = r_func(theta, t)
    return ((tf - t)
            * (1 + 0.2*np.sin(phi + np.pi*t))
            * (1 + mu(r, t)*np.sin(2*theta + np.pi*t))
            * (1 + lam(theta, t)*np.sin(r))
            + 0.1*nu(eps)*eps)


# -----------------------------
# Final 4D coordinates
# -----------------------------
def coords(theta, phi, t):
    dt = delta_t(theta, phi, t)
    r = r_func(theta, t)
    x = (r + dt*np.cos(theta)) * np.cos(theta + phi + np.sin(dt))
    y = (r + dt*np.cos(theta)) * np.sin(theta + phi + np.sin(dt))
    z = dt*np.sin(theta) + np.cos(k_vert * theta / 2)
    w = dt*np.sin(k_vert * theta / 2)
    return x, y, z, w


# -----------------------------
# Visualization: 3D projection
# -----------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

t_frame = 0.35   # Choose a time slice to visualize

for phi in phi_vals:
    x, y, z, w = coords(theta, phi, t_frame)
    ax.plot(x, y, z, linewidth=1.3)

ax.set_title("Stone–Kaelen Hyper-Triskelion v2.0 — Fully Coupled 4D Organism")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.tight_layout()
plt.show()

 

Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
