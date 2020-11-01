# Null hypothesis ->        function 'L(x)' correctly describes the relationship between the mass weight and the
#                           distance change in the equilibrium position
# Alternative hypothesis -> function 'L(x)' does not correctly describe the relationship between the mass weight and
#                           the distance change in the equilibrium position

x = [0, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300]
y = [0, 0.08, 0.165, 0.245, 0.325, 0.41, 0.49]

# Expected value function
def L(x):
    return 2.1171428571428574 * x + -0.0015714285714286125


# chi-square statistic(X^2) is the sum of all the trials' ((observed - expected)^2)/expected
chi_square_statistic = 0
for i in range(len(x) - 1):
    chi_square_statistic += ((y[i] - L(x[i])) ** 2) / L(x[i])
print(chi_square_statistic)

# With a statistical significance of 0.05 and a Degrees of Freedom of 6, the critical chi-square value is 12.59
chi_square_statistic_critical = 12.59

if (chi_square_statistic < chi_square_statistic_critical):
    print("Since {} < {} , the null hypothesis is correct, there is no statistical significance so reject alternative "
          "hypotheses.".format(chi_square_statistic, chi_square_statistic_critical))
else:
    print("Since {} > {} , the null hypothesis is rejected, there is a statistical significance so should test for "
          "alternative hypotheses.".format(chi_square_statistic, chi_square_statistic_critical))
