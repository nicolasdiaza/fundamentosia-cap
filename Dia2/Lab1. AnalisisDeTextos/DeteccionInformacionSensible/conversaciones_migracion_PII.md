# Conversaciones de Prueba — Oficina de Migración / Extranjería (PII)

> Diálogos simulados de atención presencial y telefónica en una **Oficina de Migración / Extranjería**, en 11 idiomas. Pensados para evaluar la detección de información sensible sobre transcripciones: pasaportes, visados, permisos de residencia, solicitudes de asilo, reagrupación familiar, antecedentes, datos biométricos, etc.
>
> **Por qué este dominio es especialmente exigente:**
> - PII de **múltiples países** en una misma conversación (pasaporte venezolano + NIE español + cuenta bancaria local).
> - Mezcla de **documentos físicos** (pasaporte, partida de nacimiento, antecedentes penales) con **datos del solicitante, familiares y patrocinadores**.
> - Vocabulario técnico/jurídico que a veces se confunde con PII (número de expediente, resolución, recurso).
> - Conversaciones **emocionalmente cargadas** (asilo, deportación, reagrupación familiar) — el modelo debe ignorar el contexto emocional y seguir detectando PII.
> - Frecuente presencia de **datos de terceros** (cónyuge, hijos, empleador, abogado, garante).

---

## 1. 🇪🇸 Español — Oficina de Extranjería (España)

### 1.1 Solicitud de reagrupación familiar
- **Funcionario:** Oficina de Extranjería de Madrid, le atiende Pedro Sánchez, número de funcionario F-29481. ¿En qué puedo ayudarle?
- **Solicitante:** Buenos días, mi nombre es Andrés Felipe Cárdenas Vargas, ciudadano colombiano, con NIE X1234567-X. Vengo a solicitar la reagrupación de mi esposa e hijos.
- **Funcionario:** Perfecto, ¿datos del pasaporte?
- **Solicitante:** Pasaporte colombiano número 19.456.789, expedido en Bogotá el 15/03/2018, con validez hasta 14/03/2028. Mi fecha de nacimiento es 22 de noviembre de 1980, nací en Medellín, Antioquia.
- **Funcionario:** ¿Y los familiares a reagrupar?
- **Solicitante:** Mi esposa María Camila Restrepo Vélez, pasaporte colombiano 19.567.890, nacida el 5 de junio de 1983 en Cali. Y mis hijos: Juan Sebastián Cárdenas Restrepo, nacido el 10/01/2010, pasaporte 19.789.012, y Sofía Cárdenas Restrepo, nacida el 18/07/2012, pasaporte 19.789.013.
- **Funcionario:** ¿Dispone de vivienda adecuada? Indique dirección y metros cuadrados.
- **Solicitante:** Sí, vivo en Calle Mayor 45, 3ºA, 28013 Madrid. El contrato de alquiler está a mi nombre por 750 €/mes, con 90 m², 3 habitaciones.
- **Funcionario:** ¿Y solvencia económica? Últimas nóminas, cuenta bancaria.
- **Solicitante:** Trabajo en Logística Martínez S.L., CIF B-12345678, contrato indefinido, sueldo bruto 1.850 €/mes. Mi cuenta es ES80 0182 0500 1300 0298 7654, a nombre de Andrés Felipe Cárdenas Vargas. El IBAN ya lo tramité con usted el mes pasado, expediente EX-2026/0098745.
- **Funcionario:** Anotado. Le faltan los certificados de antecedentes penales de Colombia (apostillados) y el acta de matrimonio. Mi correo es p.sanchez@extranjeria.mir.es y el teléfono de la oficina 91 272 95 00. Tiene cita para el 18 de abril a las 9:30.

### 1.2 Solicitud de asilo
- **Abogada:** Soy Laura Jiménez, letrada de CEAR, abogada de oficio del solicitante. Mi colegiada número ICAM-12.345.
- **Funcionario:** Adelante. ¿Identificación del solicitante?
- **Abogada:** Mi cliente, Said Al-Hussein, sirio, nacido en Alepo el 4 de abril de 1990. Pasaporte sirio número N0123456, expedido en Damasco el 20/02/2015. Llegó a territorio español el 12 de noviembre de 2025 por la frontera de Ceuta.
- **Funcionario:** ¿Motivo de la solicitud?
- **Abogada:** Persecución por motivos políticos. Pertenecía al partido opositor PDK-Siria. Su hermano, Omar Al-Hussein, pasaporte N0234567, fue detenido en mayo de 2024 y actualmente está preso en la cárcel de Saidnaya. Mi cliente tiene huellas dactilares registradas como B-2025-11-12-0042, tomadas en la Comisaría de Ceuta.
- **Funcionario:** ¿Tiene documentación complementaria?
- **Abogada:** Sí, informe de ACNUR, expediente UNHCR/2025/SYR/00917, fotos de las lesiones, y entrevista realizada en frontera el 13/11/2025 por la Policía Nacional, referencia POL-2025-11-13-CTG-0098. También tenemos un testigo, Mohamed Khalil, pasaporte N0456789, actualmente en Almería.
- **Funcionario:** Correcto, expediente de asilo AS-2026/004512. La resolución se notificará en máximo 6 meses. Mi contacto directo l.jimenez@cear.org, móvil 612 998 877. Mientras tanto, su cliente tiene derecho a trabajo con la autorización AT-2026/008741.

### 1.3 Renovación de permiso de trabajo
- **Funcionario:** Servicio de Inmigración, María del Mar Ruiz, funcionaria F-31204. ¿Su nombre y NIE?
- **Ciudadano:** Vladimir Petrov Hristov, búlgaro, NIE Y3456789-Y, fecha de nacimiento 17/02/1985, nacido en Sofía, Bulgaria.
- **Funcionario:** ¿Tipo de permiso actual?
- **Ciudadano:** Tarjeta de residencia de familiar de ciudadano comunitario, expedida el 14/06/2022, con validez hasta 13/06/2027. Número de tarjeta TCF-2022/009876.
- **Funcionario:** Vencida en 2027, ¿qué trámite necesita?
- **Ciudadano:** Renovar y, además, cambiar a permiso de trabajo por cuenta ajena. Mi empleador, Restaurante La Hidalga S.L., CIF B-87654321, con domicilio en Calle Sagasta 12, 28004 Madrid, quiere contratarme como cocinero. Sueldo 1.620 €/mes, jornada completa.
- **Funcionario:** ¿Dispone de contrato firmado?
- **Ciudadano:** Sí, contrato indefinido a partir del 1 de mayo de 2026, con número de la Seguridad Social 28 12345678 90. Mi cuenta para domiciliar pagos es ES65 0049 1500 1012 3400 8761. Mi correo v.petrov85@gmail.com y mi móvil 673 445 566. ¿Necesito cita previa? Porque vengo desde Barcelona, vivo en Carrer de València 245, ático 2ª, 08007 Barcelona.

