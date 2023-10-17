abstract class Character {
  private string type;
  protected Character(string characterType) { type = characterType; }

  public abstract int DamagePoints(Character target);

  public virtual bool Vulnerable() { return false; }

  public override string ToString() { return $"Character is a {this.type}"; }
}

class Warrior : Character {
  public Warrior() : base("Warrior") {}

  public override int DamagePoints(Character target) {
    return target.Vulnerable() ? 10 : 6;
  }
}

class Wizard : Character {
  private bool spellPrepared;

  public Wizard() : base("Wizard") { spellPrepared = false; }

  public override int DamagePoints(Character target) {
    return spellPrepared ? 12 : 3;
  }

  public override bool Vulnerable() { return !this.spellPrepared; }

  public void PrepareSpell() { this.spellPrepared = true; }
}
