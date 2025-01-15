# Importando a biblioteca tkinter que é usada para criar aplicativos GUI
import tkinter as tk
# Importando ttk do tkinter para widgets temáticos
from tkinter import ttk

# Dicionário com linguagens de programação como chaves e seus emojis como valores
itens = {"Python": "", "Java": "", "C++": "", "Ruby": "", "JavaScript": "", "Go": "", "Swift": "", "Kotlin": ""}

# Dicionário com estados e seus municípios
ESTADOS_MUNICIPIOS = {
    "Acre": ["Acrelândia", "Assis Brasil", "Brasiléia", "Bujari", "Capixaba",
             "Cruzeiro do Sul", "Epitaciolândia", "Feijó", "Jordão", "Mâncio Lima",
             "Manoel Urbano", "Marechal Thaumaturgo", "Plácido de Castro", "Porto Acre", "Porto Walter",
             "Rio Branco", "Rodrigues Alves", "Santa Rosa do Purus", "Sena Madureira", "Senador Guiomard",
             "Tarauacá", "Xapuri"],
    "Alagoas": ["Água Branca", "Anadia", "Arapiraca", "Atalaia", "Barra de Santo Antônio",
                "Barra de São Miguel", "Batalha", "Belém", "Belo Monte", "Boca da Mata",
                "Branquinha", "Cacimbinhas", "Cajueiro", "Campestre", "Campo Alegre",
                "Campo Grande", "Canapi", "Capela", "Carneiros", "Chã Preta",
                "Coité do Nóia", "Colônia Leopoldina", "Coqueiro Seco", "Coruripe", "Craíbas",
                "Delmiro Gouveia", "Dois Riachos", "Estrela de Alagoas", "Feira Grande", "Feliz Deserto",
                "Flexeiras", "Girau do Ponciano", "Ibateguara", "Igaci", "Igreja Nova",
                "Inhapi", "Jacaré dos Homens", "Jacuípe", "Japaratinga", "Jaramataia",
                "Jequiá da Praia", "Joaquim Gomes", "Jundiá", "Junqueiro", "Lagoa da Canoa",
                "Limoeiro de Anadia", "Maceió", "Major Isidoro", "Mar Vermelho", "Maragogi",
                "Maravilha", "Marechal Deodoro", "Maribondo", "Mata Grande", "Matriz de Camaragibe",
                "Messias", "Minador do Negrão", "Monteirópolis", "Murici", "Novo Lino",
                "Olho d'Água das Flores", "Olho d'Água do Casado", "Olho d'Água Grande", "Olivença", "Ouro Branco",
                "Palestina", "Palmeira dos Índios", "Pão de Açúcar", "Pariconha", "Paripueira",
                "Passo de Camaragibe", "Paulo Jacinto", "Penedo", "Piaçabuçu", "Pilar",
                "Pindoba", "Piranhas", "Poço das Trincheiras", "Porto Calvo", "Porto de Pedras",
                "Porto Real do Colégio", "Quebrangulo", "Rio Largo", "Roteiro", "Santa Luzia do Norte",
                "Santana do Ipanema", "Santana do Mundaú", "São Brás", "São José da Laje", "São José da Tapera",
                "São Luís do Quitunde", "São Miguel dos Campos", "São Miguel dos Milagres", "São Sebastião", "Satuba",
                "Senador Rui Palmeira", "Tanque d'Arca", "Taquarana", "Teotônio Vilela", "Traipu",
                "União dos Palmares", "Viçosa"],
    "Amapá": ["Amapá", "Calçoene", "Cutias", "Ferreira Gomes", "Itaubal",
              "Laranjal do Jari", "Macapá", "Mazagão", "Oiapoque", "Pedra Branca do Amapari",
              "Porto Grande", "Pracuúba", "Santana", "Serra do Navio", "Tartarugalzinho",
              "Vitória do Jari"],
    "Amazonas": ["Alvarães", "Amaturá", "Anamã", "Anori", "Apuí",
                 "Atalaia do Norte", "Autazes", "Barcelos", "Barreirinha", "Benjamin Constant",
                 "Beruri", "Boa Vista do Ramos", "Boca do Acre", "Borba", "Caapiranga",
                 "Canutama", "Carauari", "Careiro", "Careiro da Várzea", "Coari",
                 "Codajás", "Eirunepé", "Envira", "Fonte Boa", "Guajará",
                 "Humaitá", "Ipixuna", "Iranduba", "Itacoatiara", "Itamarati",
                 "Itapiranga", "Japurá", "Jaru", "Jutaí", "Lábrea",
                 "Manacapuru", "Manaquiri", "Manaus", "Manicoré", "Maraã",
                 "Maués", "Nhamundá", "Nova Olinda do Norte", "Novo Airão", "Novo Aripuanã",
                 "Parintins", "Pauini", "Presidente Figueiredo", "Rio Preto da Eva", "Santa Isabel do Rio Negro",
                 "Santo Antônio do Içá", "São Gabriel da Cachoeira", "São Paulo de Olivença", "São Sebastião do Uatumã", "Silves",
                 "Tabatinga", "Tapauá", "Tefé", "Tonantins", "Uarini",
                 "Urucará", "Urucurituba"],
    "Bahia": ["Abaíra", "Abaré", "Acajutiba", "Adustina", "Água Fria",
              "Aiquara", "Alagoinhas", "Alcobaça", "Almadina", "Amargosa",
              "Amélia Rodrigues", "América Dourada", "Anagé", "Andaraí", "Andorinha",
              "Angical", "Anguera", "Antas", "Antônio Cardoso", "Antônio Gonçalves",
              "Aporá", "Apuarema", "Araças", "Aracatu", "Araci",
              "Aramari", "Arataca", "Aratuípe", "Aurelino Leal", "Baianópolis",
              "Baixa Grande", "Banzaê", "Barra", "Barra da Estiva", "Barra do Choça",
              "Barra do Mendes", "Barra do Rocha", "Barreiras", "Barro Alto", "Barro Preto",
              "Barrocas", "Belmonte", "Belo Campo", "Biritinga", "Boa Nova",
              "Boa Vista do Tupim", "Bom Jesus da Lapa", "Bom Jesus da Serra", "Boninal", "Bonito",
              "Boquira", "Botuporã", "Brejões", "Brejolândia", "Brotas de Macaúbas",
              "Brumado", "Buerarema", "Buritirama", "Caatiba", "Cabaceiras do Paraguaçu",
              "Cachoeira", "Caculé", "Caém", "Caetanos", "Caetité",
              "Cafarnaum", "Cairu", "Caldeirão Grande", "Camacan", "Camaçari",
              "Camamu", "Campo Alegre de Lourdes", "Campo Formoso", "Canápolis", "Canarana",
              "Canavieiras", "Candeal", "Candeias", "Candiba", "Cândido Sales",
              "Cansanção", "Canudos", "Capela do Alto Alegre", "Capim Grosso", "Caraíbas",
              "Caravelas", "Cardeal da Silva", "Carinhanha", "Casa Nova", "Castro Alves",
              "Catolândia", "Catu", "Caturama", "Central", "Chorrochó",
              "Cícero Dantas", "Cipó", "Coaraci", "Cocos", "Conceição da Feira",
              "Conceição do Almeida", "Conceição do Coité", "Conceição do Jacuípe", "Conde", "Condeúba",
              "Contendas do Sincorá", "Cordeiros", "Coribe", "Coronel João Sá",
              "Correntina", "Cotegipe", "Cravolândia", "Crisópolis", "Cristópolis",
              "Cruz das Almas", "Curaçá", "Dário Meira", "Dias d'Ávila", "Dom Basílio",
              "Dom Macedo Costa", "Elísio Medrado", "Encruzilhada", "Entre Rios", "Érico Cardoso",
              "Esplanada", "Euclides da Cunha", "Eunápolis", "Fátima", "Feira da Mata",
              "Feira de Santana", "Filadélfia", "Firmino Alves", "Floresta Azul", "Formosa do Rio Preto",
              "Gandu", "Gavião", "Gentio do Ouro", "Glória", "Gongogi",
              "Governador Mangabeira", "Guajeru", "Guanambi", "Guaratinga", "Heliópolis",
              "Iaçu", "Ibiassucê", "Ibicaraí", "Ibicuí", "Ibicoara",
              "Ibicuí", "Ibipeba", "Ibitiara", "Ibititá", "Ibotirama",
              "Ichu", "Igaporã", "Igrapiúna", "Iguaí", "Ilhéus",
              "Inhambupe", "Ipecaetá", "Ipiaú", "Ipirá", "Ipupiara",
              "Irajuba", "Iramaia", "Iraquara", "Irará", "Irecê",
              "Itabela", "Itaberaba", "Itabuna", "Itacaré", "Itagi",
              "Itagibá", "Itagimirim", "Itaguaçu da Bahia", "Itaju do Colônia", "Itajuípe",
              "Itamaraju", "Itamari", "Itambé", "Itanagra", "Itanhém",
              "Itaparica", "Itapé", "Itapebi", "Itapetinga", "Itapicuru",
              "Itapitanga", "Itaquara", "Itarantim", "Itatim", "Itiruçu",
              "Itiúba", "Itororó", "Ituaçu", "Ituberá", "Iuiú",
              "Jaborandi", "Jacaraci", "Jacobina", "Jaguaquara", "Jaguarari",
              "Jaguaripe", "Jandaíra", "Jequié", "Jeremoabo", "Jiquiriçá",
              "Jitaúna", "João Dourado", "Juazeiro", "Jucuruçu", "Jussara",
              "Jussari", "Jussiape", "Lafaiete Coutinho", "Lagoa Real", "Laje",
              "Lajedão", "Lajedinho", "Lajedo do Tabocal", "Lamarão", "Lapão",
              "Lauro de Freitas", "Lençóis", "Licínio de Almeida", "Livramento de Nossa Senhora", "Luís Eduardo Magalhães",
              "Macajuba", "Macarani", "Macaúbas", "Macururé", "Madre de Deus",
              "Maetinga", "Maiquinique", "Mairi", "Malhada", "Malhada de Pedras",
              "Manoel Vitorino", "Mansidão", "Maracás", "Maragogipe", "Maraú",
              "Marcionílio Souza", "Mascote", "Mata de São João", "Matina", "Medeiros Neto",
              "Miguel Calmon", "Milagres", "Mirangaba", "Mirante", "Monte Santo",
              "Morpará", "Morro do Chapéu", "Mortugaba", "Mucugê", "Mucuri",
              "Mulungu do Morro", "Mundo Novo", "Muniz Ferreira", "Muquém do São Francisco", "Muritiba",
              "Mutuípe", "Nazaré", "Nilo Peçanha", "Nordestina", "Nova Canaã",
              "Nova Fátima", "Nova Ibiá", "Nova Itarana", "Nova Redenção", "Nova Soure",
              "Nova Viçosa", "Novo Horizonte", "Novo Triunfo", "Olindina", "Oliveira dos Brejinhos",
              "Ouriçangas", "Ourolândia", "Palmas de Monte Alto", "Palmeiras", "Paramirim",
              "Paratinga", "Paripiranga", "Pau Brasil", "Paulo Afonso", "Pé de Serra",
              "Pedrão", "Pedro Alexandre", "Piatã", "Pilão Arcado", "Pindaí",
              "Pindobaçu", "Pintadas", "Piraí do Norte", "Piripá", "Piritiba",
              "Planaltino", "Planalto", "Poções", "Pojuca", "Ponto Novo",
              "Porto Seguro", "Potiraguá", "Prado", "Presidente Dutra", "Presidente Jânio Quadros",
              "Presidente Tancredo Neves", "Queimadas", "Quijingue", "Quixabeira", "Rafael Jambeiro",
              "Remanso", "Retirolândia", "Riachão das Neves", "Riachão do Jacuípe", "Riacho de Santana",
              "Ribeira do Amparo", "Ribeira do Pombal", "Ribeirão do Largo", "Rio de Contas", "Rio do Antônio",
              "Rio do Pires", "Rio Real", "Rodelas", "Ruy Barbosa", "Salinas da Margarida",
              "Salvador", "Santa Bárbara", "Santa Brígida", "Santa Cruz Cabrália", "Santa Cruz da Vitória",
              "Santa Inês", "Santa Luzia", "Santa Maria da Vitória", "Santa Rita de Cássia", "Santa Terezinha",
              "Santaluz", "Santana", "Santanópolis", "Santo Amaro", "Santo Antônio de Jesus",
              "Santo Estêvão", "São Desidério", "São Domingos", "São Felipe", "São Félix",
              "São Félix do Coribe", "São Francisco do Conde", "São Gabriel", "São Gonçalo dos Campos", "São José da Vitória",
              "São José do Jacuípe", "São Miguel das Matas", "São Sebastião do Passé", "Sapeaçu", "Sátiro Dias",
              "Saubara", "Saúde", "Seabra", "Sebastião Laranjeiras", "Senhor do Bonfim",
              "Sento Sé", "Serra do Ramalho", "Serra Dourada", "Serra Preta", "Serrinha",
              "Serrolândia", "Simões Filho", "Sítio do Mato", "Sítio do Quinto", "Sobradinho",
              "Souto Soares", "Tabocas do Brejo Velho", "Tanhaçu", "Tanque Novo", "Tanquinho",
              "Taperoá", "Tapiramutá", "Teixeira de Freitas", "Teodoro Sampaio", "Teofilândia",
              "Teolândia", "Terra Nova", "Tremedal", "Tucano", "Uauá",
              "Ubaíra", "Ubaitaba", "Ubatã", "Uibaí", "Umburanas",
              "Una", "Urandi", "Uruçuca", "Utinga", "Valença",
              "Valente", "Várzea da Roça", "Várzea do Poço", "Várzea Nova", "Varzedo",
              "Vera Cruz", "Vereda", "Vitória da Conquista", "Wagner", "Wanderley",
              "Wenceslau Guimarães", "Xique-Xique"],
    "Ceará": ["Abaiara", "Acarape", "Acaraú", "Acopiara", "Aiuaba",
              "Alcântaras", "Altaneira", "Alto Santo", "Amontada", "Antonina do Norte",
              "Apuiarés", "Aquiraz", "Aracati", "Aracoiaba", "Araioses",
              "Ararendá", "Araripe", "Aratuba", "Arneiroz", "Assaré",
              "Aurora", "Baixio", "Banabuiú", "Barbalha", "Barreira",
              "Barro", "Barroquinha", "Baturité", "Beberibe", "Bela Cruz",
              "Boa Viagem", "Brejo Santo", "Camocim", "Campos Sales", "Canindé",
              "Capistrano", "Caridade", "Cariré", "Caririaçu", "Cariús",
              "Carnaubal", "Cascavel", "Catarina", "Catunda", "Caucaia",
              "Cedro", "Chaval", "Choró", "Chorozinho", "Coreaú",
              "Crateús", "Crato", "Croatá", "Cruz", "Deputado Irapuan Pinheiro",
              "Ererê", "Eusébio", "Farias Brito", "Forquilha", "Fortaleza",
              "Fortim", "Frecheirinha", "General Sampaio", "Graça", "Granja",
              "Granjeiro", "Groaíras", "Guaiúba", "Guaraciaba do Norte", "Guaramiranga",
              "Hidrolândia", "Horizonte", "Ibaretama", "Ibiapina", "Ibicuitinga",
              "Icó", "Iguatu", "Independência", "Ipaporanga", "Ipaumirim",
              "Ipu", "Ipueiras", "Iracema", "Irauçuba", "Itaiçaba",
              "Itaitinga", "Itapajé", "Itapipoca", "Itapiúna", "Itarema",
              "Itatira", "Jaguaretama", "Jaguaribara", "Jaguaribe", "Jaguaruana",
              "Jardim", "Jati", "Jijoca de Jericoacoara", "Juazeiro do Norte", "Jucás",
              "Lavras da Mangabeira", "Limoeiro do Norte", "Madalena", "Maracanaú", "Maranguape",
              "Marco", "Martinópole", "Massapê", "Mauriti", "Meruoca",
              "Milagres", "Milhã", "Miraíma", "Missão Velha", "Mombaça",
              "Monsenhor Tabosa", "Morada Nova", "Moraújo", "Morrinhos", "Mucambo",
              "Mulungu", "Nova Olinda", "Nova Russas", "Novo Oriente", "Ocara",
              "Orós", "Pacajus", "Pacatuba", "Pacoti", "Pacujá",
              "Palhano", "Palmácia", "Paracuru", "Paraipaba", "Parambu",
              "Paramoti", "Pedra Branca", "Penaforte", "Pentecoste", "Pereiro",
              "Pindoretama", "Piquet Carneiro", "Pires Ferreira", "Poranga", "Porteiras",
              "Potengi", "Potiretama", "Quiterianópolis", "Quixadá", "Quixelô",
              "Quixeramobim", "Quixeré", "Redenção", "Reriutaba", "Russas",
              "Saboeiro", "Salitre", "Santa Quitéria", "Santana do Acaraú", "Santana do Cariri",
              "São Benedito", "São Gonçalo do Amarante", "São João do Jaguaribe", "São Luís do Curu", "Senador Pompeu",
              "Senador Sá", "Sobral", "Solonópole", "Tabuleiro do Norte", "Tamboril",
              "Tarrafas", "Tauá", "Tejuçuoca", "Tianguá", "Trairi",
              "Tururu", "Ubajara", "Umari", "Umirim", "Uruburetama",
              "Uruoca", "Varjota", "Várzea Alegre", "Viçosa do Ceará"],
    "Distrito Federal": ["Brasília", "Ceilândia", "Taguatinga", "Samambaia", "Plano Piloto"],
    "Espírito Santo": ["Vitória", "Vila Velha", "Serra", "Cariacica", "Linhares"],
    "Goiás": ["Abadia de Goiás", "Abadiânia", "Acreúna", "Adelândia", "Água Fria de Goiás",
              "Água Limpa", "Águas Lindas de Goiás", "Alexânia", "Aloândia", "Alto Horizonte",
              "Alto Paraíso de Goiás", "Alvorada do Norte", "Amaralina", "Americano do Brasil", "Amorinópolis",
              "Anápolis", "Anhanguera", "Anicuns", "Aparecida de Goiânia", "Aparecida do Rio Doce",
              "Aporé", "Araçu", "Aragarças", "Aragoiânia", "Araguapaz",
              "Arenópolis", "Aruanã", "Aurilândia", "Avelinópolis", "Baliza",
              "Barro Alto", "Bela Vista de Goiás", "Bom Jardim de Goiás", "Bom Jesus de Goiás", "Bonfinópolis",
              "Bonópolis", "Brazabrantes", "Britânia", "Buriti Alegre", "Buriti de Goiás",
              "Buritinópolis", "Cabeceiras", "Cachoeira Alta", "Cachoeira de Goiás", "Cachoeira Dourada",
              "Caçu", "Caiapônia", "Caldas Novas", "Caldazinha", "Campestre de Goiás",
              "Campinaçu", "Campinorte", "Campo Alegre de Goiás", "Campo Limpo de Goiás", "Campos Belos",
              "Campos Verdes", "Carmo do Rio Verde", "Castelândia", "Catalão", "Caturaí",
              "Cavalcante", "Ceres", "Cezarina", "Chapadão do Céu", "Cidade Ocidental",
              "Cocalzinho de Goiás", "Colinas do Sul", "Córrego do Ouro", "Corumbá de Goiás", "Corumbaíba",
              "Cristalina", "Cristianópolis", "Crixás", "Cromínia", "Cumari",
              "Damianópolis", "Damolândia", "Davinópolis", "Diorama", "Divinópolis de Goiás",
              "Doverlândia", "Edealina", "Edéia", "Estrela do Norte", "Faina",
              "Fazenda Nova", "Firminópolis", "Flores de Goiás", "Formosa", "Formoso",
              "Gameleira de Goiás", "Goianápolis", "Goiandira", "Goianésia", "Goiânia",
              "Goianira", "Goiás", "Goiatuba", "Gouvelândia", "Guapó",
              "Guaraíta", "Guarani de Goiás", "Guarinos", "Heitoraí", "Hidrolândia",
              "Hidrolina", "Iaciara", "Inaciolândia", "Indiara", "Inhumas",
              "Ipameri", "Ipiranga de Goiás", "Iporá", "Israelândia", "Itaberaí",
              "Itaguari", "Itaguaru", "Itajá", "Itapaci", "Itapirapuã",
              "Itapuranga", "Itarumã", "Itauçu", "Itumbiara", "Ivolândia",
              "Jandaia", "Jaraguá", "Jataí", "Jaupaci", "Jesúpolis",
              "Joviânia", "Jussara", "Lagoa Santa", "Leopoldo de Bulhões", "Luziânia",
              "Mairipotaba", "Mambaí", "Mara Rosa", "Marzagão", "Matrinchã",
              "Maurilândia", "Mimoso de Goiás", "Minaçu", "Mineiros", "Moiporá",
              "Monte Alegre de Goiás", "Montes Claros de Goiás", "Montividiu", "Montividiu do Norte", "Morrinhos",
              "Morro Agudo de Goiás", "Mossâmedes", "Mozarlândia", "Mundo Novo", "Mutunópolis",
              "Nazário", "Nerópolis", "Niquelândia", "Nova América", "Nova Aurora",
              "Nova Crixás", "Nova Glória", "Nova Iguaçu de Goiás", "Nova Roma", "Nova Veneza",
              "Novo Brasil", "Novo Gama", "Novo Planalto", "Orizona", "Ouro Verde de Goiás",
              "Ouvidor", "Padre Bernardo", "Palestina de Goiás", "Palmeiras de Goiás", "Palmelo",
              "Palminópolis", "Panamá", "Paranaiguara", "Paraúna", "Perolândia",
              "Petrolina de Goiás", "Pilar de Goiás", "Piranhas", "Pirenópolis",
              "Pires do Rio", "Planaltina", "Pontalina", "Porangatu", "Porteirão",
              "Portelândia", "Posse", "Professor Jamil", "Quirinópolis", "Rialma",
              "Rianápolis", "Rio Quente", "Rio Verde", "Rubiataba", "Sanclerlândia",
              "Santa Bárbara de Goiás", "Santa Cruz de Goiás", "Santa Fé de Goiás", "Santa Helena de Goiás", "Santa Isabel",
              "Santa Rita do Araguaia", "Santa Rita do Novo Destino", "Santa Rosa de Goiás", "Santa Tereza de Goiás", "Santa Terezinha de Goiás",
              "Santo Antônio da Barra", "Santo Antônio de Goiás", "Santo Antônio do Descoberto", "São Domingos", "São Francisco de Goiás",
              "São João da Paraúna", "São João d'Aliança", "São Luís de Montes Belos", "São Luiz do Norte", "São Miguel do Araguaia",
              "São Miguel do Passa Quatro", "São Patrício", "São Simão", "Senador Canedo", "Serranópolis",
              "Silvânia", "Simolândia", "Sítio d'Abadia", "Taquaral de Goiás", "Teresina de Goiás",
              "Terezópolis de Goiás", "Três Ranchos", "Trindade", "Trombas", "Turvânia",
              "Turvelândia", "Uirapuru", "Uruaçu", "Uruana", "Urutaí",
              "Valparaíso de Goiás", "Varjão", "Vianópolis", "Vicentinópolis", "Vila Boa",
              "Vila Propício"],
    "Maranhão": ["Açailândia", "Afonso Cunha", "Água Doce do Maranhão", "Alcântara", "Água Doce do Maranhão",
                 "Alcântara", "Altamira do Maranhão", "Alto Alegre do Maranhão", "Alto Alegre do Pindaré", "Alto Parnaíba", "Amapá do Maranhão",
                 "Amarante do Maranhão", "Anajatuba", "Anapurus", "Apicum-Açu", "Araguanã",
                 "Araioses", "Arame", "Arari", "Axixá", "Bacabal",
                 "Bacabeira", "Bacuri", "Bacurituba", "Balsas", "Barão de Grajaú",
                 "Barra do Corda", "Barreirinhas", "Belágua", "Bela Vista do Maranhão", "Benedito Leite",
                 "Bequimão", "Bernardo do Mearim", "Boa Vista do Gurupi", "Bom Jardim", "Bom Jesus das Selvas",
                 "Bom Lugar", "Brejo", "Brejo de Areia", "Buriti", "Buriti Bravo",
                 "Buriticupu", "Buritirana", "Cachoeira Grande", "Cajapió", "Cajari",
                 "Campestre do Maranhão", "Cândido Mendes", "Cantanhede", "Capinzal do Norte", "Carolina",
                 "Carutapera", "Caxias", "Cedral", "Central do Maranhão", "Centro do Guilherme",
                 "Centro Novo do Maranhão", "Chapadinha", "Cidelândia", "Codó", "Coelho Neto",
                 "Colinas", "Conceição do Lago-Açu", "Coroatá", "Cururupu", "Davinópolis",
                 "Dom Pedro", "Duque Bacelar", "Esperantinópolis", "Estreito", "Feira Nova do Maranhão",
                 "Fernando Falcão", "Formosa da Serra Negra", "Fortaleza dos Nogueiras", "Fortuna", "Godofredo Viana",
                 "Gonçalves Dias", "Governador Archer", "Governador Edison Lobão", "Governador Eugênio Barros", "Governador Luiz Rocha",
                 "Governador Newton Bello", "Governador Nunes Freire", "Graça Aranha", "Grajaú", "Guimarães",
                 "Humberto de Campos", "Icatu", "Igarapé do Meio", "Igarapé Grande", "Imperatriz",
                 "Itaipava do Grajaú", "Itapirapuã", "Itinga do Maranhão", "Jatobá", "Jenipapo dos Vieiras",
                 "João Lisboa", "Joselândia", "Junco do Maranhão", "Lago da Pedra", "Lago do Junco",
                 "Lago dos Rodrigues", "Lago Verde", "Lagoa do Mato", "Lagoa Grande do Maranhão", "Lajeado Novo",
                 "Lima Campos", "Loreto", "Luís Domingues", "Magalhães de Almeida", "Maracaçumé",
                 "Marajá do Sena", "Maranhãozinho", "Mata Roma", "Matinha", "Matões",
                 "Matões do Norte", "Milagres do Maranhão", "Mirador", "Miranda do Norte", "Mirinzal",
                 "Monção", "Montes Altos", "Morros", "Nina Rodrigues", "Nova Colinas",
                 "Nova Iorque", "Nova Olinda do Maranhão", "Olho d'Água das Cunhãs", "Olinda Nova do Maranhão", "Paço do Lumiar",
                 "Palmeirândia", "Paraibano", "Parnarama", "Passagem Franca", "Pastos Bons",
                 "Paulino Neves", "Paulo Ramos", "Pedreiras", "Pedro do Rosário", "Penalva",
                 "Peri Mirim", "Peritoró", "Pindaré-Mirim", "Pinheiro", "Pio XII",
                 "Pirapemas", "Poção de Pedras", "Porto Franco", "Porto Rico do Maranhão", "Presidente Dutra",
                 "Presidente Juscelino", "Presidente Médici", "Presidente Sarney", "Presidente Vargas", "Primeira Cruz",
                 "Raposa", "Riachão", "Ribamar Fiquene", "Rosário", "Sambaíba",
                 "Santa Filomena do Maranhão", "Santa Helena", "Santa Inês", "Santa Luzia", "Santa Luzia do Paruá",
                 "Santa Quitéria do Maranhão", "Santa Rita", "Santana do Maranhão", "Santo Amaro do Maranhão", "Santo Antônio dos Lopes",
                 "São Benedito do Rio Preto", "São Bento", "São Bernardo", "São Domingos do Azeitão", "São Domingos do Maranhão",
                 "São Félix de Balsas", "São Francisco do Brejão", "São Francisco do Maranhão", "São João Batista", "São João do Carú",
                 "São João do Paraíso", "São João do Soter", "São João dos Patos", "São José de Ribamar", "São José dos Basílios",
                 "São Luís", "São Luís Gonzaga do Maranhão", "São Mateus do Maranhão", "São Pedro da Água Branca", "São Pedro dos Crentes",
                 "São Raimundo das Mangabeiras", "São Raimundo do Doca Bezerra", "São Roberto", "São Vicente Ferrer", "Satubinha",
                 "Senador Alexandre Costa", "Senador La Rocque", "Serrano do Maranhão", "Sítio Novo", "Sucupira do Norte",
                 "Sucupira do Riachão", "Tasso Fragoso", "Timbiras", "Timon", "Trizidela do Vale",
                 "Tufilândia", "Tuntum", "Turiaçu", "Turilândia", "Tutóia",
                 "Urbano Santos", "Vargem Grande", "Viana", "Vila Nova dos Martírios", "Vitória do Mearim",
                 "Vitorino Freire", "Zé Doca"],
    "Mato Grosso": ["Acorizal", "Água Boa", "Alta Floresta", "Alto Araguaia", "Alto Boa Vista",
                    "Alto Garças", "Alto Paraguai", "Alto Taquari", "Apiacás", "Araguaiana",
                    "Araguainha", "Araputanga", "Arenápolis", "Aripuanã", "Barão de Melgaço",
                    "Barra do Bugres", "Barra do Garças", "Bom Jesus do Araguaia", "Brasnorte", "Cáceres",
                    "Campinápolis", "Campo Novo do Parecis", "Campo Verde", "Campos de Júlio", "Canabrava do Norte",
                    "Canarana", "Carlinda", "Castanheira", "Chapada dos Guimarães", "Cláudia",
                    "Cocalinho", "Colíder", "Colniza", "Comodoro", "Confresa",
                    "Conquista D'Oeste", "Cotriguaçu", "Cuiabá", "Curvelândia", "Denise",
                    "Diamantino", "Dom Aquino", "Feliz Natal", "Figueirópolis D'Oeste", "Gaúcha do Norte",
                    "General Carneiro", "Glória D'Oeste", "Guarantã do Norte", "Guiratinga", "Indiavaí",
                    "Ipiranga do Norte", "Itanhangá", "Itaúba", "Itiquira", "Jaciara",
                    "Jangada", "Jauru", "Juara", "Juína", "Juruena",
                    "Juscimeira", "Lambari D'Oeste", "Lucas do Rio Verde", "Luciara", "Marcelândia",
                    "Matupá", "Mirassol d'Oeste", "Nobres", "Nortelândia", "Nossa Senhora do Livramento",
                    "Nova Bandeirantes", "Nova Brasilândia", "Nova Canaã do Norte", "Nova Guarita", "Nova Lacerda",
                    "Nova Marilândia", "Nova Maringá", "Nova Monte Verde", "Nova Mutum", "Nova Nazaré",
                    "Nova Olímpia", "Nova Santa Helena", "Nova Ubiratã", "Nova Xavantina", "Novo Horizonte do Norte",
                    "Novo Mundo", "Novo Santo Antônio", "Novo São Joaquim", "Paranaíta", "Paranatinga",
                    "Pedra Preta", "Peixoto de Azevedo", "Planalto da Serra", "Poconé", "Pontal do Araguaia",
                    "Ponte Branca", "Pontes e Lacerda", "Porto Alegre do Norte", "Porto dos Gaúchos", "Porto Esperidião",
                    "Porto Estrela", "Poxoréu", "Primavera do Leste", "Querência", "Reserva do Cabaçal",
                    "Ribeirão Cascalheira", "Ribeirãozinho", "Rio Branco", "Rondolândia", "Rondonópolis",
                    "Rosário Oeste", "Salto do Céu", "Santa Carmem", "Santa Cruz do Xingu", "Santa Rita do Trivelato",
                    "Santa Terezinha", "Santo Afonso", "Santo Antônio do Leste", "Santo Antônio do Leverger", "São Félix do Araguaia",
                    "São José do Povo", "São José do Rio Claro", "São José do Xingu", "São José dos Quatro Marcos", "São Pedro da Cipa",
                    "Sapezal", "Serra Nova Dourada", "Sinop", "Sorriso", "Tabaporã",
                    "Tangará da Serra", "Tapurah", "Terra Nova do Norte", "Tesouro", "Torixoréu",
                    "União do Sul", "Vale de São Domingos", "Várzea Grande", "Vera", "Vila Bela da Santíssima Trindade",
                    "Vila Rica"],
    "Mato Grosso do Sul": ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá", "Ponta Porã"],
    "Minas Gerais": ["Belo Horizonte", "Uberlândia", "Contagem", "Juiz de Fora", "Betim"],
    "Pará": ["Belém", "Ananindeua", "Santarém", "Marabá", "Castanhal"],
    "Paraíba": ["João Pessoa", "Campina Grande", "Santa Rita", "Patos", "Bayeux"],
    "Paraná": ["Curitiba", "Londrina", "Maringá", "Ponta Grossa", "Cascavel"],
    "Pernambuco": ["Recife", "Jaboatão dos Guararapes", "Olinda", "Caruaru", "Petrolina"],
    "Piauí": ["Teresina", "Parnaíba", "Picos", "Piripiri", "Floriano"],
    "Rio de Janeiro": ["Rio de Janeiro", "São Gonçalo", "Duque de Caxias", "Nova Iguaçu", "Niterói"],
    "Rio Grande do Norte": ["Natal", "Mossoró", "Parnamirim", "São Gonçalo do Amarante", "Macaíba"],
    "Rio Grande do Sul": [
        "Aceguá", "Água Santa", "Agudo", "Ajuricaba", "Alecrim",
        "Alegrete", "Alegria", "Almirante Tamandaré do Sul", "Alpestre", "Alto Alegre",
        "Alto Feliz", "Alvorada", "Amaral Ferrador", "Ametista do Sul", "André da Rocha",
        "Anta Gorda", "Antônio Prado", "Arambaré", "Araricá", "Aratiba",
        "Arroio do Meio", "Arroio do Sal", "Arroio do Tigre", "Arroio dos Ratos", "Arroio Grande",
        "Arvorezinha", "Augusto Pestana", "Áurea", "Bagé", "Balneário Pinhal",
        "Barão", "Barão de Cotegipe", "Barão do Triunfo", "Barra do Guarita", "Barra do Quaraí",
        "Barra do Ribeiro", "Barra do Rio Azul", "Barra Funda", "Barracão", "Barros Cassal",
        "Benjamin Constant do Sul", "Bento Gonçalves", "Boa Vista das Missões", "Boa Vista do Buricá", "Boa Vista do Cadeado",
        "Boa Vista do Incra", "Boa Vista do Sul", "Bom Jesus", "Bom Princípio", "Bom Progresso",
        "Bom Retiro do Sul", "Boqueirão do Leão", "Bossoroca", "Bozano", "Braga",
        "Brochier", "Butiá", "Caçapava do Sul", "Cacequi", "Cachoeira do Sul",
        "Cachoeirinha", "Cacique Doble", "Caibaté", "Caiçara", "Camaquã",
        "Camargo", "Cambará do Sul", "Campestre da Serra", "Campina das Missões", "Campinas do Sul",
        "Campo Bom", "Campo Novo", "Campos Borges", "Candelária", "Cândido Godói",
        "Candiota", "Canela", "Canguçu", "Canoas", "Canudos do Vale",
        "Capão Bonito do Sul", "Capão da Canoa", "Capão do Cipó", "Capão do Leão", "Capela de Santana",
        "Capitão", "Capivari do Sul", "Caraá", "Carazinho", "Carlos Barbosa",
        "Carlos Gomes", "Casca", "Caseiros", "Catuípe", "Caxias do Sul",
        "Centenário", "Cerrito", "Cerro Branco", "Cerro Grande", "Cerro Grande do Sul",
        "Feliz", "Flores da Cunha", "Floriano Peixoto", "Fontoura Xavier", "Formigueiro",
        "Forquetinha", "Fortaleza dos Valos", "Frederico Westphalen", "Garibaldi", "Garruchos",
        "Gaurama", "General Câmara", "Gentil", "Getúlio Vargas", "Giruá",
        "Glorinha", "Gramado", "Gramado dos Loureiros", "Gramado Xavier", "Gravataí",
        "Guabiju", "Guaíba", "Guaporé", "Guarani das Missões", "Harmonia",
        "Herval", "Herveiras", "Horizontina", "Hulha Negra", "Humaitá",
        "Ibarama", "Ibiaçá", "Ibiraiaras", "Ibirapuitã", "Ibirubá",
        "Igrejinha", "Ijuí", "Ilópolis", "Imbé", "Imigrante",
        "Independência", "Inhacorá", "Ipê", "Ipiranga do Sul", "Iraí",
        "Itaara", "Itacurubi", "Itapuca", "Itaqui", "Itati",
        "Itatiba do Sul", "Ivorá", "Ivoti", "Jaboticaba", "Jacuizinho",
        "Jacutinga", "Jaguarão", "Jaguari", "Jaquirana", "Jari",
        "Jóia", "Júlio de Castilhos", "Lagoa Bonita do Sul", "Lagoa dos Três Cantos", "Lagoa Vermelha",
        "Lagoão", "Lajeado", "Lajeado do Bugre", "Lavras do Sul", "Liberato Salzano",
        "Linha Nova", "Maçambará", "Machadinho",
        "Manoel Viana", "Maquiné", "Maratá", "Marau", "Mariana Pimentel",
        "Mariano Moro", "Marques de Souza", "Mata", "Mato Castelhano",
        "Mato Leitão", "Mato Queimado", "Maximiliano de Almeida", "Minas do Leão", "Miraguaí",
        "Montauri", "Monte Alegre dos Campos", "Monte Belo do Sul", "Montenegro", "Mormaço",
        "Morrinhos do Sul", "Morro Redondo", "Morro Reuter", "Mostardas", "Muçum",
        "Muitos Capões", "Muliterno", "Não-Me-Toque", "Nicolau Vergueiro", "Nonoai",
        "Nova Alvorada", "Nova Araçá", "Nova Bassano", "Nova Boa Vista", "Nova Bréscia",
        "Nova Candelária", "Nova Esperança do Sul", "Nova Hartz", "Nova Pádua",
        "Nova Palma", "Nova Petrópolis", "Nova Prata", "Nova Ramada", "Nova Roma do Sul",
        "Nova Santa Rita", "Novo Barreiro", "Novo Cabrais", "Novo Hamburgo", "Novo Machado",
        "Novo Tiradentes", "Novo Xingu", "Osório", "Paim Filho", "Palmares do Sul",
        "Palmeira das Missões", "Palmitinho", "Panambi", "Pantano Grande", "Paraí",
        "Paraíso do Sul", "Pareci Novo", "Parobé", "Passa Sete", "Passo do Sobrado",
        "Passo Fundo", "Paulo Bento", "Paverama", "Pedras Altas", "Pedro Osório",
        "Pejuçara", "Pelotas", "Picada Café", "Pinhal", "Pinhal da Serra",
        "Pinhal Grande", "Pinheiro Machado", "Pinto Bandeira", "Pirapó",
        "Piratini", "Planalto", "Poço das Antas", "Pontão", "Ponte Preta",
        "Portão", "Porto Alegre", "Porto Lucena", "Porto Mauá", "Porto Vera Cruz",
        "Porto Xavier", "Pouso Novo", "Presidente Lucena", "Progresso", "Protásio Alves",
        "Putinga", "Quaraí", "Quatro Irmãos", "Quevedos", "Quinze de Novembro",
        "Redentora", "Relvado", "Restinga Seca", "Rio dos Índios", "Rio Grande",
        "Rio Pardo", "Riozinho", "Roca Sales", "Rodeio Bonito", "Rolador",
        "Rolante", "Ronda Alta", "Rondinha", "Roque Gonzales", "Rosário do Sul",
        "Sagrada Família", "Saldanha Marinho", "Salto do Jacuí", "Salvador das Missões", "Salvador do Sul",
        "Sananduva", "Santa Bárbara do Sul", "Santa Cecília do Sul", "Santa Clara do Sul", "Santa Cruz do Sul",
        "Santa Maria", "Santa Maria do Herval", "Santa Margarida do Sul", "Santa Rosa", "Santa Tereza",
        "Santa Vitória do Palmar", "Santana da Boa Vista", "Santana do Livramento", "Santiago", "Santo Ângelo",
        "Santo Antônio da Patrulha", "Santo Antônio das Missões", "Santo Antônio do Palma", "Santo Antônio do Planalto", "Santo Augusto",
        "Santo Cristo", "Santo Expedito do Sul", "São Borja", "São Domingos do Sul", "São Francisco de Assis",
        "São Francisco de Paula", "São Gabriel", "São Jerônimo", "São João da Urtiga", "São João do Polêsine",
        "São Jorge", "São José das Missões", "São José do Herval", "São José do Hortêncio", "São José do Inhacorá",
        "São José do Norte", "São José do Ouro", "São José do Sul", "São José dos Ausentes", "São Leopoldo",
        "São Lourenço do Sul", "São Luiz Gonzaga", "São Marcos", "São Martinho", "São Martinho da Serra",
        "São Miguel das Missões", "São Nicolau", "São Paulo das Missões", "São Pedro da Serra", "São Pedro das Missões",
        "São Pedro do Butiá", "São Pedro do Sul", "São Sebastião do Caí", "São Sepé", "São Valentim",
        "São Valentim do Sul", "São Valério do Sul", "São Vendelino", "São Vicente do Sul", "Sapiranga",
        "Sapucaia do Sul", "Sarandi", "Seberi", "Sede Nova", "Segredo",
        "Selbach", "Senador Salgado Filho", "Sentinela do Sul", "Serafina Corrêa", "Sério",
        "Sertão", "Sertão Santana", "Sete de Setembro", "Severiano de Almeida", "Silveira Martins",
        "Sinimbu", "Sobradinho", "Soledade", "Tabaí", "Tapejara",
        "Tapera", "Tapes", "Taquara", "Taquari", "Taquaruçu do Sul",
        "Tavares", "Tenente Portela", "Terra de Areia", "Teutônia", "Tio Hugo",
        "Tiradentes do Sul", "Toropi", "Torres", "Tramandaí", "Travesseiro",
        "Três Arroios", "Três Cachoeiras", "Três Coroas", "Três de Maio", "Três Forquilhas",
        "Três Palmeiras", "Três Passos", "Trindade do Sul", "Triunfo", "Tucunduva",
        "Tunas", "Tupanci do Sul", "Tupanciretã", "Tupandi", "Tuparendi",
        "Turuçu", "Ubiretama", "União da Serra", "Unistalda", "Uruguaiana",
        "Vacaria", "Vale do Sol", "Vale Real", "Vale Verde", "Vanini",
        "Venâncio Aires", "Vera Cruz", "Veranópolis", "Vespasiano Corrêa", "Viadutos",
        "Viamão", "Vicente Dutra", "Victor Graeff", "Vila Flores", "Vila Lângaro",
        "Vila Maria", "Vila Nova do Sul", "Vista Alegre", "Vista Alegre do Prata", "Vista Gaúcha",
        "Vitória das Missões", "Westfália", "Xangri-lá"
    ],
    "Rondônia": ["Porto Velho", "Ji-Paraná", "Ariquemes", "Vilhena", "Cacoal"],
    "Roraima": ["Boa Vista", "Rorainópolis", "Caracaraí", "Alto Alegre", "Mucajaí"],
    "Santa Catarina": ["Florianópolis", "Joinville", "Blumenau", "São José", "Criciúma"],
    "São Paulo": ["São Paulo", "Guarulhos", "Campinas", "São Bernardo do Campo", "Santo André"],
    "Sergipe": ["Aracaju", "Nossa Senhora do Socorro", "Lagarto", "Itabaiana", "São Cristóvão"],
    "Tocantins": ["Palmas", "Araguaína", "Gurupi", "Porto Nacional", "Paraíso do Tocantins"]
}