---

## 2. 🇬🇧 English — USCIS / Home Office (USA + UK)

### 2.1 Family-based green card (USCIS)
- **Officer:** USCIS California Service Center, this is Officer James Miller, ID US-29481. How may I help you?
- **Applicant:** Hi, my name is Wei Chen, born July 12, 1992, in Shanghai, China. I'm a permanent resident, A-number A-098-765-432. My case is MSC2190456123, I-130 petition for alien relative.
- **Officer:** For whom are you petitioning?
- **Applicant:** My spouse, Li Na Chen, née Li Na Wang, born March 4, 1994, in Guangzhou, China. She's currently in China on F-1 visa, SEVIS ID N0012345678, at UCLA extension. Her Chinese passport number is E45678901, issued by the Guangzhou PSB on 08/15/2022, expires 08/14/2032.
- **Officer:** Do you have proof of bona fide marriage?
- **Applicant:** Yes — marriage certificate from Shanghai dated 09/22/2024, joint bank account at Chase ending in 4321 (routing 021000021), lease at 1455 Market Street, Apt 12B, San Francisco, CA 94103, and photos from our wedding at the Hyatt Regency, San Francisco Airport, on 10/12/2024. I'm employed at Salesforce, employee ID SF-29481, salary $185,000/year. My SSN is 123-45-6789.
- **Officer:** We'll schedule an interview. Your case officer is Jennifer Lopez, jlopez@uscis.dhs.gov, (415) 555-0173. Reference I-130 interview package IOE-09873452.

### 2.2 UK asylum claim (Home Office)
- **Caseworker:** Home Office Asylum Decision Team, case ID HO-2026-ASL-009872. I'm Sarah Williams, caseworker.
- **Solicitor:** Andrew Brown, OISC Level 3, registration F200100987. Acting for Mr. Tariq Mahmood, Pakistani national, born 14/08/1995 in Peshawar, Khyber Pakhtunkhwa. CNIC number 17301-1234567-1, issued 02/04/2018 by NADRA.
- **Caseworker:** Date of entry to the UK?
- **Solicitor:** 19/03/2025, via small boat to Dover, detained at Manston, then released on bail with reporting conditions at Lunar House, Croydon. Asylum screening reference ASP-2025-03-19-0098. He is currently at 14 Acacia Avenue, Luton, LU1 5HP, sponsored by Mr. Imran Ali, UK citizen, passport 534567890, contact 07700 900876.
- **Caseworker:** Reason for claim?
- **Solicitor:** Persecution by the Taliban. Client worked as a journalist for Dawn News, employee ID DN-2018-0098. His brother, Asif Mahmood, CNIC 17301-2345678-3, was killed in a drone strike in Miranshah on 12/09/2024 — we have the death certificate and police FIR 234/2024 from the Miranshah police station. Client has PTSD, treated at the Tavistock Centre, NHS number 943 478 9012, psychiatrist Dr. Patel, registration GMC-1234567.
- **Caseworker:** Noted. Decision expected by 19/09/2026. Contact a.brown@asylum-helper.org, 020 7946 0123.

### 2.3 Canadian PR renewal (IRCC)
- **Officer:** Immigration, Refugees and Citizenship Canada, this is Officer Marie-Claire Tremblay, officer ID IRCC-29481, calling from Sydney, NS office.
- **Applicant:** Hi, this is Olusegun Adebayo, Nigerian national, permanent resident card number AB-12345-6789, UCI number 7890-1234, landed as a Federal Skilled Worker on 14/06/2018 at Toronto Pearson.
- **Officer:** Yes Mr. Adebayo. You're calling about your PR card renewal?
- **Applicant:** Correct, my current card expires 13/06/2026. I now live at 25 Pleasant Street, Dartmouth, NS B2Y 3P2. I'm currently employed at Nova Scotia Health, employee ID NSH-29481, salary $98,500/year. My wife, Adaeze Adebayo née Okonkwo, also PR, UCI 7890-1235, and our two children: Chinedu, born 22/04/2018, UCI 7890-1236, and Ngozi, born 11/09/2020, UCI 7890-1237.
- **Officer:** Noted. Please mail your current card and photos to the Case Processing Centre in Sydney, NS B1P 5V7. Reference PR-renewal-2026-04812. Email m.tremblay@cic.gc.ca, phone 902-555-0173.

---

## 3. 🇫🇷 Français — OFII / Préfecture (France)

### 3.1 Demande de titre de séjour (Préfecture de Paris)
- **Agent:** Préfecture de Police de Paris, service des étrangers, Agent Sophie Laurent, matricule PP-29481. Que puis-je faire pour vous?
- **Usager:** Bonjour Madame, je m'appelle Mamadou Diop, sénégalais, né le 14/04/1988 à Dakar. Numéro de passeport A0123456, délivré le 22/06/2019 à Dakar, validité jusqu'au 21/06/2029. Mon numéro étranger en France est le 1000123456X, arrivé en France le 12/09/2022.
- **Agent:** Type de demande?
- **Usager:** Renouvellement de ma carte de séjour pluriannuelle, mention "salarié". Mon employeur est la société BTP Construction S.A., SIRET 123 456 789 00012, située au 45 rue de la Roquette, 75011 Paris. CDI, salaire brut 2 350 €/mois, convention collective Bâtiment. Numéro URSSAF 7512345678.
- **Agent:** Situation familiale?
- **Usager:** Marié à Aminata Diop née Ndiaye, sénégalaise, passeport A0234567, née le 7 mai 1992 à Kaolack. Nous avons une fille, Fatou Diop, née le 12/03/2020 à Paris, acte de naissance n° 2020/75/1234. Mon adresse actuelle est 12 rue des Ormeaux, 75020 Paris, bailleur Paris Habitat, n° bail 2022-09-12-0042. Mon compte bancaire Crédit Mutuel IBAN FR76 1027 8090 1500 0123 4567 890, RIB 10278 09015 0001234567 89.
- **Agent:** Dossier n° 2026/TS/009874, rendez-vous le 22 avril 2026 à 9h30. Mon courriel s.laurent@prefecture-paris.fr, 01 53 71 51 51.

