# Clasificador de consultas entrantes

**Versión:** 1.0  
**Total de mensajes:** 40  
**Idiomas:** es (Español), en (English), pt (Português), fr (Français)  
**Formatos:** email, chat  

## Categorías

- **`renovacion_visa`** — Renovación de visa existente (próxima a vencer o ya vencida)
- **`primera_solicitud`** — Primera solicitud de visa (nunca ha tramitado)
- **`asilo`** — Solicitud de asilo o protección internacional/refugio
- **`consulta_estatus`** — Consulta sobre el estado de un trámite ya iniciado
- **`solicitud_documentos`** — Pedido de certificados, constancias o documentos oficiales
- **`queja`** — Queja, reclamo o expresión de insatisfacción con el servicio

## Niveles de dificultad

- **facil** — Mensaje claro, categoría inequívoca
- **medio** — Algún elemento distractorio pero la categoría es clara
- **dificil** — Mezcla elementos de 2+ categorías, requiere lectura cuidadosa
- **ambiguo** — Honestamente podría ser 2 categorías — el modelo debe elegir la más probable

## Mensajes

| ID | Lang | Formato | Categoría | Dificultad | Mensaje |
|----|------|---------|-----------|-----------|---------|
| msg-001 | es | email | `renovacion_visa` | facil | Estimados señores de la Oficina de Migración,  Mi visa de trabajo temporal vence el 15 de marzo del próximo... |
| msg-002 | es | chat | `renovacion_visa` | facil | hola buenas tardes, mi visa de trabajo se me vence en 2 meses y no sé qué hacer, me pueden ayudar? |
| msg-003 | en | email | `renovacion_visa` | facil | Dear Migration Office,  I am writing to inquire about the renewal process for my work visa, which expires i... |
| msg-004 | en | chat | `renovacion_visa` | medio | hi! my student visa expires in 3 months. do I need to start the renewal from scratch or is there a simplifi... |
| msg-005 | pt | email | `renovacion_visa` | facil | Prezados,  Meu visto de trabalho vence em 45 dias. Gostaria de saber qual é o procedimento para renová-lo e... |
| msg-006 | fr | email | `renovacion_visa` | facil | Madame, Monsieur,  Mon visa de travail expire dans deux mois. Je souhaite connaître la procédure de renouve... |
| msg-007 | es | email | `primera_solicitud` | facil | Buenos días,  Soy colombiana y nunca he tramitado una visa para entrar a su país. Me han ofrecido un puesto... |
| msg-008 | es | chat | `primera_solicitud` | facil | Buenas, nunca he pedido visa antes. Quiero ir a estudiar una maestría de 2 años. Por dónde empiezo? Cuánto ... |
| msg-009 | en | email | `primera_solicitud` | medio | Hello,  I am a citizen of India and I would like to apply for a student visa to attend a one-year MBA progr... |
| msg-010 | en | chat | `primera_solicitud` | medio | hi there, my wife and i want to apply for tourist visas. we've never done this before. is there a way to do... |
| msg-011 | pt | email | `primera_solicitud` | facil | Olá, bom dia,  Sou brasileiro e gostaria de solicitar um visto de trabalho pela primeira vez. Recebi uma pr... |
| msg-012 | fr | email | `primera_solicitud` | facil | Bonjour,  Je suis haïtien et je n'ai jamais fait de demande de visa. Je voudrais obtenir un visa touristiqu... |
| msg-013 | es | email | `asilo` | facil | Señores Oficina de Migración,  Me dirijo a ustedes en una situación de suma urgencia. Soy periodista indepe... |
| msg-014 | es | chat | `asilo` | facil | Hola, necesito ayuda urgente. Me quieren matar en mi país por ser homosexual, llegué ayer. Dónde puedo pedi... |
| msg-015 | en | email | `asilo` | facil | To whom it may concern,  I am writing to apply for asylum in your country. I am a human rights activist fro... |
| msg-016 | en | chat | `asilo` | medio | i fled my country 3 weeks ago because of political violence. i'm staying with a cousin but i don't know wha... |
| msg-017 | pt | email | `asilo` | facil | Prezados senhores,  Sou engenheiro e atuo em um movimento político de oposição em meu país. Fui preso e tor... |
| msg-018 | fr | email | `asilo` | facil | Madame, Monsieur,  Ma vie est en danger dans mon pays en raison de mon engagement pour les droits des minor... |
| msg-019 | es | email | `consulta_estatus` | facil | Estimados,  Presenté mi solicitud de visa de trabajo hace tres meses y aún no he recibido respuesta. Mi núm... |
| msg-020 | es | chat | `consulta_estatus` | facil | buenas tardes, en qué va mi trámite? lo presenté hace como 4 meses y no sé nada |
| msg-021 | en | email | `consulta_estatus` | facil | Hello,  I submitted my residency renewal application six weeks ago (reference number: RES-2024-78901). I wo... |
| msg-022 | en | chat | `consulta_estatus` | medio | hey, any update on case #2024-FAM-9923? I submitted it 2 months ago. the website says 'in process' but I wa... |
| msg-023 | pt | email | `consulta_estatus` | facil | Prezados,  Gostaria de saber o status do meu processo de visto, número 2024-BR-33542, enviado há 90 dias. A... |
| msg-024 | fr | email | `consulta_estatus` | facil | Bonjour,  J'ai déposé une demande de regroupement familial il y a cinq mois (dossier n° 2024-RF-12789). Pou... |
| msg-025 | es | email | `solicitud_documentos` | facil | Buenas tardes,  Necesito obtener una constancia de residencia vigente para presentarla en un trámite bancar... |
| msg-026 | es | chat | `solicitud_documentos` | facil | cómo saco un certificado de movimientos migratorios? lo necesito para un trabajo |
| msg-027 | en | email | `solicitud_documentos` | facil | Dear Sir/Madam,  I require an official certificate confirming my legal residence in the country for the pas... |
| msg-028 | en | chat | `solicitud_documentos` | medio | hi, where do I get a copy of my original residence permit? I lost mine and need it for a new job. can I dow... |
| msg-029 | pt | email | `solicitud_documentos` | facil | Prezados,  Preciso de uma segunda via do meu Cartão de Residência, que foi extraviado. Qual é o procediment... |
| msg-030 | fr | email | `solicitud_documentos` | facil | Madame, Monsieur,  Je souhaiterais obtenir un duplicata de ma carte de séjour, qui a été volée le mois dern... |
| msg-031 | es | email | `queja` | facil | Señores,  Quiero expresar mi profunda insatisfacción con el servicio recibido. El pasado martes esperé más ... |
| msg-032 | es | chat | `queja` | facil | esto es un robo, llevo 4 meses esperando mi visa y nadie me contesta los correos. una vergüenza |
| msg-033 | en | email | `queja` | facil | To whom it may concern,  I am writing to file a formal complaint about the unacceptable delay in processing... |
| msg-034 | en | chat | `queja` | medio | this is ridiculous. I have called 6 times in the last month and nobody picks up. your website says 30 days ... |
| msg-035 | pt | email | `queja` | facil | Prezados,  Estou extremamente insatisfeito com o atendimento recebido na última sexta-feira. O funcionário ... |
| msg-036 | fr | email | `queja` | facil | Madame, Monsieur,  Je me permets de vous écrire pour exprimer mon mécontentement. Après trois visites à vos... |
| msg-037 | es | email | `queja` | ambiguo | Estimados,  Llevo más de cuatro meses esperando una respuesta sobre mi solicitud y nadie me ha dado una exp... |
| msg-038 | en | email | `renovacion_visa` | ambiguo | Hello,  My visa expired last week and I didn't receive any renewal notice. I tried calling your office but ... |
| msg-039 | es | chat | `asilo` | ambiguo | hola, vengo de Venezuela, llegué hace 3 semanas. necesito saber qué tipo de trámite puedo hacer aquí. no qu... |
| msg-040 | es | email | `solicitud_documentos` | ambiguo | Señores,  Urgente: llevo dos semanas esperando que me envíen los documentos que solicité. Ya mandé tres cor... |

