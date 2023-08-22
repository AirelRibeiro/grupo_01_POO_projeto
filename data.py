from Farmacia import (
    Laboratorio,
    MedicamentoQuimioterapico,
    MedicamentoFitoterapico,
    Cliente,
)

MedicamentoQuimioterapico(
    "Cisplatina",
    "Composto A",
    Laboratorio(
        "FarMax",
        "Avenida da Saúde, 1717",
        "(56) 5656-5656",
        "Rio de Janeiro",
        "RJ",
    ),
    "Tratamento de câncer",
    100.0,
    True,
),
MedicamentoQuimioterapico(
    "Doxorrubicina",
    "Composto B",
    Laboratorio(
        "FarMax",
        "Avenida da Saúde, 1717",
        "(56) 5656-5656",
        "Rio de Janeiro",
        "RJ",
    ),
    "Tratamento de tumores",
    150.0,
    False,
),
MedicamentoQuimioterapico(
    "Carboplatina",
    "Composto C",
    Laboratorio(
        "NaturaMed",
        "Avenida das Plantas, 1414",
        "(23) 2323-2323",
        "Porto Alegre",
        "RS",
    ),
    "Tratamento de câncer",
    120.0,
    True,
),
MedicamentoQuimioterapico(
    "Paclitaxel",
    "Composto D",
    Laboratorio(
        "Vida Pharma",
        "Avenida da Cura, 890",
        "(55) 5555-5555",
        "Salvador",
        "BA",
    ),
    "Inibidor de crescimento celular",
    130.0,
    False,
),
MedicamentoQuimioterapico(
    "Vinorelbina",
    "Composto E",
    Laboratorio(
        "NaturaMed",
        "Avenida das Plantas, 1414",
        "(23) 2323-2323",
        "Porto Alegre",
        "RS",
    ),
    "Tratamento de câncer",
    110.0,
    True,
),
MedicamentoQuimioterapico(
    "Ifosfamida",
    "Composto F",
    Laboratorio(
        "MedLife", "Rua das Curas, 789", "(88) 8888-8888", "Fortaleza", "CE"
    ),
    "Ciclofosfamida análoga",
    140.0,
    False,
),
MedicamentoQuimioterapico(
    "Etoposídeo",
    "Composto G",
    Laboratorio(
        "Vida Pharma",
        "Avenida da Cura, 890",
        "(55) 5555-5555",
        "Salvador",
        "BA",
    ),
    "Inibidor de DNA topoisomerase",
    160.0,
    True,
),
MedicamentoQuimioterapico(
    "Mitomicina C",
    "Composto H",
    Laboratorio(
        "MedLife", "Rua das Curas, 789", "(88) 8888-8888", "Fortaleza", "CE"
    ),
    "Inibidor de DNA",
    180.0,
    False,
),
MedicamentoQuimioterapico(
    "Pemetrexede",
    "Composto I",
    Laboratorio(
        "Lab Pharma",
        "Rua das Flores, 123",
        "(11) 1111-1111",
        "São Paulo",
        "SP",
    ),
    "Inibidor de timidilato sintase",
    170.0,
    True,
),

MedicamentoFitoterapico(
    "Erva de São João",
    "Hipericina",
    Laboratorio(
        "Lab Pharma",
        "Rua das Flores, 123",
        "(11) 1111-1111",
        "São Paulo",
        "SP",
    ),
    "Auxilia no tratamento de depressão",
    50.0,
),
MedicamentoFitoterapico(
    "Ginkgo Biloba",
    "Flavonoides",
    Laboratorio(
        "Vida Pharma",
        "Avenida da Cura, 890",
        "(55) 5555-5555",
        "Salvador",
        "BA",
    ),
    "Melhora a circulação cerebral",
    60.0,
),
MedicamentoFitoterapico(
    "Valeriana",
    "Ácido Valerênico",
    Laboratorio(
        "Vida Pharma",
        "Avenida da Cura, 890",
        "(55) 5555-5555",
        "Salvador",
        "BA",
    ),
    "Indicado para ansiedade e insônia",
    40.0,
),
MedicamentoFitoterapico(
    "Cavalinha",
    "Silício",
    Laboratorio(
        "Vida Pharma",
        "Avenida da Cura, 890",
        "(55) 5555-5555",
        "Salvador",
        "BA",
    ),
    "Auxilia na saúde dos ossos e pele",
    45.0,
),
MedicamentoFitoterapico(
    "Cúrcuma",
    "Curcumina",
    Laboratorio(
        "Lab Pharma",
        "Rua das Flores, 123",
        "(11) 1111-1111",
        "São Paulo",
        "SP",
    ),
    "Propriedades anti-inflamatórias",
    55.0,
),
MedicamentoFitoterapico(
    "Camomila",
    "Apigenina",
    Laboratorio(
        "Lab Pharma",
        "Rua das Flores, 123",
        "(11) 1111-1111",
        "São Paulo",
        "SP",
    ),
    "Relaxante e calmante",
    30.0,
),
MedicamentoFitoterapico(
    "Alcachofra",
    "Cinarina",
    Laboratorio(
        "Lab Pharma",
        "Rua das Flores, 123",
        "(11) 1111-1111",
        "São Paulo",
        "SP",
    ),
    "Estimula a função hepática",
    65.0,
),
MedicamentoFitoterapico(
    "Hortelã",
    "Mentol",
    Laboratorio(
        "Lab Pharma",
        "Rua das Flores, 123",
        "(11) 1111-1111",
        "São Paulo",
        "SP",
    ),
    "Alívio de desconfortos gastrointestinais",
    35.0,
),
MedicamentoFitoterapico(
    "Alho",
    "Alicina",
    Laboratorio(
        "Lab Pharma",
        "Rua das Flores, 123",
        "(11) 1111-1111",
        "São Paulo",
        "SP",
    ),
    "Propriedades antioxidantes e cardiovasculares",
    25.0,
),

Cliente("37294877017", "Maria Alguém", "15/03/1990")
Cliente("98929495010", "Lady Loki", "20/05/1985")
Cliente("23747163092", "João Ninguém", "10/12/1978")
Cliente("69875374024", "Patricia Pilar", "05/08/2000")
Cliente("18414569005", "Candido Souza", "30/01/1992")
Cliente("18414569005", "Lucas Alberto", "25/11/1987")
Cliente("27148565006", "Sueli Silva", "18/06/1965")
Cliente("06014860053", "Rufino Ribeiro", "22/09/1998")
Cliente("68982230033", "Paulo José", "08/04/1973")
Cliente("78609227030", "Antônia Maria", "12/07/1980")
Cliente("62181099090", "Sônia Larissa", "05/09/1995")
Cliente("24560683000", "Paulo José Souza", "21/02/1967")
Cliente("30712868054", "Anastácia Luzia", "14/10/2002")
Cliente("88526118005", "Fausto Ferdinando", "27/03/1989")
Cliente("17555581043", "José Maria", "09/11/1976")
Cliente("48210641034", "João Pessoa", "03/06/1997")
Cliente("19527697018", "Tânia Paraíba", "16/12/1960")
Cliente("37050473022", "Larissa Juliana", "19/08/2004")
Cliente("02200260091", "Nielda Carla", "01/01/1993")
Cliente("12791264000", "Suzana Bernardes", "30/07/1984")