# Criando a janela principal do aplicativo
root = tk.Tk()
# Definindo o título da janela
root.title("Widgets Avançados ")
# Definindo tela cheia ao abrir
root.state("zoomed")
# Definindo a cor de fundo da janela
root.configure(bg="lightgray")

# Criando um frame para conter a listbox e sua barra de rolagem
frame_listbox = tk.Frame(root, bg="lightgray")
# Colocando o frame na janela com algum espaçamento
frame_listbox.pack(pady=10)

# Criando um widget de barra de rolagem e associando-o ao frame
scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
# Criando um widget de listbox e associando-o ao frame
listbox = tk.Listbox(
    frame_listbox,
    height=4,
    yscrollcommand=scrollbar.set,
    font=("Arial", 20),
    bg="white",
    fg="black",
    selectbackground="red",
    selectforeground="white",
    activestyle="dotbox",
)

# Configurando a barra de rolagem para funcionar com a listbox
scrollbar.config(command=listbox.yview)
# Colocando a barra de rolagem no lado direito e fazendo-a preencher o eixo Y
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
# Colocando a listbox no lado esquerdo e fazendo-a preencher os eixos X e Y
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Iterando sobre os itens do dicionário (linguagem e emoji)
for item, emoji in itens.items():
    # Inserindo cada linguagem e seu emoji na listbox
    listbox.insert(tk.END, f"{item} {emoji}")

