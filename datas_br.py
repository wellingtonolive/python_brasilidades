from _datetime import datetime, timedelta;


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today();

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "marco", "abril", "maio",
            "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        days_of_the_week = [
            "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sabado", "Domingo"
        ]

        number_day = self.momento_cadastro.weekday()

        return days_of_the_week[number_day]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada


    def tempo_cadastro(self):
        tempo_cad = datetime.today() - self.momento_cadastro
        return tempo_cad