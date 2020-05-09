C11, C12, C13, C14, C15, C16, C22, C23, C24, C25, C26, C33, C34, C35, C36, C44, C45, C46, C55, C56, C66 = symbols('C11 C12 C13 C14 C15 C16 C22 C23 C24 C25 C26 C33 C34 C35 C36 C44 C45 C46 C55 C56 C66')
c11, c12, c13, c14, c15, c16, c22, c23, c24, c25, c26, c33, c34, c35, c36, c44, c45, c46, c55, c56, c66 = symbols('c11 c12 c13 c14 c15 c16 c22 c23 c24 c25 c26 c33 c34 c35 c36 c44 c45 c46 c55 c56 c66')

C11=c11
C12=c12
C13=c13
C14=c14
C15=c15
C16=c16
C22=c22
C23=c23
C24=c24
C25=c25
C26=c26
C33=c33
C34=c34
C35=c35
C36=c36
C44=c44
C45=c45
C46=c46
C55=c55
C56=c56
C66=c66

C_0 = Matrix([[C11,C12,C13,C14,C15,C16],[C12,C22,C23,C24,C25,C26],[C13,C23,C33,C34,C35,C36],[C14,C24,C34,C44,C45,C46],[C15,C25,C35,C45,C55,C56],[C16,C26,C36,C46,C56,C66]])

C11=c11
C12=c13
C13=c12
C14=c15
C15=-c14
C16=-c16
C22=c33
C23=c23
C24=c35
C25=-c34
C26=-c36
C33=c22
C34=c25
C35=-c24
C36=-c26
C44=c55
C45=-c45
C46=-c56
C55=c44
C56=c46
C66=c66

C_x_90 = Matrix([[C11,C12,C13,C14,C15,C16],[C12,C22,C23,C24,C25,C26],[C13,C23,C33,C34,C35,C36],[C14,C24,C34,C44,C45,C46],[C15,C25,C35,C45,C55,C56],[C16,C26,C36,C46,C56,C66]])

C11=c33
C12=c23
C13=c13
C14=-c36
C15=-c35
C16=c34
C22=c22
C23=c12
C24=-c26
C25=-c25
C26=c24
C33=c11
C34=-c16
C35=-c15
C36=c14
C44=c66
C45=c56
C46=-c46
C55=c55
C56=-c45
C66=c44

C_y_90 = Matrix([[C11,C12,C13,C14,C15,C16],[C12,C22,C23,C24,C25,C26],[C13,C23,C33,C34,C35,C36],[C14,C24,C34,C44,C45,C46],[C15,C25,C35,C45,C55,C56],[C16,C26,C36,C46,C56,C66]])

C11=c22
C12=c12
C13=c23
C14=-c24
C15=c26
C16=-c25
C22=c11
C23=c13
C24=-c14
C25=c16
C26=-c15
C33=c33
C34=-c34
C35=c36
C36=-c35
C44=c44
C45=-c46
C46=c45
C55=c66
C56=-c56
C66=c55

C_z_90 = Matrix([[C11,C12,C13,C14,C15,C16],[C12,C22,C23,C24,C25,C26],[C13,C23,C33,C34,C35,C36],[C14,C24,C34,C44,C45,C46],[C15,C25,C35,C45,C55,C56],[C16,C26,C36,C46,C56,C66]])

display("C_0 =")
display(C_0)
print("")
display()
display("C_i_pi/2 =")
display(C_x_90)
print("")
display("C_j_pi/2 =")
display(C_y_90)
print("")
display("C_k_pi/2 =")
display(C_z_90)