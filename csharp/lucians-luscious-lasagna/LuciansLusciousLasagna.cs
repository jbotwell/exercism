class Lasagna {
  static int min_per_layer = 2;

  public int ExpectedMinutesInOven() { return 40; }

  public int RemainingMinutesInOven(int elapsedTime) {
    return this.ExpectedMinutesInOven() - elapsedTime;
  }

  public int PreparationTimeInMinutes(int layers) {
    return Lasagna.min_per_layer * layers;
  }

  public int ElapsedTimeInMinutes(int layers, int timeInOven) {
    return layers * Lasagna.min_per_layer + timeInOven;
  }
}
