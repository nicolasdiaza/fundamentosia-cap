# Validador de alertas en expedientes

**Versión:** 1.0  
**Total de casos:** 28  

**⚠️ Restricción clave:** _El modelo NO debe generar aprobación ni rechazo. Solo levanta alertas para revisión humana._

## Tipos de alerta

- **`documento`** — Problemas con documentos (vencimiento, inconsistencia, faltante, ilegible, tipo incorrecto)
- **`overstay`** — Overstay anterior (estadía prolongée más allá del permiso)
- **`cambio_empleador`** — Cambios de empleador recientes o problemáticos (frecuencia, industria, notificación)

## Niveles de severidad

- **alta** — Bloqueante. Requiere atención inmediata.
- **media** — Relevante. Documentar y dar seguimiento.
- **baja** — Marginal. Para registro, no bloqueante.

## Niveles de dificultad

- **facil** — Caso claro, 0-1 alertas evidentes
- **medio** — Caso con 2 alertas o 1 alerta que requiere interpretación
- **dificil** — Caso con 3+ alertas, o alertas superpuestas
- **ambiguo** — Caso borderline — podría tener o no alerta según la política de la oficina

## Formato esperado de salida (JSON)

```json
{
  "alertas": [
    {
      "tipo": "documento|overstay|cambio_empleador",
      "severidad": "alta|media|baja",
      "descripcion": "explicación de la alerta",
      "evidencia": "el dato concreto que la disparó"
    }
  ],
  "sin_alertas": false,
  "requiere_revision_humana": true,
  "decision_final": null
}
```

**Nunca** debe haber un valor distinto de `null` en `decision_final`.

## Resumen de casos

| ID | Dificultad | Alertas | Resumen |
|----|-----------|---------|---------|
| case-001 | facil | 0 (ninguna) | Profesional estable, 4 años mismo empleador, todo en regla |
| case-011 | facil | 0 (ninguna) | Estudiante internacional, estable, sin empleador |
| case-014 | facil | 0 (ninguna) | Reunificación familiar, sin empleador, todo en regla |
| case-017 | facil | 0 (ninguna) | Residente permanente de largo plazo, expediente impecable |
| case-021 | facil | 0 (ninguna) | Renovación con cambio menor de domicilio |
| case-025 | facil | 0 (ninguna) | Profesional en transferencia intra-corporativa, documentación impecable |
| case-002 | facil | 1 (documento) | Pasaporte vence en 45 días (URGENTE) |
| case-003 | facil | 1 (overstay) | Overstay de 15 días hace 2 años |
| case-004 | medio | 1 (cambio_empleador) | 3 empleadores en 18 meses (todos notificados) |
| case-005 | medio | 1 (documento) | Inconsistencia de nombre en documentos (1 letra) |
| case-010 | facil | 1 (documento) | Falta el certificado de antecedentes penales |
| case-013 | medio | 1 (overstay) | Overstay de 60 días hace 3 años (mitigado) |
| case-016 | medio | 1 (documento) | Documento de identidad con daños (parcialmente ilegible) |
| case-006 | medio | 2 (overstay, overstay) | 2 overstays previos (30 y 45 días) |
| case-007 | medio | 2 (documento, cambio_empleador) | Pasaporte vence en 2 meses + cambio de empleador sin notificación formal |
| case-008 | medio | 2 (overstay, cambio_empleador) | Overstay reciente + 4 empleadores en 2 años |
| case-015 | dificil | 2 (cambio_empleador, cambio_empleador) | Visa de trabajo pero ahora freelance — posible irregularidad |
| case-020 | medio | 1 (cambio_empleador) | Visa de trabajo para software, trabaja en construcción |
| case-023 | medio | 2 (documento, documento) | Pasaporte vence en 90 días + falta acta apostillada |
| case-009 | dificil | 3 (documento, overstay, cambio_empleador) | Caso crítico: pasaporte vencido, overstay grave, patrón de cambio de empleador |
| case-019 | dificil | 3 (overstay, documento, cambio_empleador) | Asilo con overstay en otro país, documento dañado, trabajo informal |
| case-026 | dificil | 4 (overstay, overstay, cambio_empleador, documento) | Múltiples problemas: overstays, cambios de empleador, documento dañado |
| case-012 | ambiguo | 0 (ninguna) | Cambio de雇主 reciente PERO notificado y legítimo — NO debería ser alerta |
| case-018 | ambiguo | 0 (ninguna) | Overstay 'técnico' de 2 días por vuelo cancelado — multado y resuelto |
| case-022 | ambiguo | 1 (overstay) | Overstay de hace 10 años — historial impecable desde entonces |
| case-024 | ambiguo | 0 (ninguna) | Transición de visa de trabajo a independiente — ¿alerta de cambio de empleador? |
| case-027 | ambiguo | 1 (cambio_empleador) | Empleo en industria relacionada, no idéntica — ¿es alerta? |
| case-028 | ambiguo | 1 (documento) | Pasaporte vence en exactamente 6 meses — umbral de muchas aerolíneas |

## Casos completos

### case-001 — facil
_Profesional estable, 4 años mismo empleador, todo en regla_

```json
{
  "id": "case-001",
  "difficulty": "facil",
  "summary": "Profesional estable, 4 años mismo empleador, todo en regla",
  "person": {
    "nombre": "Carlos Mendoza",
    "nacionalidad": "Argentina",
    "fecha_nacimiento": "1988-04-12",
    "id_documento": "AR-30123456"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2022-03-15",
    "fecha_vencimiento": "2026-03-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "AA1234567",
      "fecha_emision": "2020-01-10",
      "fecha_vencimiento": "2030-01-10",
      "pais_emisor": "Argentina",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2022-001",
      "fecha_emision": "2022-03-01",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    },
    {
      "tipo": "certificado_antecedentes",
      "numero": "CA-2022-789",
      "fecha_emision": "2022-02-20",
      "fecha_vencimiento": "2024-02-20",
      "pais_emisor": "Argentina",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2022-03-10",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "residencia"
    }
  ],
  "previous_visas": [
    {
      "tipo": "trabajo",
      "fecha_emision": "2018-06-01",
      "fecha_vencimiento": "2022-03-15",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "TechCorp SA",
      "industria": "software",
      "fecha_inicio": "2022-03-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": []
}
```

### case-011 — facil
_Estudiante internacional, estable, sin empleador_