# Função para exibir o item selecionado da listbox
def exibir_selecao():
    # Obtendo o item selecionado da listbox
    selecionado = listbox.get(listbox.curselection())
    # Atualizando o rótulo de resultado com o item selecionado
    label_resultado.config(text=f"Você selecionou: {selecionado}")

def exibir_opcoes():
    linguagem = var_radio.get()
    preferencias = []
    if var_check1.get():
        preferencias.append("Dark Mode")
    if var_check2.get():
        preferencias.append("Auto Save")

    # Atualizando o rótulo de opções com a linguagem e preferências selecionadas
    label_opcoes.config(text=f"Linguagem: {linguagem}\nPreferências: {', '.join(preferencias)}")

# Criando um widget de rótulo com o texto "Selecione um item da Lista"
# Definindo a fonte para Arial, tamanho 24
label_titulo = tk.Label(root, text="Selecione um item da Lista", font=("Arial", 24), bg="lightgray")
# Colocando o rótulo na janela com algum espaçamento
label_titulo.pack(pady=10)

# Criando um widget de botão rotulado "Exibir Seleção"
botao_exibir = tk.Button(root, text="Exibir Seleção", font=("Arial", 24), bg="green", fg="white", command=exibir_selecao)
botao_exibir.pack(pady=10)

