from datetime import datetime


class GerarLog:
    def __call__(self, func):
        def wrapper(*args, **kargs):
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[LOG] {data_hora} - Executando {func.__name__}")
            return func(*args, **kargs)
        return wrapper