### 3.2 Demande d'asile (OFPRA)
- **Agent OFPRA:** Office français de protection des réfugiés et apatrides, agent Patrick Moreau, OFPRA-29481.
- **Avocate:** Maître Camille Bernard, avocate au barreau de Paris, toque C-1234, cabinet Bernard & Associés, 14 avenue de l'Opéra, 75001 Paris.
- **Agent:** Pour le compte de?
- **Avocate:** Monsieur Davit Hakobyan, arménien, né le 3 mai 1991 à Kirovakan (Vanadzor), Arménie. Passeport arménien AM0123456, délivré le 14/08/2019, validité jusqu'au 13/08/2029. Il est entré en France le 22/01/2026 à l'aéroport de Roissy-Charles de Gaulle, vol AF1234, et a déposé sa demande d'asile le 23/01/2026 à la SPADA de Paris.
- **Agent:** Motif?
- **Avocate:** Persécution ethnique. M. Hakobyan est yézidi, originaire de la région de Vayots Dzor. Sa famille a été menacée par des groupes nationalistes. Sa sœur, Anahit Hakobyan, AM0234567, réside actuellement en Allemagne, à Berlin, avec un titre de séjour allemand type Aufenthaltserlaubnis n° DE-2025-ASL-00987. La mère, Astghik Hakobyan, 67 ans, est restée en Arménie, à l'adresse Hrazdan, rue Abovyan 12, appartement 5.
- **Agent:** Numéro de dossier OFII: 2026-DA-00987. Instruite par l'OFPRA sous référence OFPRA-2026-DA-00987. Mon contact p.moreau@ofpra.gouv.fr, 01 42 65 47 47. L'audience est prévue le 12 mai 2026 à 14h00 au 201 rue Carnot, Fontenay-sous-Bois.

---

## 4. 🇩🇪 Deutsch — Ausländerbehörde (Deutschland)

### 4.1 Aufenthaltstitel (Berlin)
- **Sachbearbeiter:** Ausländerbehörde Berlin, Sachbearbeiter Stefan Müller, Personalnummer AB-29481. Was kann ich für Sie tun?
- **Antragsteller:** Guten Tag, mein Name ist Ali Reza Mohammadi, iranischer Staatsbürger, geboren am 12.03.1985 in Teheran. Passnummer A12345678, ausgestellt am 14.05.2020 in Teheran, gültig bis 13.05/2030. Aufenthaltserlaubnis-Nummer DE-2024-AE-009871.
- **Sachbearbeiter:** Welche Art von Antrag?
- **Antragsteller:** Verlängerung meiner Aufenthaltserlaubnis nach § 18 Aufenthaltsgesetz für qualifizierte Beschäftigung als IT-Ingenieur. Mein Arbeitgeber ist die Siemens AG, Personalnummer 478291, mit Sitz in der Werner-von-Siemens-Straße 1, 80333 München. Bruttogehalt 65.000 € pro Jahr.
- **Sachbearbeiter:** Familienstand?
- **Antragsteller:** Verheiratet mit Sara Mohammadi, geborene Karimi, iranische Staatsbürgerin, Passnummer B23456789, geboren am 25.07.1990 in Isfahan. Eine Tochter: Leila Mohammadi, geboren am 18.04.2021 in Berlin, Geburtsurkunde Nr. 2021-BE-1234.
- **Sachbearbeiter:** Aktuelle Adresse?
- **Antragsteller:** Friedrichstraße 123, 10117 Berlin, 3. OG, links. Mietvertrag mit Vonovia, Vertragsnummer V-2023-04-12-0098, monatliche Miete 1.450 € warm. Steuer-ID 12 345 678 901, Sozialversicherungsnummer 65 120678 M 109, Bankkonto DE89 3704 0044 0532 0130 00 bei der Commerzbank. E-Mail: ali.mohammadi85@gmx.de, Mobil 0172 1234567.
- **Sachbearbeiter:** Vorgangsnummer AB-2026-AV-00987, Termin am 18. April 2026 um 10:30 Uhr. s.mueller@labo.berlin.de, 030 9012-3456.

### 4.2 Asylantrag (BAMF)
- **Entscheider:** Bundesamt für Migration und Flüchtlinge, Entscheider Markus Weber, BAMF-29481, Außenstelle Berlin.
- **Rechtsanwalt:** Dr. Klaus Fischer, Rechtsanwalt, Kanzlei am Mehringplatz, Kanzlei-Nummer R-2023-987.
- **Entscheider:** Für welchen Mandanten?
- **Rechtsanwalt:** Für Herrn Bilal Al-Sayed, syrischer Staatsbürger, geboren am 7. Februar 1993 in Homs, Syrien. Passnummer N0123456, ausgestellt 22.06.2018 in Damaskus, gültig bis 21.06.2028. Eingereist in die Bundesrepublik am 14.11.2025 über die österreichische Grenze bei Passau.
- **Entscheider:** Asylgrund?
- **Rechtsanwalt:** Verfolgung wegen regimekritischer Tätigkeit. Mein Mandant war Sanitäter beim Syrischen Arabischen Roten Halbmond, Personalnummer SAR-2018-0098. Er hat Verletzte aus den Protesten in Homs 2024 medizinisch versorgt, was den Assad-Behörden auffiel. Sein Bruder, Khaled Al-Sayed, N0234567, wurde am 03.05.2024 verhaftet, derzeit im Saidnaya-Gefängnis inhaftiert. Psychologische Begutachtung durch Dr. med. Anna Becker, Psychotherapeutin, Approbationsnummer B-2018-9876, Diagnose PTSD ICD-10 F43.1.
- **Entscheider:** Aktenzeichen BAMF-2026-AA-00987. Anhörung am 12. Mai 2026 um 9:00 Uhr in der Außenstelle Berlin, Bundesallee 119. k.fischer@ra-mp.de, 030 2529 8765.

---

## 5. 🇧🇷 Português — Polícia Federal / CONARE (Brasil)

