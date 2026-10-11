import sys
import os
import site

if sys.prefix != sys.base_prefix:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print(f"Package installation path: {site.getsitepackages()[0]}")
else:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print(
        "\nWARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n"
    )
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print(
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\\Scripts\\activate # On Windows\n"
        "\nThen run this program again."
    )