```json
{
  "id": "case-011",
  "difficulty": "facil",
  "summary": "Estudiante internacional, estable, sin empleador",
  "person": {
    "nombre": "Marie Dubois",
    "nacionalidad": "Francia",
    "fecha_nacimiento": "1999-08-23",
    "id_documento": "FR-9876543"
  },
  "current_visa": {
    "tipo": "estudiante",
    "fecha_emision": "2023-09-01",
    "fecha_vencimiento": "2025-08-31",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "FR22AB12345",
      "fecha_emision": "2022-05-15",
      "fecha_vencimiento": "2032-05-15",
      "pais_emisor": "Francia",
      "status": "valido"
    },
    {
      "tipo": "carta_universidad",
      "numero": "UNI-2023-4455",
      "fecha_emision": "2023-08-15",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    },
    {
      "tipo": "comprobante_solvencia",
      "numero": "CS-2023-100",
      "fecha_emision": "2023-08-20",
      "fecha_vencimiento": "2024-08-20",
      "pais_emisor": "Francia",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-08-25",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "estudios"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2022-07-01",
      "fecha_vencimiento": "2022-12-31",
      "pais": "Local"
    }
  ],
  "employment_history": [],
  "planted_alerts": []
}
```

### case-014 — facil
_Reunificación familiar, sin empleador, todo en regla_

```json
{
  "id": "case-014",
  "difficulty": "facil",
  "summary": "Reunificación familiar, sin empleador, todo en regla",
  "person": {
    "nombre": "Yusuf Demir",
    "nacionalidad": "Turquía",
    "fecha_nacimiento": "1978-11-30",
    "id_documento": "TR-45678901"
  },
  "current_visa": {
    "tipo": "reunificacion_familiar",
    "fecha_emision": "2023-01-15",
    "fecha_vencimiento": "2028-01-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "TR-U1234567",
      "fecha_emision": "2019-06-20",
      "fecha_vencimiento": "2029-06-20",
      "pais_emisor": "Turquía",
      "status": "valido"
    },
    {
      "tipo": "acta_matrimonio",
      "numero": "AM-2022-88",
      "fecha_emision": "2010-05-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Turquía",
      "status": "valido"
    },
    {
      "tipo": "certificado_antecedentes",
      "numero": "CA-TR-2022-500",
      "fecha_emision": "2022-11-05",
      "fecha_vencimiento": "2023-11-05",
      "pais_emisor": "Turquía",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-01-10",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "reunificacion_familiar"
    }
  ],
  "previous_visas": [],
  "employment_history": [],
  "planted_alerts": []
}
```

### case-017 — facil
_Residente permanente de largo plazo, expediente impecable_

```json
{
  "id": "case-017",
  "difficulty": "facil",
  "summary": "Residente permanente de largo plazo, expediente impecable",
  "person": {
    "nombre": "Olga Petrova",
    "nacionalidad": "Rusia",
    "fecha_nacimiento": "1973-05-08",
    "id_documento": "RU-77889900"
  },
  "current_visa": {
    "tipo": "residencia_permanente",
    "fecha_emision": "2014-09-01",
    "fecha_vencimiento": null,
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "RU-PS7788990",
      "fecha_emision": "2018-03-12",
      "fecha_vencimiento": "2028-03-12",
      "pais_emisor": "Rusia",
      "status": "valido"
    },
    {
      "tipo": "carta_residencia_permanente",
      "numero": "RP-2014-001",
      "fecha_emision": "2014-09-01",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2014-08-20",
      "fecha_salida": "2015-12-15",
      "pais": "Local",
      "proposito": "trabajo"
    },
    {
      "fecha_entrada": "2016-02-01",
      "fecha_salida": "2016-04-10",
      "pais": "Rusia",
      "proposito": "visita_familiar"
    },
    {
      "fecha_entrada": "2016-05-01",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "residencia"
    }
  ],
  "previous_visas": [
    {
      "tipo": "trabajo",
      "fecha_emision": "2014-09-01",
      "fecha_vencimiento": "2017-09-01",
      "pais": "Local"
    },
    {
      "tipo": "residencia_temporal",
      "fecha_emision": "2017-09-01",
      "fecha_vencimiento": "2019-09-01",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "Consulting Partners",
      "industria": "consultoria",
      "fecha_inicio": "2014-09-15",
      "fecha_fin": null,
      "tipo_visa": "residencia_permanente",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": []
}
```

### case-021 — facil
_Renovación con cambio menor de domicilio_

```json
{
  "id": "case-021",
  "difficulty": "facil",
  "summary": "Renovación con cambio menor de domicilio",
  "person": {
    "nombre": "Camila Rojas",
    "nacionalidad": "Chile",
    "fecha_nacimiento": "1993-07-19",
    "id_documento": "CL-22334455"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-02-01",
    "fecha_vencimiento": "2028-02-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "CL-P2233445",
      "fecha_emision": "2021-04-10",
      "fecha_vencimiento": "2031-04-10",
      "pais_emisor": "Chile",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-789",
      "fecha_emision": "2024-01-20",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    },
    {
      "tipo": "comprobante_domicilio",
      "numero": "CD-2024-1001",
      "fecha_emision": "2024-01-15",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2024-01-25",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "trabajo",
      "fecha_emision": "2020-02-01",
      "fecha_vencimiento": "2024-02-01",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "DataInsights",
      "industria": "analisis_datos",
      "fecha_inicio": "2020-02-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": []
}
```

### case-025 — facil
_Profesional en transferencia intra-corporativa, documentación impecable_

```json
{
  "id": "case-025",
  "difficulty": "facil",
  "summary": "Profesional en transferencia intra-corporativa, documentación impecable",
  "person": {
    "nombre": "Lin Wang",
    "nacionalidad": "China",
    "fecha_nacimiento": "1985-12-03",
    "id_documento": "CN-99887766"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-06-01",
    "fecha_vencimiento": "2027-06-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "CN-EA9988776",
      "fecha_emision": "2023-02-20",
      "fecha_vencimiento": "2033-02-20",
      "pais_emisor": "China",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-ICT-005",
      "fecha_emision": "2024-05-15",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    },
    {
      "tipo": "carta_transferencia_ICT",
      "numero": "ICT-2024-200",
      "fecha_emision": "2024-05-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2024-05-25",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo_ICT"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "AsiaSubsidiary Corp",
      "industria": "tecnologia",
      "fecha_inicio": "2018-03-01",
      "fecha_fin": "2024-05-31",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "LocalSubsidiary Corp",
      "industria": "tecnologia",
      "fecha_inicio": "2024-06-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo_ICT",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": []
}
```

### case-002 — facil
_Pasaporte vence en 45 días (URGENTE)_

