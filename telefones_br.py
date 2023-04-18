import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Número de Telefone Inválido")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True;
        else:
            return False;

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        res = re.search(padrao, self.telefone)
        numero_formatado = "+{} ({}){}-{}".format(
            res.group(1),
            res.group(2),
            res.group(3),
            res.group(4)

        )
        return numero_formatado
