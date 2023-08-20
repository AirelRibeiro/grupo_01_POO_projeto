from Farmacia import *

controller = Controller(
    Cliente,
    Laboratorio,
    MedicamentoQuimioterapico,
    MedicamentoFitoterapico,
    Venda,
)

controller.main()