```json
{
  "id": "case-002",
  "difficulty": "facil",
  "summary": "Pasaporte vence en 45 días (URGENTE)",
  "person": {
    "nombre": "Ana López",
    "nacionalidad": "Colombia",
    "fecha_nacimiento": "1995-02-14",
    "id_documento": "CO-52345678"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-01-15",
    "fecha_vencimiento": "2026-01-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "CO-CC5234567",
      "fecha_emision": "2014-06-01",
      "fecha_vencimiento": "2025-02-28",
      "pais_emisor": "Colombia",
      "status": "por_vencer"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-200",
      "fecha_emision": "2023-01-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-01-10",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "LogiCo",
      "industria": "logistica",
      "fecha_inicio": "2023-01-15",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "alta",
      "descripcion": "El pasaporte vence en 45 días, antes de los próximos 6 meses requeridos para viajes internacionales",
      "evidencia": "Pasaporte CO-CC5234567 con fecha_vencimiento 2025-02-28"
    }
  ]
}
```

### case-003 — facil
_Overstay de 15 días hace 2 años_

```json
{
  "id": "case-003",
  "difficulty": "facil",
  "summary": "Overstay de 15 días hace 2 años",
  "person": {
    "nombre": "Miguel Santos",
    "nacionalidad": "Brasil",
    "fecha_nacimiento": "1991-06-22",
    "id_documento": "BR-11223344"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-08-01",
    "fecha_vencimiento": "2026-08-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "BR-FL1122334",
      "fecha_emision": "2022-03-10",
      "fecha_vencimiento": "2032-03-10",
      "pais_emisor": "Brasil",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-500",
      "fecha_emision": "2023-07-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2021-03-01",
      "fecha_salida": "2021-06-15",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2023-07-25",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2021-03-01",
      "fecha_vencimiento": "2021-06-01",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "AgriExport",
      "industria": "agroindustria",
      "fecha_inicio": "2023-08-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "overstay",
      "severidad": "media",
      "descripcion": "Overstay previo de 14 días (visita como turista en 2021, salió 15 días después del vencimiento)",
      "evidencia": "Visa de turista venció 2021-06-01, salida registrada 2021-06-15"
    }
  ]
}
```

### case-004 — medio
_3 empleadores en 18 meses (todos notificados)_

```json
{
  "id": "case-004",
  "difficulty": "medio",
  "summary": "3 empleadores en 18 meses (todos notificados)",
  "person": {
    "nombre": "David Kim",
    "nacionalidad": "Corea del Sur",
    "fecha_nacimiento": "1993-09-17",
    "id_documento": "KR-M8877665"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-02-01",
    "fecha_vencimiento": "2026-02-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "KR-M8877665",
      "fecha_emision": "2022-01-15",
      "fecha_vencimiento": "2032-01-15",
      "pais_emisor": "Corea del Sur",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-700",
      "fecha_emision": "2024-08-01",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-01-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "StartupA",
      "industria": "software",
      "fecha_inicio": "2023-02-01",
      "fecha_fin": "2023-08-15",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "StartupB",
      "industria": "software",
      "fecha_inicio": "2023-08-20",
      "fecha_fin": "2024-03-10",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "StartupC",
      "industria": "software",
      "fecha_inicio": "2024-03-15",
      "fecha_fin": "2024-08-01",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "StartupD",
      "industria": "software",
      "fecha_inicio": "2024-08-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "cambio_empleador",
      "severidad": "media",
      "descripcion": "4 empleadores en 18 meses — frecuencia alta que puede indicar inestabilidad o uso instrumental de la visa",
      "evidencia": "Empleos: StartupA (feb-ago 2023), StartupB (ago 2023-mar 2024), StartupC (mar-ago 2024), StartupD (ago 2024-actual)"
    }
  ]
}
```

### case-005 — medio
_Inconsistencia de nombre en documentos (1 letra)_

```json
{
  "id": "case-005",
  "difficulty": "medio",
  "summary": "Inconsistencia de nombre en documentos (1 letra)",
  "person": {
    "nombre": "Sofía Vargas",
    "nacionalidad": "México",
    "fecha_nacimiento": "1997-11-25",
    "id_documento": "MX-99887766"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-05-01",
    "fecha_vencimiento": "2026-05-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "MX-G9988776",
      "fecha_emision": "2022-08-15",
      "fecha_vencimiento": "2032-08-15",
      "pais_emisor": "México",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-320",
      "fecha_emision": "2023-04-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "inconsistente"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-04-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "MediaMakers",
      "industria": "medios",
      "fecha_inicio": "2023-05-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "media",
      "descripcion": "Discrepancia de nombre entre pasaporte y contrato laboral — 'Bargas' en contrato vs 'Vargas' en pasaporte",
      "evidencia": "Pasaporte: Sofía Vargas / Contrato: Sofía Bargas (probable typo, requiere verificación)"
    }
  ]
}
```

### case-010 — facil
_Falta el certificado de antecedentes penales_

```json
{
  "id": "case-010",
  "difficulty": "facil",
  "summary": "Falta el certificado de antecedentes penales",
  "person": {
    "nombre": "Yuki Tanaka",
    "nacionalidad": "Japón",
    "fecha_nacimiento": "1996-04-30",
    "id_documento": "JP-TT3344556"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-01-15",
    "fecha_vencimiento": "2027-01-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "JP-TT3344556",
      "fecha_emision": "2023-05-20",
      "fecha_vencimiento": "2033-05-20",
      "pais_emisor": "Japón",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-150",
      "fecha_emision": "2024-01-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2024-01-12",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "RoboticsLab",
      "industria": "robotica",
      "fecha_inicio": "2024-01-15",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "alta",
      "descripcion": "Falta el certificado de antecedentes penales, requisito obligatorio para el tipo de visa",
      "evidencia": "No se encontró documento de tipo 'certificado_antecedentes' en el expediente"
    }
  ]
}
```

### case-013 — medio
_Overstay de 60 días hace 3 años (mitigado)_