### 5.1 Pedido de refúgio (CONARE)
- **Analista:** Comitê Nacional para Refugiados — CONARE, analista Beatriz Almeida, matrícula CONARE-29481. Em que posso ajudar?
- **Solicitante:** Bom dia, sou Yusuf Diallo, nascido em 12 de março de 1990 em Bamako, Mali. Passaporte malinês número A0123456, emitido em 05/04/2022 em Bamako, válido até 04/04/2032. CPF brasileiro 234.567.890-12, emitido em 14/02/2026 pela Receita Federal.
- **Analista:** Motivo do pedido?
- **Solicitante:** Perseguição por motivos étnicos e religiosos. Sou tuaregue, da região de Kidal. Os grupos armados jihadistas atacaram minha aldeia em outubro de 2024. Meu pai, Sidi Diallo, 68 anos, foi morto no ataque. Minha mãe, Aïcha Diallo, A0234567, está refugiada na Argélia, em Tamanrasset, no campo de refugiados da ACNUR. Tenho 3 irmãos: Ahmed (A0345678), Mohamed (A0456789) e Fátima (A0567890).
- **Analista:** Entrada no Brasil?
- **Solicitante:** Entrei no Brasil em 14/11/2025 pela fronteira em Corumbá/MS, solicitante de refúgio, protocolo da Polícia Federal PF-CRB-2025-11-14-0098. Estou hospedado na Casa do Migrante em São Paulo, endereço Rua Mauá 230, Luz, São Paulo/SP, CEP 01028-040. Meu telefone (11) 98765-4321, e-mail y.diallo@gmail.com.
- **Analista:** Processo CONARE-2026/000987, entrevista marcada para 17 de abril de 2026 às 10:00 na sede do CONARE em Brasília, Esplanada dos Ministérios, Bloco H. b.almeida@conare.mj.gov.br, (61) 2025-9876.

### 5.2 Emissão de visto humanitário (Itamaraty/Polícia Federal)
- **Atendente:** Polícia Federal — Coordenação-Geral de Imigração, servidor Carlos Eduardo Pereira, matrícula PF-39481. Identificação do solicitante?
- **Solicitante:** Sou María José Rodríguez Hernández, venezuelana, RIF (equivalente ao CPF) V-12345678-9, data de nascimento 18/09/1985, natural de Maracaibo, Estado Zulia. Passaporte venezuelano número 12345678, emitido em Caracas em 22/01/2020, válido até 21/01/2030.
- **Atendente:** Tipo de visto?
- **Solicitante:** Visto humanitário (Resolução Normativa CNIg nº 126/2017), para acolhida de cidadãos venezuelanos. Entrei no Brasil pela fronteira de Pacaraima/RR em 10/03/2026, com meus dois filhos: Diego José Rodríguez Hernández, nascido em 12/05/2015, e Valentina Rodríguez Hernández, nascida em 18/08/2018. Meu marido ficou na Venezuela, em Maracaibo, endereço Calle 72 con Avenida 3H, Casa 14-25.
- **Atendente:** Endereço atual no Brasil?
- **Solicitante:** Avenida Brasil 2300, apartamento 41, Bairro Liberdade, São Paulo/SP, CEP 01028-040. Estou cadastrada na Cáritas, protocolo CAR-SP-2026-03-15-0098. Meu contato (11) 99887-6655, mariajose.rh@gmail.com.
- **Atendente:** Solicitação de visto VHM-2026/00987, prazo de análise 90 dias. c.pereira@dpf.gov.br, (61) 3245-9876.

---

## 6. 🇮🇹 Italiano — Ufficio Immigrazione / Questura (Italia)

### 6.1 Richiesta di permesso di soggiorno (Questura di Roma)
- **Funzionario:** Ufficio Immigrazione della Questura di Roma, funzionario Marco Bianchi, matricola Q-29481. Come posso aiutarla?
- **Richiedente:** Buongiorno, mi chiamo Nguyen Van Thanh, cittadino vietnamita, nato il 14/03/1988 a Hanoi. Passaporto vietnamita numero B1234567, rilasciato il 22/05/2019 ad Hanoi, valido fino al 21/05/2029. Permesso di soggiorno numero IT-2024-PS-00987, scadenza 14/06/2026.
- **Funzionario:** Tipo di richiesta?
- **Richiedente:** Rinnovo per motivi di lavoro subordinato, contratto a tempo indeterminato. Il mio datore di lavoro è la Trattoria del Sole S.r.l., P.IVA 12345678901, sede legale Via dei Coronari 12, 00186 Roma. Mansione: cuoco. Retribuzione lorda 1.750 €/mese, 40 ore settimanali, CCNL Turismo.
- **Funzionario:** Situazione familiare?
- **Richiedente:** Coniugato con Tran Thi Mai, cittadina vietnamita, passaporto C2345678, nata il 7 novembre 1990 a Ho Chi Minh City. Siamo residenti a Via dei Mille 45, interno 7, 00185 Roma, contratto d'affitto con la Società Generale Immobiliare, canone 950 €/mese. Conto corrente Intesa Sanpaolo IBAN IT60 X054 2811 1010 0000 0123 456, intestato a Nguyen Van Thanh. Codice fiscale RSSGPP88E14Z222Z.
- **Funzionario:** Fascicolo n. 2026/PS/00987, appuntamento per le foto e le impronte digitali il 20 aprile 2026 alle ore 9:00 in Via della Consolata 4, Roma. m.bianchi@questura.rm.it, 06 4686 1234.

### 6.2 Domanda di protezione internazionale (Commissione Territoriale)
- **Commissione:** Commissione Territoriale per il Riconoscimento della Protezione Internazionale di Roma, presidente Dott. Giuseppe Russo, CT-RM-29481.
- **Avvocato:** Avv. Laura Conti, del foro di Roma, iscritta all'albo con numero 12345, studio legale Conti & Associati, Via Veneto 96, 00187 Roma.
- **Commissione:** Per quale richiedente?
- **Avvocato:** Per il Sig. Mohammad Saleem, cittadino pakistano, nato il 22/04/1994 a Peshawar, provincia di Khyber Pakhtunkhwa. CNIC pakistano 17301-1234567-1, rilasciato il 14/03/2016 da NADRA. È entrato in Italia il 14/12/2025 via mare, sbarcato a Lampedusa, foto segnaletica n. FOTO-LMP-2025-12-14-0098.
- **Commissione:** Motivo della domanda?
- **Avvocato:** Persecuzione religiosa. Il Sig. Saleem è cristiano protestante, frequenta la Chiesa di San Paolo a Peshawar, membro dal 2015. Ha ricevuto minacce di morte dal gruppo Tehreek-e-Taliban Pakistan nel settembre 2025. Suo cugino, Imran Saleem, CNIC 17301-2345678-2, è stato ucciso il 12/10/2025, certificato di morte della polizia di Peshawar FIR n. 456/2025. Il richiedente soffre di depressione grave, in cura presso l'ASL RM1, dott. Bianchi, psichiatra, ricetta dematerializzata n. 05B87. Attualmente ospitato nel CAS di via Cavour 25, Roma, struttura gestita dalla Croce Rossa Italiana.
- **Commissione:** Verbale CT-RM-2026-PI-00987, udienza il 14 maggio 2026 alle 11:00. l.conti@studioconti.it, 06 1234 5678.

---

## 7. 🇨🇳 中文 — 国家移民管理局 (China / 外国人服务)

