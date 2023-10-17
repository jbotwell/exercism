using System;

class RemoteControlCar {
  private int speed;
  private int batteryDrain;
  private int distanceDriven;
  private int battery;

  public RemoteControlCar(int speedGiven, int batteryDrainGiven) {
    speed = speedGiven;
    batteryDrain = batteryDrainGiven;
    distanceDriven = 0;
    battery = 100;
  }

  public bool BatteryDrained() {
    return (this.battery - this.batteryDrain) < 0;
  }

  public int DistanceDriven() { return this.distanceDriven; }

  public void Drive() {
    if (!this.BatteryDrained()) {
      this.distanceDriven += speed;
      this.battery -= batteryDrain;
    }
  }

  public int ChargesLeft() { return this.battery / this.batteryDrain; }

  public int Speed() { return this.speed; }

  public static RemoteControlCar Nitro() { return new RemoteControlCar(50, 4); }
}

class RaceTrack {
  private int distance;
  public RaceTrack(int distanceGiven) { distance = distanceGiven; }

  public bool TryFinishTrack(RemoteControlCar car) {
    float chargesNeeded = (float)this.distance / (float)car.Speed();
    return chargesNeeded <= car.ChargesLeft();
  }
}
