using System;
using System.Collections.Generic;

public static class DialingCodes {
  public static Dictionary<int, string> GetEmptyDictionary() {
    return new Dictionary<int, string> {};
  }

  public static Dictionary<int, string> GetExistingDictionary() {
    return new Dictionary<int, string> {
      { 1, "United States of America" },
      { 55, "Brazil" },
      { 91, "India" },
    };
  }

  public static Dictionary<int, string>
  AddCountryToEmptyDictionary(int countryCode, string countryName) {
    var myDict = GetEmptyDictionary();
    myDict.Add(countryCode, countryName);
    return myDict;
  }

  public static Dictionary<int, string>
  AddCountryToExistingDictionary(Dictionary<int, string> existingDictionary,
                                 int countryCode, string countryName) {
    existingDictionary.Add(countryCode, countryName);
    return existingDictionary;
  }

  public static string
  GetCountryNameFromDictionary(Dictionary<int, string> existingDictionary,
                               int countryCode) {
    return existingDictionary.GetValueOrDefault(countryCode, string.Empty);
  }

  public static bool CheckCodeExists(Dictionary<int, string> existingDictionary,
                                     int countryCode) {
    return existingDictionary.ContainsKey(countryCode);
  }

  public static Dictionary<int, string>
  UpdateDictionary(Dictionary<int, string> existingDictionary, int countryCode,
                   string countryName) {
    if (existingDictionary.ContainsKey(countryCode)) {
      existingDictionary[countryCode] = countryName;
    }
    return existingDictionary;
  }

  public static Dictionary<int, string>
  RemoveCountryFromDictionary(Dictionary<int, string> existingDictionary,
                              int countryCode) {
    if (existingDictionary.ContainsKey(countryCode)) {
      existingDictionary.Remove(countryCode);
    }
    return existingDictionary;
  }

  public static string
  FindLongestCountryName(Dictionary<int, string> existingDictionary) {
    int length = 0;
    string longest = "";
    foreach (string country in existingDictionary.Values) {
      if (country.Length > length) {
        length = country.Length;
        longest = country;
      }
    }

    return longest;
  }
}