## Mensajes completos (para imprimir o repartir)

### msg-001 — `renovacion_visa` (es, email, facil)

```
Estimados señores de la Oficina de Migración,

Mi visa de trabajo temporal vence el 15 de marzo del próximo año y quisiera iniciar el proceso de renovación lo antes posible. ¿Podrían indicarme qué documentos necesito presentar y cuál es el plazo máximo para hacerlo?

Agradezco su atención.

Atentamente,
Carlos Mendoza
Pasaporte: 12.345.678
```

### msg-002 — `renovacion_visa` (es, chat, facil)

```
hola buenas tardes, mi visa de trabajo se me vence en 2 meses y no sé qué hacer, me pueden ayudar?
```

### msg-003 — `renovacion_visa` (en, email, facil)

```
Dear Migration Office,

I am writing to inquire about the renewal process for my work visa, which expires in approximately six weeks. I have been employed at the same company for the past two years and would like to continue working legally in the country.

Could you please send me the list of required documents and the applicable fees?

Kind regards,
Sarah Johnson
Foreign Resident ID: 9876543
```

### msg-004 — `renovacion_visa` (en, chat, medio)

```
hi! my student visa expires in 3 months. do I need to start the renewal from scratch or is there a simplified process? thanks
```

### msg-005 — `renovacion_visa` (pt, email, facil)

