using System;

public static class LogAnalysis {

  public static string SubstringAfter(this string str, string after) {
    return str.Substring(str.IndexOf(after) + after.Length);
  }

  public static string SubstringBetween(this string str, string start,
                                        string finish) {
    var start_index = str.IndexOf(start) + start.Length;
    var substring_length = str.IndexOf(finish) - start_index;
    return str.Substring(start_index, substring_length);
  }

  public static string Message(this string str) {
    return str.SubstringAfter(":").Trim();
  }

  public static string LogLevel(this string str) {
    return str.SubstringBetween("[", "]");
  }
}
