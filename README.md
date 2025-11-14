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