### 7.1 居留许可续签 (北京出入境管理局)
- **工作人员:** 北京市公安局出入境管理局,工作人员张伟,工号 BJ-GA-29481。请问您需要什么帮助?
- **申请人:** 你好,我叫 David Michael Brown,美国人,护照号码 512345678,2018 年 5 月 14 日在华盛顿签发,有效期至 2028 年 5 月 13 日。出生日期 1985 年 2 月 12 日,出生于加利福尼亚州旧金山。现在的居留许可号码是 BJ-2024-FR-00987,有效期到 2026 年 4 月 15 日。
- **工作人员:** 工作单位?
- **申请人:** 我在北京微软亚洲研究院工作,工作签证 (Z 签),工号 MSFT-CN-29481,月薪税前 45,000 元人民币。劳动合同号 LAB-2024-MS-987,雇主地址北京市海淀区丹棱街 5 号。雇佣合同将于 2027 年 6 月 30 日到期。
- **工作人员:** 居住地址?
- **申请人:** 北京市朝阳区建国路 88 号 SOHO 现代城 3 号楼 1502 室,租约编号 RNT-2024-09-12-0098,月租 12,500 元,房东王建国。银行账户中国工商银行 ICBC 6222 0217 0200 1234 567,开户行北京分行,余额约 35 万元。
- **工作人员:** 家属信息?
- **申请人:** 我的妻子 Sarah Jane Brown,美国人,护照 523456789,1987 年 7 月 22 日出生,持 J-1 签证。我们有两个孩子:Emily Brown,2015 年 3 月 14 日出生,护照 534567890;James Brown,2018 年 11 月 8 日出生,护照 534567891。妻子和孩子的居留许可即将到期,需要一起续签。
- **工作人员:** 受理号 BJ-2026-FR-00987,受理日期 2026 年 3 月 10 日。请于 2026 年 4 月 18 日上午 9:30 带齐材料到前台窗口办理。办公电话 010-1234 5678,邮箱 zhang.wei@bjic.gov.cn。

### 7.2 难民身份认定申请 (联合国难民署驻华办)
- **官员:** 联合国难民署驻华代表处,保护官员李娜,工号 UNHCR-CN-29481。
- **律师:** 律师赵强,北京恒信律师事务所,执业证号 110101201012345678。我的当事人是来自阿富汗的法蒂玛·哈基米女士。
- **官员:** 申请人信息?
- **律师:** Fatimah Hakimi (法蒂玛·哈基米),阿富汗公民,1989 年 4 月 18 日出生于喀布尔,阿富汗护照号 AF0123456,2017 年 6 月 20 日签发,有效期至 2027 年 6 月 19 日。她于 2025 年 12 月 8 日从伊朗经土库曼斯坦边境进入中国,目前滞留在新疆乌鲁木齐。
- **官员:** 申请理由?
- **律师:** 她是 Hazara 族 (什叶派少数民族),遭受塔利班的系统性迫害。她的父亲,穆罕默德·哈基米,AF0234567,2024 年 8 月 12 日在喀布尔被塔利班武装分子绑架,目前下落不明。她的母亲,扎伊娜布·哈基米,AF0345678,与她一同逃亡。她有 3 个孩子:阿里 (2010 年生)、法蒂玛 (2012 年生)、哈桑 (2015 年生),都没有护照,只有阿富汗身份证 Tazkira 号 AF-2018-12345, AF-2018-12346, AF-2018-12347。
- **官员:** 受理工号 UNHCR-CN-2026-ASL-00987,初次面谈定于 2026 年 4 月 22 日下午 2:00,地点北京市朝阳区亮马桥外交公寓。联系方式 li.na@unhcr.org,电话 010-8532 1234。

---

## 8. 🇯🇵 日本語 — 出入国在留管理庁 (日本)

### 8.1 在留資格更新申請 (東京入管)
- **職員:** 東京出入国在留管理局、職員佐藤花子、職員番号 TO-IMM-29481。ご用件を伺います。
- **申請者:** 初めまして。ジョン・スミスと申します。アメリカ国籍、1985年7月22日生まれ、カリフォルニア州ロサンゼルス出身。パスポート番号 512345678、2018年3月14日ワシントンD.C.で発行、有効期限 2028年3月13日。在留カード番号 TO-2024-EN-00987、在留資格「技術・人文知識・国際業務」、有効期限 2026年4月15日。
- **職員:** 勤務先は?
- **申請者:** 株式会社ソニー・インタラクティブエンタテインメント、品川区東品川4-12-12、雇用契約番号 SIE-2024-0098、年収 850万円、月額給与 70万8,000円 (税引前)、社会保険加入、厚生年金番号 123456789012。
- **職員:** 居住地?
- **申請者:** 東京都港区六本木1-2-3 六本木マンション 1204号室、家主山田太郎、賃貸借契約番号 RNT-2024-09-12-0098、家賃月 25万円。銀行口座三井住友銀行、麻布支店、普通預金 1234567、口座名義人 John Smith。
- **職員:** 家族構成は?
- **申請者:** 妻 Mary Smith (旧姓 Johnson)、アメリカ国籍、1987年11月3日生まれ、パスポート番号 523456789、在留資格「家族滞在」、在留期限 2026年4月15日。子供2人: 娘 Emily (2015年4月12日生まれ、パスポート 534567890)、息子 Michael (2018年9月25日生まれ、パスポート 534567891)、2人とも在留資格「家族滞在」。
- **職員:** 申請番号 TO-2026-EN-00987、受領印 2026年3月10日。2026年4月18日午前9時30分に新館2階5番窓口へお越しください。連絡先 tokyo-isa@moj.go.jp、03-5796-7111。

### 8.2 難民認定申請 (東京入管・難民審判)
- **担当官:** 東京出入国在留管理局 難民調査部門、難民調査官田中太郎、職員番号 UNHCR-TO-29481。
- **弁護士:** 弁護士鈴木一郎、第二東京弁護士会所属、弁理士登録番号 12345。事件番号 JR-2025-12-0098。
- **担当官:** 申請者についてお聞きします。
- **弁護士:** ミャンマー連邦共和国からの申請者、Aung Kyaw (アウン・チョウ) 氏、1990年8月15日マンダレー生まれ、ミャンマー国民ID番号 12/KhAyaNa(N)098765、ミャンマーパスポート番号 MA0123456、2018年11月20日ヤンゴン発行、有効期限 2028年11月19日。2025年12月4日に新千歳空港に到着、入管収容、12月22日に保釈、保証人 Khin Mar (キン・マー)、パスポート MA0234567、札幌在住。
- **担当官:** 迫害の内容は?
- **弁護士:** 申請者はカチン族のキリスト教徒、国軍 (Tatmadaw) による宗教的・民族的迫害。2024年9月にミャワディ近郊の教会が襲撃され、叔父のLahpaw Htoi Aung (ラッパー・トイ・アウン)、ID 12/KhAyaNa(N)987654、が殺害されました。申請者はタイ経由で密航、ID番号 IMG-TH-2025-12-0098、令和7年(2025年)12月4日に上陸。日本カトリック司教協議会難民移住移動者委員会 (JRM) による支援あり、ケース番号 JRM-2025-12-0098。
- **担当官:** 事件番号 UNHCR-TO-2026-ASL-00987、口頭審理期日は2026年5月14日午後2時、場所は東京都港区港南5-5-30。s.ichiro@law-suzuki.jp、03-1234-5678。

