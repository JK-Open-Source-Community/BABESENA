#!/usr/bin/env python
# coding: utf-8

# # Electromagnetic Theory
# 
# - $\Omega$
#     
#     $\Omega = 2\pi[1-cos(\theta)]$  for a cone whose cross-section subtends the angle $2\theta$
#     
#     $\Omega = 4\pi$  for full sphere
#     
# - $\mu$ and $\epsilon$
#     
#     $\mu_o = 4\pi \times 10^{-7} \frac{H}{m}$ 
#     
#     $\epsilon _o = 8.854187817 × 10⁻¹² \frac{F}{m}$
#     
#     $B= \mu H$ 
#     
#      $D = \epsilon E$
#     
# - gauss law
#     - Integral form of Gauss law
#         
#          $\displaystyle\oiint D\cdot dS = \psi _{e} \varpropto Q$
#         
#     - Gauss Divergence theorem
#         
#          $\displaystyle\oiint D\cdot dS = \iiint \nabla \cdot D dV$
#         
#     - Point form of Gauss Law
#         
#         $\rho _{v} = \nabla \cdot \vec{D}$ 
#         
# - ampere's law
#     - Integral form of Ampere's law
#         
#           $\displaystyle\oint \vec{H}\cdot \vec{dl} = I$
#         
#     - Ampere Circulation
#         
#          $\displaystyle\oint H\cdot dl = \iint (\nabla \times H) dS$
#         
#     - Point form of Ampere Law
#         
#         $\vec{J} = \nabla \times \vec{H}$ 
#         
#     - modified ampere's law
#         
#          $\displaystyle\oint H\cdot dl = I_c + I_d$
#         
#         $\nabla\times H = J_c+J_d$
#         
# 
# rate of change of any scalar with del is `gradient`
# 
# - what is condition for path independent line integral
#     
#     $\nabla \times A=0$
#     
# 
# `solenoidal` → $\nabla . \vec F =0$
# 
# `irrotational` → $\nabla \times \vec F =0$
# 
# - curl of gradient
#     
#     is always zero and its line integral is path independent
#     
# - current density
#     - surface current
#         
#         $K=\dfrac{I}{width}$$\dfrac{ampere}{m}$ 
#         
#     - volume current
#         
#         $J=\dfrac{I}{S}$   $\dfrac{ampere}{m^2}$ 
#         
# - right hand (index-middle-thumb) sequence of unit vectors
#     - $a_x \bot a_y \bot a_z$
#     - $a_{\rho}\bot a_{\phi} \bot a_{z}$
#     - $a_r \bot a_\theta \bot a_\phi$
# - scaling factors
#     
#     $\begin{array}{c:c}
#     \color{orange} \text{parameters} & \color{orange} \text {scaling\space factors} \\ \hdashline
#     \begin{array}{c:c:c} x & y & z \\ \hdashline \rho & \phi & z \\ \hdashline r & \theta & \phi \\ \hdashline u & v & w \end{array} 
#     & \begin{array}{c:c:c} 1 & 1 & 1 \\ \hdashline 1 & \rho & 1 \\ \hdashline 1 & r & r\cdot sin(\theta) \\ \hdashline h_1 & h_2 & h_3 \end{array} \end{array}$ 
#     
#     $\vec{dl} = (h_1du)a_u+(h_2dv)a_v+(h_3dw)a_w$
#     
#     $\boxed{\vec{dS} = (h_2h_3dvdw)a_u+(h_3h_1dwdu)a_v+(h_1h_2dudv)a_w}$
#     
#     $dV = h_1h_2h_3dudvdw$
#     
# - divergence and curl using scaling factors
#     
#     $\nabla\cdot A \neq A\cdot\nabla$
#     
#     - $\nabla$
#         
#         $=\dfrac{1}{h_1}\dfrac{\partial}{\partial u}a_u+\dfrac{1}{h_2}\dfrac{\partial}{\partial v}a_v+\dfrac{1}{h_3}\dfrac{\partial}{\partial w}a_w$
#         
#     - $\nabla\cdot\vec{A}$  if  $\vec{A}=A_ua_u+A_va_v+A_wa_w$
#         
#         $=\dfrac{1}{h_1h_2h_3}\Big\lbrack\dfrac{\partial (h_2h_3A_u)}{\partial u}+\dfrac{\partial(h_3h_1A_v)}{\partial v}+\dfrac{\partial(h_1h_2A_w)}{\partial w}\Big\rbrack$
#         
#     - $\nabla\times\vec{A}$  if  $\vec{A}=A_ua_u+A_va_v+A_wa_w$
#         
#         $=\dfrac{1}{h_1h_2h_3}\begin{vmatrix}
#          h_1a_u & h_2a_v & h_3a_w \\
#           \frac{\partial}{\partial u} & \frac{\partial}{\partial v} & \frac{\partial}{\partial w}\\ h_1A_u & h_2A_v & h_3A_w
#         \end{vmatrix}$
#         
#     - $\nabla ^2 G$
#         
#         $\color{skyblue}\nabla ^2 = \nabla \cdot ( \nabla G)$
#         
#         $\nabla ^2 G =\dfrac{1}{h_1h_2h_3}\Big\lbrack\dfrac{\partial }{\partial u}\Big(\dfrac{h_2h_3}{h_1}\dfrac{\partial G}{\partial u}\Big)+\dfrac{\partial }{\partial v}\Big(\dfrac{h_1h_3}{h_2}\dfrac{\partial G}{\partial v}\Big)+\dfrac{\partial }{\partial w}\Big(\dfrac{h_1h_2}{h_3}\dfrac{\partial G}{\partial w}\Big)\Big\rbrack$
#         
# - $\displaystyle\int_{\theta=0}^{\theta=\pi} \int_{\phi=0}^{\phi=2\pi} sin(\theta)d\theta d\phi$
#     
#     $=4\pi$
#     
# - $\displaystyle \int_{0}^{\frac{\pi}{2}}  sin^3(\theta)d\theta$
#     
#     $=\dfrac{2}{3}$
#     
# - position vectors
#     - cartesian
#         
#         $\vec{r}=x a_x +y a_y +z a_z$ 
#         
#     - cylindrical
#         
#         $\vec{r}=\rho a_\rho$ 
#         
#         $\neq \rho a_\rho + \phi a_\phi +z a_z$
#         
#     - spherical
#         
#         $\vec{r}=r a_r$
#         
#         $\neq r a_\rho + \theta a_\theta +\phi a_\phi$
#         
# - gauss law application
#     - point charge
#         
#         $D(r)_r = \dfrac{Q}{4\pi r^2} a_r$
#         
#     - hollow sphere - surface
#         
#         $D(r) = \rho_s \frac {R^2}{r^2}$  ,  $r>R$
#         
#     - infinite line
#         
#         $D=\dfrac{\rho_L}{2\pi\rho}a_\rho$ 
#         
#     - hollow cylinder
#         
#         $D=\dfrac{\rho_s}{\rho}R$ ,   $\rho > R$
#         
#     - solid cylinder
#         
#         $D=\frac{\rho_v\rho}{2}$  , $\rho<R$
#         
#         $D=\frac{\rho_vR^2}{2\rho}$  , $\rho>R$
#         
#     - infinite sheet
#         
#         $D=\frac{\rho_s}{2}(\pm a_N)$
#         
# - ampere law application
#     - infinite wire
#         
#         $H=\frac{I}{2\pi\rho}a_\phi$ 
#         
#         $a_\phi=I\times \rho$
#         
#     - biot-savart law
#         
#         $\boxed{dH = \dfrac{Idl \times a_r}{4\pi r^2} = \dfrac{KdS \times a_r}{4\pi r^2} = \dfrac{JdV \times a_r}{4\pi r^2} }$
#         
#     - hollow cylinder
#         
#         $H=\dfrac{K}{\rho}R$ ,   $\rho > R$
#         
#     - solid cylinder
#         
#         $H=\frac{J\rho}{2}$  , $\rho<R$
#         
#         $H=\frac{JR^2}{2\rho}$  , $\rho>R$
#         
#     - infinite sheet
#         
#         $H=\dfrac{K\times a_N}{2}$
#         
# - un-symmetric charge
#     
#     $\displaystyle\int dD = \int \dfrac{\rho_L dl}{4\pi  r^2}a_r = \iint \frac{\rho_S dS}{4\pi  r^2}a_r = \iiint \frac{\rho_V dV}{4\pi  r^2}a_r$ 
#     
# - un-symmetric current
#     - finite length wire
#         
#         $H = \dfrac{I}{4\pi \rho}[sin(\alpha_1)-sin(\alpha_2)]a_\phi$     
#         
#          ($\pm\alpha_1$ and $\pm\alpha_2$ are measured from horizontal level )
#         
# - dipole
#     
#     $torque = \vec R \times \vec F$ 
#     
#     - electric
#         
#         $V=\dfrac{Q \cdot d\cdot cos(\theta)}{4\pi \epsilon r^2}$
#         
#         can calculate E by $E = -\nabla V$
#         
#     - magnetic
#         
#         $torque = \vec M \times \vec B$
#         
#         $\vec M = \displaystyle \iint I  d\vec s$  
#         
# - laplace and poisson
#     
#     $\nabla^2V = \dfrac{-\rho_v}{\epsilon}$ (poisson)
#     
#     $\nabla ^2V = 0$ (laplace)
#     
# - vector potential
#     
#     $\vec A = \dfrac{W}{I dl_1}=\displaystyle { \int \vec B\times \vec {dl_2} \space} \frac{weber}{m} = \frac{\mu I dl_3}{4\pi r}$
#     
#     $\vec B = \nabla \times \vec A$
#     
# - boundary conditions of fields
#     - electric field
#         
#         $D_{n_2} = D_{n_1}+\rho_s$ 
#         
#         $E_{t_1}=E_{t_2}$
#         
#     - magnetic field
#         
#         $B_{n_1}=B_{n_2}$
#         
#         $H_{t_2} = H_{t_1}+\vec K\times a_N$ 
#         
# - maxwell's equations
#     
#     $\displaystyle\begin{array}{c:c}
#     \color{orange} \text{integral} & \color{orange} \text {point} \\ \hdashline \oiint D\cdot dS =  Q &  \nabla \cdot \vec{D}=\rho _{v} \\ \oint E\cdot dl =  0 & \nabla \times \vec{E}=0 \\\oiint B\cdot dS =  0 &  \nabla \cdot \vec{B}=0 \\ \oint H\cdot dl =  I & \nabla \times \vec{H}=0 \end{array}$ 
#     
# 
# $j = e^{j90\degree}$ (delay)
# 
# - continuity equation
#     
#     $\nabla\cdot J = \dfrac{\partial \rho_v}{\partial t}$
#     
# - conduction and displacement current
#     
#     $J_c = \sigma E$
#     
#     $J_d = \dfrac{\partial D}{\partial t} =\dfrac{\partial \epsilon E}{\partial t}$
#     
# - faraday law, lenz law and lorentz law
#     
#     $\displaystyle\boxed{\nabla\times E = - \dfrac{\partial B}{\partial t}}$
#     
#     $\boxed{\displaystyle\nabla\times H =  \dfrac{\partial D}{\partial t} + J_C}$
#     
#     $\displaystyle\oint E \cdot dl= - \iint\dfrac{\partial B}{\partial t}\cdot dS$
#     
#     $\displaystyle\oint H \cdot dl=  \iint\dfrac{\partial D}{\partial t}\cdot dS + I_C$
#     
# - helmholtz
#     
#     $\nabla ^2 E = \gamma^2 E$
#     
#     $\nabla ^2 H = \gamma^2 H$
#     
# - $\gamma$
#     
#     $\boxed{{{\gamma }} = \alpha + j \beta =\sqrt {j\omega \mu \left( {\sigma + j\omega \epsilon} \right)}}$
#     
#     $e^{-\gamma z} = e^{-\alpha z} e^{-j\beta z}$ (amplitude and phase variations)
#     
#     skin depth, $\delta$ = $\dfrac{1}{\alpha} =\dfrac{1}{\sigma R_S }$ —→ $|E| = E_o e^{-1}$ 
#     
#     loss tangent $=|\dfrac{J_c}{J_d}| = \dfrac{\sigma}{\omega \epsilon}$ 
#     
#     $\alpha = \omega \sqrt{\dfrac{\mu\epsilon}{2}(\sqrt{1+(\frac{\sigma}{\omega \epsilon} )^2}-1)}$
#     
#     $\beta = \omega \sqrt{\dfrac{\mu\epsilon}{2}(\sqrt{1+(\frac{\sigma}{\omega \epsilon} )^2}+1)}$
#     
# - $\eta$ (intrinsic impedance)
#     
#     $\boxed{\eta = R + j X = \dfrac{E\angle \theta_1}{H\angle \theta_2} = \sqrt{\dfrac{j\omega\mu}{\sigma+j\omega\epsilon}}=\sqrt{\dfrac{\mu}{\epsilon }}}$
#     
#     $\eta_o = \sqrt{\dfrac{\mu_o}{\epsilon _o}}= 120\pi = 377\Omega$
#     
# - $v_p$ (phase velocity) and $v_g$ (group velocity)
#     
#     $v_p=\dfrac{\omega}{\beta}=  \dfrac{1}{\sqrt{\mu\epsilon}}$ 
#     
#     $\theta = \omega t = \beta z$
#     
#     $v_g =\dfrac{d \omega}{d \overline \beta}$
#     
#     $v_g v_p =c^2$
#     
# - poynting vector
#     
#     $P_{avg} = \dfrac{1}{2}|E\times H|=E_{rms} \times H_{rms}$ 
#     
#     $\displaystyle power= \iint P_{avg}\cdot dS$
#     
#     ohmic power dissipated per unit volume : $J\cdot E = \sigma E^2   \dfrac{watts}{m}$
#     
# - reflections and transmission
#     - normal incidence
#         
#         $\dfrac{E^t_o}{E^i_o} = \tau$ 
#         
#         $\boxed{\Gamma_E =\dfrac{E^r_o}{E^i_o} = \dfrac{\eta_2-\eta_1}{\eta_2+\eta_1} }$
#         
#         $\boxed{\Gamma_H =\dfrac{H^r_o}{H^i_o} =\dfrac{\eta_1-\eta_2}{\eta_1+\eta_2} = -\Gamma_E }$
#         
#         - boundary conditions
#             - $E_{tang1}=E_{tang2}$
#                 
#                 $\boxed{1+\Gamma = \tau}$ 
#                 
#             - $H_{tang1}=H_{tang2}$
#                 
#                 $\boxed{1-\Gamma = \dfrac{\eta_1}{\eta_2}\tau}$
#                 
#     - inclined incidence
#         
#         $\theta _i=\theta _t$
#         
#         - snell's law
#             
#             $\dfrac{sin(\theta_i)}{sin(\theta_t)}=\sqrt{\dfrac{\epsilon_2}{\epsilon_1}}$
#             
#         - brewster's angle
#             
#             $tan(\theta_i) =\sqrt{\dfrac{\epsilon_2}{\epsilon_1}}$
#             
#         
#         $\boxed{\Gamma _S = \dfrac{\dfrac{\eta_2}{cos(\theta_t)}-\dfrac{\eta_1}{cos(\theta_i)}}{\dfrac{\eta_2}{cos(\theta_t)}+\dfrac{\eta_1}{cos(\theta_i)}}}$
#         
#         $\boxed{\Gamma _P = \dfrac{\eta_2cos(\theta_t)-\eta_1{cos(\theta_i)}}{\eta_2{cos(\theta_t)}+\eta_1{cos(\theta_i)}}}$
#         
# - transmission line
#     
#     $\gamma=\sqrt{(R+j\omega L)(G+j\omega C)}$
#     
#     $Z_o =  \sqrt{\dfrac{(R+j\omega L)}{(G+j\omega C)}}$
#     
#     $Z_{series} = R+j\omega L$
#     
#     $Y_{shunt} = G+j\omega C$
#     
#     $\boxed{\Gamma = \dfrac{Z_L - Z_o}{Z_L + Z_o}}$
#     
#     $\boxed{\text{SWR} = \dfrac{1 + |\Gamma|}{1 - |\Gamma|}} = \dfrac{|V_\text{max}|}{|V_\text{min}|}= \dfrac{|I_\text{max}|}{|I_\text{min}|}$
#     
#     - standing waves
#         
#         $2\beta x_{\text{max}} = 2n\pi +\theta$ 
#         
#         $2\beta x_{\text{min}} = (2n+1)\pi +\theta$ 
#         
#     - lossless → $\alpha =0$
#         
#         $\boxed{R=G=0}$
#         
#     - distortionless → $\omega \propto \beta$
#         
#         $V(t) \leftrightarrow V(x) \implies \omega t = \beta x$  
#         
#         $\boxed{\dfrac{L}{R} = \dfrac{C}{G}}$
#         
#     - distortions
#         - delay distortion
#             
#             $\beta\propto \omega$ 
#             
#         - frequency distortion
#             
#             $\alpha \propto \omega$
#             
#     - $Z_{in}$
#         
#         $Z_{in} = R_o(\dfrac{Z_Lcos(\beta x)+jR_o sin(\beta x)}{R_ocos(\beta x)+jZ_L sin(\beta x)})$
#         
#         $Z_{in} = \begin{cases}
#            R_o\dfrac{Z_L +j R_o}{R_o +j Z_L} & l=\dfrac{\lambda}{8} \\
#            \dfrac{R_o^2}{Z_L} & l=\dfrac{\lambda}{4} \\ Z_L & l=\dfrac{\lambda}{2}
#         \end{cases}$
#         
#     - capacitance and inductance
#         
#         $c=\dfrac{2\pi\epsilon l}{ln(\frac{b}{a})}$ for co-axial cable
#         
#         $c=\dfrac{\pi\epsilon l}{ln(\frac{D}{r})}$
#         
#         $\dfrac{L}{l}\cdot\dfrac{C}{l} = \mu\epsilon$
#         
#     - smith chart
#         
#         ![Electromagnetic%20Theory%20d4718a13eaf9480984c7d37be18795e2/Untitled.png](Electromagnetic%20Theory%20d4718a13eaf9480984c7d37be18795e2/Untitled.png)
#         
# - antenna
#     
#     $|E_\theta| = \dfrac{I_m}{2}\dfrac{dl}{\lambda}\dfrac{\sin \theta}{r}\eta$
#     
#     $P_{avg} = \frac{1}{2}E_\theta H_\phi$                   $P_{total} = \oiint P_{avg} \cdot ds$ 
#     
#     $\boxed{W_r =I_{rms}^2 R_r= I_{rms}^2 80\pi^2 \Big ( \dfrac{dl}{\lambda} \Big)^2}$     ( isotropic antenna )
#     
#     uniform current : $dl<<\lambda$
#     
#     - linear current : $l \rightarrow \frac{\lambda}{10} -\frac{\lambda}{20}$
#         
#         $I_{avg} = \frac{I_o+0}{2}$ → $\frac{I_{rms}^2}{4}$  
#         
#     - harmonic current : $l \rightarrow \frac{\lambda}{2} , \frac{\lambda}{4},\frac{\lambda}{8}$
#         
#         $I_{avg} = \dfrac{\int_0^{\pi}I_m\sin(t)dt}{\pi}=\dfrac{2I_m}{\pi}$ → $\dfrac{4I_{rms}^2}{\pi^2}$  
#         
#         $\frac{\lambda}{2}$  → $R_r = 80\pi^2\dfrac{4}{\pi^2}\Big(\dfrac{\frac{\lambda}{2}}{\lambda}\Big)^2 =73 \Omega$
#         
#         $\frac{\lambda}{4}$  → $R_r =73\Big(\dfrac{\frac{\lambda}{4}}{\frac{\lambda}{2}}\Big)= 36.5 \Omega$
#         
#         $\frac{\lambda}{8}$  → $R_r = 36.5\Big(\dfrac{\frac{\lambda}{8}}{\frac{\lambda}{4}}\Big)=18.25 \Omega$
#         
#         $R_r \not\propto \frac{1}{\lambda^2}$
#         
#     - fraunhofer region
#         
#         for practical antenna of 'D' dimension radiation fields are considered strong beyond
#         
#         $r> \dfrac{2D^2}{\lambda}$
#         
#     - radiation intensity
#         
#         $\dfrac{dW_r}{dS} = P(r,\theta,\phi)$
#         
#         $\dfrac{dW_r}{d\Omega} = U(\theta,\phi)$
#         
#         $U(\theta,\phi)= P(r,\theta,\phi) r^2$
#         
#         $dS \rightarrow r^2 \sin \theta d\theta d\phi$
#         
#         $d\Omega \rightarrow  \sin \theta d\theta d\phi$
#         
#         $dS = r^2 d\Omega$
#         
#     - radiation pattern
#         - half power beam width (HPBW)
#             
#             $\theta _{HPP_1} -\theta _{HPP_2}$  via $\theta _{max}$
#             
#             $\displaystyle \theta_{HPBW} =\int_{\theta_1}^{\theta_2}\sin \theta d\theta$
#             
#             $\phi_{HPBW}=\phi _{HPP_2} -\phi _{HPP_1}$ 
#             
#             beam solid angle : $\displaystyle \Omega _A = \theta_A \times \phi _A =\int_{\theta_1}^{\theta_2}\sin \theta d\theta \times \phi_A$
#             
#         - beam width first null (BWFN)
#             
#             $\theta _{NP_1} -\theta _{NP_2}$  
#             
#         
#         $HPBW \approx \dfrac{BWFN}{2}$ for `complex pattern`
#         
#     - directive gain, $G_D$
#         
#         $U_{avg} = \dfrac{W_r}{4\pi}$
#         
#         $\displaystyle G_D(\theta ,\phi) = \dfrac{U(\theta ,\phi)}{U_{avg}}=\dfrac{U(\theta ,\phi)}{\Bigg(\dfrac{\int_{\theta=0}^{\pi}\int_{\phi=0}^{2\pi}U(\theta ,\phi) d\Omega}{4\pi}\Bigg)}$
#         
#         $G_D = \dfrac{4\pi}{\Omega_A}$
#         
#         - maximum gain
#             
#             hertzian dipole : maximum gain = 1.5
#             
#             half wave dipole : maximum gain = 1.63
#             
#     - antenna array
#         
#         $E_{total} = E_o + E_o e^{j\psi}=2E_o \cos(\frac{\psi}{2})$
#         
#         $\psi =\alpha +\beta d\cos\theta$
#         
#         `end fire` : $\psi =0$,        $\alpha = \pm \beta d$,       $\theta_{max} =0\degree , 180\degree$  
#         
#         `broadside array` : $\psi =0$,      $\alpha =0$,      $\theta_{max} =90\degree$  
#         
#         - N-element-uniform-isotropic sources
#             
#             $E_T = E_o \dfrac{\sin(\frac{N\psi}{2})}{\sin(\frac{\psi}{2})}$
#             
#             $\psi =0\rightarrow NE_o$ 
#             
#     - multiplication of pattern
#         
#         $\text{final pattern = unit pattern $\times$ array factor } = U(\theta,\phi) \cos (\frac{\psi}{2})$
#         
#     - friis formula
#         
#         `capture area`: $G_D= \dfrac{4\pi}{\lambda^2}A_e$ 
#         
#         $\boxed{W_r=\dfrac{W_tG_tG_r}{(\frac{4\pi d}{\lambda})^2}}$
#         
#         $\Big(\dfrac{4\pi d}{\lambda}\Big)^2 = L_s$  loss due to radial scattering or spreading
#         
#     - polarization loss factor
#         
#         $PLF = |\cos \theta |^2 =|\hat{E_T}\cdot \hat{E_R}|^2$ 
#         
# - polarization
#     - linear
#         - single component of E
#         - 2 components of E (both in phase)
#     - circular
#         - 2 components having equal amplitude and out of phase by $90 \degree$
#     - elliptical
#         - 2 components of E
#             - unequal amplitude with any phase other than $0\degree / 180 \degree$
#             - equal amplitude with any phase other than $0\degree/ 90\degree / 180 \degree$
#     - sense of rotation
#         
#         propagation > thumb
#         
#         field rotation > fingers 
#         
#         which ever hand will follow the above will be rotation 
#         
# - waveguide
#     - parallel plane
#         
#         $E_{tang} =0$                    $E_{normal} =E_{max}$
#         
#         $H_{normal} =0$                $H_{tang} = H_{max}$
#         
#         $\boxed{\beta_x a = m\pi}$
#         
#         $\boxed{\beta_x^2+\overline \beta^2 = \beta ^2 = \omega^2 \mu\epsilon}$ 
#         
#         cut off → $\overline \beta =0$
#         
#         $\overline \beta = \beta \cos (\theta)$                $\beta_c=\beta _x= \beta \sin (\theta)$
#         
#         $\overline \lambda = \dfrac{\lambda}{\cos(\theta)}$ 
#         
#     - rectangular
#         
#         $\omega_c = \Bigg(\sqrt{\Big(\dfrac{m\pi}{a}\Big)^2 +\Big(\dfrac{n\pi}{b}\Big)^2} \Bigg) c$
#         
#         $TE_{mn}$  /$TM_{mn}$ → m horizontal axis feeds and n vertical axis feeds 
#         
#         non-existing modes in TM → `evanescent modes` → m = 0 / n =0 
#         
#         `dominant mode` → least cut off
#         
#         `degenerate modes` → same cut off
#         
#         $\eta _{TE} \text{  or  } \eta _{TM} = \dfrac{E_{transverse}}{H_{transverse}}$
#         
#         $\eta _{TE} = \dfrac{120\pi}{\sqrt{1-(\frac{f_c}{f})^2}}$
#         
#         $\eta _{TM} = 120\pi\sqrt{1-(\frac{f_c}{f})^2}$
#         
#     - circular
#         
#         $E(\rho =a) _{tang} =0$
#         
#         $H(\rho =a)_{normal} =0$
#         
#         - TE
#             
#             $J'_n(\beta_\rho \rho) =0$ → $\beta_\rho \rho = X'_{np}$  $(H_{tang} = H_{max})$
#             
#             $\boxed{\omega_c = \dfrac{X_{np}' c}{ a}}$
#             
#         - TM
#             
#             $J_n(\beta_\rho \rho) =0$ → $\beta_\rho \rho = X_{np}$  $(E_{tang} = 0)$
#             
#             $\boxed{\omega_c = \dfrac{X_{np} c}{ a}}$
#             
#         - $X_{np}$  and $X'_{np}$
#             
#             $`p^{th}$ root of $n^{th}$ order`
#             
#             n = 0, 1, 2 . . .
#             
#             p = 1, 2, 3 . . .
#             
#             n → number of feeds in $\phi$
#             
#             p → number of feeds in $\rho$
#             
#             n=0 → $\phi=0\degree \text{ or } 180\degree$
#             
#             $TE_{n0}$  and $TM_{n0}$ → `evanescent modes`
#             
#             $X_{11} ' = 1.84$    $(TE_{11} )$ → `dominant mode`
#             
#             $X_{01} =2.40$    $(TM_{01} )$→`least $f_c$TM`
#             
#             $X'_{21} =3.05$    $(TE_{21} )$
#             
#             $X'_{01} =X_{11} = 3.83$    $(TM_{11} \text{ and } TE_{01})$→`first degenerate modes`
#             
#             `for any p` : $X'_{0p} =X_{1p}$    $(TM_{1p} \text{ and } TE_{0p})$→`degenerate modes`
#             
#     - TE and TM
#         - RWG
#             - TM waves → $H_z =0$
#                 
#                 $E_z = E_o \sin \Big(\dfrac{m\pi}{a}x\Big)\sin \Big(\dfrac{n\pi}{b}y\Big) e^{-j\overline \beta z} e^{j\omega t} a_z$
#                 
#                 $E_x = C_1\dfrac{\partial E_z}{\partial x}$
#                 
#                 $E_y = C_2\dfrac{\partial E_z}{\partial y}$
#                 
#                 $H_x = C_3 E_y$ 
#                 
#                 $H_y = C_4 E_x$ 
#                 
#             - TE waves → $E_z =0$
#                 
#                 $H_z = H_o \cos \Big(\dfrac{m\pi}{a}x\Big)\cos \Big(\dfrac{n\pi}{b}y\Big) e^{-j\overline \beta z} e^{j\omega t} a_z$
#                 
#                 $H_x = C_1\dfrac{\partial H_z}{\partial x}$
#                 
#                 $H_y = C_2\dfrac{\partial H_z}{\partial y}$
#                 
#                 $E_x = C_3 H_y$ 
#                 
#                 $E_y = C_4 H_x$ 
#                 
#         - CWG
#             - TM waves → $H_z =0$
#                 
#                 $E_z = E_o J_n(\beta_{\rho}\rho)\cos (n\phi) e^{-j\overline \beta z} e^{j\omega t} a_z$
#                 
#                 $E_\rho = C_1\dfrac{\partial E_z}{\partial \rho}$
#                 
#                 $E_\phi = C_2\dfrac{\partial E_z}{\partial \phi }$
#                 
#                 $H_\phi  = C_3 E_\rho$ 
#                 
#                 $H_\rho = C_4 E_\phi$ 
#                 
#             - TE waves → $E_z =0$
#                 
#                 $H_z = H_o J_n(\beta'_{\rho}\rho)\cos (n\phi) e^{-j\overline \beta z} e^{j\omega t} a_z$
#                 
#                 $H_\rho = C_1\dfrac{\partial H_z}{\partial \rho}$
#                 
#                 $H_\phi = C_2\dfrac{\partial H_z}{\partial \phi }$
#                 
#                 $E_\phi  = C_3 H_\rho$ 
#                 
#                 $E_\rho = C_4 H_\phi$
