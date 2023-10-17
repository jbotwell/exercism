using System;

static class AssemblyLine {
  static int cars_per_level = 221;

  public static double SuccessRate(int speed) {
    if (speed == 0) {
      return 0;
    } else if (speed <= 4) {
      return 1;
    } else if (speed <= 8) {
      return 0.9;
    } else if (speed == 9) {
      return 0.8;
    } else {
      return 0.77;
    }
  }

  public static double ProductionRatePerHour(int speed) {
    return (speed * cars_per_level * AssemblyLine.SuccessRate(speed));
  }

  public static int WorkingItemsPerMinute(int speed) {
    return (int)AssemblyLine.ProductionRatePerHour(speed) / 60;
  }
}
