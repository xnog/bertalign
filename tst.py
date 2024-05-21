from bertalign import Bertalign
# from nltk import tokenize

src = """
CARTOR 
Registro Civil e Tabelionato da Se 
REPÚBLICA FEDERATIVA DO BRASIL REGISTRO CIVIL DAS PESSOAS NATURAIS Certidão Inteiro Teor de Casamento 
NOME 
FERRASO VENTURA E ANGELINA FERRARES 
DESCRIÇÃO INTEIRO TEOR 
MATRÍCULA 
02258202551893200001009000001581 
CERTIFICA a pedido verbal de pessoa interessada que revendo no Cartório do Registro Civil das Pessoas Naturais e Tabelionato de Notas da Sede da Comarca de Rio Novo do Sul, Estado do Espírito Santo, o Livro de Registro de Casamento do Distrito de Princesa, o Livro AA n 1A, Fls. 09, termo n 15, encontrou o seguinte: Aos vinte e quatro (24) dias do mês de outubro (10) do ano de mil oitocentos e noventa e três (1893), as onze (11) horas da manhã em casa da residência do cidadão Antônio Gonsalves da Costa, Juiz Distrital, deste Distrito, presentes o mesmo Juiz comigo escrivão de seu cargo e as testemunhas Resmini Pedro e Fabro Luigi, receberam-se em matrimônio FERRASO VENTURA, filho de Ferraso Caetano e Sandrina Angela, de vinte e oito (28) anos de idade, natural de Verona no Reino da Itália, lavrador, residente neste Distrito, e dona ANGELINA FERRARES, filha de Ferrares Gilberto e Barola Petronilla, de dezenove (19) anos de idade, natural de Mantua no Reino da Itália, lavradora, e residente neste Distrito. Tem a contraente uma filha natural de três (03) anos de idade. Em firmeza do que eu Antônio José da Penha, lavrei este termo que vai por todos assinado, e por não saber ler nem escrever os contraentes, assinam por ele Gobbi Angelo, e por ela Ferri Josephe. AVERBAÇÃO: Consta à margem do termo averbação de Retificação de Registro Civil conforme mandado judicial que me foi apresentado sendo ele expedido nos autos de n 0005691- 08.2020.8.08.0030, em sentença proferida pelo MM Juiz de Direito Vara da Fazenda Pública Estadual, Municipal, Registros Públicos e Meio Ambiente da Comarca de Linhares, o Dr. André Bijos Dadalto em data de 13/12/2020 tendo transitada em julgado no dia e após a decisão de cumpra-se do MM. Juiz de Direito da Vara única da Comarca de Rio Novo do Sul-ES, o Dr. Ralfh Rocha de Souza, procedi com as seguintes retificações: 1 - Onde consta Ferraso Ventura, passe a constar Bonaventura Ferrazo. 2 ? onde consta Ferraso Caetano passe a constar Gaetano Ferazzo. 3 ? onde consta Sandrinha Angela passe a constar Caterina Desco. Tudo em conformidade com a sentença. Nada mais continha na referida certidão, traslado do seu próprio original, do que dou fé. Eu, Patrícia Mara Moreira Amaral, Oficiala Substituta, escrevi e assino. 
Certifico que, em data de 26 de Fevereiro de 2024, foi materializada esta certidão enviada pela Central de Informações do Registro Civil, sendo a autenticidade de sua assinatura digital padrão ICP-Brasil por mim conferida. Certidão lavrada por Patricia Mara Moreira Amaral - Substituta-legal do Registro Civil das Pessoas Naturais de Rio Novo do Sul, o(a) qual assinou eletronicamente aos 23 de Fevereiro de 2024, nos termos do Provimento n° 46/2015 do Conselho Nacional de Justiça. 
Oficial de Registro Civil das Pessoas Naturais 
Rio Novo do Sul - ES José Geraldo Santana - Oficial Rua Coronel Joaquim Alves, 89 - Centro CEP: 29290-000 E-mail: cartoriorns@hotmail.com Tel: (28) 35331100 
O Conteúdo da Certidão é verdadeiro. Dou Fé, 
домаше 
Colatina 
Sede 
Leticia da Silva Araujo - Escrevente Valor recebido pela certidão eletrônica: R$ 82,05 Valor recebido pela materialização: R$ 73,87 
Poder Judiciário do Estado do Espírito Santo Selo Digital de Fiscalização 022582.SKQ2303.02107 Emolumentos: R$ 63,11 Encargos: R$ 18,94 Total: R$ 
82,05 
Consulte autenticidade em www.tjes.jus.br 
Poder Judiciário do Estado do Espírito Santo Selo Digital de Fiscalização 023986.OLC2302.06448 Emol.: R$56,83 Encargos: R$17,04 Total: R$73,87 Consulte autenticidade em www.tjes.jus.br 
CARTÓRIO COLATINA-ES REGISTRO CIVIL E TABELIONATO DE NOTAS DA SEDE. Leticia da Silva Araujo Escrevente 
ARPENBRASILA BA 022795745 BRP 

"""

