from Farmacia import *
import data

controller = Controller(
    Cliente,
    Laboratorio,
    MedicamentoQuimioterapico,
    MedicamentoFitoterapico,
    Venda,
)

controller.main()
