from datetime import datetime


class GerarLog:
    def __call__(self, func):
        def wrapper(*args, **kargs):
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            results = func(*args, **kargs)
            log_mensagem = f"[LOG] {data_hora} - Executando {func.__name__} - Argumentos: {args}, {kargs} - Retorno: {results}"
            with open('log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(log_mensagem + '\n')
            return results
        return wrapper