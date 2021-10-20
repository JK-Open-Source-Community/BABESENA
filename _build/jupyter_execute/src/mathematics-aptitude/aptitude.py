#!/usr/bin/env python
# coding: utf-8

# # Aptitude

# ## Percentage

# ````{dropdown} percentage change
# 
# :::{dropdown} by what percent is x more/less `than` y
# $\%=\dfrac{x-y}{y}\times 100$ 
# ::: 
# 
# ::::{dropdown} 15% increase in x or 15% more than x
# 
# ```{dropdown} fundamental
#             
# x + (15% of x )
#             
# $=x + (\frac{15}{100} \times x )$
#             
# $=x+0.15x$
#             
# $=1.15x$
# ```            
#             
# ```{dropdown} quick
#             
# $(1+0.15)x$
#             
# $1.15x$
# ```
# ::::
# 
# ::::{dropdown} 15% decrease in x or 15% less than x
# 
# ```{dropdown} fundamental
#             
# x - (15% of x )
#             
# $=x - (\frac{15}{100} \times x )$
#             
# $=x-0.15x$
#             
# $=0.85x$
# ```   
# 
# ```{dropdown} quick
#             
# $(1-0.15)x$
#             
# $=0.85x$
# ```
# ::::
#         
# ::::{dropdown} 200% increase in x or 200% more than x
# 
# ```{dropdown} fundamental
#             
# x + (200% of x )
#             
# $=x + (\frac{200}{100} \times x )$
#             
# $=x+2x$
#             
# $=3x$
# ```
# 
# ```{dropdown} quick
# $(1+2)x$
# $=3x$
# ```
# 
# ::::
# ````

# 
# ````{dropdown} successive percentage
#     
# $$x \xrightarrow{a\% \uparrow } (1+\frac{a}{100} )x \xrightarrow{b\% \uparrow } (1+\frac{b}{100} )(1+\frac{a}{100} )x \xrightarrow{c\% \uparrow } (1+\frac{c}{100} )(1+\frac{b}{100} )(1+\frac{a}{100} )x \cdots$$
#     
# $$x \xrightarrow{a\% \uparrow } (1+a\% )x \xrightarrow{b\% \uparrow} (1+b\% )(1+a\% )x \xrightarrow{c\% \uparrow} (1+c\% )(1+b\% )(1+a\% )x \cdots$$
#     
# $$x \xrightarrow{a\% \downarrow } (1-\frac{a}{100} )x \xrightarrow{b\% \downarrow} (1-\frac{b}{100} )(1-\frac{a}{100} )x \xrightarrow{c\% \downarrow} (1-\frac{c}{100} )(1-\frac{b}{100} )(1-\frac{a}{100} )x \cdots$$
#     
# $$x \xrightarrow{a\% \downarrow } (1-a\% )x \xrightarrow{b\% \downarrow} (1-b\% )(1-a\% )x \xrightarrow{c\% \downarrow} (1-c\% )(1-b\% )(1-a\% )x \cdots$$
# ````
# 
# ```{dropdown} x % of y
# 
# $$\dfrac{x}{100} \times y$$
# 
# ```
# 
# ````{dropdown} examples
# 
# ```{dropdown} % increase
#         
# 1.1x = 10% increase in x 
#         
# 1.2x = 20% increase in x
# ```
# 
# ```{dropdown} % decrease
#         
# 0.8x = 20% decrease in x
#         
# 0.2X = 80% decrease in x
# 
# ```
# 
# ````

# ## Logarithms
# 
# - if $log_a(x)=y$  then, x=?
#     
#     $\boxed{x = a^y}$
#     
#     $log_a(x) \ne x \cdot log(a)$
#     
# - $log_a(m \times n)$
#     
#     $= log_a(m) + log_a(n)$ 
#     
#     $\neq log_a(m + n)$
#     
# - $log_a(\frac{m}{n})$
#     
#     $= log_a(m)- log_a(n)$
#     
#     $\neq log_a(m-n)$
#     
# - $log_a(x^m)$
#     
#     $= m\cdot log_a(x)$
#     
# - $log_{a^n}(x)$
#     
#     $=\frac{1}{n}log_a(x)$ 
#     
# - $log_a(1)$
#     
#     $=0$
#     
# - $log_a(a)$
#     
#     $=1$
#     
# - $a^{log_a(x)}$
#     
#     $=x$
#     
# - $a^{\frac{1}{n}}$
#     
#     $a^{\frac{1}{n}} = \sqrt[n]{a}$ = $n^{th} \text{ root of a}$ 
#     
#     $a^{\frac{1}{2}} = \sqrt[2]{a}$  
#     
#     $a^{\frac{1}{3}} = \sqrt[3]{a}$

# ## SI-CI
# 
# - CI
#     
#     $\text{amount}=P(1+\frac{r}{100} )^n$
#     
#     $\text{CI}=A-I= P(1+\frac{r}{100} )^n -P$
#     
#     $\text{CI}\ne P(1+\frac{r}{100} )^n$
#     
#     CI = CI in this year - CI of previous Year 
#     
# - Difference CI-SI for 2 years
#     
#     $CI-SI=\color {green}P(\frac{r}{100})^2$
#     
# - Difference CI-SI for 3 years
#     
#     $CI-SI=\color {green}P(\frac{r}{100})^3 + 3P(\frac{r}{100})^2$

# ## Permutation And Combination
# 
# - Permutation
#     
#     $^nP_r=^nC_r\times R!$
#     
# - $^nC_{r-1}+^nC_r=^{n+1}C_r$
# - $\binom{n}{r}$
#     
#     $=\frac{n!}{(n-r)!r!}$
#     
# - properties of $\binom{n}{r}$
#     
#     $\binom{n}{r}=\binom{n}{n-r}$
#     
#     $\binom{n}{0}=1$
#     
#     $\binom{n}{1}=n$
#     
# - $(a + b)^n$
#     
#     $= \binom{n}{0}a^{n}b^{0} +\binom{n}{1}a^{n-1}b^{1}+\binom{n}{2}a^{n-2}b^{2}+...+\binom{n}{n-1}a^{1}b^{n-1}+\binom{n}{n}a^{0}b^{n}$

# ## Number System
# 
# - $N = a^p b^q  c^r$
#     - number of factors of N
#         
#         =(p + 1) (q + 1) (r + 1)
#         
#     - can be expressed as the product of two factors in
#         
#         1/2 {(p + 1) (q + 1) (r + 1)} ways
#         
#     - if N is a perfect square, it can be expressed
#         - as a product of two DIFFERENT factors in
#             
#             1/2 {(p + 1) (q + 1) (r + 1) - 1 } ways
#             
#         - as a product of two factors in
#             
#              1/2 {(p + 1) (q + 1) (r + 1)  +1} ways
#             
# - LCM × HCF
#     
#     = product of two numbers
#     
# - $\sum\limits_{k=1}^{n} k=1^1 + 2^1 + 3^1 + … + n^1$
#     
#     $= \dfrac{n(n + 1)}{2}$
#     
# - $\sum\limits_{k=1}^{n} k^2=1² + 2² + 3² + … + n²$
#     
#     $= \dfrac{n ( n + 1 ) (2n + 1)} { 6}$
#     
# - $1³ + 2³ + 3³ + …+ n³$
#     
#      $= \Big(\dfrac{n(n + 1)}{ 2}\Big)^2$
