using System;

public static class PhoneNumber {
  public static (bool IsNewYork, bool IsFake, string LocalNumber)
      Analyze(string phoneNumber) {
    var pieces = phoneNumber.Split("-");
    var isNewYork = pieces[0] == "212";
    var isFake = pieces[1] == "555";
    return (isNewYork, isFake, pieces[2]);
  }

  public static bool IsFake((bool IsNewYork, bool IsFake,
                             string LocalNumber)phoneNumberInfo) {
    return phoneNumberInfo.IsFake;
  }
}