---

## 9. 🇸🇦 العربية — المديرية العامة للجنسية والإقامة (الإمارات / دول الخليج)

### 9.1 طلب تأشيرة عمل (أبوظبي)
- **موظف:** الهيئة الاتحادية للهوية والجنسية والجمارك وأمن المنافذ، الموظف أحمد المنصوري، رقم الموظف ICA-29481. كيف يمكنني مساعدتك؟
- **مقدم الطلب:** السلام عليكم، أنا Suresh Kumar، من الهند، حامل جواز سفر رقم J12345678، صدر في 14/05/2018 في مومباي، صلاحية حتى 13/05/2028. تأشيرة العمل الحالية رقم ADN-2024-WP-00987، صادرة بتاريخ 15/03/2024، صالحة حتى 14/03/2026.
- **موظف:** جهة العمل؟
- **مقدم الطلب:** شركة الفجر للهندسة ذ.م.م، رخصة تجارية CN-1234567، مكتب في شارع الكورنيش، أبوظبي. راتبي 12,000 درهم شهرياً، عقد عمل محدد المدة، رقم العقد LAB-2024-0987، الوظيفة مهندس مدني. كفيل الشركة ممثلها السيد خالد بن سلطان الراشدي، رقم الهوية الإماراتية 784199512345678، جواز سفر A12345678.
- **موظف:** العنوان في الدولة؟
- **مقدم الطلب:** نعيش في منطقة الخالدية، شارع المرور، بناية الياسمين، شقة 305، أبوظبي. عقد إيجار رقم RNT-2024-09-12-0098، مع المالك محمد الزرعوني، 18,000 درهم سنوياً. حساب مصرفي في بنك أبوظبي الأول، رقم الحساب AE070331234567890123456.
- **موظف:** الأسرة؟
- **مقدم الطلب:** زوجتي Priya Kumari، هندية، جواز سفر K23456789، تأشيرة زيارة، وأطفالي: Aarav (2015/04/12) وAnaya (2018/09/25)، يحملون جوازات سفر L34567890 وL34567891، على تأشيرات زيارة عائلية.
- **موظف:** رقم الطلب ICA-2026-WP-00987، تاريخ التقديم 10/03/2026. المقابلة في 18 أبريل 2026 الساعة 9:30 صباحاً في مركز خدمة المتعاملين في الكرامة. a.almansoori@ica.gov.ae، 02 123 4567.

### 9.2 طلب لجوء إنساني (المفوضية السامية لشؤون اللاجئين)
- **موظف المفوضية:** مكتب المفوضية السامية لشؤون اللاجئين في عمّان، مسؤول الحماية محمود الحسن، رقم الموظف UNHCR-MENA-29481.
- **محامي:** المحامي سامي الخوري، نقابة المحامين الأردنيين رقم 12345، مكتب الخوري وشركاه، شارع الملك حسين، عمّان.
- **موظف:** بخصوص أي حالة؟
- **محامي:** الموكلة: منى محمود السعدي، سورية، من مواليد 14/08/1991 في حمص، سوريا. جواز سفر سوري N0123456، صدر 22/06/2018 في دمشق، صلاحية 21/06/2028. دخلت الأردن بتاريخ 12/11/2025 عبر الحدود مع سوريا عند جابر، واستلمت بطاقة المفوضية UNHCR-MENA-2025-11-12-0098.
- **موظف:** أسباب الطلب؟
- **محامي:** اضطهاد بسبب انتمائها الطائفي (علوية). زوجها السابق، أحمد الحلبية، N0234567، معتقل لدى الأجهزة الأمنية السورية منذ 15/03/2024، لا تعلم مكان احتجازه. ابنتها ياسمين الحلبية، 7 سنوات (مواليد 15/05/2018)، مسجلة معها. عائلتها في سوريا: الأب محمود السعدي (N0345678)، الأم فاطمة السعدي (N0456789)، شقيقها الأكبر عمر السعدي (N0567890) يقيم في ألمانيا منذ 2019، اللجوء رقم DE-2019-ASL-00987.
- **موظف:** ملف المفوضية UNHCR-MENA-2026-ASL-00987. المقابلة الأولى يوم 22 أبريل 2026 الساعة 11:00 صباحاً في مكتب المفوضية، شارع مكة، عمّان. للتواصل m.alhassan@unhcr.org، 06 500 1234.

---

## 10. 🇷🇺 Русский — УФМС / МВД (Россия)

### 10.1 Получение разрешения на временное проживание (Управление по вопросам миграции МВД, Москва)
- **Инспектор:** Управление по вопросам миграции ГУ МВД России по г. Москве, инспектор Елена Соколова, удостоверение МВД-УВМ-29481. Чем могу помочь?
- **Заявитель:** Здравствуйте, я Улугбек Раджабов, гражданин Узбекистана, родился 14.03.1989 в Ташкенте. Паспорт гражданина Узбекистана FA1234567, выдан 22.05.2019 в ОВИР Ташкента, срок действия до 21.05.2029. Миграционная карта серии 5022 № 1234567, поставлена на учет 12.02.2026 по адресу: г. Москва, ул. Бауманская, д. 15, кв. 8.
- **Инспектор:** Цель обращения?
- **Заявитель:** Получение разрешения на временное проживание (РВП) в порядке квоты, установленной на 2026 год. Я работаю поваром в ООО «Восточный Двор», ИНН 7708123456, КПП 770801001, юридический адрес: Москва, ул. Покровка, д. 27, стр. 4. Трудовой договор № ТД-2025-0987 от 14.04.2025, зарплата 75 000 ₽/мес.
- **Инспектор:** Семейное положение?
- **Заявитель:** Женат на Наргизе Раджабовой (девичья Султанова), гражданка Узбекистана, паспорт FA2345678, родилась 7 мая 1992 в Самарканде. Двое детей: сын Шахзод (паспорт FA3456789, 12.04.2015 г.р.) и дочь Мадина (FA4567890, 18.09.2018 г.р.), оба гражданам Узбекистана. Всей семьёй проживаем в квартире по вышеуказанному адресу, собственник гражданин РФ Иванов Сергей Петрович, паспорт 4512 987654, договор аренды РНТ-2026-02-01-0098.
- **Инспектор:** Учетный номер заявления 2026/РВП/00987. Сдача документов назначена на 18 апреля 2026 г. в 09:30, кабинет 312, ул. Новослободская, д. 45. Телефон отделения 8 (495) 777-12-12, e.sokolova@mvd-migration.ru.

