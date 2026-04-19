import subprocess
import threading

user_input = input("ENTER SOMETHING: ")

results = {}

def run(name, cmd):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        results[name] = output.decode().strip()
    except subprocess.CalledProcessError as e:
        results[name] = f"ERROR:\n{e.output.decode()}"
    except Exception as e:
        results[name] = f"ERROR: {e}"

threads = [
    # C++
    threading.Thread(target=run, args=("cpp", ["cpp\\cpp_prog.exe", user_input])),

    # Rust
    threading.Thread(target=run, args=("rust", ["rust\\rust_prog.exe", user_input])),

    # Node.js
    threading.Thread(target=run, args=("node", ["node", "node\\node.js", user_input])),

    # PowerShell
    threading.Thread(target=run, args=("powershell", [
        "powershell", "-ExecutionPolicy", "Bypass",
        "-File", "powershell\\powershell.ps1", user_input
    ])),

    # Go
    threading.Thread(target=run, args=("go", ["go", "run", "go\\main.go", user_input])),

    # Java
    threading.Thread(target=run, args=("java", ["java", "-cp", "java", "Main", user_input])),

    # C#
    threading.Thread(target=run, args=("csharp", [
        "dotnet", "run", "--project", "csharp_app", "--", user_input
    ])),

    # F#
    threading.Thread(target=run, args=("fsharp", [
        "dotnet", "run", "--project", "fsharp_app", "--", user_input
    ])),

    # Ruby
    threading.Thread(target=run, args=("ruby", ["ruby", "ruby\\script.rb", user_input])),

    # PHP
    threading.Thread(target=run, args=("php", ["php", "php\\script.php", user_input])),

    # Nim
    threading.Thread(target=run, args=("nim", ["nim\\nim_prog.exe", user_input])),

    # Lua (no PATH needed)
    threading.Thread(target=run, args=("lua", [
        "C:\\lua\\lua55.exe", "lua\\script.lua", user_input
    ])),

threading.Thread(
    target=run,
    args=("malbolge", ["py", "malbolge\\pyinterpreter.py", "malbolge\\hello.mal"])
),

threading.Thread(
    target=run,
    args=("dart", ["C:\\dart\\bin\\dart.exe", "dart\\main.dart", user_input])
), 

threading.Thread(
    target=run,
    args=("vbnet", ["dotnet", "run", "--project", "vb_app", "--", user_input])
),

threading.Thread(
    target=run,
    args=("haskell", ["runghc", "haskell\\main.hs", user_input])
),  

threading.Thread(
    target=run,
    args=("octave", [
        "C:\\Program Files\\GNU Octave\\Octave-10.1.0\\mingw64\\bin\\octave-cli.exe",
        "octave\\script.m",
        user_input
    ])
),
]

# Run all
for t in threads:
    t.start()

for t in threads:
    t.join()

# Print results sorted
print("\n=== FINAL OUTPUT ===")
for k in sorted(results):
    print(f"{k}: {results[k]}")