void main(List<String> args) {
  var input = args.isNotEmpty ? args[0] : "";

  print("[Dart] upper: ${input.toUpperCase()}");
  print("[Dart] reversed: ${input.split('').reversed.join()}");
  print("[Dart] length: ${input.length}");
}