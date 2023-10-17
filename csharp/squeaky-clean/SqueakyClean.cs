using System;
using System.Linq;

public static class Identifier {
  public static string Clean(string identifier) {
    return SpaceToUnderscore(OmitGreekLowercase(
        OmitNonLetters(KebabToCamel(CtrlToCtrl(identifier)))));
  }

  private static string SpaceToUnderscore(string identifier) {
    return identifier.Replace(" ", "_");
  }

  private static string CtrlToCtrl(string identifier) {
    return identifier.Replace("\0", "CTRL");
  }

  private static string KebabToCamel(string identifier) {
    string[] splitOnDash = identifier.Split('-');
    string camelCaseId = splitOnDash[0];

    for (int i = 1; i < splitOnDash.Length; i++) {
      string piece = splitOnDash[i];
      string capitalizedPiece = char.ToUpper(piece[0]) + piece.Substring(1);
      camelCaseId += capitalizedPiece;
    }

    return camelCaseId;
  }

  private static string OmitNonLetters(string identifier) {
    return new string(
        identifier.Where(c => char.IsLetter(c) || c == ' ').ToArray());
  }

  private static string OmitGreekLowercase(string identifier) {
    return new string(identifier.Where(c => c < 'α' || c > 'ω').ToArray());
  }
}