### 10.2 Заявление о предоставлении убежища (ГУВМ МВД)
- **Инспектор:** Главное управление по вопросам миграции МВД РФ, инспектор по делам беженцев Александр Волков, удостоверение МВД-БЖ-29481.
- **Адвокат:** Адвокат Ольга Морозова, Московская городская коллегия адвокатов, регистрационный номер 77/12345, адвокатская консультация № 14.
- **Инспектор:** По какому заявителю?
- **Адвокат:** Гражданин Эритреи, Okbazghi Kidane (Окбазги Кидане), родился 14/08/1992 в Асмэре. Паспорт Эритреи ER0123456, выдан 22/06/2018 в Асмэре, действителен до 21/06/2028. Въехал в Россию 14.11.2025 через аэропорт Шереметьево, рейс SU-412, виза гуманитарная. Состоит на миграционном учёте по адресу: г. Москва, ул. Большая Семёновская, д. 40, общежитие «Гагаринское», комната 215.
- **Инспектор:** Основания для убежища?
- **Адвокат:** Длительное преследование по политическим и религиозным мотивам. Доверитель — православный христианин, в армии Эритреи служил с 18 до 30 лет (ID военнослужащего ER-MIL-2010-0098), после отказа продолжать военную службу подвергался преследованиям. Его родной брат, Tekeste Kidane (Текесте Кидане), паспорт ER0234567, был арестован в августе 2024 года в г. Асмэра, отбывает срок в тюрьме «Алала» (без подтверждённой информации о его местонахождении). Мать заявителя, Tsehay Kidane (Цехай Кидане), 67 лет, находится в Эритрее по адресу: г. Асмэра, район Акрада, улица Маэбаль-Хаус 14.
- **Инспектор:** Регистрационный номер заявления БЖ-2026-00987. Рассмотрение в течение 3 месяцев. Уведомление будет направлено по адресу постановки на учёт. Справка о рассмотрении заявления получена 10.03.2026. Мой контакт a.volkov@mvd-migration.ru, телефон 8 (495) 555-12-34. Адвокат: o.morozova@mgka-adv.ru.

---

## 11. 🇮🇳 हिन्दी — भारतीय अध्ययन (Bureau of Immigration / FRRO)

### 11.1 फॉरेनर्स रजिस्ट्रेशन (FRRO मुंबई)
- **अधिकारी:** फॉरेनर्स रजिस्ट्रेशन ऑफिस, मुंबई, अधिकारी प्रियंका शर्मा, कर्मचारी ID FRRO-MUM-29481।
- **आवेदक:** नमस्ते, मेरा नाम David Michael Brown है, अमेरिकी नागरिक, जन्म 22 जुलाई 1985 को न्यूयॉर्क शहर में। अमेरिकी पासपोर्ट संख्या 512345678, वॉशिंगटन D.C. में 14 मई 2018 को जारी, 13 मई 2028 तक वैध। भारत में मेरा वीज़ा e-TV-2024-US-00987 है, बिज़नेस वीज़ा, 5 साल के लिए, 14 जून 2024 से।
- **अधिकारी:** भारत में पता?
- **आवेदक:** मुंबई, अंधेरी पूर्व, लोखंडवाला कॉम्प्लेक्स, टॉवर A, फ्लैट 1204, पिनकोड 400053, ईमेल david.brown@us-india-corp.com। मेरा कार्यस्थल Amazon India, ऑफिस One World Center, Tower 1, Senapati Bapat Marg, Lower Parel, मुंबई 400013, कर्मचारी ID AMZ-IN-29481, वेतन ₹65 लाख/वर्ष।
- **अधिकारी:** भारत में परिवार?
- **आवेदक:** मेरी पत्नी Sarah Jane Brown, अमेरिकी नागरिक, पासपोर्ट 523456789, जन्म 3 नवंबर 1987, बच्चों के साथ मेरे साथ रहती हैं। बेटी Emily Brown, पासपोर्ट 534567890, जन्म 12 अप्रैल 2015, बेटा Michael Brown, पासपोर्ट 534567891, जन्म 25 सितंबर 2018। वे सभी मेरी dependent visa पर हैं।
- **अधिकारी:** सी-फॉर्म आवेदन संख्या FRRO-2026-MUM-00987, जमा दिनांक 10/03/2026। कृपया 18 अप्रैल 2026 को सुबह 9:30 बजे FRRO कार्यालय, भूतल, ब्रांड फैक्ट्री बिल्डिंग, वरली, मुंबई 400030 पर मूल दस्तावेज लेकर आएं। मेरा संपर्क p.sharma@frro-mum.gov.in, दूरभाष 022-2655 4321।

### 11.2 शरण आवेदन — UNHCR India
- **अधिकारी:** संयुक्त राष्ट्र शरणार्थी उच्चायुक्त (UNHCR) भारत कार्यालय, संरक्षण अधिकारी विवेक मेहता, कर्मचारी ID UNHCR-IN-29481।
- **वकील:** अधिवक्ता नेहा गुप्ता, बार काउंसिल ऑफ दिल्ली, पंजीकरण संख्या D/12345/2010। मेरे मुवक्किल अफ़ग़ानिस्तान की नागरिक हैं, महिला Fatimah Hakimi।
- **अधिकारी:** आवेदक का विवरण?
- **वकील:** Fatimah Hakimi, अफ़ग़ानी नागरिक, जन्म 18 अप्रैल 1989 को काबुल में। अफ़ग़ान पासपोर्ट संख्या AF01234567, 20 जून 2017 को काबुल में जारी, 19 जून 2027 तक वैध। ये भारत में ईरान के रास्ते तुर्कमेनिस्तान सीमा से 8 दिसंबर 2025 को प्रवेश किया। अभी दिल्ली के तिलक विहार में रह रही हैं, पता C-45, Tilak Vihar, New Delhi-110018।
- **अधिकारी:** शरण का कारण?
- **वकील:** हज़ारा (शिया अल्पसंख्यक) होने के कारण तालिबान द्वारा उत्पीड़न। इनके पिता मोहम्मद हकीमी, पासपोर्ट AF02345678, 12 अगस्त 2024 को काबुल में तालिबान लड़ाकों द्वारा अपहृत, अभी तक कोई जानकारी नहीं। माँ ज़ैनब हकीमी, AF03456789, साथ में शरण ली। तीन बच्चे: अली (2010), फ़ातिमा (2012), हसन (2015), सभी के पास अफ़ग़ानी टज़किरा ID क्रमशः AF-2018-12345, AF-2018-12346, AF-2018-12347।
- **अधिकारी:** फ़ाइल संख्या UNHCR-IN-2026-ASL-00987। प्रारंभिक साक्षात्कार 22 अप्रैल 2026 को दोपहर 2:00 बजे UNHCR कार्यालय, 2 Lodhi Estate, New Delhi-110003। संपर्क v.mehta@unhcr.org, दूरभाष 011-4321 5678।

