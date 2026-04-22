import sys
import os
import io
import subprocess
from importlib import import_module
from contextlib import redirect_stdout

# Configuração dos Testes (Input, Argumentos, Resultado Esperado)
TEST_DATA = {
    "ex0": [([], None, "Hello, World! This is my first garden project!\n")],
    "ex1": [([ "Bio-Garden" ], None, "Welcome to Bio-Garden!\n")],
    "ex2": [([ "10", "5" ], None, "The total area of the plot is 50 square meters.\n")],
    "ex3": [([ "10", "20", "30" ], None, "The total harvest is 60 units.\n")],
    "ex4": [([ "60" ], None, "This plant still needs time to grow.\n"),
            ([ "61" ], None, "This plant is ready to harvest!\n")],
    "ex5": [([ "2" ], None, "The plant is fine for now.\n"),
            ([ "3" ], None, "Time to water the plant!\n")],
    "ex6": {
        "ft_count_harvest_iterative": [([ "3" ], None, "3\n2\n1\nDone!\n")],
        "ft_count_harvest_recursive": [([ "3" ], None, "3\n2\n1\nDone!\n")]
    },
    "ex7": [([], ["tomato", 15, "packets"], "Tomato seeds: 15 packets available.\n"),
            ([], ["basil", 5, "unknown"], "Unknown unit type\n")]
}

def check_quality(file_path):
    print(f"🔍 Qualidade: ", end="")
    f8 = subprocess.run(["flake8", file_path], capture_output=True, text=True)
    my = subprocess.run(["mypy", file_path], capture_output=True, text=True)
    
    if f8.returncode == 0 and my.returncode == 0:
        print("✅ PEP8 & Tipagem OK")
        return True
    print("❌ Erros encontrados:")
    if f8.stdout: print(f"   [Flake8]\n{f8.stdout}")
    if my.stdout: print(f"   [Mypy]\n{my.stdout}")
    return False

def run_logic_test(folder, func_name, inputs, args, expected):
    sys.path.insert(0, os.path.abspath(folder))
    try:
        module = import_module(func_name)
        func = getattr(module, func_name)
        sys.stdin = io.StringIO("\n".join(inputs))
        f = io.StringIO()
        with redirect_stdout(f):
            func(*args) if args else func()
        output = f.getvalue()
        if output == expected:
            print(f"   ✅ Lógica: OK")
        else:
            print(f"   ❌ Lógica: FALHOU")
            print(f"      Esperado: {repr(expected)}\n      Recebido: {repr(output)}")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
    finally:
        sys.path.remove(os.path.abspath(folder))

def main():
    print("🚀 INICIANDO AUDITORIA SUPER TESTER 🚀\n")
    for ex, tests in TEST_DATA.items():
        print(f"--- {ex.upper()} ---")
        # No ex6 temos dois ficheiros
        if isinstance(tests, dict):
            for f_name, t_list in tests.items():
                file_p = f"{ex}/{f_name}.py"
                if os.path.exists(file_p):
                    if check_quality(file_p):
                        for inp, arg, exp in t_list:
                            run_logic_test(ex, f_name, inp, arg, exp)
        else:
            # Caso normal: um ficheiro por pasta
            f_name = [f for f in os.listdir(ex) if f.startswith("ft_") and f.endswith(".py")][0].replace(".py", "")
            file_p = f"{ex}/{f_name}.py"
            if check_quality(file_p):
                for inp, arg, exp in tests:
                    run_logic_test(ex, f_name, inp, arg, exp)
    print("\n🏁 Fim da Auditoria.")

if __name__ == "__main__":
    main()