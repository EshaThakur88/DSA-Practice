"""Example 1:
Input: N1 = 9, N2 = 12

Output: 3
Explanation:
Factors of 9: 1, 3, 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3
Greatest common factor: 3 (GCD)

Example 2:
Input: N1 = 20, N2 = 15

Output: 5
Explanation:
Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 15: 1, 3, 5, 15c
Common Factors: 1, 5
Greatest common factor: 5 (GCD)"""

# ✅ BEST & INTERVIEW-READY SOLUTION (Euclidean Algorithm)

def compute(N1, N2):
  factors_1 = []
  factors_2 = []
  for i in range(1, (N1//2)+1):
    if N1%i==0:
      factors_1.append(i)
  factors_1.append(N1)
  for i in range(1, (N2//2)+1):
    if N2%i==0:
      factors_2.append(i)
  factors_2.append(N2)

  common_factors = set(factors_1) & set(factors_2)
  gcd=1
  # for i in common_factors:
  #   gcd=gcd*i

  return max(common_factors)



def main():
  print(f"Output: {compute(20, 12)}")  # Expected output: 3

main()