```json
{
  "id": "case-013",
  "difficulty": "medio",
  "summary": "Overstay de 60 días hace 3 años (mitigado)",
  "person": {
    "nombre": "Elena Popescu",
    "nacionalidad": "Rumania",
    "fecha_nacimiento": "1995-08-11",
    "id_documento": "RO-66554433"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-03-01",
    "fecha_vencimiento": "2027-03-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "RO-DT6655443",
      "fecha_emision": "2023-01-10",
      "fecha_vencimiento": "2033-01-10",
      "pais_emisor": "Rumania",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-220",
      "fecha_emision": "2024-02-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    },
    {
      "tipo": "comprobante_pago_multa",
      "numero": "MULTA-2021-789",
      "fecha_emision": "2021-09-15",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2021-06-01",
      "fecha_salida": "2021-09-15",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2024-02-26",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2021-06-01",
      "fecha_vencimiento": "2021-07-15",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "BuildPro",
      "industria": "construccion",
      "fecha_inicio": "2024-03-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "overstay",
      "severidad": "baja",
      "descripcion": "Overstay previo de 62 días en 2021, mitigado con pago de multa y registro oficial",
      "evidencia": "Visa turista venció 2021-07-15, salida 2021-09-15. Multa pagada (comprobante MULTA-2021-789)"
    }
  ]
}
```

### case-016 — medio
_Documento de identidad con daños (parcialmente ilegible)_

```json
{
  "id": "case-016",
  "difficulty": "medio",
  "summary": "Documento de identidad con daños (parcialmente ilegible)",
  "person": {
    "nombre": "Aisha Khan",
    "nacionalidad": "India",
    "fecha_nacimiento": "1996-12-08",
    "id_documento": "IN-J6677889"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-11-01",
    "fecha_vencimiento": "2026-11-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "IN-J6677889",
      "fecha_emision": "2023-02-15",
      "fecha_vencimiento": "2033-02-15",
      "pais_emisor": "India",
      "status": "valido"
    },
    {
      "tipo": "documento_nacional_identidad",
      "numero": "DNI-IN-2020-44521",
      "fecha_emision": "2020-03-10",
      "fecha_vencimiento": "2030-03-10",
      "pais_emisor": "India",
      "status": "danado"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-880",
      "fecha_emision": "2023-10-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-10-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "FinTech Co",
      "industria": "fintech",
      "fecha_inicio": "2023-11-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "media",
      "descripcion": "Documento Nacional de Identidad presenta daños físicos que comprometen la legibilidad de algunos campos",
      "evidencia": "DNI-IN-2020-44521 con status 'danado' — solicitar copia legible o verificación"
    }
  ]
}
```

### case-006 — medio
_2 overstays previos (30 y 45 días)_

```json
{
  "id": "case-006",
  "difficulty": "medio",
  "summary": "2 overstays previos (30 y 45 días)",
  "person": {
    "nombre": "Ahmed Hassan",
    "nacionalidad": "Egipto",
    "fecha_nacimiento": "1983-07-04",
    "id_documento": "EG-A2233445"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-04-01",
    "fecha_vencimiento": "2027-04-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "EG-A2233445",
      "fecha_emision": "2019-08-10",
      "fecha_vencimiento": "2029-08-10",
      "pais_emisor": "Egipto",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-340",
      "fecha_emision": "2024-03-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2017-05-01",
      "fecha_salida": "2017-06-30",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2020-09-01",
      "fecha_salida": "2020-11-15",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2024-03-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2017-05-01",
      "fecha_vencimiento": "2017-05-31",
      "pais": "Local"
    },
    {
      "tipo": "turista",
      "fecha_emision": "2020-09-01",
      "fecha_vencimiento": "2020-10-15",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "ImportExport LLC",
      "industria": "comercio",
      "fecha_inicio": "2024-04-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "overstay",
      "severidad": "media",
      "descripcion": "Overstay de 30 días en 2017 (visita como turista)",
      "evidencia": "Visa turista venció 2017-05-31, salida 2017-06-30"
    },
    {
      "tipo": "overstay",
      "severidad": "alta",
      "descripcion": "Overstay de 31 días en 2020 (visita como turista) — patrón reincidente",
      "evidencia": "Visa turista venció 2020-10-15, salida 2020-11-15"
    }
  ]
}
```

### case-007 — medio
_Pasaporte vence en 2 meses + cambio de empleador sin notificación formal_

```json
{
  "id": "case-007",
  "difficulty": "medio",
  "summary": "Pasaporte vence en 2 meses + cambio de empleador sin notificación formal",
  "person": {
    "nombre": "Laura Martín",
    "nacionalidad": "España",
    "fecha_nacimiento": "1990-03-28",
    "id_documento": "ES-PAA112233"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2022-09-15",
    "fecha_vencimiento": "2026-09-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "ES-PAA112233",
      "fecha_emision": "2015-04-20",
      "fecha_vencimiento": "2025-05-20",
      "pais_emisor": "España",
      "status": "por_vencer"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-960",
      "fecha_emision": "2024-07-01",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2022-09-10",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "Initech",
      "industria": "software",
      "fecha_inicio": "2022-09-15",
      "fecha_fin": "2024-06-30",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "Innovatech",
      "industria": "software",
      "fecha_inicio": "2024-07-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": false
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "alta",
      "descripcion": "Pasaporte vence en menos de 60 días, requiere renovación urgente",
      "evidencia": "Pasaporte ES-PAA112233 con fecha_vencimiento 2025-05-20"
    },
    {
      "tipo": "cambio_empleador",
      "severidad": "alta",
      "descripcion": "Cambio de empleador sin notificación formal a la oficina de migración",
      "evidencia": "Cambio Initech → Innovatech (jul 2024) con notificado_a_migracion: false"
    }
  ]
}
```

### case-008 — medio
_Overstay reciente + 4 empleadores en 2 años_

```json
{
  "id": "case-008",
  "difficulty": "medio",
  "summary": "Overstay reciente + 4 empleadores en 2 años",
  "person": {
    "nombre": "Tariq Ali",
    "nacionalidad": "Pakistán",
    "fecha_nacimiento": "1988-10-19",
    "id_documento": "PK-AC9988776"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-01-15",
    "fecha_vencimiento": "2027-01-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "PK-AC9988776",
      "fecha_emision": "2021-05-08",
      "fecha_vencimiento": "2031-05-08",
      "pais_emisor": "Pakistán",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-110",
      "fecha_emision": "2024-01-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2022-08-01",
      "fecha_salida": "2022-09-15",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2024-01-12",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2022-08-01",
      "fecha_vencimiento": "2022-09-05",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "TechCo",
      "industria": "software",
      "fecha_inicio": "2022-03-01",
      "fecha_fin": "2022-07-15",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "DataCo",
      "industria": "software",
      "fecha_inicio": "2022-10-01",
      "fecha_fin": "2023-04-30",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "CloudCo",
      "industria": "software",
      "fecha_inicio": "2023-05-15",
      "fecha_fin": "2023-12-20",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "AICo",
      "industria": "software",
      "fecha_inicio": "2024-01-15",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "overstay",
      "severidad": "alta",
      "descripcion": "Overstay de 10 días en 2022 — relativamente reciente",
      "evidencia": "Visa turista venció 2022-09-05, salida 2022-09-15"
    },
    {
      "tipo": "cambio_empleador",
      "severidad": "alta",
      "descripcion": "4 empleadores en ~22 meses con un overstay entremedio — patrón consistente con 'visa hopping'",
      "evidencia": "TechCo (mar-jul 2022), DataCo (oct 2022-abr 2023), CloudCo (may-dic 2023), AICo (ene 2024-actual)"
    }
  ]
}
```

