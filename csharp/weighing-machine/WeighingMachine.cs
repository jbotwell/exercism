using System;

class WeighingMachine {

  public WeighingMachine(int precision) => Precision = precision;

  double _weight;

  public int Precision { get; }

  public double Weight {
    get { return _weight; }
    set {
      if (value < 0) {
        throw new ArgumentOutOfRangeException("weight cannot be less than 0");
      } else {
        _weight = value;
      }
    }
  }

  public string DisplayWeight {
    get { return (Weight - TareAdjustment).ToString("F" + Precision) + " kg"; }
  }

  public double TareAdjustment { get; set; } = 5;
}
