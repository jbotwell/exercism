using System;

static class LogLine {
  public static string Message(string logLine) {
    string[] bothSides = logLine.Split(':');
    string rightSide = bothSides[1];

    return rightSide.Trim();
  }

  public static string LogLevel(string logLine) {
    string[] bothSides = logLine.Split(':');
    string leftSide = bothSides[0];
    char[] brackets = { '[', ']' };

    return leftSide.Trim(brackets).ToLower();
  }

  public static string Reformat(string logLine) {
    var message = LogLine.Message(logLine);
    var level = LogLine.LogLevel(logLine);

    return $"{message} ({level})";
  }
}
