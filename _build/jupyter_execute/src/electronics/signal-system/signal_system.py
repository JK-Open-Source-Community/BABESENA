#!/usr/bin/env python
# coding: utf-8

# # Signals and Systems
# 
# - terminology
#     - linear
#         - system which follows principle of `superposition`
#             - law of additivity
#                 
#                 $x_1(t)+x_2(t) \longrightarrow \boxed{system} \longrightarrow  y_1(t)+y_2(t)$
#                 
#             - law of homogenity
#                 
#                 $kx(t) \longrightarrow \boxed{system} \longrightarrow  ky(t)$
#                 
#     - time invariant
#         
#         $x(t-t_o) \longrightarrow \boxed{system} \longrightarrow  y(t-t_o)$
#         
#     
#     `causal`: output of system is independent of future values of input
#     
#     `anti-causal`: output of system depends on only future values of input
#     
#     `static`: output of system depends on only present values of input
#     
#     `dynamic`: output of system depends on past or future values of input at any instant 
#     
# - $\delta$
#     
#     $\displaystyle\int _{-\infty}^{\infty}x(t) \frac{d^n}{d t^n}\delta(t-t_1) dt=(-1)^n\frac{d^n}{d t^n}x(t) \Big| _{t=t_1}$ only if $x(t) \Big|_{t=\infty} = finite$
#     
#     $x(t)\delta (t-t_1) =x(t_1) \delta (t-t_1)$
#     
# - average
#     
#     $\text{average} =\displaystyle\frac{1}{T_o} \int_{\frac{-T_o}{2}}^{\frac{T_o}{2}} x(t) dt$
#     
# - energy
#     
#     $\rm{E=\displaystyle \int_{-\infty}^{\infty}|x(t)|^2dt}$
#     
#     $\rm{E=\displaystyle \sum_{-\infty}^{\infty}|x[n]|^2}$
#     
# - power
#     
#     $power =\frac{1}{T_o} \displaystyle\int_{\frac{-T_o}{2}}^{\frac{T_o}{2}}\mid x(t)\mid^2 dt = MSV(x(t))=\overline {x^2(t)}$
#     
#     $power = \begin{cases}
#        \rm{P=\displaystyle \dfrac{1}{N} \sum_{n=N}|x[n]|^2} &\text{if   periodic}  \\
#        \rm{P=\lim \limits_{x\rightarrow \infty}\displaystyle \dfrac{1}{2N+1} \sum_{n=-N}^{N}|x[n]|^2} &\text{if   non-periodic}
#     \end{cases}$
#     
# - half wave symmetry
#     
#     $x(t)=-x(t\pm \frac{T}{2})$
#     
# - conjugate symmetric
#     
#     $x(t)=x^*(-t)$
#     
# - conjugate anti-symmetric
#     
#     $x(t)=-x^*(-t)$
#     
# 
# $x(t)=x_{CS}(t)+x_{CAS}(t)$
# 
# $|A+B|^2 = |A|^2+|B|^2+AB^*+A^*B$
# 
# - parseval's theorem
#     
#     $\displaystyle \boxed{E_{x(t)}=\frac{1}{2\pi}\int_{-\infty}^{+\infty}|X(j\omega)|^2d\omega = \int_{-\infty}^{+\infty}|X(f)|^2df = \int_{-\infty}^{+\infty}|x(t)|^2dt}$
#     
#     $\displaystyle \boxed{E_{x[n]}=\sum \limits_{n=-\infty}^{+\infty}|x[n]|^2 =\frac{1}{2\pi}\int_{-\pi}^{+\pi}|X(e^{j\omega})|^2d\omega }$
#     
# - energy of standard signals
#     
#     $-k\cdot x(-at+b) \rightarrow \dfrac{k^2 E_x}{|a|}$ 
#     
#     - rectangular pulse
#         
#         $energy=A^2\times(duration)$
#         
#     - triangular pulse
#         
#         $energy=\frac{A^2}{3}\times(duration)$
#         
# - convolution
#     
#     $\displaystyle h(t)*x(t) = \int_{-\infty}^{\infty}x(\tau)\cdot h(t-\tau)d\tau$ 
#     
#     - time delay
#         
#         $x_1(t-t_1)*x_2(t-t_2)=y(t-t_1-t_2)$
#         
#     - time scaling
#         
#         $x_1(at)*x_2(at)=\dfrac{1}{|a|}y(at)$
#         
#     
#     $x(t)*u(t) = \int _{-\infty} ^t x(\tau) d\tau$
#     
#     $x(t)*\delta(t-t_1) = x(t-t_1)$ 
#     
#     - area
#         
#         $x_1(t)*x_2(t) =y(t)$
#         
#         $A_{x_1(t)} \times A_{x_2(t)} = A_{y(t)}$
#         
# - sampling
#     
#     $M_s(\omega) = f_s \sum \limits_{n=-\infty}^{\infty} M(\omega-n\omega_s)$
#     
#     $M_s(f) = f_s \sum \limits_{n=-\infty}^{\infty} M(f-nf_s)$
#     
#     - no aliasing
#         
#         $f_s \ge 2f_m$ 
#         
#     - filter cutoff
#         
#         $f_m \le f_c \le f_s-f_m$ 
#         
#     - nyquist
#         
#         $NR=f_{NY} = 2 f_{max} = (f_s) _{min}$
#         
#         $NI =T_{NY}=\dfrac{1}{f_{NY}}$
#         
#     - rectangular
#         
#         $M_s(f) = \sum \limits_{n=-\infty}^{\infty}\frac{2A}{a}sinc(\frac{2n}{a}) M(f-nf_s)$
#         
#     - bandpass sampling theorem
#         
#         $f_s \ge \dfrac{2f_H}{k}$
#         
#         $k=\Big[\dfrac{f_H}{f_H-f_L}\Big]$                   $[\cdot]$ → GIF
#         
# 
# ## fourier series
# 
# - dirichlet conditions
#     - signal must have finite number of maxima and minima over the range of time period.
#     - signal must have a finite number of discontinuities over the range of time period.
#     - signal must be absolutely integrable over a period.
# - $\color{lightgreen} x(t)=a_o+\sum_{n=1} ^{\infty}a_n cos(n\omega_ot)+\sum_{n=1} ^{\infty}b_n sin(n\omega_ot)$
#     
#     $\displaystyle a_o=\frac{1}{T_o}\int_{T_o} x(t) dt$
#     
#     $\displaystyle a_n=\frac{2}{T_o}\int_{T_o} x(t) cos(n\omega_ot) dt$
#     
#     $\displaystyle b_n=\frac{2}{T_o}\int_{T_o} x(t) sin(n\omega_ot) dt$
#     
# - $x(t)=\sum\limits_{n=-\infty}^{\infty} C_n e^{jn\omega_ot}$
#     
#     $\displaystyle C_n=\frac{1}{T_o} \int _{T_o} x(t) e^{-jn\omega_o t}dt$
#     
#     $\displaystyle C^{*}_{-n}=\frac{1}{T_o} \int _{T_o} x^*(t) e^{-jn\omega_o t}dt$
#     
#     - properties
#         - conjugation
#             
#             $x^*(t) \longleftrightarrow C_{-n} ^*$
#             
#         - time reversal
#             
#             $x(-t) \longleftrightarrow C_{-n}$ 
#             
#         - time scaling
#             
#             $x(at) \longleftrightarrow C_{n}$  but period = $\dfrac{T_o}{a}$
#             
#         - time shifting
#             
#             $x(t+t_o) \longleftrightarrow e^{+jn\omega_o t_o}C_{n}$  
#             
#         - frequency shifting
#             
#             $x(t+t_o)e^{\pm jm\omega_o t_o} \longleftrightarrow C_{n\mp m}$  
#             
#         - convolution in time
#             
#             $x_1(t)*x_2(t) \longleftrightarrow T_o(C_{1n}\cdot C_{2n} )$ 
#             
#         - multiplication in time
#             
#             $x_1(t)\cdot x_2(t) \longleftrightarrow C_{1n}* C_{2n}$ 
#             
#         - differentiation in time
#             
#             $\dfrac{d^kx(t)}{dt^k} \longleftrightarrow (jn\omega_o)^kC_{n}$ 
#             
#         - integration in time
#             
#             $\displaystyle \int_{-\infty}^{t} x(\tau) d\tau  \longleftrightarrow \dfrac{C_{n}}{jn\omega_o}$ 
#             
# 
# ## transforms
# 
# - laplace transform
#     - bilateral
#         
#         $\displaystyle F(s)=\int_{-\infty}^{+\infty}f(t)e^{-st}dt$
#         
#     - unilateral
#         
#         $\displaystyle  F(s)=\int_{0}^{\infty}f(t)e^{-st}dt$
#         
#     - properties
#         - conjugation
#             
#             $f^*(t)\leftrightarrow F^*(s^*)$
#             
#         - time reversal
#             
#             $f(-t)\leftrightarrow F(-s)$
#             
#         - time scaling
#             
#             $f(at)\leftrightarrow\frac{1}{\mid a \mid}F(\frac{s}{a})$
#             
#         - time shifting
#             
#             $f(t\pm t_0)\leftrightarrow F(s)e^{\pm st_0}$
#             
#         - frequency shifting
#             
#             $e^{\pm s_0 t}f(t) \leftrightarrow F(s\mp s_0)$
#             
#         - convolution in time
#             
#             $f_1(t)*f_2(t)\leftrightarrow F_1(s)\times F_2(s)$
#             
#         - convolution in frequency
#             
#             $f_1(t)\times f_2(t)\leftrightarrow \frac{1}{2\pi j}\lbrack F_1(s)*F_2(s) \rbrack$
#             
#         - differentiation in time
#             - bilateral
#                 
#                 $\dfrac{d^n}{dt^n}f(t) \leftrightarrow s^nF(s)$
#                 
#             - unilateral
#                 
#                 $\dfrac{d^n}{dt^n}f(t) \leftrightarrow s^nF(s)- s^{n-1}f(0^-)-s^{n-2}f'(0^-)-...$
#                 
#         - integration in time
#             - bilateral
#                 
#                 $\displaystyle \int_{-\infty}^tf(\tau)d\tau \leftrightarrow \frac{F(s)}{s}$ 
#                 
#             - unilateral
#                 
#                 $\displaystyle\int_{-\infty}^tf(\tau)d\tau \leftrightarrow \frac{F(s)}{s} + \frac{\int_{-\infty}^{0^-}f(\tau)d\tau }{s}$
#                 
#         - differentiation in frequency
#             
#             $\displaystyle t^nf(t) \leftrightarrow  (-1)^{n}\frac{d^n}{ds^n}F(s)$ 
#             
#         - integration in frequency
#             
#             $\displaystyle\frac{f(t)}{t} \leftrightarrow  \int_{s}^\infty F(s)d\tau$
#             
#         - initial value theorem
#             
#             $f(0^+)=\underset{s\rightarrow\infty}{lim}\space sF(s)$
#             
#             note : initial value theorem is applied only on remainder function
#             
#         - final value theorem
#             
#             $f(\infty)=\underset{s\rightarrow0}{lim}\space sF(s)$
#             
#     - standard results
#         - $\delta(t)$
#             
#             $\delta \leftrightarrow 1$
#             
#         - $u(t)$
#             
#             $u(t)\leftrightarrow \frac{1} {s}$
#             
#         - $t^nu(t)$
#             
#             $t^nu(t) \longleftrightarrow  \dfrac{n!}{s^{n+1}}$
#             
#         - $cos(\omega_o t)u(t)$
#             
#             $cos(\omega_o t)u(t)\leftrightarrow \dfrac{s} {s^2+\omega_o^2}$
#             
#         - $sin(\omega_o t)u(t)$
#             
#             $sin(\omega_o t)u(t)\leftrightarrow \dfrac{\omega_o} {s^2+\omega_o^2}$
#             
# - fourier transform
#     
#     $\rm{X\left(j\omega\right)=\displaystyle \int \limits_{ - \infty }^\infty {x(t)e^{-j\omega t}}dt}$ (CTFT)
#     
#     $\rm{x\left(t\right)=\dfrac{1}{2\pi}\displaystyle \int \limits_{ - \infty }^\infty {X(j\omega)e^{j\omega t}}d\omega}$ (inverse CTFT)
#     
#     $\rm{X\left(e^{j\omega}\right)=\displaystyle \sum \limits_{ - \infty }^\infty {x[n]e^{-j\omega n}}}$ (DTFT)
#     
#     $\rm{x\left[n\right]=\dfrac{1}{2\pi}\displaystyle \int \limits_{ - \pi }^\pi {X(j\omega)e^{j\omega n}}d\omega}$
#     
#     $\text{z-transform} \overset{z=e^{j\omega}} \longleftrightarrow \text{DTFT}$
#     
#     - duality
#         - $x(t) \leftrightarrow X(\omega)$
#             
#             $\boxed{X(t) \leftrightarrow 2\pi x(-\omega)}$
#             
#         - $x(t) \leftrightarrow X(f)$
#             
#             $\boxed{X(t) \leftrightarrow x(-f)}$
#             
#     - modulation
#         
#         $x(t)\cdot cos(\omega_ot) \leftrightarrow \dfrac{2\pi}{2} [X(\omega-\omega_o)+X(\omega+\omega_o)]$
#         
#         $\boxed{x(t)\cdot cos(\omega_ot) \leftrightarrow \frac{1}{2} [X(f-f_o)+X(f+f_o)]}$
#         
#         $x(t)\cdot sin(\omega_ot) \leftrightarrow \dfrac{2\pi }{2j} [X(\omega-\omega_o)-X(\omega+\omega_o)]$
#         
#         $x(t)\cdot sin(\omega_ot) \leftrightarrow \dfrac{1}{2j} [X(f-f_o)-X(f+f_o)]$
#         
#     - sinc
#         
#         $Sa(bt)=\dfrac{sin(bt)}{bt}$
#         
#         $\dfrac{sin(at)}{bt}=\dfrac{a}{b}sinc(\dfrac{at}{\pi})$
#         
#         $\boxed{A\cdot rect(\frac{t}{T}) \longleftrightarrow AT\cdot Sa(\frac{\omega T}{2})}$ 
#         
#         $\boxed{A\cdot tri(\frac{t}{T}) \longleftrightarrow  AT\cdot Sa^2(\frac{\omega T}{2})}$ 
#         
#         
#     - properties
#         - time shifting
#             
#             $x(t\pm t_0)\leftrightarrow X(j\omega)e^{\pm j\omega t_0}$
#             
#             $x[n\pm n_0]\leftrightarrow X(e^{j\omega})e^{\pm j\omega n_0}$
#             
#         - frequency shifting
#             
#             $e^{\pm j\omega_0 t}x(t)\leftrightarrow X[j(\omega\mp\omega)]$
#             
#             $e^{\pm j\omega_0 t}x[n]\leftrightarrow X(e^{j (\omega\mp\omega)})$
#             
#         - conjugation
#             
#             $x^*[n]\leftrightarrow X^*(e^{-j\omega})$
#             
#         - time reversal
#             
#             $x[-n] \leftrightarrow X(e^{-j\omega})$            
#             
#         - area under $x(t)$
#             
#             $X(0)=\displaystyle\int_{-\infty}^{\infty}x(t)dt$
#             
#         - area under $X(j\omega)$
#             
#             $2\pi\cdot x(0)=\displaystyle\int_{-\infty}^{\infty}X(j\omega)d\omega$
#             
#         - differentiation in frequency
#             
#              $t^nx(t) \leftrightarrow  j\frac{d^n}{d\omega^n}X(j\omega)$ 
#             
#         - differentiation in time
#             
#              $\frac{d^n}{dt^n}x(t) \leftrightarrow  (j \omega)^nX(j\omega)$
#             
#             $x[n]-x[n-1] \leftrightarrow  (1-e^{-j\omega}) X(e^{j\omega})$
#             
#         - integration/accumulation in time
#             
#             $\int _{-\infty} ^{t} x(\tau)d\tau \leftrightarrow \frac{X(j\omega)}{j\omega} + \pi X(0) \delta (\omega)$
#             
#             $\sum_{k=-\infty} ^n x[k] \leftrightarrow  \dfrac{X[e^{j\omega}]}{1-e^{-j\omega}}  + \pi X(e^{j0}) \sum_{k=-\infty} ^\infty\delta (\omega-2\pi k )$
#             
#         - $x(t) \leftrightarrow X(\omega) \space pairs$
#             
#             $\begin{array}{c:c}
#             \color{orange} {x(t)} & \color{orange}  {X(\omega)} \\ \hdashline
#              R & CS \\ CS & R \\ I & CAS \\ CAS & I \\ R+E & R+E \\ I+E & I+E \\ R+O & I+O \\ I+O & R+O 
#             &  \end{array}$ 
#             
#             $\begin{array}{c:c}
#             \color{orange} {x(t)} & \color{orange}  {X(\omega)} \\ \hdashline
#              continuous  & NP \\ NP & continuous \\ discreate & P \\ P & discreate \\ continuous +P & discreate +NP \\ continuous + NP & continuous + NP \\ discreate+P & discreate+P \\ discreate+NP & continuous+P    \end{array}$ 
#             
#     - standard results
#         - $e^{-at}u(t)$
#             
#             $e^{-at}u(t) \longleftrightarrow \dfrac{1}{a+j\omega}$
#             
#         - $e^{-a|t|}$
#             
#             $e^{-a|t|} \longleftrightarrow \dfrac{2a}{a^2+\omega^2}$
#             
#         - $e^{-a t^2}$
#             
#             $e^{-a t^2} \longleftrightarrow \sqrt{\dfrac{\pi}{a}}e^{-\frac{\omega^2}{4a}}$ 
#             
#         - $u(t)$
#             
#             $u(t) \longleftrightarrow \dfrac{1}{j\omega} + \pi\delta(\omega)$
#             
#         - $u[n]$
#             
#             $\boxed{a^nu[n] \longleftrightarrow  \dfrac{1}{1-ae^{-j\omega}} }$ ,   |a| < 1
#             
#             $u[n] \longleftrightarrow  \dfrac{1}{1-e^{-j\omega}}  + \pi \sum\limits_{k=-\infty} ^\infty\delta (\omega-2\pi k )$
#             
# - z-transform
#     
#     $X[z] \longleftrightarrow \sum \limits_{ n=- \infty }^\infty x[n] z^{-n}$
#     
#     - properties
#         - time shifting
#             
#             $x[n-n_o]\leftrightarrow  z^{-n_o} X[z]$
#             
#         - time scaling
#             
#             $x[\frac{n}{m}]\leftrightarrow X[z^m]$               ROC : $R^{\frac{1}{m}}$
#             
#         - time reversal
#             
#             $x[-n] \leftrightarrow X[z^{-1}]$             ROC : $R^{-1}$
#             
#         - scaling of z (exponential sequence property)
#             
#             $a^n x[n] \leftrightarrow  X[\frac{z}{a}]$           ROC : $|a| R$
#             
#         - conjugation
#             
#             $x^*[n] \leftrightarrow  X^* [z^*]$         ROC : R 
#             
#         - accumulation
#             
#             $\displaystyle\sum_{k=-\infty} ^n x[k] \leftrightarrow  \dfrac{X[z]}{1-z^{-1}}$           ROC $> R \cap |z|>1$
#             
#         - convolution in time
#             
#             $x_1[n]*x_2[n]  \leftrightarrow  X_1[z]\cdot X_2[z]$
#             
#         - multiplication in time
#             
#             $x_1[n]\cdot x_2[n] \leftrightarrow  \dfrac{1}{2\pi j} \{ X_1[z] *X_2[z] \}$
#             
#         - differentiation in time
#             
#             $x[n]-x[n-1] \leftrightarrow  (1-z^{-1}) X[z]$
#             
#         - differentiation in z-domain
#             
#             $n\cdot x[n] \leftrightarrow  -z \dfrac{d X[z]}{dz}$          
#             
#         - initial value theorem
#             
#             $x[n] _{n=0} = \lim \limits_{z\rightarrow \infty} X[z]$   
#             
#             condition : $x[n]=0, n<0$
#             
#         - final value theorem
#             
#             $\lim \limits_{n\rightarrow \infty} x[n] \leftrightarrow  \lim \limits_{z\rightarrow 1} \{ (1-z^{-1})X[z]\}$
#             
#             condition 1 : $x[n]=0, n<0$ 
#             
#             condition 2 :  $(1-z^{-1})X[z]$ should have poles inside unit circle in z-plane
#             
#     - standard results
#         - $u[n]$
#             
#             $\boxed{a^nu[n] \longleftrightarrow  \dfrac{1}{1-az^{-1}} }$ ,                   |a| < 1
#             
#             $\boxed{-a^nu[-n-1] \longleftrightarrow  \dfrac{1}{1-az^{-1}} }$ ,     |a| > 1
#             
#             $u[n] \longleftrightarrow  \dfrac{1}{1-z^{-1}}$                                 |z|>1
#             
#             $-u[-n-1] \longleftrightarrow  \dfrac{1}{1-z^{-1}}$                   |z|<1
