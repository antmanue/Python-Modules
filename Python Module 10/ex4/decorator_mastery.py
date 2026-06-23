import functools
import time
from typing import Any, Callable


def spell_timer(
    func: Callable[..., Any]
) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(
    min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(
        func: Callable[..., Any]
    ) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None:
                if len(args) >= 3:
                    power = args[2]
                elif len(args) >= 1:
                    power = args[0]

            if power is not None and power < min_power:
                return "insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(
        func: Callable[..., Any]
    ) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempts in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if attempts == max_attempts:
                        raise err
        return wrapper
    return decorator

if __name__ == "__main__":
    print("=== Guilda dos Magos: Campo de Treino ===")

    # 1. Feitiço normal com timer e validador de poder
    @spell_timer
    @power_validator(min_power=15)
    def cast_fireball(power: int) -> str:
        time.sleep(0.05)  # Simula o tempo de invocação
        return " Fireball lançada com sucesso!"

    print("\n[Teste 1] Lançar com poder=20 (Deve funcionar):")
    print(cast_fireball(20))

    print("\n[Teste 2] Lançar com poder=10 (Deve falhar):")
    print(cast_fireball(10))

    miss = {"count": 0}

    @retry_spell(max_attempts=3)
    def unstable_ritual() -> str:
        if  miss["count"] < 2:
            miss["count"] += 1
            print(f"Tentativa    miss['count'] falhou... Magia instável!")
            raise RuntimeError("Mana flutuante!")
        return "Ritual instável concluído com sucesso!"

    print("\n[Teste 3] Lançar feitiço instável (Deve tentar 3 vezes e vencer):")
    try:
        print(unstable_ritual())
    except Exception as err:
        print(f"O feitiço falhou definitivamente: {err}")
