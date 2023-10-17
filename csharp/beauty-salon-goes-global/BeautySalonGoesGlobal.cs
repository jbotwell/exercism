using System;
using System.Globalization;

public enum Location { NewYork, London, Paris }

public enum AlertLevel { Early, Standard, Late }

public static class Appointment {
  public static DateTime ShowLocalTime(DateTime dtUtc) {
    return dtUtc.ToLocalTime();
  }

  public static DateTime Schedule(string appointmentDateDescription,
                                  Location location) {
    DateTime appt = DateTime.Parse(appointmentDateDescription);
    TimeZoneInfo local = GetTZInfo(location);
    TimeZoneInfo utc = TimeZoneInfo.Utc;

    return TimeZoneInfo.ConvertTime(appt, local, utc);
  }

  public static DateTime GetAlertTime(DateTime appointment,
                                      AlertLevel alertLevel) {
    int minBefore = alertLevel switch {
      AlertLevel.Early => 1440,
      AlertLevel.Standard => 105,
      AlertLevel.Late => 30,
    };
    return appointment.AddMinutes(-1 * minBefore);
  }

  public static bool HasDaylightSavingChanged(DateTime dt, Location location) {
    var tzInfo = GetTZInfo(location);
    var weekAgo = dt.AddDays(-7);
    TimeSpan currentOffset = tzInfo.GetUtcOffset(dt);
    TimeSpan pastOffset = tzInfo.GetUtcOffset(weekAgo);
    return currentOffset != pastOffset;
  }

  public static DateTime NormalizeDateTime(string dtStr, Location location) {
    string format = location switch { Location.NewYork => "MM/dd/yyyy HH:mm:ss",
                                      Location.London => "dd/MM/yyyy HH:mm:ss",
                                      Location.Paris => "dd/MM/yyyy HH:mm:ss" };

    try {
      return DateTime.ParseExact(dtStr, format, null);
    } catch (FormatException) {
      return DateTime.MinValue;
    }
  }

  private static TimeZoneInfo GetTZInfo(Location city) {
    string tzCity = city switch {
      Location.NewYork => "America/New_York",
      Location.London => "Europe/London",
      Location.Paris => "Europe/Paris",
    };

    return TimeZoneInfo.FindSystemTimeZoneById(tzCity);
  }
}
