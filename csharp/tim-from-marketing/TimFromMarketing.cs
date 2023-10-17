using System;

static class Badge {
  public static string Print(int? id, string name, string? department) {
    string first_part;
    if (id is not null) {
      first_part = $"[{id}] - ";
    } else {
      first_part = "";
    }

    department ??= "OWNER";

    return $"{first_part}{name} - {department.ToUpper()}";
  }
}