### case-015 — dificil
_Visa de trabajo pero ahora freelance — posible irregularidad_

```json
{
  "id": "case-015",
  "difficulty": "dificil",
  "summary": "Visa de trabajo pero ahora freelance — posible irregularidad",
  "person": {
    "nombre": "Hans Müller",
    "nacionalidad": "Alemania",
    "fecha_nacimiento": "1988-02-09",
    "id_documento": "DE-C12AB3456"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-03-01",
    "fecha_vencimiento": "2026-03-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "DE-C12AB3456",
      "fecha_emision": "2022-06-12",
      "fecha_vencimiento": "2032-06-12",
      "pais_emisor": "Alemania",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-110",
      "fecha_emision": "2023-02-25",
      "fecha_vencimiento": "2023-09-30",
      "pais_emisor": "Local",
      "status": "vencido"
    },
    {
      "tipo": "declaracion_ingresos_freelance",
      "numero": "DIF-2024-001",
      "fecha_emision": "2024-01-15",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-02-25",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "BuildMax",
      "industria": "construccion",
      "fecha_inicio": "2023-03-01",
      "fecha_fin": "2023-09-30",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "(freelance — varios clientes)",
      "industria": "consultoria_tech",
      "fecha_inicio": "2023-10-01",
      "fecha_fin": null,
      "tipo_visa": null,
      "notificado_a_migracion": false
    }
  ],
  "planted_alerts": [
    {
      "tipo": "cambio_empleador",
      "severidad": "alta",
      "descripcion": "Visa de trabajo pero trabaja como freelance desde hace ~1 año, sin visa de trabajador independiente",
      "evidencia": "Empleador formal venció 2023-09-30; desde entonces freelance sin tipo_visa"
    },
    {
      "tipo": "cambio_empleador",
      "severidad": "alta",
      "descripcion": "Cambio de industria (construcción → consultoría tech) sin notificación ni ajuste de visa",
      "evidencia": "BuildMax (construcción) → freelance tech sin documentar cambio de actividad ante migración"
    }
  ]
}
```

### case-020 — medio
_Visa de trabajo para software, trabaja en construcción_

```json
{
  "id": "case-020",
  "difficulty": "medio",
  "summary": "Visa de trabajo para software, trabaja en construcción",
  "person": {
    "nombre": "Ricardo Oliveira",
    "nacionalidad": "Brasil",
    "fecha_nacimiento": "1993-06-15",
    "id_documento": "BR-TT5544332"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-07-01",
    "fecha_vencimiento": "2026-07-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "BR-TT5544332",
      "fecha_emision": "2022-04-08",
      "fecha_vencimiento": "2032-04-08",
      "pais_emisor": "Brasil",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-450",
      "fecha_emision": "2023-06-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "inconsistente"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-06-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "CodeFactory",
      "industria": "software",
      "fecha_inicio": "2023-07-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "cambio_empleador",
      "severidad": "alta",
      "descripcion": "La visa fue otorgada para trabajo en software, pero la persona actualmente trabaja en construcción según reportes de inspección",
      "evidencia": "Empleador en expediente: CodeFactory (software). Trabajo real según inspección: obra de construcción (sin documentar cambio)"
    }
  ]
}
```

### case-023 — medio
_Pasaporte vence en 90 días + falta acta apostillada_

```json
{
  "id": "case-023",
  "difficulty": "medio",
  "summary": "Pasaporte vence en 90 días + falta acta apostillada",
  "person": {
    "nombre": "Wei Chen",
    "nacionalidad": "China",
    "fecha_nacimiento": "1994-08-22",
    "id_documento": "CN-EA3344556"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-10-01",
    "fecha_vencimiento": "2026-10-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "CN-EA3344556",
      "fecha_emision": "2014-02-10",
      "fecha_vencimiento": "2025-11-15",
      "pais_emisor": "China",
      "status": "por_vencer"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-770",
      "fecha_emision": "2023-09-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-09-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "ManufactCo",
      "industria": "manufactura",
      "fecha_inicio": "2023-10-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "media",
      "descripcion": "Pasaporte vence en ~3 meses, requiere atención con anticipación",
      "evidencia": "Pasaporte CN-EA3344556 con fecha_vencimiento 2025-11-15"
    },
    {
      "tipo": "documento",
      "severidad": "alta",
      "descripcion": "Falta acta de nacimiento apostillada, requerida para el tipo de trámite actual",
      "evidencia": "No se encontró documento de tipo 'acta_nacimiento' en el expediente"
    }
  ]
}
```

### case-009 — dificil
_Caso crítico: pasaporte vencido, overstay grave, patrón de cambio de empleador_

```json
{
  "id": "case-009",
  "difficulty": "dificil",
  "summary": "Caso crítico: pasaporte vencido, overstay grave, patrón de cambio de empleador",
  "person": {
    "nombre": "Roberto Silva",
    "nacionalidad": "Perú",
    "fecha_nacimiento": "1985-12-14",
    "id_documento": "PE-77665544"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2022-01-15",
    "fecha_vencimiento": "2025-01-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "PE-LM7766554",
      "fecha_emision": "2014-05-20",
      "fecha_vencimiento": "2024-08-10",
      "pais_emisor": "Perú",
      "status": "vencido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-001",
      "fecha_emision": "2024-01-05",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2019-04-01",
      "fecha_salida": "2019-06-30",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2022-01-10",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2019-04-01",
      "fecha_vencimiento": "2019-05-01",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "AgroExport A",
      "industria": "agricultura",
      "fecha_inicio": "2018-05-01",
      "fecha_fin": "2018-11-15",
      "tipo_visa": "turista",
      "notificado_a_migracion": false
    },
    {
      "empleador": "LogiCo B",
      "industria": "logistica",
      "fecha_inicio": "2022-01-15",
      "fecha_fin": "2022-08-31",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "BuildInc C",
      "industria": "construccion",
      "fecha_inicio": "2022-09-15",
      "fecha_fin": "2023-04-30",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "RetailCo D",
      "industria": "retail",
      "fecha_inicio": "2023-05-15",
      "fecha_fin": "2023-12-20",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "ServiceCo E",
      "industria": "servicios",
      "fecha_inicio": "2024-01-05",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "alta",
      "descripcion": "Pasaporte está vencido hace 6 meses — documento inválido para cualquier trámite migratorio",
      "evidencia": "Pasaporte PE-LM7766554 con fecha_vencimiento 2024-08-10, status 'vencido'"
    },
    {
      "tipo": "overstay",
      "severidad": "alta",
      "descripcion": "Overstay de 60 días en 2019",
      "evidencia": "Visa turista venció 2019-05-01, salida 2019-06-30"
    },
    {
      "tipo": "cambio_empleador",
      "severidad": "alta",
      "descripcion": "5 empleadores en ~6 años con 1 empleo informal durante visa de turista — patrón irregular",
      "evidencia": "AgroExport A (informal), LogiCo B, BuildInc C, RetailCo D, ServiceCo E"
    }
  ]
}
```

