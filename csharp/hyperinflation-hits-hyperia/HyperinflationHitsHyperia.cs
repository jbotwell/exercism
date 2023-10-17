using System;

public static class CentralBank {
  public static string DisplayDenomination(long @base, long multiplier) {
    long denom;
    try {
      checked { denom = @base * multiplier; }
    } catch (OverflowException) {
      return "*** Too Big ***";
    }

    return denom.ToString();
  }

  public static string DisplayGDP(float @base, float multiplier) {
    float gdp;
    checked { gdp = @base * multiplier; }
    if (gdp == float.PositiveInfinity) {
      return "*** Too Big ***";
    }

    return gdp.ToString();
  }

  public static string DisplayChiefEconomistSalary(decimal salaryBase,
                                                   decimal multiplier) {
    decimal salary;
    try {
      checked { salary = salaryBase * multiplier; }
    } catch (OverflowException) {
      return "*** Much Too Big ***";
    }

    return salary.ToString();
  }
}