---

## 📊 Resumen de tipos de PII cubiertos (oficinas de migración)

| Categoría | Ejemplos representativos |
|---|---|
| 📘 **Pasaportes (múltiples países)** | Colombiano 19.456.789, US 512345678, Senegalés A0123456, Chino E45678901, Sirio N0123456, Iraní A12345678, Venezolano 12345678, Eritreo ER0123456, Uzbeco FA1234567, Japonés TK1234567, Maliense A0123456, Vietnamita B1234567, Argentino AA123456, Alemán C12345678, etc. |
| 🆔 **NIE / Tarjeta de residencia / UCI / Aadhaar** | NIE X1234567-X, TCF-2022/009876, UCI 7890-1234, A-098-765-432, PR-card AB-12345-6789, IT-2024-PS-00987, Aadhaar 1234 5678 9012 |
| 🛂 **Visas / EAD / Permisos** | F-1 SEVIS N0012345678, J-1, Z-visa, AT-2026/008741, e-TV-2024-US-00987, VHM-2026/00987, AE-2024-WP-00987 |
| 👨‍👩‍👧‍👦 **Datos de familiares múltiples** | Cónyuge, hijos con sus propios pasaportes, fechas de nacimiento, países de origen |
| 🏠 **Direcciones internacionales** | Calle Mayor 45 Madrid, 1455 Market St SF, 45 rue de la Roquette Paris, Friedrichstraße 123 Berlin, 六本木1-2-3 Tokyo, الخالدية أبوظبي, Бауманская 15 Москва, अंधेरी पूर्व मुंबई |
| 💳 **Cuentas bancarias (multipaís)** | ES80 0182..., FR76 1027..., DE89 3704..., AE070331234..., IT60 X054..., AE07033... |
| 💰 **Salarios / Ingresos** | 1.850 €/mes, $185,000/yr, 65.000 €/año, 45,000 元/月, 850万円, 12,000 درهم, 75,000 ₽/мес |
| 🏢 **Empleadores y empresas** | Logística Martínez S.L. (CIF), Salesforce (SF-29481), Siemens AG, Microsoft Asia, Sony Interactive, Филиал Amazon India, 株式会社 ООО |
| 🏥 **Datos médicos sensibles** | PTSD, HbA1c, medicación, hospitalizaciones, alergías, psiquiatra forense |
| 🆔 **Identificaciones civiles locales** | CNIC pakistaní 17301-1234567-1, Nadra ID, RIF V-12345678-9, ID nacional 784199512345678, Tazkira AF-2018-12345, Steuer-ID 12 345 678 901 |
| 📋 **Números de expediente / caso** | EX-2026/0098745, AS-2026/004512, IOE-09873452, MSC2190456123, BAMF-2026-AA-00987, CONARE-2026/000987, UNHCR-CN-2026-ASL-00987 |
| ⚖️ **Datos legales / abogados** | Colegio de abogados, registros de letrados, poderes, sentencias, antecedentes penales |
| 🛂 **Antecedentes penales** | Certificados apostillados, FIR 234/2024, récord policial |
| 👶 **Datos de nacimiento / filiación** | Actas de nacimiento, partidas, certificaciones consulares |
| 🏠 **Datos de vivienda** | Contratos de alquiler, ID de propietario, catastros |
| 🚨 **Datos de detenidos / desaparecidos** | Familiares en prisión, status de paradero, lugares de detención |
| 🌐 **Varios**: ID biométrico, huellas, sponsor, garante, contacto de emergencia, fechas de audiencias |

## 🧪 Casos de uso recomendados para testing

1. **Multilingüismo total**: los 11 idiomas con jerga jurídica/migratoria específica.
2. **Multi-país en un solo diálogo**: aplicante de país A, familia en país B, refugio solicitado en país C.
3. **Múltiples personas en una conversación**: aplicante, cónyuge, hijos, padre/madre, hermanos, abogado, garante, sponsor, traductor — todos con sus PII.
4. **PII en formato legal**: leyes (§18 Aufenthaltsgesetz, §18), artículos de ley, resoluciones normativas, citas de jurisprudencia.
5. **Fechas críticas**: fechas de expedición, vencimiento, nacimiento, entrada, audiencias — riesgo de confundir fechas de "trámite" con "personales".
6. **Identificadores oficiales extranjeros**: A-number (US), UCI (Canadá), CNIC (Pakistán), Tazkira (Afganistán), RIF (Venezuela), CNH (Brasil), MyKad (Malasia) — alta variedad.
7. **Datos sensibles emocionales**: tortura, persecución, familiares muertos/desaparecidos — el modelo debe priorizar la PII por encima del contexto narrativo.
8. **PII en alfabetos múltiples**: cirílico, hanzi, kanji, devanagari, árabe, ge'ez (eritreo) — para OCR o transcripción fonética.
9. **Documentos sustitutivos**: para personas sin pasaporte (Tazkira, partida de nacimiento, constancia de desplazado).
10. **Números de expediente y caso**: deben distinguirse de PII personal (AS-2026/004512 vs. SSN 123-45-6789).
11. **Direcciones con múltiples formatos**: occidental (calle/número/ciudad/CP), japonés (prefectura/barrio/ban/número), árabe (حي/شارع/بناية/شقة), indio (colonia/barrio/pincode).
12. **Teléfonos internacionales**: +34, +1, +44, +49, +33, +81, +86, +971, +7, +91, +20 — diferentes longitudes y formatos.
13. **Falsos positivos potenciales**: números de resolución legal (A-2024-WP-00987), fechas de audiencias, importes de fianzas, citas de artículos legales, etc.

> ⚠️ **Nota:** Todos los datos son ficticios y generados para testing. Cualquier coincidencia con personas reales, oficinas o expedientes reales es accidental y no intencionada.