### case-019 — dificil
_Asilo con overstay en otro país, documento dañado, trabajo informal_

```json
{
  "id": "case-019",
  "difficulty": "dificil",
  "summary": "Asilo con overstay en otro país, documento dañado, trabajo informal",
  "person": {
    "nombre": "Fatima Al-Rashid",
    "nacionalidad": "Irak",
    "fecha_nacimiento": "1991-03-30",
    "id_documento": "IQ-A8899776"
  },
  "current_visa": {
    "tipo": "asilo",
    "fecha_emision": "2023-06-01",
    "fecha_vencimiento": "2025-06-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "IQ-A8899776",
      "fecha_emision": "2010-01-10",
      "fecha_vencimiento": "2020-01-10",
      "pais_emisor": "Irak",
      "status": "vencido"
    },
    {
      "tipo": "documento_identidad_nacional",
      "numero": "DIN-IQ-2010-2244",
      "fecha_emision": "2010-03-15",
      "fecha_vencimiento": null,
      "pais_emisor": "Irak",
      "status": "danado"
    },
    {
      "tipo": "carta_asilo",
      "numero": "AS-2023-145",
      "fecha_emision": "2023-06-01",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2018-04-01",
      "fecha_salida": "2018-08-15",
      "pais": "Schengen-A",
      "proposito": "asilo_tramite"
    },
    {
      "fecha_entrada": "2023-05-15",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "asilo_otorgado"
    }
  ],
  "previous_visas": [
    {
      "tipo": "asilo_tramite",
      "fecha_emision": "2018-04-01",
      "fecha_vencimiento": "2018-06-15",
      "pais": "Schengen-A"
    }
  ],
  "employment_history": [
    {
      "empleador": "(cuidado de personas, no formal)",
      "industria": "servicios_personales",
      "fecha_inicio": "2023-09-01",
      "fecha_fin": "2023-12-15",
      "tipo_visa": null,
      "notificado_a_migracion": false
    },
    {
      "empleador": "(traducciones freelance)",
      "industria": "servicios",
      "fecha_inicio": "2024-02-01",
      "fecha_fin": "2024-08-30",
      "tipo_visa": null,
      "notificado_a_migracion": false
    },
    {
      "empleador": "CateringCo (formal, autorizado)",
      "industria": "catering",
      "fecha_inicio": "2024-10-01",
      "fecha_fin": null,
      "tipo_visa": "asilo_permiso_laboral",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "overstay",
      "severidad": "alta",
      "descripcion": "Overstay previo en país Schengen (90 días de visa de asilo en trámite, permaneció 136 días)",
      "evidencia": "Visa Schengen-A venció 2018-06-15, salida 2018-08-15"
    },
    {
      "tipo": "documento",
      "severidad": "alta",
      "descripcion": "Documento Nacional de Identidad dañado por conflicto, datos parcialmente ilegibles",
      "evidencia": "DIN-IQ-2010-2244 con status 'danado'"
    },
    {
      "tipo": "cambio_empleador",
      "severidad": "media",
      "descripcion": "2 empleos informales sin notificación ni autorización, previo al empleo formal con permiso",
      "evidencia": "Trabajos como cuidadora y traductora freelance (2023-2024) sin documentar"
    }
  ]
}
```

### case-026 — dificil
_Múltiples problemas: overstays, cambios de empleador, documento dañado_

```json
{
  "id": "case-026",
  "difficulty": "dificil",
  "summary": "Múltiples problemas: overstays, cambios de empleador, documento dañado",
  "person": {
    "nombre": "Dmitri Volkov",
    "nacionalidad": "Ucrania",
    "fecha_nacimiento": "1982-09-25",
    "id_documento": "UA-FD4455667"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-02-15",
    "fecha_vencimiento": "2027-02-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "UA-FD4455667",
      "fecha_emision": "2017-11-20",
      "fecha_vencimiento": "2027-11-20",
      "pais_emisor": "Ucrania",
      "status": "valido"
    },
    {
      "tipo": "documento_identidad_nacional",
      "numero": "DIN-UA-2017-99821",
      "fecha_emision": "2017-06-10",
      "fecha_vencimiento": "2027-06-10",
      "pais_emisor": "Ucrania",
      "status": "danado"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-555",
      "fecha_emision": "2024-02-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2019-07-01",
      "fecha_salida": "2019-08-30",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2021-05-01",
      "fecha_salida": "2021-05-25",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2024-02-10",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2019-07-01",
      "fecha_vencimiento": "2019-07-31",
      "pais": "Local"
    },
    {
      "tipo": "turista",
      "fecha_emision": "2021-05-01",
      "fecha_vencimiento": "2021-05-20",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "ConstructionsCo",
      "industria": "construccion",
      "fecha_inicio": "2022-03-15",
      "fecha_fin": "2022-09-30",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "ManufacturingInc",
      "industria": "manufactura",
      "fecha_inicio": "2022-10-15",
      "fecha_fin": "2023-06-30",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "LogiTrans",
      "industria": "logistica",
      "fecha_inicio": "2023-07-15",
      "fecha_fin": "2024-01-20",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "ServicesGroup",
      "industria": "servicios",
      "fecha_inicio": "2024-02-15",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "overstay",
      "severidad": "media",
      "descripcion": "Overstay de 30 días en 2019",
      "evidencia": "Visa turista venció 2019-07-31, salida 2019-08-30"
    },
    {
      "tipo": "overstay",
      "severidad": "media",
      "descripcion": "Overstay de 5 días en 2021",
      "evidencia": "Visa turista venció 2021-05-20, salida 2021-05-25"
    },
    {
      "tipo": "cambio_empleador",
      "severidad": "alta",
      "descripcion": "4 empleadores en ~24 meses con cambios frecuentes de industria",
      "evidencia": "ConstructionsCo → ManufacturingInc → LogiTrans → ServicesGroup (cada 6-9 meses)"
    },
    {
      "tipo": "documento",
      "severidad": "baja",
      "descripcion": "DNI dañado — información parcialmente ilegible, solicitar copia actualizada",
      "evidencia": "DIN-UA-2017-99821 con status 'danado'"
    }
  ]
}
```

