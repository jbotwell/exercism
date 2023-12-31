using System;

enum AccountType { Guest, User, Moderator }

[Flags]
enum Permission : byte {
  Read = 0b1,
  Write = 0b10,
  Delete = 0b100,
  All = Read | Write | Delete,
  None = 0b0,
}

static class Permissions {
  public static Permission Default(AccountType accountType) {
    return accountType switch { AccountType.Guest => Permission.Read,
                                AccountType.User =>
                                    Permission.Read | Permission.Write,
                                AccountType.Moderator => Permission.All,
                                _ => Permission.None };
  }

  public static Permission Grant(Permission current, Permission grant) {
    return current | grant;
  }

  public static Permission Revoke(Permission current, Permission revoke) {
    return current & ~revoke;
  }

  public static bool Check(Permission current, Permission check) {
    return current.HasFlag(check);
  }
}