tgt = """
    169.772                                           1.698 LOA - RGS
STEMMA DELLA REPUBBLICA. REPUBBLICA FEDERATIVA DEL BRASILE. STATO DI ESPÍRITO SANTO. UFFICIO DELLO STATO CIVILE DI RIO NOVO DO SUL.
JOSÉ GERALDO SANTANA ... UFFICIALE DELLO STATO CIVILE.
CERTIFICATO INTEGRALE DI MATRIMONIO
Nomi: FERRASO VENTURA e ANGELINA FERRARES.
Matricola: 02258202551893200001009000001581.
Certifica a richiesta verbale della persona interessata che, esaminando presso l’Ufficio dello Stato Civile presso la sede del Circondario di Rio Novo do Sul, Stato di Espírito Santo, il libro degli atti di matrimonio del Distretto di Princesa, libro AA n. 1A, fl. 09, atto n. 15, ha trovato il seguente: Il giorno ventiquattro (24) del mese di ottobre (10) dell’anno milleottocentonovantatré (1893), alle ore undici (11) di mattina presso la residenza del cittadino Antônio Gonsalves da Costa, giudice distrettuale di questo Distretto, presenti lo stesso giudice con me, funzionario del suo incarico e i testimoni Resmini Pedro e Fabro Luigi, hanno contratto matrimonio FERRASO VENTURA, figlio di FERRASO CAETANO e SANDRINA ANGELA, di anni ventotto (28), nato a Verona, nel Regno d’Italia, contadino, residente in questo Distretto, e ANGELINA FERRARES, figlia di FERRARES GILBERTO e BAROLA PETRONILLA, di anni diciannove (19), nata a Mantova, nel Regno d’Italia, contadina, residente in questo Distretto. La sposa ha una figlia naturale di tre (03) anni. In virtù di ciò io Antônio José da Penha ho trascritto questo atto, che è firmato da tutti, e poiché gli sposi non sanno né leggere né scrivere, hanno firmato per conto e vece di lui Gobbi Angelo e per conto e vece di lei Ferri Josephe. Annotazione: A margine dell’atto contiene annotazione di rettifica di atto civile conforme mandato giudiziale a me presentato ed è stato emesso negli atti n. 0005691-08.2020.8.08.0030, nella sentenza pronunciata dal giudice della sezione civile del Circondario di Linhares, André Bijos Dadalto il 13/12/2020, passata in giudicato il giorno e dopo la decisione di adempimento emessa dal giudice della Sezione Civile del Circondario di Rio Novo do Sul-ES, Ralfh Rocha de Souza, ho apportato le seguenti rettifiche: 1- dove consta Ferraso Ventura, far constare BONAVENTURA FERRAZO; 2- dove consta Ferraso Caetano, far constare GAETANO FERAZZO; 3- dove consta Sandrinha Angela, far constare CATERINA DESCO. Tutto in conformità con la sentenza. Nient’altro contiene nel suddetto atto, estratto dall’originale, ne faccio fede. Io, Patrícia Mara Moreira Amaral, sostituta ufficiale, ho scritto e firmo. Certifico che il 26 febbraio 2024 è stato materializzato questo certificato inviato dal Centro Informativo del Registro Civile, essendo l’autenticità della sua firma digitale standard ICP-Brasile controllata da me. Certificato trascritto da Patrícia Mara Moreira Amaral – Sostituta Ufficiale dello Stato Civile di Rio Novo do Sul, che ha firmato via elettronica il 23 febbraio 2024, ai sensi del Provvedimento n. 46/2015 del Consiglio Nazionale di Giustizia. 
          Il contenuto del certificato è vero. Ne faccio fede. 
          F.to Leticia da Silva Araujo ... Funzionaria dello Stato Civile di Colatina ... Timbro e sigillo digitale di controllo: 022582.SKQ2303.02107 e 023986.OLC2302.06448. 
ARPENBRASIL  BA 022795745 BRP.
........................................................................
Io, sottoscritta, Nerina Bortoluzzi Herzog, Traduttrice Giurata ed Interprete Commerciale della Lingua Italiana dello Stato di Espírito Santo, Brasile, ho estratto questa traduzione dal Certificato Integrale di Matrimonio di BONAVENTURA FERRAZO e ANGELINA FERRARES. Certifico e ne faccio fede che la traduzione è vera e mi esento da ogni responsabilità per il contenuto e l’autenticità del documento a me presentato.
Vila Velha - ES, il 03 aprile 2024.

"""


# src = "\n".join(tokenize.sent_tokenize(src))
# tgt = "\n".join(tokenize.sent_tokenize(tgt))

aligner = Bertalign(src, tgt)
aligner.align_sents()

aligner.print_sents()
