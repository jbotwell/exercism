using System.Linq;

class BirdCount {
  private int[] birdsPerDay;

  public BirdCount(int[] birdsPerDay) { this.birdsPerDay = birdsPerDay; }

  public static int[] LastWeek() {
    int[] lastWeekCounts = { 0, 2, 5, 3, 7, 8, 4 };
    return lastWeekCounts;
  }

  public int Today() { return this.birdsPerDay.Last(); }

  public void IncrementTodaysCount() {
    int birdsLength = this.birdsPerDay.Length;
    this.birdsPerDay[birdsLength - 1] += 1;
  }

  public bool HasDayWithoutBirds() { return this.birdsPerDay.Any(n => n == 0); }

  public int CountForFirstDays(int numberOfDays) {
    int birdsVisited = 0;
    foreach (int day in this.birdsPerDay.Take(numberOfDays)) {
      birdsVisited += day;
    }
    return birdsVisited;
  }

  public int BusyDays() {
    return this.birdsPerDay.Where(n => n >= 5).ToArray().Length;
  }
}
