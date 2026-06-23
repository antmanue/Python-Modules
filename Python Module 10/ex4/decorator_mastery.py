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


class MageGuild:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return isinstance(name, str) and len(name) > 1


if __name__ == "__main__":
    # ⏱️ 1. Testing spell timer
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)  # Define o tempo esperado pelo subject
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    # ⏳ 2. Testing retrying spell
    print("\nTesting retrying spell...")

    attempt_count = 0

    @retry_spell(max_attempts=3)
    def waaaaaaagh() -> None:
        global attempt_count
        attempt_count += 1

        if attempt_count < 3:
            print(f"Spell failed, retrying... (attempt {attempt_count}/3)")
            raise ValueError("Fail")

        print("Spell casting failed after 3 attempts")
        raise ValueError("Waaaaaaagh spelled !")

    try:
        waaaaaaagh()
    except Exception as e:
        # Imprime exatamente o erro levantado na última tentativa
        print(e)

    # 🛡️ 3. Testing MageGuild and Power Validator
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A"))

    @power_validator(min_power=15)
    def cast_lightning(power: int) -> str:
        return f"Successfully cast Lightning with {power} power"

    # Teste de sucesso (poder 15 >= min_power 15)
    try:
        print(cast_lightning(15))
    except Exception as e:
        print(e)

    # Teste de falha (poder 10 < min_power 15)
    try:
        print(cast_lightning(10))
    except Exception as err:
        # Como o decorator faz "raise ValueError", imprimimos apenas a mensagem
        print(err)