# Criando um widget de rótulo para exibir o resultado da seleção
label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
label_resultado.pack(pady=10)

var_radio = tk.StringVar(value="Java")
label_radio = tk.Label(root, text="Escolha sua linguagem favorita:", font=("Arial", 18), bg="lightgray")
label_radio.pack(pady=10)

for linguagem in ["Python", "Java", "C++"]:
    rb = tk.Radiobutton(root, text=linguagem, variable=var_radio, value=linguagem, bg="lightgray")
    rb.pack(anchor=tk.CENTER)

var_check1 = tk.BooleanVar()
var_check2 = tk.BooleanVar()

check1 = tk.Checkbutton(root, text="Dark Mode", variable=var_check1, bg="lightgray")
check2 = tk.Checkbutton(root, text="Auto Save", variable=var_check2, bg="lightgray")
check1.pack(anchor=tk.CENTER)
check2.pack(anchor=tk.CENTER)

botao_opcoes = tk.Button(root, text="Exibir Opções", font=("Arial", 24), bg="blue", fg="white", command=exibir_opcoes)
botao_opcoes.pack(pady=10, padx=10, anchor=tk.CENTER)

label_opcoes = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
label_opcoes.pack(pady=10, padx=10, anchor=tk.CENTER)

# Função para atualizar a lista de municípios quando um estado é selecionado
def atualizar_municipios(event=None):
    try:
        # Obtendo o estado selecionado
        estado_selecionado = listbox_estados.get(listbox_estados.curselection())
        # Limpando a lista de municípios
        listbox_municipios.delete(0, tk.END)
        # Preenchendo com os municípios do estado selecionado
        for municipio in ESTADOS_MUNICIPIOS[estado_selecionado]:
            listbox_municipios.insert(tk.END, municipio)
        # Atualizando o label de seleção
        label_selecao.config(text=f"Estado selecionado: {estado_selecionado}")
    except:
        pass

