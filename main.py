from acesso_cep import BuscaEndereco;

cep = "03945060"

obj_cep = BuscaEndereco(cep)

bairro, cidade, uf = obj_cep.acessa_via_cep()

print(bairro, cidade, uf)