### case-012 — ambiguo
_Cambio de雇主 reciente PERO notificado y legítimo — NO debería ser alerta_

```json
{
  "id": "case-012",
  "difficulty": "ambiguo",
  "summary": "Cambio de雇主 reciente PERO notificado y legítimo — NO debería ser alerta",
  "person": {
    "nombre": "Pedro Ramírez",
    "nacionalidad": "Chile",
    "fecha_nacimiento": "1992-04-08",
    "id_documento": "CL-D2233445"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-09-01",
    "fecha_vencimiento": "2026-09-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "CL-D2233445",
      "fecha_emision": "2021-05-10",
      "fecha_vencimiento": "2031-05-10",
      "pais_emisor": "Chile",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-820",
      "fecha_emision": "2024-08-15",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    },
    {
      "tipo": "carta_notificacion_cambio",
      "numero": "CN-2024-330",
      "fecha_emision": "2024-08-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-08-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "ConsultingGroup",
      "industria": "consultoria",
      "fecha_inicio": "2023-09-01",
      "fecha_fin": "2024-08-15",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "StrategicPartners",
      "industria": "consultoria",
      "fecha_inicio": "2024-08-15",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [],
  "notes": "Este es un caso LIMPIO pero un modelo mal entrenado podría flaggear el cambio reciente de雇主. La pista es la carta_notificacion_cambio con status valido. Si el modelo sabe leerla, no levanta alerta."
}
```
**Nota del facilitador:** _Este es un caso LIMPIO pero un modelo mal entrenado podría flaggear el cambio reciente de雇主. La pista es la carta_notificacion_cambio con status valido. Si el modelo sabe leerla, no levanta alerta._

### case-018 — ambiguo
_Overstay 'técnico' de 2 días por vuelo cancelado — multado y resuelto_

```json
{
  "id": "case-018",
  "difficulty": "ambiguo",
  "summary": "Overstay 'técnico' de 2 días por vuelo cancelado — multado y resuelto",
  "person": {
    "nombre": "Cheng Wei",
    "nacionalidad": "China",
    "fecha_nacimiento": "1990-07-12",
    "id_documento": "CN-EA5566778"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-11-15",
    "fecha_vencimiento": "2026-11-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "CN-EA5566778",
      "fecha_emision": "2022-09-08",
      "fecha_vencimiento": "2032-09-08",
      "pais_emisor": "China",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-1000",
      "fecha_emision": "2023-11-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    },
    {
      "tipo": "carta_aerolinea_cancelacion",
      "numero": "AIR-2022-99821",
      "fecha_emision": "2022-12-30",
      "fecha_vencimiento": null,
      "pais_emisor": "Internacional",
      "status": "valido"
    },
    {
      "tipo": "comprobante_pago_multa",
      "numero": "MULTA-2023-005",
      "fecha_emision": "2023-01-05",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2022-10-15",
      "fecha_salida": "2023-01-12",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2023-11-12",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2022-10-15",
      "fecha_vencimiento": "2023-01-10",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "ManufactAsia",
      "industria": "manufactura",
      "fecha_inicio": "2023-11-15",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [],
  "notes": "Overstay TÉCNICO de 2 días por vuelo cancelado (visita turista venció 2023-01-10, salió 2023-01-12). Multa pagada. Un modelo demasiado sensible podría flaggearlo; un buen modelo reconoce la evidencia atenuante (carta de aerolínea + multa pagada)."
}
```
**Nota del facilitador:** _Overstay TÉCNICO de 2 días por vuelo cancelado (visita turista venció 2023-01-10, salió 2023-01-12). Multa pagada. Un modelo demasiado sensible podría flaggearlo; un buen modelo reconoce la evidencia atenuante (carta de aerolínea + multa pagada)._

### case-022 — ambiguo
_Overstay de hace 10 años — historial impecable desde entonces_

```json
{
  "id": "case-022",
  "difficulty": "ambiguo",
  "summary": "Overstay de hace 10 años — historial impecable desde entonces",
  "person": {
    "nombre": "Ivan Petrov",
    "nacionalidad": "Bulgaria",
    "fecha_nacimiento": "1973-08-17",
    "id_documento": "BG-PP9988776"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-05-01",
    "fecha_vencimiento": "2027-05-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "BG-PP9988776",
      "fecha_emision": "2022-02-15",
      "fecha_vencimiento": "2032-02-15",
      "pais_emisor": "Bulgaria",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-665",
      "fecha_emision": "2024-04-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2014-03-01",
      "fecha_salida": "2014-05-15",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2015-08-01",
      "fecha_salida": "2015-08-30",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2018-02-01",
      "fecha_salida": "2018-02-28",
      "pais": "Local",
      "proposito": "turista"
    },
    {
      "fecha_entrada": "2024-04-26",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "turista",
      "fecha_emision": "2014-03-01",
      "fecha_vencimiento": "2014-03-15",
      "pais": "Local"
    },
    {
      "tipo": "turista",
      "fecha_emision": "2015-08-01",
      "fecha_vencimiento": "2015-08-30",
      "pais": "Local"
    },
    {
      "tipo": "turista",
      "fecha_emision": "2018-02-01",
      "fecha_vencimiento": "2018-02-28",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "EngineeringFirm",
      "industria": "ingenieria",
      "fecha_inicio": "2024-05-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "overstay",
      "severidad": "baja",
      "descripcion": "Overstay antiguo de 61 días en 2014, no reincidente en 10 años de historial posterior",
      "evidencia": "Visa turista venció 2014-03-15, salida 2014-05-15. Historial posterior impecable (2015, 2018, 2024) sin incidentes."
    }
  ],
  "notes": "El overstay REALMENTE ocurrió, pero la severidad es discutible: el modelo debe decidir si reportarlo (recomendable) y con qué severidad. Severidad 'baja' es razonable; 'alta' sería un error de calibración."
}
```
**Nota del facilitador:** _El overstay REALMENTE ocurrió, pero la severidad es discutible: el modelo debe decidir si reportarlo (recomendable) y con qué severidad. Severidad 'baja' es razonable; 'alta' sería un error de calibración._

