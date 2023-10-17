using System;
using System.Linq;

public static class TelemetryBuffer {
  public static byte[] ToBuffer(long reading) {
    (byte prefix, byte[] ba) = reading switch {
      long n when n < int.MinValue => ((byte)0xf8, BitConverter.GetBytes(n)),
      long n when n < short.MinValue =>
          ((byte)0xfc, BitConverter.GetBytes((int)n)),
      long n when n < ushort.MinValue =>
          ((byte)0xfe, BitConverter.GetBytes((short)n)),
      long n when n <= ushort.MaxValue =>
          ((byte)0x2, BitConverter.GetBytes((ushort)n)),
      long n when n <= int.MaxValue =>
          ((byte)0xfc, BitConverter.GetBytes((int)n)),
      long n when n <= uint.MaxValue =>
          ((byte)0x4, BitConverter.GetBytes((uint)n)),
      long n => ((byte)0xf8, BitConverter.GetBytes(n)),
    };

    byte[] prefixArray = { prefix };
    Array.Resize(ref ba, 8);
    return prefixArray.Concat(ba).ToArray();
  }

  public static long FromBuffer(byte[] buffer) {
    var prefix = buffer[0];
    var toTake = prefix > 8 ? 0x100 - prefix : prefix;
    var ba = buffer.Skip(1).Take(toTake).ToArray();
    return prefix switch {
      2 => (long)BitConverter.ToUInt16(ba, 0),
      4 => (long)BitConverter.ToUInt32(ba, 0),
      8 => (long)BitConverter.ToUInt64(ba, 0),
      0xfe => (long)BitConverter.ToInt16(ba, 0),
      0xfc => (long)BitConverter.ToInt32(ba, 0),
      0xf8 => (long)BitConverter.ToInt64(ba, 0),
      _ => 0
    };
  }
}
