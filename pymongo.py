from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['pawsy_database']

clinica_data = {
    'nm_clinica': 'Clinica Veterinária XYZ',
    'cnpj_clinica': '12345678901234',
    'email_clinica': 'clinica@xyz.com',
    'tl_clinica': '987654321',
    'pw_clinica': 'senha_clinica_xyz',
    'status_loja': True
}

clinica_collection = db['clinica']
inserted_clinica = clinica_collection.insert_one(clinica_data)
print(f"Inserido na 'clinica'. ID: {inserted_clinica.inserted_id}")

medico_data = {
    'nm_medico': 'Dr. João Silva',
    'cd_cpf': '12345678901',
    'dt_nascimento': '1990-01-01',
    'nm_email': 'joao@clinicaxyz.com',
    'num_celular': '987654321',
    'pw_medic': 'senha_medico_xyz',
    'id_especialidade': 1,
    'id_endereco': 2,
    'cd_crmv': 654321
}

medico_collection = db['medico']
inserted_medico = medico_collection.insert_one(medico_data)
print(f"Inserido na 'medico'. ID: {inserted_medico.inserted_id}")

pet_data = {
    'id_tutor': 1,
    'id_raca': 1,
    'id_pelagem': 1,
    'id_sexo': 1,
    'id_animal': 1,
    'num_peso': 5.5,
    'dt_nascimento': '2020-01-01',
    'resumo': 'Pet feliz e saudável',
    'nm_pet': 'Rex',
    'url_img': 'url_imagem_pet.jpg',
    'tx_alergia': 'Sem alergias',
    'bl_castrado': True,
    'tx_comportamento': 'Brincalhão',
    'tx_tratamento': 'Sem tratamento',
    'num_altura': 0.5
}

pet_collection = db['pet']
inserted_pet = pet_collection.insert_one(pet_data)
print(f"Inserido na 'pet'. ID: {inserted_pet.inserted_id}")

clinicas = clinica_collection.find()
print("\nDocumentos na coleção 'clinica':")
for clinica in clinicas:
    print(clinica)

update_criteria = {'nm_medico': 'Dr. João Silva'}
new_values = {'$set': {'nm_medico': 'Dr. Joana Silva'}}
medico_collection.update_one(update_criteria, new_values)
print("\nDocumento 'medico' atualizado.")

medicos = medico_collection.find()
print("\nDocumentos na coleção 'medico' após a atualização:")
for medico in medicos:
    print(medico)

#documentação usada para realização da atv
#https://ronanlopes.me/python-com-mongodb-nosql-getting-started/