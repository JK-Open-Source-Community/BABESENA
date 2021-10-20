#!/usr/bin/env python
# coding: utf-8

# # Control System 

# - tachometer
#     
#     is derivative feedback
#     
# - type
#     
#     type is defined for OLTF of unity feedback systems 
#     
# - dominant pole
#     
#     if $\frac{p_1}{p_2}\ge5$ → $\text{TF}=\frac{\text{DC Gain}}{\text{significant pole}}$
#     
#     eliminate poles at origin and significant poles → $\text{DC Gain}=\lim \limits_{s\rightarrow 0}  \text{TF}$ 
#     
# - sensitivity
#     
#     $\displaystyle S^T_G = \dfrac{\frac{\partial T}{T}}{\frac{\partial G}{G}}$
#     
#     $\displaystyle S^T_H = \dfrac{\frac{\partial T}{T}}{\frac{\partial H}{H}}$
#     
# - mason gain
#     
#     $\boxed{\text{TF} = \frac{{ \sum _{k = 1}^n {M_k}{{\rm{\Delta }}_k}}}{{\rm{\Delta }}}}$
#     
#     $\Delta$ = 1 - (sum of loop gains of individual loops) + (sum of product of loop gain of two non-touching loops) - (sum of product of loop gain of three non-touching loops) + $\dots$
#     
#     $\Delta_k$ = 1 - (sum of loop gains of individual loops which are not common with given path) + (sum of product of loop gain of two non-touching loops which are not common with given path) - (sum of product of loop gain of three non-touching loops which are not common with given path) + $\dots$
#     
# - first order
#     
#     $\text{TF}=\dfrac{k}{1+s\tau}$
#     
#     - impulse response
#         
#         $c(t) = \dfrac{1}{\tau}e^{-\frac{t}{\tau}}$
#         
#     - step response
#         
#         $c(t)=u(t)\lbrack1-e^{\frac{-t}{\tau}}\rbrack$
#         
#     - ramp response
#         
#         $c(t)=tu(t)-\tau\lbrack1-e^{\frac{-t}{\tau}}\rbrack u(t)$
#         
# - steady state error
#     
#     $e(t)=r(t)-c(t)$
#     
#     - non-unity
#         
#         if $e(t)=r(t)-c(t)$ then → $G'(s) = \dfrac{G(s)}{1+G(s)H(s)-G(s)}$ 
#         
#     
#     $K_p = \lim \limits_{s\rightarrow 0} G(s)$
#     
#     $K_v = \lim \limits_{s\rightarrow 0} s\cdot G(s)$
#     
#     $K_a = \lim \limits_{s\rightarrow 0} s^2\cdot G(s)$
#     
#     $\boxed{\def\arraystretch{1.5}\begin{array}{c:c:c} 
#     \frac{1}{s} & u(t) & E_{ss} = \frac{1}{1+K_p}
#      \\ \hdashline 
#     \frac{1}{s^2} & t \cdot u(t) & E_{ss} = \frac{1}{K_v} \\ \hdashline 
#     \frac{1}{s^3} & \frac{t^2}{2} u(t)& E_{ss} = \frac{1}{K_a} 
#     \end{array}}$
#     
# - time domain analysis
#     - first order
#         
#         $\text{CLTF}=\dfrac{1}{s\tau +1}$
#         
#         - time domain parameters
#             
#             50% of final value: delay → $t_d =0.693\tau =\ln(2) \tau$
#             
#             10% → 90% : rise-time → $t_r =  2.2\tau$
#             
#             - settling time ($t_s)$
#                 
#                 5% error → $t_s \approx 3 \tau$
#                 
#                 2% error → $t_s \approx 4 \tau$
#                 
#                 0% error → $t_s \approx 5\tau$
#                 
#     - second order
#         
#         CLTF $= \dfrac{\omega_n^2}{s^2+2\zeta \omega_n s + \omega_n ^2}$
#         
#         $\boxed{s=-\zeta \omega_n  \pm \omega_n \sqrt{\zeta^2-1}=-\alpha\pm j\omega_d}$
#         
#         damping frequency: $\omega_d$  
#         
#         damping factor: $\alpha$
#         
#         damping ratio: $\zeta$
#         
#         $\tau =\dfrac{1}{\zeta \omega_n}=\dfrac{1}{\alpha}$
#         
#         $cos(\theta) = \zeta$
#         
#         - impulse response
#             
#             $c(t) = \omega_n\dfrac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}sin(\omega_n t)$                                     for $0<\zeta<1$
#             
#         - step response
#             
#             $c(t) = 1- \dfrac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}sin(\omega_n t+\theta)$                           for $0<\zeta<1$
#             
#         - time domain parameters
#             
#             50% of final value: delay → $\boxed{t_d =\dfrac{0.7\zeta +1}{\omega_n}}$
#             
#             10% → 90% : rise-time → $\boxed{t_r =  \dfrac{n\pi-\theta}{\omega_d}}$
#             
#             peak time → $\boxed{t_p =\dfrac{n\pi}{\omega
#             _d}} \begin{cases}
#                n=odd &\text{maxima}  \\
#                n=even &\text{minima}
#             \end{cases}$
#             
#             first time-period: $T_p = t_{p_3} - t_{p_1}=\dfrac{2\pi}{\omega
#             _d}$  
#             
#             % maxima-overshoot → $\boxed{\frac{c(t_p)-c(\infty)}{c(\infty)}\times 100}=e^{\frac{-\zeta\pi}{\sqrt{1-\zeta^2}}}\times 100 \%$
#             
#             - settling time ($t_s)$
#                 
#                 5% error → $t_s \approx 3 \tau$
#                 
#                 2% error → $t_s \approx 4 \tau$
#                 
#                 0% error → $t_s \approx 5\tau$
#                 
#             
#             no of cycles → $\dfrac{t_s}{T_{p}} \approx \dfrac{4\tau}{T_p}$
#             
# - routh hurwitz
#     - third order equation
#         
#         $\boxed{\begin{array}{c:c} 
#         stable & IP>OP
#          \\ \hdashline 
#         marginal & IP=OP \\ \hdashline 
#         unstable & IP<OP
#         \end{array}}$
#         
#         auxiliary equation → coefficients of $s^2$ and $s^0$
#         
#     
#     $\epsilon \rightarrow 0^+$
#     
#     - ROZ → poles symmetrical about origin
#         
#         A → auxiliary equation from row above the ROZ 
#         
#         roots of A are symmetrical poles
#         
#         replace ROZ by $\frac{dA}{ds}$
#         
#         - two ROZ → repeated symmetrical poles
#             
#             roots of A are repeated symmetrical poles
#             
#     - gain margin and phase crossover
#         
#         last row of routh-hurwitz table must not be zero for $0<k_1<\infty$
#         
#         → make first element of odd row zero
#         
#         → compare roots of $\frac{d(AE)}{ds} =0$ with $s=\pm j \omega_{pc}$
#         
#         - otherwise
#             
#             $\omega_{pc}$  is not defined
#             
#             $\boxed{\begin{array}{c:c:c} 
#             CLTF & OLTF & GM (dB)
#              \\ \hdashline 
#             \begin{array}{c}
#                stable \\
#                unstable
#             \end{array} & min\space phase  &  \begin{array}{c}
#                \infty \\
#                -\infty
#             \end{array} \\ \hdashline 
#              \begin{array}{c}
#                stable \\
#                unstable
#             \end{array} & non-min\space phase -I  &  \begin{array}{c}
#                \infty \\
#                -\infty
#             \end{array} \\ \hdashline \begin{array}{c}
#                stable \\
#                unstable
#             \end{array} & non-min\space phase -II  &  \begin{array}{c}
#                -\infty \\
#                \infty
#             \end{array} 
#             \end{array}}$
#             
# - root locus
#     - root locus is symmetric about real axis
#     - number of root locus branches is P or Z whichever is greater
#     - root locus exists if their is odd sum of poles and zeroes
#     - asymptotes = $N = P\sim Z$
#     - angle = $\dfrac{(2q+1)180^o}{N}$
#     - centroid = $\dfrac{(real \space part \space of \space poles)-(real \space part \space of \space zeroes)}{N}$
#     - break points $\dfrac{dK}{ds}=0$ by characteristic equation (valid/invalid breakpoints) and intersection with imaginary axis by RH criteria (auxiliary equation)
#     - angle of departure $\phi _d = 180 ^{\circ} + \angle GH(s) |_\text{at +ve imaginary complex pole}$
#     - angle of arrival $\phi _a = 180 ^{\circ} - \angle GH(s) |_\text{at +ve imaginary complex zero}$
# - frequency domain analysis
#     - bode plot ($\omega$  vs $dB$ )
#         
#         $dB = 20 \cdot log(|G(j\omega)H(j\omega)|)$
#         
#         $\dfrac{20dB}{decade} = \dfrac{6dB}{octave}$
#         
#         - at pole
#             
#             slope = $- 20n \space \frac{dB}{decade}$
#             
#             phase = $-n\frac{\pi}{2}$
#             
#         - at zero
#             
#             slope = $+ 20n \space \frac{dB}{decade}$
#             
#             phase = $+n\frac{\pi}{2}$
#             
#         - magnitude
#             
#             eliminate corner frequencies $\ge\omega_{known}$
#             
#             origin frequency $(\omega=0.1)$ is not corner frequency
#             
#             write TF in time constant format : $\dfrac{K(\dfrac{s}{\tau_1}+1)(\dfrac{s}{\tau_2}+1)\dots}{(\dfrac{s}{\tau_a}+1)(\dfrac{s}{\tau_b}+1)\dots}$
#             
#             $M = 20 \cdot log(|G(j\omega)H(j\omega)|)$
#             
#     - polar plot ($|M|$ vs $\phi$ )
#         
#         direction : $\phi_o - \phi_{\infty}$
#         
#         $\boxed{\begin{array}{c:c:c} 
#         \omega & M & \phi
#          \\ \hdashline 
#         0 & M _0 & \phi _0 \\ \hdashline 
#         \infty & M _{\infty} &  \phi _{\infty}
#         \end{array}}$
#         
#         gain cross over frequency ($\omega_{gc}$) : $\boxed{M = |G(s)H(s)| = 1 }$ 
#         
#         phase cross over frequency ($\omega_{pc}$) : $\boxed {\angle G(s)H(s) = \pm 180^{\circ}}$
#         
#         gain margin $= \dfrac{1}{|G(j\omega_{pc})H(j\omega_{pc})|}$
#         
#         phase margin $= 180^{\circ} +\angle G(j\omega_{gc})H(j\omega_{gc})$
#         
#         $\boxed{\begin{array}{c:c} 
#         \omega _{pc} > \omega_{gc}  & stable \\ \hdashline 
#         \omega _{pc} = \omega_{gc}  &  marginal \space stable \\ \hdashline 
#         \omega _{pc} < \omega_{gc} & unstable\end{array}}$
#         
#     - nyquist plot
#         
#         $N=P-Z$
#         
#         N = number of encirclement of origin by GH(s) in GH(s) plane. N is +ve if contour and contour in GH(s) plane are opposite in direction
#         
#         P = number of poles of GH(s) strictly inside contour in s-plane
#         
#         Z = number of zeroes of GH(s) strictly inside contour in s-plane
#         
#         NYQUIST contour is CLOCKWISE
#         
# - compensator and controller
#     - lead compensator
#         
#         LEAD behaves similar to HIGH-PASS filter (zero dominant)
#         
#         $TF = \alpha \Big( \dfrac{1+s\tau}{1+\alpha\tau s}\Big)$     where $\alpha <1$ and $\tau = R_1 C$ 
#         
#         $\alpha=\dfrac{R_2}{R_1+R_2}$
#         
#         
#     - lag compensator
#         
#         LAG behaves similar to LOW-PASS filter (pole dominant) 
#         
#         $TF = \dfrac{1+s\tau}{1+\beta\tau s}$     where $\beta >1$ and $\tau = R_2 C$ 
#         
#         $\beta=\dfrac{R_1+R_2}{R_2}$
#         
#         
#         
#     - lead-lag and lag-lead
#         
#         LEAD LAG behaves similar to BAND-PASS filter (zero dominant)
#         
#         LAG LEAD behaves similar to BAND-REJECT filter (pole dominant)
#         
# - state space analysis
#     
#     $\dot{X } = A X + BU$
#     
#     $Y = CX +DU$
#     
#     $TF = \dfrac{Y(s)}{U(s)}$
#     
#     - controllability
#         
#         $Q_c = \begin{bmatrix}
#           B  &
#           AB & A^2B \dots A^{n-1}B 
#         \end{bmatrix}$
#         
#         $rank(Q_c)=rank(A)=n$  → completely controllable system
#         
#         $|Q_c|\ne 0$ → controllable system
#         
#     - observability
#         
#         $Q_o = \begin{bmatrix}
#           C  \\
#           CA \\ CA^2\\ \vdots \\ C A^{n-1}
#         \end{bmatrix}$
#         
#         $|Q_o|\ne 0$ → observable system
#         
#         $rank(Q_o)=rank(A)=n$  → completely observable system
