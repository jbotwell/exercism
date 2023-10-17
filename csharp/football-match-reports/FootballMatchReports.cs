using System;

public static class PlayAnalyzer {
  public static string AnalyzeOnField(int shirtNum) {
    return shirtNum switch {
      1 => "goalie",
      2 => "left back",
      3 => "center back",
      4 => "center back",
      5 => "right back",
      6 => "midfielder",
      7 => "midfielder",
      8 => "midfielder",
      9 => "left wing",
      10 => "striker",
      11 => "right wing",
      _ => throw new ArgumentOutOfRangeException(
          "Shirt number should be between 1 and 11.")
    };
  }

  public static string AnalyzeOffField(object report) {
    return report switch {
      int n => $"There are {n} supporters at the match.",
      string s => s,
      Injury i => $"Oh no! {i.GetDescription()} Medics are on the field.",
      Incident i => i.GetDescription(),
      Manager m when m.Club == null => m.Name,
      Manager m => $"{m.Name} ({m.Club})",
      _ => throw new ArgumentException("Bad argument.")
    };
  }
}
