using System;

class RemoteControlCar {
  private int distanceDriven;
  private int battery;

  public RemoteControlCar() {
    distanceDriven = 0;
    battery = 100;
  }

  public static RemoteControlCar Buy() { return new RemoteControlCar(); }

  public string DistanceDisplay() {
    return $"Driven {this.distanceDriven} meters";
  }

  public string BatteryDisplay() {
    if (this.battery > 0) {
      return $"Battery at {this.battery}%";
    } else {
      return "Battery empty";
    }
  }

  public void Drive() {
    if (this.battery > 0) {
      this.distanceDriven += 20;
      this.battery -= 1;
    }
  }
}
