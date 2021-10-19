#!/usr/bin/env python
# coding: utf-8

# # Communication System

# $\displaystyle\int _{-\infty}^{\infty}ae^{-b|x|}dx=\dfrac{2a}{b}$
# 
# $\displaystyle\int _{0}^{\infty}e^{-x^2}dx=\dfrac{\sqrt{\pi}}{2}$
# 
# :::{dropdown} terminology
# 
# `baseband signal or lowpass signal` include frequencies that are very near zero, by comparison with its highest frequency
# 
# `band pass signal`  a band of frequencies ranging from some non zero value to another non zero value
# 
# :::
# 

# 
# ```{dropdown} q function
#     
# $$ Q(x) = \dfrac{1}{\sqrt{2\pi}} \displaystyle\int_x ^{\infty} e^{\frac{-z^2}{2}}dz $$
#     
# $Q(x)+Q(-x)=1$
#     
# $Q(-\infty)=1$
#     
# $Q(\infty)=0$
# 
# ```    
# 

# ```{dropdown} CDF
#     
# $F_X(x) = P(X\leq x) = 1-P(X>x)$
#     
# ```{dropdown} properties of CDF
# 
# 1. $0\le F_X(x)\le1$
# 2. $F_X(\infty)=P(X\le \infty)=1$
# 3. $F_X(-\infty)=P(X\le - \infty)=0$
# 4. $F_X(-\infty)+F_X(\infty)=1$
# 5. $F_X(x)$ is non-decreasing function of x 
# 
# ```{dropdown} graph of CDF is continuous from right at a point x=a 
# $ F_X(a)=F_X(a^{+}) $
# ```
# ```{dropdown} range calculations   
# 
# $\color{green}{F_X(b^+)-F_X(a^+)=P(a<X\le b)}$          
# change inequalities according to $b^{\pm}$ and $a^{\pm}$
# $\color{green}  P(X=a) =F_X(a^+)-F_X(a^-)$ = size of jump
# 
# ```
# 
# ```
# ```
# ```
# 

# ```{dropdown} PDF
#     
# $$f_X(x) = \dfrac{d}{dx}F_X(x)$$
#     
# ```{dropdown} properties of PDF
# 1. $f_X(x)\ge0$
# 2. $F_X(\infty)=\int_{-\infty}^{\infty}f_X(x)dx=1$ 
# 3. $\color{lightgreen}F_X(x)=P(X\le x)=P(-\infty <X\le x)=\color{skyblue}\int_{-\infty}^{x}f_X(x)dx$ 
# 4. $\color{green} P(a <X\le b)=\int_{a^+}^{b^+}f_X(x)dx$
# 5.  $P(X=a) =\int_{a^-}^{a^+}f_X(x)dx$
# ```
# ```

# ```{dropdown} PMF
#     
# $p_X(x_i)=P(X=x_i)$
#     
# $f_X(x)=\sum_i p_X(x_i)\delta(x-x_i)$
#     
# $F_X(x)=\sum_i p_X(x_i)u(x-x_i)$
# ```

#    
# ```{dropdown} joint probability
#     
# $P(\frac{A}{B})=\frac{P(A\cap B)}{P(B)}$
#     
# $P(A\cap B)=P(\frac{A}{B})P(B)=P(\frac{B}{A})P(A)$
# ```
# 