### case-024 — ambiguo
_Transición de visa de trabajo a independiente — ¿alerta de cambio de empleador?_

```json
{
  "id": "case-024",
  "difficulty": "ambiguo",
  "summary": "Transición de visa de trabajo a independiente — ¿alerta de cambio de empleador?",
  "person": {
    "nombre": "André Dupont",
    "nacionalidad": "Francia",
    "fecha_nacimiento": "1985-11-03",
    "id_documento": "FR-AA4455667"
  },
  "current_visa": {
    "tipo": "trabajador_independiente",
    "fecha_emision": "2024-01-15",
    "fecha_vencimiento": "2027-01-15",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "FR-AA4455667",
      "fecha_emision": "2021-07-22",
      "fecha_vencimiento": "2031-07-22",
      "pais_emisor": "Francia",
      "status": "valido"
    },
    {
      "tipo": "constancia_trabajador_independiente",
      "numero": "CTI-2024-200",
      "fecha_emision": "2024-01-10",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2021-02-15",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [
    {
      "tipo": "trabajo",
      "fecha_emision": "2021-02-15",
      "fecha_vencimiento": "2024-01-15",
      "pais": "Local"
    }
  ],
  "employment_history": [
    {
      "empleador": "DesignStudio",
      "industria": "diseno_grafico",
      "fecha_inicio": "2021-02-15",
      "fecha_fin": "2023-12-31",
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    },
    {
      "empleador": "(freelance — múltiples clientes)",
      "industria": "diseno_grafico",
      "fecha_inicio": "2024-01-15",
      "fecha_fin": null,
      "tipo_visa": "trabajador_independiente",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [],
  "notes": "Transición LEGÍTIMA de visa de trabajo a visa de trabajador independiente (hay documento constancia_trabajador_independiente). Un modelo poco sofisticado podría flaggear el cambio de 'empleador' sin notar el cambio de tipo de visa."
}
```
**Nota del facilitador:** _Transición LEGÍTIMA de visa de trabajo a visa de trabajador independiente (hay documento constancia_trabajador_independiente). Un modelo poco sofisticado podría flaggear el cambio de 'empleador' sin notar el cambio de tipo de visa._

### case-027 — ambiguo
_Empleo en industria relacionada, no idéntica — ¿es alerta?_

```json
{
  "id": "case-027",
  "difficulty": "ambiguo",
  "summary": "Empleo en industria relacionada, no idéntica — ¿es alerta?",
  "person": {
    "nombre": "Sven Eriksson",
    "nacionalidad": "Suecia",
    "fecha_nacimiento": "1988-06-30",
    "id_documento": "SE-LM7788990"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2023-04-01",
    "fecha_vencimiento": "2026-04-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "SE-LM7788990",
      "fecha_emision": "2021-08-05",
      "fecha_vencimiento": "2031-08-05",
      "pais_emisor": "Suecia",
      "status": "valido"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2023-330",
      "fecha_emision": "2023-03-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2023-03-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "DataCorp",
      "industria": "data_science",
      "fecha_inicio": "2023-04-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "cambio_empleador",
      "severidad": "baja",
      "descripcion": "Visa otorgada para 'analisis_datos' pero el contrato indica 'data_science' — industrias relacionadas pero no idénticas",
      "evidencia": "Solicitud original mencionaba 'analisis_datos', contrato actual indica 'data_science'. Diferencia semántica, no necesariamente problemática."
    }
  ],
  "notes": "Caso límite: ¿es realmente un cambio problemático? La industria es la misma familia (data). Un modelo con buena calibración debería levantar alerta de severidad baja o NONE; un modelo alarmista podría decir 'alta'."
}
```
**Nota del facilitador:** _Caso límite: ¿es realmente un cambio problemático? La industria es la misma familia (data). Un modelo con buena calibración debería levantar alerta de severidad baja o NONE; un modelo alarmista podría decir 'alta'._

### case-028 — ambiguo
_Pasaporte vence en exactamente 6 meses — umbral de muchas aerolíneas_

```json
{
  "id": "case-028",
  "difficulty": "ambiguo",
  "summary": "Pasaporte vence en exactamente 6 meses — umbral de muchas aerolíneas",
  "person": {
    "nombre": "Nadia Petrova",
    "nacionalidad": "Bielorrusia",
    "fecha_nacimiento": "1990-01-20",
    "id_documento": "BY-MP3344556"
  },
  "current_visa": {
    "tipo": "trabajo",
    "fecha_emision": "2024-05-01",
    "fecha_vencimiento": "2027-05-01",
    "status": "vigente"
  },
  "documents": [
    {
      "tipo": "pasaporte",
      "numero": "BY-MP3344556",
      "fecha_emision": "2019-11-12",
      "fecha_vencimiento": "2025-11-12",
      "pais_emisor": "Bielorrusia",
      "status": "por_vencer"
    },
    {
      "tipo": "contrato_laboral",
      "numero": "CT-2024-444",
      "fecha_emision": "2024-04-25",
      "fecha_vencimiento": null,
      "pais_emisor": "Local",
      "status": "valido"
    }
  ],
  "travel_history": [
    {
      "fecha_entrada": "2024-04-28",
      "fecha_salida": null,
      "pais": "Local",
      "proposito": "trabajo"
    }
  ],
  "previous_visas": [],
  "employment_history": [
    {
      "empleador": "TechVenture",
      "industria": "tecnologia",
      "fecha_inicio": "2024-05-01",
      "fecha_fin": null,
      "tipo_visa": "trabajo",
      "notificado_a_migracion": true
    }
  ],
  "planted_alerts": [
    {
      "tipo": "documento",
      "severidad": "baja",
      "descripcion": "Pasaporte vence en ~6 meses — en el umbral mínimo que muchas aerolíneas requieren para viajes internacionales",
      "evidencia": "Pasaporte BY-MP3344556 con fecha_vencimiento 2025-11-12. La persona no tiene viajes programados a corto plazo según expediente."
    }
  ],
  "notes": "¿Es alerta o no? El pasaporte está por vencer (6 meses), pero la persona está estable, no viaja pronto, y puede renovarlo sin urgencia. Severidad baja es razonable; un modelo con umbral < 6 meses lo ignoraría."
}
```
**Nota del facilitador:** _¿Es alerta o no? El pasaporte está por vencer (6 meses), pero la persona está estable, no viaja pronto, y puede renovarlo sin urgencia. Severidad baja es razonable; un modelo con umbral < 6 meses lo ignoraría._
