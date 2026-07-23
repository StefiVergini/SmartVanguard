
#for row in rows:
#    repository.create(
#        db,
#        name=row["Nombre"],
#        age=row["Edad"]
#    )


"""
SERVICIO PARA SUBIDA MASIVA DE ARCHIVOS
HACER DSP LA FUNCION
dataset_rows = []

for row in dataframe.iterrows():

    dataset_rows.append(

        DatasetRow(

            dataset_id=dataset.id,

            row_number=i,

            raw_text=texto,

            content_json=row.to_dict()

        )

    )

#se llama a la funcion para conectar con db
dataset_row_repository.bulk_create(
    db,
    dataset_rows
)

#LO MISMO PARA EMBEDDINGS
embedding_repository.bulk_create(
    db,
    embeddings
)
"""