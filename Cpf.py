from validate_docbr import CPF


class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_is_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.format_cpf()

    def cpf_is_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de Digitos Inválida")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