```
Prezados,

Meu visto de trabalho vence em 45 dias. Gostaria de saber qual é o procedimento para renová-lo e se posso continuar trabalhando enquanto o processo está em andamento.

Obrigado,
Rafael Souza
Passaporte: BR123456
```

### msg-006 — `renovacion_visa` (fr, email, facil)

```
Madame, Monsieur,

Mon visa de travail expire dans deux mois. Je souhaite connaître la procédure de renouvellement ainsi que les documents à fournir.

Cordialement,
Amadou Diallo
Passeport: FR87654321
```

### msg-007 — `primera_solicitud` (es, email, facil)

```
Buenos días,

Soy colombiana y nunca he tramitado una visa para entrar a su país. Me han ofrecido un puesto de trabajo como ingeniera de software en una empresa de su capital y quisiera saber qué tipo de visa necesito solicitar y cuáles son los requisitos.

Quedo atenta a su respuesta.

Saludos cordiales,
Laura Restrepo
```

### msg-008 — `primera_solicitud` (es, chat, facil)

```
Buenas, nunca he pedido visa antes. Quiero ir a estudiar una maestría de 2 años. Por dónde empiezo? Cuánto cuesta?
```

### msg-009 — `primera_solicitud` (en, email, medio)

```
Hello,

I am a citizen of India and I would like to apply for a student visa to attend a one-year MBA program at a university in your country. This would be my first time applying for any kind of visa. Could you please guide me through the process and let me know the approximate timeline?

Thank you,
Priya Patel
```

### msg-010 — `primera_solicitud` (en, chat, medio)

```
hi there, my wife and i want to apply for tourist visas. we've never done this before. is there a way to do it online or do we need to come in person? thanks!
```

### msg-011 — `primera_solicitud` (pt, email, facil)

```
Olá, bom dia,

Sou brasileiro e gostaria de solicitar um visto de trabalho pela primeira vez. Recebi uma proposta de emprego de uma empresa no exterior. Quais são os documentos necessários e quanto tempo leva o processo?

Obrigado,
Marcos Lima
```

### msg-012 — `primera_solicitud` (fr, email, facil)

```
Bonjour,

Je suis haïtien et je n'ai jamais fait de demande de visa. Je voudrais obtenir un visa touristique pour rendre visite à ma famille pendant trois semaines. Pouvez-vous m'indiquer la marche à suivre ?

Merci d'avance,
Jean Pierre
```

### msg-013 — `asilo` (es, email, facil)

```
Señores Oficina de Migración,

Me dirijo a ustedes en una situación de suma urgencia. Soy periodista independiente en mi país de origen y he recibido amenazas de muerte debido a mis investigaciones. Temo por mi vida y la de mi familia. Solicito formalmente protección internacional y asilo político en su país.

Adjunto documentación de respaldo.

Atentamente,
Roberto Salazar
```

