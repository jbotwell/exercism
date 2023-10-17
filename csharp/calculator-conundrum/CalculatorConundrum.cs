using System;

public static class SimpleCalculator {
  public static string Calculate(int operand1, int operand2, string operation) {
    if (operation == "/" && operand2 == 0) {
      return "Division by zero is not allowed.";
    }

    int answer = operation switch {
      "+" => operand1 + operand2,
      "*" => operand1 * operand2,
      "/" => operand1 / operand2,
      "" => throw new ArgumentException("Give an operation."),
      null => throw new ArgumentNullException("Null not acceptable."),
      _ => throw new ArgumentOutOfRangeException("Did not recognize operation.")
    };

    return $"{operand1} {operation} {operand2} = {answer}";
  }
}