# Função para exibir o município selecionado
def exibir_municipio_selecionado(event=None):
    try:
        # Obtendo o município selecionado
        municipio = listbox_municipios.get(listbox_municipios.curselection())
        # Atualizando o label de município
        label_municipio.config(text=f"Município selecionado: {municipio}")
    except:
        pass

# Criando o frame para a lista de estados
frame_estados = tk.Frame(root, bg="lightgray")
frame_estados.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH)

# Label para a lista de estados
label_estados = tk.Label(frame_estados, text="Estados", font=("Arial", 24), bg="lightgray")
label_estados.pack(pady=10)

# Frame para conter a listbox de estados e sua scrollbar
frame_listbox_estados = tk.Frame(frame_estados, bg="lightgray")
frame_listbox_estados.pack(fill=tk.BOTH, expand=True)

# Criando scrollbar para a lista de estados
scrollbar_estados = tk.Scrollbar(frame_listbox_estados)
scrollbar_estados.pack(side=tk.RIGHT, fill=tk.Y)

# Criando listbox para estados
listbox_estados = tk.Listbox(
    frame_listbox_estados,
    height=10,
    width=30,
    font=("Arial", 20),
    bg="white",
    fg="black",
    selectbackground="blue",
    selectforeground="white",
    activestyle="dotbox",
    yscrollcommand=scrollbar_estados.set
)
listbox_estados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_estados.config(command=listbox_estados.yview)

