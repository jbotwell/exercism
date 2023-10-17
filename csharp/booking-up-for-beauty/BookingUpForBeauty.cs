using System;
using System.Globalization;

static class Appointment {
  public static DateTime Schedule(string appointmentDateDescription) {
    return DateTime.Parse(appointmentDateDescription);
  }

  public static bool HasPassed(DateTime appointmentDate) {
    return appointmentDate < DateTime.Now;
  }

  public static bool IsAfternoonAppointment(DateTime appointmentDate) {
    return appointmentDate.Hour >= 12 && appointmentDate.Hour < 18;
  }

  public static string Description(DateTime appointmentDate) {
    var apptString = appointmentDate.ToString(
        "M/d/yyyy h:mm:ss tt", CultureInfo.GetCultureInfo("en-US"));
    return $"You have an appointment on {apptString}.";
  }

  public static DateTime AnniversaryDate() {
    return new DateTime(DateTime.Now.Year, 9, 15, 0, 0, 0);
  }
}