### msg-014 — `asilo` (es, chat, facil)

```
Hola, necesito ayuda urgente. Me quieren matar en mi país por ser homosexual, llegué ayer. Dónde puedo pedir refugio?
```

### msg-015 — `asilo` (en, email, facil)

```
To whom it may concern,

I am writing to apply for asylum in your country. I am a human rights activist from my home country, and I have been persecuted, detained, and threatened because of my work. I fear for my life if I return. I have supporting documentation from international organizations.

Please advise me on the next steps.

Sincerely,
Fatima Al-Rashid
```

### msg-016 — `asilo` (en, chat, medio)

```
i fled my country 3 weeks ago because of political violence. i'm staying with a cousin but i don't know what to do next. can i apply for refugee status? i'm scared they'll deport me
```

### msg-017 — `asilo` (pt, email, facil)

```
Prezados senhores,

Sou engenheiro e atuo em um movimento político de oposição em meu país. Fui preso e torturado por isso. Preciso urgentemente de proteção internacional. Como devo proceder para formalizar meu pedido de refúgio?

Atenciosamente,
João Mendes
```

### msg-018 — `asilo` (fr, email, facil)

```
Madame, Monsieur,

Ma vie est en danger dans mon pays en raison de mon engagement pour les droits des minorités. J'ai fui il y a deux semaines et je me trouve actuellement dans votre pays. Je souhaite déposer une demande d'asile. Pouvez-vous m'indiquer la procédure ?

Cordialement,
Aminata Traoré
```

### msg-019 — `consulta_estatus` (es, email, facil)

```
Estimados,

Presenté mi solicitud de visa de trabajo hace tres meses y aún no he recibido respuesta. Mi número de expediente es 2024-MV-45821. ¿Podrían informarme en qué estado se encuentra mi trámite?

Gracias,
María González
```

### msg-020 — `consulta_estatus` (es, chat, facil)

```
buenas tardes, en qué va mi trámite? lo presenté hace como 4 meses y no sé nada
```

### msg-021 — `consulta_estatus` (en, email, facil)

```
Hello,

I submitted my residency renewal application six weeks ago (reference number: RES-2024-78901). I would like to check the current status. The deadline for the decision is approaching and I need to plan accordingly.

Thank you,
James O'Brien
```

### msg-022 — `consulta_estatus` (en, chat, medio)

```
hey, any update on case #2024-FAM-9923? I submitted it 2 months ago. the website says 'in process' but I want to know if there's an actual estimated date
```

### msg-023 — `consulta_estatus` (pt, email, facil)

```
Prezados,

Gostaria de saber o status do meu processo de visto, número 2024-BR-33542, enviado há 90 dias. Ainda não recebi nenhuma comunicação.

Atenciosamente,
Ana Silva
```

### msg-024 — `consulta_estatus` (fr, email, facil)

```
Bonjour,

J'ai déposé une demande de regroupement familial il y a cinq mois (dossier n° 2024-RF-12789). Pourriez-vous me dire où en est l'instruction de mon dossier ?

Cordialement,
Mariam Koné
```

### msg-025 — `solicitud_documentos` (es, email, facil)

```
Buenas tardes,

Necesito obtener una constancia de residencia vigente para presentarla en un trámite bancario. ¿Podrían indicarme cuál es el procedimiento, los documentos requeridos y el costo?

Saludos,
Pedro Ramírez
```

### msg-026 — `solicitud_documentos` (es, chat, facil)

```
cómo saco un certificado de movimientos migratorios? lo necesito para un trabajo
```

### msg-027 — `solicitud_documentos` (en, email, facil)

```
Dear Sir/Madam,

I require an official certificate confirming my legal residence in the country for the past five years. This document is required by the tax authority. Please let me know how to request it.

Best regards,
Michael Chen
```

### msg-028 — `solicitud_documentos` (en, chat, medio)

```
hi, where do I get a copy of my original residence permit? I lost mine and need it for a new job. can I download it or do I need to come in?
```

### msg-029 — `solicitud_documentos` (pt, email, facil)

