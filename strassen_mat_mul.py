
import numpy as np
import re

A_whole = np.array([
	[0, 1, 2, 3],
	[1, 2, -1, 2],
	[3, -1, 3, 1],
	[2, 1, 3, 0]
])

B_whole = np.array([
	[2, -3, -1, 0],
	[0, 3, 2, 4],
	[3, 2, 0, 1],
	[0, 3, 2, 4]
])


def segment(arr):
	A11 = arr[:2, :2]
	A21 = arr[2:, :2]
	A12 = arr[:2, 2:]
	A22 = arr[2:, 2:]
	
	return ((A11, A12), (A21, A22))


A = segment(A_whole)
B = segment(B_whole)

P_vals = """P1 = A[0][0] @ (B[0][1] - B[1][1])
P2 = (A[0][0] + A[0][1]) @ B[1][1]
P3 = (A[1][0] + A[1][1]) @ B[0][0]
P4 = A[1][1] @ (B[1][0] - B[0][0])
P5 = (A[0][0] + A[1][1]) @ (B[0][0] + B[1][1])
P6 = (A[0][1] - A[1][1]) @ (B[1][0] + B[1][1])
P7 = (A[0][0] - A[1][0]) @ (B[0][0] + B[0][1])"""

exec(P_vals)

print(P5)

C11 = P5 + P4 - P2 + P6
C12 = P1 + P2
C21 = P3 + P4
C22 = P5 + P1 - P3 - P7


C1 = np.concatenate((C11, C12), axis=1)
C2 = np.concatenate((C21, C22), axis=1)
C = np.concatenate((C1, C2), axis=0)


def latex_line(string):
	bases = {"A": A, "B": B}
	mats = re.findall("(A|B)\[(0|1)\]\[(0|1)\]", string)
	
	exp = string.split("=")[1]
	string += " = " + latex_matrix(eval(exp))
	
	string = string.replace("@", "\cdot")
	for pat in mats:
		recon = f"{pat[0]}[{pat[1]}][{pat[2]}]"
		latex_rep = latex_matrix(bases[pat[0]][int(pat[1])][int(pat[2])])
		string = string.replace(recon, latex_rep)
	
	string = re.sub("P([0-9])", "P_{\\1}", string)

	string = f"\\[\n{string}\n\\]"
	
	return string



def latex_matrix(arr):
	s = ""
	for row in arr.tolist():
		s += " & ".join(map(str, row)) + "\\\\\n"
	return f"\\begin{{bmatrix}}\n{s}\\end{{bmatrix}}"


#for line in P_vals.split("\n"):
#	print(latex_line(line))

"""
print(latex_matrix(P1))
print(latex_matrix(P2))
print(latex_matrix(P3))
print(latex_matrix(P4))
print(latex_matrix(P5))
print(latex_matrix(P6))
print(latex_matrix(P7))
"""


print(latex_matrix(C11))
print(latex_matrix(C12))
print(latex_matrix(C21))
print(latex_matrix(C22))
print("")
print(latex_matrix(C))