# Preenchendo a lista de estados
for estado in sorted(ESTADOS_MUNICIPIOS.keys()):
    listbox_estados.insert(tk.END, estado)

# Criando o frame para a lista de municípios
frame_municipios = tk.Frame(root, bg="lightgray")
frame_municipios.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH)

# Label para a lista de municípios
label_municipios = tk.Label(frame_municipios, text="Municípios", font=("Arial", 24), bg="lightgray")
label_municipios.pack(pady=10)

# Frame para conter a listbox de municípios e sua scrollbar
frame_listbox_municipios = tk.Frame(frame_municipios, bg="lightgray")
frame_listbox_municipios.pack(fill=tk.BOTH, expand=True)

# Criando scrollbar para a lista de municípios
scrollbar_municipios = tk.Scrollbar(frame_listbox_municipios)
scrollbar_municipios.pack(side=tk.RIGHT, fill=tk.Y)

# Criando listbox para municípios
listbox_municipios = tk.Listbox(
    frame_listbox_municipios,
    height=10,
    width=30,
    font=("Arial", 20),
    bg="white",
    fg="black",
    selectbackground="blue",
    selectforeground="white",
    activestyle="dotbox",
    yscrollcommand=scrollbar_municipios.set
)
listbox_municipios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_municipios.config(command=listbox_municipios.yview)

# Frame para exibir as seleções
frame_selecao = tk.Frame(root, bg="lightgray")
frame_selecao.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH)

# Labels para mostrar as seleções
label_selecao = tk.Label(frame_selecao, text="Estado selecionado: ", font=("Arial", 18), bg="lightgray")
label_selecao.pack(pady=10)

label_municipio = tk.Label(frame_selecao, text="Município selecionado: ", font=("Arial", 18), bg="lightgray")
label_municipio.pack(pady=10)

# Vinculando eventos de seleção às funções
listbox_estados.bind('<<ListboxSelect>>', atualizar_municipios)
listbox_municipios.bind('<<ListboxSelect>>', exibir_municipio_selecionado)

# Iniciando o loop de eventos do Tkinter para executar o aplicativo
root.mainloop()