# 
# ````{dropdown} statistical parameters
#     
# $r^{th}$ order moment of X = $E(X^r)$
#     
# $r^{th}$ order central moment of X = $E[(X-\mu_X)^r]$
#     
# ```{dropdown} expectation operator
# 
# $\displaystyle  E[X]=\int _{-\infty}^{\infty}xf_X(x)dx$
#         
# $\boxed{\displaystyle E[g(x)]=\int _{-\infty}^{\infty}g(x)f_X(x)dx}$
#         
# $E[g(x)]=\sum _{i} g(x_i)P[X=x_i]$
#         
# $E[aX+bY+c]=aE[X]+bE[Y]+c$
# 
# ```
#    
# ```{dropdown} mean $(\mu_x)$
#         
# $E[X]=\overline {X} = \mu_X$  = mean value or dc value of RV
#         
# $\mu_X ^2$  = dc power
# ```
#         
# ```{dropdown} mean square value $(E[X^2])$
#         
# $E[X^2]$ = total average power of RV = ac power + dc power
#         
# $\displaystyle E[X^2]=\int _{-\infty}^{\infty}x^2f_X(x)dx$ 
#         
# $E[X^2]=\sum _{i} x_i^2P[X=x_i]$
# ```
#         
# ```{dropdown} variance $(\sigma_x^2)$
#         
# $\sigma_X^2=E[(X-\mu_X)^2]$ = ac power of RV (definition)
#         
# $\color{green}\sigma_X^2=E[X^2]-\mu_X^2$
#         
# ac power = total power - dc power
#         
# $standard \space deviation = \sqrt{\sigma^2_x}$ 
# ```
#         
# ```{dropdown} significance of mean
#         
# $\int_{\mu_X}^{\infty}f_X(x)dx=\int_{-\infty }^{\mu_X}f_X(x)dx=\dfrac{1}{2}$
# ```
# 
# ````
# 