```
Prezados,

Preciso de uma segunda via do meu Cartão de Residência, que foi extraviado. Qual é o procedimento para solicitação e quais documentos devo apresentar?

Atenciosamente,
Beatriz Costa
```

### msg-030 — `solicitud_documentos` (fr, email, facil)

```
Madame, Monsieur,

Je souhaiterais obtenir un duplicata de ma carte de séjour, qui a été volée le mois dernier. Pourriez-vous m'indiquer les documents à fournir et les délais de traitement ?

Cordialement,
Ousmane Coulibaly
```

### msg-031 — `queja` (es, email, facil)

```
Señores,

Quiero expresar mi profunda insatisfacción con el servicio recibido. El pasado martes esperé más de cinco horas en la fila de atención al público sin que nadie me atendiera. Cuando finalmente pude hablar con un funcionario, me trató de manera grosera y no resolvió mi consulta. Esto es inaceptable y espero una respuesta formal.

Atentamente,
Elena Vargas
```

### msg-032 — `queja` (es, chat, facil)

```
esto es un robo, llevo 4 meses esperando mi visa y nadie me contesta los correos. una vergüenza
```

### msg-033 — `queja` (en, email, facil)

```
To whom it may concern,

I am writing to file a formal complaint about the unacceptable delay in processing my application (case #2024-WV-66789). I submitted all required documents five months ago and have received no communication whatsoever, despite multiple follow-up emails. This level of service is deeply disappointing.

I look forward to your prompt response.

Regards,
David Park
```

### msg-034 — `queja` (en, chat, medio)

```
this is ridiculous. I have called 6 times in the last month and nobody picks up. your website says 30 days for tourist visas, mine has been in process for 90. fix this
```

### msg-035 — `queja` (pt, email, facil)

```
Prezados,

Estou extremamente insatisfeito com o atendimento recebido na última sexta-feira. O funcionário que me atendeu foi grosseiro, não soube responder minhas perguntas e me mandou voltar outro dia sem resolver nada. Exijo uma posição oficial sobre este ocorrido.

Atenciosamente,
Fernando Almeida
```

### msg-036 — `queja` (fr, email, facil)

```
Madame, Monsieur,

Je me permets de vous écrire pour exprimer mon mécontentement. Après trois visites à vos bureaux et six mois d'attente, mon dossier n'avance pas. Vos délais sont inacceptables et personne ne prend la peine de me répondre.

Je souhaite une réponse officielle.

Cordialement,
Sophie Mbarga
```

### msg-037 — `queja` (es, email, ambiguo)

```
Estimados,

Llevo más de cuatro meses esperando una respuesta sobre mi solicitud y nadie me ha dado una explicación. No sé si mi expediente se perdió, si falta algún documento, o si simplemente están atrasados. Necesito una respuesta ya. Esto ya parece una burla.

Atentamente,
José Luis Pérez
```
**Nota:** _queja o consulta_estatus — la persona consulta pero con tono de queja_

### msg-038 — `renovacion_visa` (en, email, ambiguo)

```
Hello,

My visa expired last week and I didn't receive any renewal notice. I tried calling your office but no one answered. I'm really stressed because I might be working illegally right now. Can you help me sort this out quickly?

Thanks,
Anna Kowalski
```
**Nota:** _renovacion_visa o queja — el mensaje es principalmente sobre renovar, pero el tono es de queja_

### msg-039 — `asilo` (es, chat, ambiguo)

```
hola, vengo de Venezuela, llegué hace 3 semanas. necesito saber qué tipo de trámite puedo hacer aquí. no quiero volver a mi país pero tampoco sé si califico para asilo. me pueden orientar?
```
**Nota:** _asilo o consulta_estatus — describe su situación de posible asilo pero pide orientación_

### msg-040 — `solicitud_documentos` (es, email, ambiguo)

```
Señores,

Urgente: llevo dos semanas esperando que me envíen los documentos que solicité. Ya mandé tres correos y nadie responde. Es para ayer, los necesito para una audiencia judicial. Por favor, atiendan esto de una vez.

Atentamente,
Lic. Daniela Soto
```
**Nota:** _solicitud_documentos o queja — pide documentos pero el tono es claramente de queja_
