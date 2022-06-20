stats_list = {
    'Mins': 'Minutes',
    'Svt': 'Saves Tipped',
    'Svp': 'Saves Parried',
    'Svh': 'Saves Held',
    'Conc': 'Conceded',
    'Pas %': '% Passes',
    'Ps C/90': "Completed Passes / 90'",
    'K Tck': 'Key Tackles',
    'Tck R': 'Tackles Ratio',
    'Int/90': 'Interceptions / 90',
    'Hdr %': '% Headers',
    'Hdrs W/90': 'Headers Won / 90',
    'Fls': 'Fouls',
    'K Ps/90': 'Key Passes / 90',
    'Ch C/90': 'Chances Created / 90',
    'Gls/90': 'Goals / 90',
    'Asts/90': 'Assists / 90',
    'Shot %': '% Shots',
    'Drb/90': 'Dribbles / 90',
    'Shot/90': 'Shots / 90',
    'Cr C': 'Crosses Completed',
    'Cr C/A': 'Crosses Completed vs Attempts',
    'ShT/90': 'Shots on Target / 90',
    'Dist/90': 'Distance Covered / 90',
    'Gls': 'Goals',
    'Ast': 'Assits',
    'Tall': 'Team allowed',
    'Tcon/90': 'Team conceded / 90',
    'Ps A/90': 'Passes Attempted / 90',
    'Pens S': 'Penalties Scored',
    'Av Rat': 'Average Rating',
    'Min': 'Minutos',
    'BDs': 'Translate 1',
    'BRe': 'Balones Rechazados',
    'BAt': 'Balones Atajados',
    'Enc': 'Encajados',
    '% Pase': '% Pases',
    'Ps C/90': 'Pases Completados / 90',
    'Ent Cl': 'Entradas Clave',
    'Ent P': 'Promedio Entradas',
    'Rob/90': 'Robos / 90',
    'Rcg %': '% Cabezazos',
    'Cab G/90': 'Cabezazos Ganados / 90',
    'FC': 'Faltas Cometidas',
    'Pas Clv/90': 'Pases Clave / 90',
    'Oc C/90': 'Ocasiones Creadas / 90',
    'Gol/90': 'Goles / 90',
    'Asis/90': 'Asistencias / 90',
    '% disparos': '% Disparos',
    'Reg/90': 'Regates / 90',
    'Tir/90': 'Tiros / 90',
    'Cen.C/I': 'Centros Completados vs Intentados',
    'Cen.Com': 'Centros Completados',
    'TirP/90': 'Tiros a puerta / 90',
    'Dist/90': 'Distancia Recorrida / 90',
    'Gol': 'Goles',
    'Asis': 'Asistencias',
    'EnEq': 'Encajados Equipo',
    'EnEq/90': 'Encajados Equipo / 90',
    'Ps I/90': 'Pases Intentados / 90',
    'Pen M': 'Penalties Marcados',
    'Media': 'Media',
    'Tck': 'Tackles / 90',
    'Gl Mst': 'Mistakes costing goals',
    'Gl Err': 'Errores que costaron goles',
    'Ent': 'Entradas / 90',
    'Salary': 'Salary',
    'Sueldo': 'Sueldo',
    'Age': 'Age',
    'Edad': 'Edad'
}

metrics_list = {
    "Ground Duels": ("Tck", "Tck R"),
    "Air Duels": ("Hdrs W/90", "Hdr %"),
    "Ball Carrying Skills": ("Ch C/90", "Drb/90"),
    "Crossing Skills": ("Cr C", "Cr C/A"),
    "Wide Creation Skills": ("Cr C", "K Ps/90"),
    "Passing Skills": ("Ps C/90", "Pas %"),
    "Goal Involvement": ("Gls/90", "Asts/90"),
    "Goalscoring Efficiency": ("Gls/90", "ShT/90"),
    "Playmaking Skills": ("K Ps/90", "Ch C/90"),
    "Goal Creation Skills": ("Ch C/90", "Asts/90"),
    "Age Profile": ("Age", "Mins"),
    "Salary Profile": ("Salary", "Mins"),
    "Wingplay Skills": ("Drb/90", "Asts/90"),
    "Best Tacklers": ("K Tck", "Tck R"),
    "Ball winners": ("Tck", "Int/90"),
    "Duelos Terrestres": ("Ent", "Ent P"),
    "Duelos Aereos": ("Cab G/90", "Rcg %"),
    "Habilidad transportando": ("Oc C/90", "Reg/90"),
    "Habilidad centrando": ("Cen.Com", "Cen.C/I"),
    "Creacion de juego con amplitud": ("Cen.Com", "Pas Clv/90"),
    "Habilidad pasando": ("Ps C/90", "% Pase"),
    "Participacion de gol": ("Gol/90", "Asis/90"),
    "Eficiencia de gol": ("Gol/90", "TirP/90"),
    "Creacion de juego corto": ("Pas Clv/90", "Oc C/90"),
    "Creacion de gol": ("Oc C/90", "Asis/90"),
    "Perfil de edad": ("Edad", "Min"),
    "Perfil de sueldo": ("Sueldo", "Min"),
    "Habilidad de juego por banda": ("Reg/90", "Asis/90"),
    "Mejores aplacadores": ("Ent Cl", "Ent P"),
    "Ganadores de balones": ("Ent", "Rob/90")
}