#         
# - standard PDF for CRV
#     - uniform PDF
#         
#         
#         X~U[a,b]
#         
#         $\mu_{X} = \frac{a+b}{2}$
#         
#         $\sigma _{X}^2=(\frac{b-a}{12})^2$
#         
#         $E[X^2]=\frac{a^2+b^2+ab}{3}$
#         
#     - triangular PDF
#         
#         $X \sim \triangle[a,c,b]$ 
#         
#         peak value = $\dfrac{2}{b-a}$
#         
#         $E[X] = \mu _X= \dfrac{a+b+c}{3}$
#         
#         $\sigma _X^2 = \dfrac{a^2+b^2+c^2-ab-bc-ca}{18}$
#         
#     - gaussian, normal distribution
#         
#         $X\sim N(\mu_X, \sigma_X ^2)$
#         
#         pdf : $\boxed{f_X(x)=\dfrac{1}{\sqrt{2\pi\sigma_X^2}}e^{\frac{-(x-\mu_X)^2}{2\sigma_X ^2}}}$
#         
#         cdf : $F_X(x)=P\{X\le x\} = 1-P\{X \gt x\}=1-Q  [ \dfrac{x-\mu_X}{\sigma_X} ]$
#         
#         $P\{X=c\}=0$
#         
#         $\boxed{P\{X\gt a\}=Q  [ \dfrac{a-\mu_X}{\sigma_X} ]}$
#         
#     - rayleigh pdf
#         
#         $f_X(x)=\frac{x}{\sigma_X^2}e^{\frac{-x^2}{2\sigma_X^2}}u(x)$
#         
#     - exponential distribution
#         
#         $f_X(x) = \begin{cases}
#            \lambda e^{-\lambda x} &\text{if } x \ge 0 \\
#            0 &\text{if } x \lt 0
#         \end{cases}$
#         
#     - laplace distribution
#         
#         $f_X(x)=ae^{-b |x|} \space where \space\dfrac{2a}{b}=1$ ( a >0 , b>0)           
#         
# - linear transformation
#     
#     Y=aX+b
#     
#     - $E[Y]$
#         
#         $aE[X]+b$
#         
#     - $E[Y^2]$
#         
#         $a^2E[X^2]+b^2+2abE[X]$
#         
#     - $\sigma_Y^2$
#         
#         $a^2\sigma_X^2$
#         
#     - $F_Y(y)$
#         
#         $P\{aX+b\le y\}$
#         
#         $P\{X\le \frac{y-b}{a}\}$
#         
#     - $f_Y(y)$
#         
#         $\frac{1}{a}f_X(\frac{y-b}{a})$
#         
#     - $X\sim U[-m,m]$
#         
#         $Y\sim U[-am+b,am+b]$
#         
#     - $X \sim \triangle[-m,0,m]$
#         
#         $Y \sim \triangle[-am+b,b,am+b]$
#         
#     - $X \sim N[\mu_X,\sigma_X^2]$
#         
#         $X \sim N[a\mu_X+b,a^2\sigma_X^2]$
#         
# - bivariate RV
#     - joint CDF
#         
#         $F_{XY}(x,y)=P\{X\le x,Y\le y \}$
#         
#         - properties
#             
#             $0\le F_{XY}(x,y) \le 1$
#             
#             $F_{XY}(\infty,\infty)=1$
#             
#             $F_{XY}(-\infty,y)=F_{XY}(x,-\infty)=F_{XY}(-\infty,-\infty)=0$
#             
#     - marginal CDF
#         
#         $F_{XY}(\infty,y)=F_{Y}(y)$
#         
#         $F_{XY}(x,\infty)=F_{X}(x)$
#         
#     - conditional CDF
#         
#         $F_{\frac{Y}{X}}(\frac{y}{x})=\dfrac{F_{XY}(x,y)}{F_{X}(x)}$
#         
#         $F_{\frac{X}{Y}}(\frac{x}{y})=\dfrac{F_{XY}(x,y)}{F_{Y}(y)}$
#         
#     
#     $F_{XY}(x,y)=F_{\frac{X}{Y}}(\frac{x}{y})F_{Y}(y)=F_{\frac{Y}{X}}(\frac{y}{x})F_{X}(x)$
#     
#     - if X and Y are independent then $F_{\frac{Y}{X}}(\frac{y}{x})=F_Y(y)$ and $F_{\frac{X}{Y}}(\frac{x}{y})=F_x(x)$
#         
#         $F_{XY}(x,y)=F_{X}(x)F_{Y}(y)$
#         
#         $f_{XY}(x,y)=f_{X}(x)f_{Y}(y)$
#         
#     - joint PDF
#         
#         $f_{XY}(x,y)=\dfrac{\partial^2F_{XY}(x,y)}{\partial x\partial y}$
#         
#         $\displaystyle F_{XY}(x,y)=\int_{-\infty}^x\int_{-\infty}^yf_{XY}(x,y)dxdy$
#         
#         $\displaystyle \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f_{XY}(x,y)dxdy=1$
#         
#         - $\displaystyle P\{x_1\le X\le x_2,y_1\le Y\le y_2\}=\iint_R f_{XY}(x,y)dxdy$
#             
#             $R=\{x_1\le X\le x_2,y_1\le Y\le y_2\} \cap \{ region \space of \space pdf\}$
#             
#     - marginal PDF
#         
#         $\displaystyle f_{X}(x)=\int_{-\infty}^{\infty}f_{XY}(x,y)dy$
#         
#         $\displaystyle f_{Y}(y)=\int_{-\infty}^{\infty}f_{XY}(x,y)dx$
#         
#     - conditional PDF
#         
#         $f_{\frac{Y}{X}}(\frac{y}{x})=\dfrac{f_{XY}(x,y)}{f_{X}(x)}$
#         
#         $f_{\frac{X}{Y}}(\frac{x}{y})=\dfrac{f_{XY}(x,y)}{f_{Y}(y)}$
#         
# - function of 2 RV
#     - $R_{XY}$ correlation
#         
#         $E[XY] = R_{XY}$
#         
#     - $\sigma _{XY}$ cross-covariance
#         
#         $E[(X- \overline {X})(Y- \overline {Y})]=cov(X,Y)=R_{XY} - \mu_X \mu _Y$
#         
#     - $\sigma ^2_{X}$  auto-covariance
#         
#         $E[(X- \overline {X})(X- \overline {X})]=\sigma _X ^2$
#         
#     - `orthogonal`
#         
#         $E[XY] = R_{XY} =0$
#         
#     - `uncorrelated`
#         
#         $cov(X,Y) = \sigma_{XY} = 0$
#         
#         $\rightarrow E[XY] = E[X]E[Y]$
#         
#     - independent
#         
#         $E[X^k Y^r] = E[X^k]E[Y^r]$ 
#         
#         - if 2 RV are independent then they will be uncorrelated always but vice-versa may not be true
#             
#             $cov(X,Y) = \sigma_{XY} = 0$
#             
#             $\rightarrow E[XY] = E[X]E[Y]= \mu_X \mu_Y$
#             
#     - correlation coefficient
#         
#         $\rho = \dfrac{\sigma _{XY}}{\sigma_X \sigma _Y}$
#         
# - maximum and minimum of 2 independent RV
#     
#     $P[max(X,Y)<z] = P[(X<z)(Y<z)]$
#     
#     $P[max(X,Y)>z] = 1-P[max(X,Y)<z]$
#     
#     $P[min(X,Y)>z] = P[(X>z)(Y>z)]$
#     
#     $P[min(X,Y)<z] = 1-P[min(X,Y)>z]$
#     
# - RP
#     
#     $E[X(t_1)X(t_2)] = R_{X(t_1)X(t_2)}$
#     
#     $\sigma _{XX} (t_1, t_2)=R_{XX} (t_1,t_2)-\mu _{X(t_1)}\mu_{X(t_2)}$
#     
#     - types of RP
#         - strict sense stationary (SSSRP)
#             
#             $k^{th}$  order PDF, CDF and PMF are independent of time shifting 
#             
#             $k^{th}$ order joint PDF : $f_{X(t_1)X(t_2)\dots X(t_k)} (x_1,x_2\dots x_k)$
#             
#         - wide sense stationary (WSSRP)
#             
#             SSSRP up-to $2^{nd}$ order
#             
#             $E[X(t)]=\mu_X$
#             
#             $E[X^2(t)] = R_{XX}(0)= constant$
#             
#             $\sigma^2_{X(t)} = constant$ 
#             
#             $E[X(t_1) X(t_2)] = R_{XX} (t_1 \sim t_2)$
#             
#             $E[X(t) X(t+\tau)] = R_{XX} (\tau)= R_{XX} (-\tau)$
#             
#             $cov(X(t_1) X(t_2)) = R_{XX} (t_1 \sim t_2) - \mu_X ^2$ 
#             
#             - $X(t)=Acos(\omega_o t +\phi)$
#                 
#                 $E[X(t)] =0$
#                 
#                 $E[X^2(t)]=\dfrac{A^2}{2}$
#                 
#                 $E[X(t)X(t+\tau)]=\dfrac{A^2}{2}cos(\omega_o \tau)$
#                 
#             - transmission through LTI
#                 
#                 $x(t) \longrightarrow \boxed{h(t)} \longrightarrow  y(t)$
#                 
#                 $R_Y(\tau) =R_X(\tau)*h(\tau)*h(-\tau)$
#                 
#                 $S_{YY}(f) = S_{XX}(f)| H(f) |^2$
#                 
#                 $E[Y(t)] = \mu_X H(s) \Big|_{s=0}$
#                 
#                 $\displaystyle E[Y^2(t)]=\int _{-\infty}^{\infty}S_{YY}(f) df= \int _{-\infty}^{\infty}S_{XX}(f)| H(f) |^2 df$
#                 
#         - ergodic
#             
#             statistical average of RP = time average of RP
#             
#             $\displaystyle\int _{-\infty}^{\infty} X(t) f(x)_{X(t)}dx=\lim \limits_{T\rightarrow \infty} \dfrac{1}{T} \int _{-\frac{1}{T}}^{\frac{1}{T}} X(t) dt$
#             
#             $R_{XX} (\infty) = \mu^2_{X}$ only when X(t) is non-periodic ergodic  
#             
#         - cyclostationary
# - density functions
#     - ESD
#         
#         $G_{XX}(\omega)=|X(\omega)|^2 \space \text{or } G_{XX}(f)=|X(f)|^2 \space$$\dfrac{\text{Joule}}{\text{Hz}}$
#         
#         $R_{XX} (\tau)  \longleftrightarrow G_{XX}(\omega)$
#         
#         $R_{XX}(0) = \text{energy} =\dfrac{1}{2\pi}\displaystyle\int_{-\infty}^{\infty} G_{XX}(\omega) d\omega=\int_{-\infty}^{\infty} G_{XX}(f) df$
#         
#     - PSD
#         
#          $S_{XX}(f)=\lim \limits_{T\rightarrow\infty}\dfrac{1}{T}|X_T(f)|^2 \space$$\dfrac{\text{Watt}}{\text{Hz}}$
#         
#         $R_{XX} (\tau)  \longleftrightarrow S_{XX}(\omega)$
#         
#         $R_{XX}(0) = \text{power}=\dfrac{1}{2\pi}\displaystyle\int_{-\infty}^{\infty} S_{XX}(\omega) d\omega=\int_{-\infty}^{\infty} S_{XX}(f) df$
#         
#     - bandpass density functions
#         
#         $A \cdot X(t) \cos(\omega_c t) \xleftrightarrow{\text{ESD}} \dfrac{A^2}{4}[G_{X}(f-f_c)+G_X(f+f_c)]$
#         
#         $A \cdot X(t) \cos(\omega_c t) \xleftrightarrow{\text{PSD}}  \dfrac{A^2}{4}[S_{X}(f-f_c)+S_X(f+f_c)]$
#         
#         - if $\theta \sim [0,2\pi]$ and $X(t)$ is WSSRP
#             
#             $A \cdot X(t) \cos(\omega_c t+\theta) \xleftrightarrow{\text{PSD}}  \dfrac{A^2}{4}[S_{X}(f-f_c)+S_X(f+f_c)]$  
#             
#             $A \cdot X(t) \cos(\omega_c t+\theta) \xleftrightarrow{\text{ACF}}\dfrac{A^2}{2}R_X (\tau) \cos (\omega_c\tau)$
#             
# 
# ## analog communication
# 
# $voice \rightarrow [300 Hz - 3.5 kHz] \\ audio \rightarrow [20 Hz - 20 kHz] \\video \rightarrow [ 0 Hz - 4.5 MHz]$
# 
# - hilbert transform
#     
#     HT is a non-causal LTI system
#     
#     $\boxed{h(t) =\dfrac{1}{\pi t}}$ 
#     
#     $\hat {x} (t) =x(t)*h(t)$
#     
#     $\boxed{\dfrac{1}{\pi t} \longleftrightarrow-j \cdot\text{sgn}(\omega)}$
#     
#     - $A\cos(\omega_o t+\phi) \longrightarrow \boxed{H(\omega)} \longrightarrow A\sin(\omega_ot+\phi)$
#         
#         $y(t) = A|H(\omega_o)|\cos (\omega_ot+\phi+\angle H(\omega_o))$
#         
#         $|H(\omega_o)|=1$ 
#         
#         $\angle H(\omega_o) = -\dfrac{\pi}{2}$ ,     $\omega _o >0$
#         
#     - for `low pass` signals
#         
#         $\text{HT} [m(t) \cos (\omega _ct)]=m(t)\sin (\omega _ct)$
#         
#         $\text{HT} [m(t) \sin (\omega _ct)]=-m(t)\cos (\omega _ct)$
#         
# - envelope
#     
#     `pre-envelope` : $\boxed{x_+(t) = x(t) +j \hat{x} (t)}$  → calculated for baseband(wideband) and bandpass (narrow band)
#     
#     `complex envelope`: $\boxed{x_c(t) =x_+(t) e^{-j\omega_c t}}$  → calculated for bandpass (narrow band)
#     
# - amplitude modulation
#     - DSB-FC
#         
#         $\mu =\dfrac{|m(t)|_{max}}{A_c}=k_a |m(t)|_{max}$
#         
#         $\boxed{S_{AM}(t)= [A_C + m(t)]\cos (2\pi f_c t)=A_C[1 + k_am(t)]\cos (2\pi f_c t)}$
#         
#         $P_{AM }=P_c +P_{SB}= P_c +\dfrac{P_m}{2}=P_c(1+k_a^2P_m)$ 
#         
#         $\eta =\dfrac{P_{SB}}{P_{AM}}$
#         
#         $P_{AM} = \overline I_{AM}^2(t)= \overline V_{AM}^2(t)$
#         
#         - sinusoidal
#             
#             $P_{AM }=P_c\Big(1+\dfrac{\mu_1^2+\mu_2^2+\dots}{2}\Big)$
#             
#         - triangular
#             
#             half-wave symmetric : $f_o,3f_o,5f_o,7f_o \dots$ 
#             
#             $P_{AM }=P_c\Big(1+\dfrac{\mu^2}{3}\Big)$
#             
#         - square wave
#             
#             $P_{AM }=P_c\Big(1+\mu^2\Big)$
#             
#         - AM modulator
#             - SLD
#                 
#                 
#                 
#                 - BPF
#                     
#                     $2f_m < f_L<f_c-f_m$
#                     
#                     $f_c+f_m<f_H<2f_c$
#                     
#                 
#                 $A_c' =a_o A_c$
#                 
#                 $k_a =\dfrac{2a_1}{a_o}$
#                 
#             - switching modulator
#                 
#                 $A_c' = \dfrac{A_c }{2}$
#                 
#                 $k_a = \dfrac{4}{\pi A_c}$
#                 
#         - AM demodulator
#             - envelop detector
#                 
#                 for detection of peaks : $\tau_c =R_s C << \dfrac{1}{f_c}$
#                 
#                 to avoid diagonal clipping : $\tau_d =R_L C << \dfrac{1}{f_m}$
#                 
#                 to avoid fluctuations or steep discharging : $\tau_d =R_L C >> \dfrac{1}{f_c}$
#                 
#             - synchronous detector (costly)
#                 
#                 received signal is multiplied by locally generated carrier
#                 
#                  $c'(t)= A_c ' cos[(\omega_c + \Delta \omega )t + \Delta \phi]$ and then passed through LPF
#                 
#                 LPF output:  $\frac{A_c A_c '}{2}\cos(\Delta \omega t +\Delta\phi)+\frac{ A_c ' m(t)}{2}\cos(\Delta \omega t +\Delta\phi)$ 
#                 
#             - SLD (impractical method)
#                 
#                 $\Big(\dfrac{S}{I}\Big)_{min} = \dfrac{2}{\mu}$ 
#                 
#     - DSB-SC
#         
#         `suppressed carrier impulse`
#         
#         $\boxed{S_{\text{DSB-SC}}(t)= A_c  m(t)\cos (2\pi f_c t)}$
#         
#         $P = P_{m}P_c = \overline {m^2(t)} \times \dfrac{A_c^2}{2}$
#         
#         `DSB modulator --→ multiplier or product modulator`
#         
#         - DSB-SC modulator
#             - balanced modulator
#                 
#                 $s(t) =2A_c k_a m(t)\cos (2\pi f_c t)$
#              
#                 
#             - ring modulator (product modulating)
#                 
#                 BPF output : $y(t) =\dfrac{4}{\pi}m(t) \cos (\omega _c t)$
#                 
#                 $x(t) \propto m(t) c(t) + m(t)\cos (3\omega_c t)+ m(t)\cos (5\omega_c t)+\dots$ 
#                 
#                 
#                 
#         - synchronous detector
#             
#             output : $y(t) = \dfrac{kA_c A_c '}{2}m(t)$ where k is filter gain
#             
#     - SSB-SC
#         
#         $\boxed{S(t)= \dfrac{A_C}{2} m(t)\cos (2\pi f_c t)\pm \dfrac{A_C}{2}\hat{m}(t)\sin (2\pi f_c t)}$
#         
#         - SSB-SC modulator
#             - phase discrimination
#                 
#                
#                 
#                 - -90 $\degree$  hilbert wideband transform (phase shifter) is not practical
#                     
#                     $\phi = - \tan^{-1} (\omega RC)$                 RC → High , $\omega$  → fixed
#                     
#                     
#                     
#             - frequency discrimination (practical method)
#                 
#                 
#                 
#         - SSB-SC demodulator (synchronous detector)
#             
#             
#             
#     - VSB-SC
#         
#         SSB-SC signal + small portion of adjacent sideband 
#         
# - angle modulation
#     - $|x(t)|_{max}$
#         
#         $$
#         \def\arraystretch{1.5}\begin{array}{c:c} 
#         A\cos (\omega_o t) + B\sin(\omega_o t)& \sqrt{A^2 + B^2} 
#          \\ \hdashline A\cos (\omega_o t) + B\cos(\omega_o t) & |A+B| 
#          \\ \hdashline A\cos (\omega_1 t) + B\cos(\omega_2 t) & |A+B| 
#          \\ \hdashline A\cos (\omega_1 t) + B\sin(\omega_2 t) & <|A+B| \text{ if $A\ne B$} \\         & =|A+B| \text{ if $A = B$} 
#         \end{array}
#         $$
#         
#     
#      $\omega _i (t) =\dfrac{d \theta_i(t)}{dt}$
#     
#     $f _i (t) =\dfrac{1}{2\pi}\dfrac{d \theta_i(t)}{dt} = f_c +\Delta f(t)$
#     
#     $\theta_i(t) = \displaystyle\int_{-\infty}^{t}\omega _i (t) dt=2\pi\int_{-\infty}^{t}f _i (t) dt$
#     
#     $\boxed{s(t) =A_c \cos (\omega _c t +\Delta\phi(t))=A_c \cos (\theta_i(t))}$
#     
#     $|\Delta\omega(t)|_{max} =\Big|\dfrac{d\Delta \phi}{dt} \Big| _{max}$               $|\Delta f(t)|_{max} = \dfrac{1}{2\pi}\Big|\dfrac{d\Delta \phi}{dt} \Big| _{max}$
#     
#     - frequency modulation
#         
#          $\dfrac{d\Delta \phi}{dt} \propto m(t)$                      
#         
#         $`K_f: \frac{rad}{V-sec}`$             $\Delta \omega (t) = K_f m(t)$         $\boxed{\omega_i(t) = \omega_c + K_f  m(t)}$          
#         
#         $`K_f: \frac{Hz}{V}`$                 $\Delta f(t) = K_f m(t)$         $\boxed{f_i(t) = f_c + K_f  m(t) }$
#         
#         modulation index / deviation ratio  $\beta$ 
#         
#         $\boxed{\beta _{FM} = \dfrac{|\Delta\omega(t)|_{max}}{\omega_{max}}=\dfrac{K_f|m(t)|_{max}}{\omega_{max}}}$
#         
#         $\boxed{\beta _{FM} =  \dfrac{|\Delta f(t)|_{max}}{f_{max}}=\dfrac{K_f|m(t)|_{max}}{f_{max}}}$
#         
#     - phase modulation
#         
#          $\Delta \phi\propto m(t)$                      
#         
#         $`K_p: \frac{rad}{V}`$             $\Delta \phi(t)  = K_p m(t)$                $\boxed{\theta_i(t) = \omega_ct + K_p  m(t)}$    
#         
#         modulation index / deviation ratio  $\beta$ 
#         
#         $\boxed{\beta _{PM} =  \dfrac{|\Delta f(t)|_{max}}{f_{max}}=\dfrac{\dfrac{K_p}{2\pi}\Big|\dfrac{dm(t)}{dt}\Big|_{max}}{f_{max}}}$
#         
#     - bessel's function
#         
#         $J_{-n}(\beta) = (-1)^n J_n(\beta)$
#         
#         $\sum \limits_{n=-\infty}^{\infty} J^2_n (\beta) =1$
#         
#         $J_n (\beta) =0$    for $n>>\beta$
#         
#         $J_0 (\beta) =0$    for  $\beta =2.4,5.5,8.6,11.8$
#         
#     
#     $\boxed{s(t) = A_c \cos (\omega_c t+\beta \sin \omega_m t) \equiv A_c \sum \limits_{n=-\infty}^{\infty}J_n (\beta)\cos [2\pi(f_c +nf_m) t]}$
#     
#     - narrow band $(\beta <<1)$
#         
#         $\theta \rightarrow small$ 
#         
#         $\cos\theta \approx 1$
#         
#         $\sin\theta \approx 0$
#         
#         NBFM: $s(t)= A_c \cos (2\pi f_c t) - A_c \beta\sin (2\pi f_m t)\sin(2\pi f_c t)$
#         
#         NBPM: $s(t)= A_c \cos (2\pi f_c t) - A_c \beta\cos (2\pi f_m t)\sin(2\pi f_c t)$
#         
#     - wide band
#         
#         
#     - BW
#         
#         $n^{th}$  order sideband ——→ BW = $n(2f_m)$
#         
#         `carson's rule` : $\boxed{BW=(\beta +1)2f_m}$  for 98% transmission ($\beta+1$ order sideband ) $J_{\beta+1} (\beta) \ne 0$
#         
#     - power
#         
#         $n^{th}$ harmonic : $\overline {s^2 (t)} = P_c [J_o^2(\beta) +2(J_1^2(\beta)+J_2^2(\beta)+\dots +J_n^2(\beta))]$
#         
#         $J_o^2(\beta) +2(J_1^2(\beta)+J_2^2(\beta)+\dots +\infty = 1$
#         
#     - frequency mixer
#         
#         frequency mixer : multiplier followed by BPF
#         
#         BPF → $f_c +f_l$  : upconverter
#         
#         BPF → $f_c \sim f_l$  : downconverter
#         
#     - frequency multiplier or angle multiplier
#         
#         frequency multiplier or angle multiplier : square law device followed by BPF
#         
#         $A\cos(\theta) \longrightarrow \boxed {\times n} \longrightarrow A' \cos(n\theta)$
#         
#     - wide band FM generation
#         - armstrong method (indirect method)
#             
#            
#             
#         - direct method of FM generation
#             
#             
#             
#             VCO : modified hartley oscillator 
#             
#             
#             
#             $L_{eq} =L_1 + L_2$ 
#             
#             $C_{junc} = C_o -km(t)$
#             
#             $\omega _i(t) = \dfrac{1}{\sqrt{LC_{junc}(t)}}$
#             
#             for `VCO as FM generator` : $\boxed{\dfrac{\Delta \omega}{\omega_o}<<<\dfrac{1}{2}}$            $\boxed{\dfrac{\Delta C}{C_o}<<<1}$
#             
#     - FM demodulator
#         
#         $s(t) \rightarrow \boxed{\dfrac{d}{dt}} \xrightarrow{ \text{amplitude  angle modulated}} \boxed{\text {ED}} \longrightarrow || \longrightarrow m(t)$      $|\Delta f_{max}| \le f_c$
#         
#         - practical FM demodulators
#             - PLL
#                 
#                 
#                 
#                 - phase comparator
#                     
#                     multiplier followed by LPF : rejects the frequencies centered at $2f_c$
#                     
#                 - VCO
#                     
#                     sinusoidal waveform generator whose output frequency varies linearly with input message signal 
#                     
#                     frequency of VCO → $f_c$
#                     
#                 
#                 phase lock : $|H(f)| \rightarrow \infty$          $v(t) = \dfrac{k_f}{k_v} m(t)$
#                 
#                 lock mode : $f_{s(t)} = f_{v(t)}$
#                 
#                 capture mode : $\phi_e (t) \rightarrow 0$
#                 
#                 $\text{lock range} \ge \text{capture range}$
