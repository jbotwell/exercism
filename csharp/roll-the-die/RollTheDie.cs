using System;

public class Player {
  public int RollDie() {
    return new System.Random().Next(1, 19);
  }

  public double GenerateSpellStrength() {
    return new System.Random().NextDouble() * 100;
  }
}
