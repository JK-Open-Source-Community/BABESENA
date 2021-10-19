#!/usr/bin/env python
# coding: utf-8

# # Mathematics 

# ```{dropdown} Calculus
# 
# $\int udv = u\cdot v-\int du\cdot v$
# 
# $\displaystyle\Gamma(n)=\int_{0}^{\infty}x^{n-1}e^{-x}dx=(n-1)!$
# 
# - $cos ^2(i\theta)+sin^2(i\theta) = cosh^2(\theta)- sinh^2(\theta)$
#     
#     $cos(i\theta) = cosh(\theta)$  
#     
#     $sin(i\theta) = i\cdot sinh(\theta)$  
#     
#     $sin(x) = \dfrac{e^{jx}-e^{-jx}}{2j}$
#     
#     $sinh(x) = \dfrac{e^{x}-e^{-x}}{2}$
#     
# 
# $2\cos \alpha \cos \beta= \cos(\alpha-\beta)+\cos(\alpha+\beta)$
# 
# $2\sin \alpha \cos \beta=  \sin(\alpha+\beta)+\sin(\alpha-\beta)$ 
# 
# $2\sin \alpha \sin \beta =  \cos(\alpha-\beta)-\cos(\alpha+\beta)$ 
# 
# - $\dfrac{sin(x)}{x}$
#     
#     zero-crossovers : $x=K \pi$, $K \in I - \{0\}$ 
#     
# - $e^{-1}$
#     
#     =0.3678
# 
# ```

# ```{dropdown} Complex Analysis
# $e^{j2\pi k}e^{j\theta} = e^{j\theta}$
# 
# $i^n+i^{n+1}+i^{n+2}+i^{n+3}=0$          
# 
# - root of unity
#     
#     sum of 'n' roots of unity = 0
#     
#     product of 'n' roots of unity = $(-1)^{n-1}$ 
#     
# - CR equation
#     
#     $f'(z_o) = u_x +i v_x=v_y-iu_y=e^{-i\theta}(u_r + iv_r)$
#     
#     - cartesian
#         
#         $u_x=v_y \\ v_x = -u_y$  
#         
#     - polar
#         
#         $u_r=\frac{1}{r}v_{\theta} \\ v_r=-\frac{1}{r}u_{\theta}$
#         
# - milne thompson method
# - residue theorem
#     
#     `singular point` → point where complex function becomes non-analytic
#     
#     laurent series around singularity: $f(z) = \sum \limits _{n=0}^{\infty} a_{n} (z-a)^{n} +\sum \limits _{m=1}^{\infty} b_{-m} (z-a)^{-m}$ 
#     
#     $\displaystyle \int_C f (z) dz = 2 \pi i \cdot\text{(sum of residues at the singular points within $z_o$ )}$
#     
#     $\text{residue}(f(z_o))=\text{coefficient of $(z-a)^{-1}$}=\lim \limits_{z\rightarrow z_o} \dfrac{1}{(n-1)!}\Big[ \dfrac{d^{n-1}}{dz^{n-1}}[(z-z_o)^nf(z)]\Big]$
# 
# ```

# ``` {dropdown} ODE 
# order → highest order derivative 
# 
# degree → degree of highest order differential coefficient provided equation is `polynomial in all differential coefficients`   
# 
# - integration and differentiation
#     
#     $\displaystyle \int \dfrac{1}{\sqrt{x^2+a^2}} dx = \sin^{-1} \Big(\frac{x}{a}\Big) + C$
#     
#     $\displaystyle \int \dfrac{1}{\sqrt{x^2-a^2}} dx = \cos^{-1} \Big(\frac{x}{a}\Big) + C$
#     
#     $\displaystyle \int \dfrac{1}{x^2-a^2} dx = \dfrac{1}{a}\tan^{-1} \Big(\frac{x}{a}\Big) + C$
#     
# - variable separable
#     
#     $f(x) dx +g(y)dy =0$
#     
# - exact differential equation
#     
#     ${M\left( {x,y} \right)dx + N\left( {x,y} \right)dy }= 0$
#     
#     $\dfrac{{\partial M}}{{\partial x}} = \dfrac{{\partial N}}{{\partial y}}$
#     
#     $\displaystyle\int dv = \int_\text{y = const} Mdx +  \int_\text{\text{independent of x}} Ndy$
#     
# - $\dfrac{dy}{dx}+p(x)y=r(x)$
#     
#     $\displaystyle y e^{-\int p(x) dx }  =  \Big[\int r(x)e^{\int p(x) dx } dx +C \Big]$  
#     
# - LDE of higher order
#     
#     $y=CF+PI$
#     
#     - CF
#         
#         CF is solution of $(D^n +a_1D^{n-1}+\dots +k_nD^0)y=0$
#         
#         if roots are `real and distinct` : $y =c_1e^{m_1x}+c_2e^{m_2x}$
#         
#         if roots are `real and equal` : $y =(c_1+c_2x)e^{mx}$ 
#         
#         if roots are `complex conjugate`: $y =(c_1\cos(\beta x)+c_2sin(\beta x))e^{\alpha x}$ 
#         
#     - PI
#         
#         PI is solution of $(D^n +a_1D^{n-1}+\dots +k_nD^0)y=x$
# 
# ```

# ```{dropdown} Linear Algebra
# - rank
#     
#     atleast one minor of A of order r doesn't vanish → rank(A) = r
#     
# - eigen vectors
#     
#     $[A] [X] =\lambda [X]$
# ```

# ```{dropdown} Probability
# - binomial distribution
#     
#     $\mu = np$
#     
#     $\sigma ^2 = npq$
#     
#     $\displaystyle P(r)= \binom{n}{r} p^r q^{n-r}$
# ```