list_en = [
    [
        'Mins',
        'Svt',
        'Svp',
        'Svh',
        'Conc',
        'Pas %',
        'Ps C/90',
        'K Tck',
        'Tck R',
        'Int/90',
        'Hdr %',
        'Hdrs W/90',
        'Fls',
        'K Ps/90',
        'Ch C/90',
        'Gls/90',
        'Asts/90',
        'Shot %',
        'Drb/90',
        'Shot/90',
        'Cr C/A',
        'Cr C',
        'ShT/90',
        'Dist/90',
        'Gls',
        'Ast',
        'Tall',
        'Tcon/90',
        'Ps A/90',
        'Pens S',
        'Av Rat',
        'Tck',
        'Gl Mst',
        'Salary',
        'Age'
    ],
    [
        'Ground Duels',
        'Air Duels',
        'Ball Carrying Skills',
        'Crossing Skills',
        'Wide Creation Skills',
        'Passing Skills',
        'Goal Involvement',
        'Goalscoring Efficiency',
        'Playmaking Skills',
        'Goal Creation Skills',
        'Age Profile',
        'Salary Profile',
        'Wingplay Skills',
        'Best Tacklers',
        'Ball winners'
    ],
    [
        "Acc",
        "Wor",
        "Vis",
        "Thr",
        "Tec",
        "Tea",
        "Tck",
        "Str",
        "Sta",
        "TRO",
        "Ref",
        "Pun",
        "Pos",
        "Pen",
        "Pas",
        "Pac",
        "1v1",
        "OtB",
        "Nat",
        "Mar",
        "L Th",
        "Lon",
        "Ldr",
        "Kic",
        "Jum",
        "Hea",
        "Han",
        "Fre",
        "Fla",
        "Fir",
        "Fin",
        "Ecc",
        "Dri",
        "Det",
        "Dec",
        "Cro",
        "Cor",
        "Cnt",
        "Cmp",
        "Com",
        "Cmd",
        "Bra",
        "Bal",
        "Ant",
        "Agi",
        "Agg",
        "Aer"
    ]
]

list_es = [
    [
        'Min',
        'BDs',
        'BRe',
        'BAt',
        'Enc',
        '% Pase',
        'Ps C/90',
        'Ent Cl',
        'Ent P',
        'Rob/90',
        'Rcg %',
        'Cab G/90',
        'FC',
        'Pas Clv/90',
        'Oc C/90',
        'Gol/90',
        'Asis/90',
        '% disparos',
        'Reg/90',
        'Tir/90',
        'Cen.C/I',
        'Cen.Com',
        'TirP/90',
        'Dist/90',
        'Gol',
        'Asis',
        'EnEq',
        'EnEq/90',
        'Ps I/90',
        'Pen M',
        'Media',
        'Gl Err',
        'Ent',
        'Sueldo',
        'Edad'
    ],
    [
        'Duelos Terrestres',
        'Duelos Aereos',
        'Habilidad transportando',
        'Habilidad centrando',
        'Creacion de juego con amplitud',
        'Habilidad pasando',
        'Participacion de gol',
        'Eficiencia de gol',
        'Creacion de juego corto',
        'Creacion de gol',
        'Perfil de edad',
        'Perfil de salario',
        'Habilidad de juego por banda',
        'Mejores aplacadores',
        'Ganadores de balones'
    ],
    [
        "Ace",
        "Sac",
        "Vis",
        "Saq",
        "Téc",
        "JEq",
        "Ent",
        "Fue",
        "Res",
        "SAL",
        "Ref",
        "Puñ",
        "Col",
        "Pen",
        "Pas",
        "Vel",
        "1v1",
        "Dmq",
        "Fís",
        "Mar",
        "Sq L",
        "Lej",
        "Lid",
        "Pue",
        "Sal",
        "Cab",
        "Blo",
        "Lib",
        "Tal",
        "Ctr",
        "Rem",
        "Exc",
        "Reg",
        "Det",
        "Dec",
        "Cen",
        "Cór",
        "Cnc",
        "Ser",
        "Com",
        "Mdo",
        "Val",
        "Equ",
        "Ant",
        "Agi",
        "Agr",
        "Aér"
    ]
]