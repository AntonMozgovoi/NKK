class ManualApproval:
    MANUAL_APPROVAL = {
  "userId": "c69172b0-c9fe-43b9-afb5-f81f80fcad47",
  "workflowId": "464c7231-e706-4ec8-ba0f-99d64105e97f",
  "jsonData": {
    "loanInfo": {
      "retailDivision": {
        "managerName": "iz000626",
        "retailOutlet": "7371_Tsentralnaya_STO_LADA_Tolyatti_Gromovoi"
      },
      "vehicle": {
        "vin": "{{vin}}",
        "mark": "LADA",
        "type": "veht_new",
        "year": "2025",
        "model": 15071213,
        "mileage": 0,
        "packaging": 60945
      },
      "vehicleCost": {
        "recommendedCost": 1525000.0,
        "recommendedDiscount": 0.0,
        "clientCost": 1525000.0,
        "extrasEquipment": 0
      },
      "loanData": {
        "loanProgram": "RN68968_1",
        "term": 84,
        "purposeCode": "CRA_PRIVATE",
        "creditSum": 1000000.0
      },
      "initialPayment": {
        "ratingTradeIn": 0,
        "initialContributionCash": 762500.0,
        "initialContributionInterestRateFinal": 50.0,
        "initialContributionFinal": 762500.0
      },
      "residualPayment": {
        "residualPayment": 0,
        "residualPaymentInterestRateFinal": 0.0
      },
      "subsidy": {
        "subsidyByProdycer": 0
      },
      "interestRate": {
        "creditRate": 19.0,
        "creditRateFinal": 19.0,
        "creditRateMarketing": 19.0
      },
      "additionalServices": [
        {
          "serviceKindCode": "LADA_KASKO_POL_1903",
          "serviceTypeCode": "kasko_l_1",
          "cost": 50000.0,
          "serviceCategoryCode": "insurance"
        }
      ]
    },
    "applicationMessages": [
      {
        "loginAuthor": "OutsourceDataEntrySpecialist_GO1",
        "postDate": "2024-06-10T10:26:00",
        "text": "VIN авто - VN4AD615338897267"
      },
      {
        "loginAuthor": "OutsourceDataEntrySpecialist_GO1",
        "postDate": "2024-06-10T10:26:00",
        "text": "Госуслуги ID - {1025972800}"
      }
    ],
    "applicantInfo": {
      "applicantPersonalInfo": {
        "age": "30",
        "esiaId": "1025972800",
        "sexCode": "M",
        "birthday": "{{birthDate}}",
        "lastName": "{{lastName}}",
        "applicantPersonalCode": "PR_APPLICANT",
        "birthTown": "г Воронеж",
        "firstName": "{{firstName}}",
        "middleName": "{{middleName}}-рандомный",
        "citizenshipCode": "RU",
        "birthCountryCode": "RU",
        "realAddressIsRegAddress": false,
        "regApplicantAddress": {
          "fullName": "614026, Пермский край, г Пермь, Орджоникидзевский р-н, ул Железнодорожная, д 4, кв 201",
          "typeCode": "addr_registration",
          "regionCode": 59,
          "address": {
            "postal_box": null,
            "flat": "201",
            "block": null,
            "city": "Пермь",
            "city_type": "г",
            "house": "4",
            "okato": "57401378000",
            "region": "Пермский",
            "region_type": "край",
            "street": "Железнодорожная",
            "street_type": "ул",
            "area": "Орджоникидзевский",
            "area_type": "р-н",
            "settlement": null,
            "settlement_type": null,
            "postal_code": "614026"
          }
        },
        "realApplicantAddress": {
          "fullName": "614026, Пермский край, г Пермь, Орджоникидзевский р-н, ул Железнодорожная, д 4, кв 201",
          "typeCode": "addr_registration",
          "regionCode": 59,
          "address": {
            "postal_box": null,
            "flat": "201",
            "block": null,
            "city": "Пермь",
            "city_type": "г",
            "house": "4",
            "okato": "57401378000",
            "region": "Пермский",
            "region_type": "край",
            "street": "Железнодорожная",
            "street_type": "ул",
            "area": "Орджоникидзевский",
            "area_type": "р-н",
            "settlement": null,
            "settlement_type": null,
            "postal_code": "614026"
          }
        }

      },
      "mainDocument": {
        "endDate": null,
        "isMain": true,
        "issuerCode": "530-875",
        "issuerName": "Отделом внутренних дел России по г. Шахты",
        "nameCode": "IC_PASSPORT",
        "number": "{{passportNumber}}",
        "series": "{{passportSeries}}",
        "startDate": "2024-07-15"
      },
     "secondDocument": {
        "endDate": null,
        "isMain": false,
        "issuerCode": null,
        "issuerName": "гибдд",
        "nameCode": "IC_DRIVING_LICENSE",
        "number": "152092",
        "series": "4580",
        "startDate": "2020-04-24"
      },
      "noFormerPassport": true,
      "otherDocuments": [
        {
          "nameCode": null,
          "series": null,
          "number": null,
          "issueDate": null
        }
      ],
      "applicantAdditionalInfo": {
        "inn": "{{inn}}",
        "snils:": null,
        "codeword": null,
        "formerFirstName": null,
        "formerLastName": null,
        "formerMiddleName": null,
        "socialStatusCode": "socstat_001",
        "maritalStatusCode": "MS_MARRIED",
        "numberOfDependent": 0
      },
      "phones": [
        {
          "phone": "79202546496",
          "isPreferred": true,
          "typeCode": "MOBILE",
          "isVerified": false,
          "additionalNumber": null
        },
        {
          "phone": "78006556496",
          "isPreferred": false,
          "typeCode": "WORKPLACE_CONTACT",
          "isVerified": false,
          "additionalNumber": null
        }
      ],
      "emails": [
        {
          "email": "800@mail.ru",
          "typeCode": "ACTUAL"
        }
      ],
      "contactUrgents": [
        {
          "birthday": "1988-03-30",
          "civilDegreeCode": "br_spouse",
          "firstName": "Виктория",
          "lastName": "Логинова",
          "middleName": "Борисовна",
          "phone": "79607655649"
        }
      ],
      "employer": {
        "inn": "5503067018",
        "companyName": "АО Авто финанс банк",
        "organizationalLegalForm": "orgform_002",
        "employerContactAddress": {
          "fullName": "109028, г Москва, Таганский р-н, Серебряническая наб, д 29",
          "typeCode": "addr_workplace",
          "regionCode": 77,
          "address": {
            "postal_box": null,
            "flat": null,
            "block": null,
            "city": "Москва",
            "city_type": "г",
            "house": "29",
            "okato": "45286580000",
            "region": "Москва",
            "region_type": "г",
            "street": "Серебряническая",
            "street_type": "наб",
            "area": "Таганский",
            "area_type": "р-н",
            "settlement": null,
            "settlement_type": null,
            "postal_code": "109028"
          }
        }
      },
      "employee": {
        "postDesc": "Начальник отдела",
        "postTypeCode": "epml_post_009",
        "contractStartDate": "2023-06-01T21:00:00.000Z",
        "seniorityStartDate": "2023-06-01T21:00:00.000Z"
      },
      "applicantAgreementsInfo": {
        "personalDataAllowed": true,
        "creditHistoryAgencySendAllowed": true,
        "creditHistoryAgencyRecieveAllowed": true
      },
      "applicantIncomeInfo": {
        "salaryDate": 30,
        "Incomes": [
          {
            "amount": 120000,
            "amountCurCode": "RUB",
            "categoryCode": "NP_INCOME_TYPE_MAIN",
            "sourceCode": "np_income_source_form",
            "typeCode": "addincome_001"
          }
        ]
      }
    }
  },
  "roleGroupId": "e082c0f1-a237-42b4-bcb2-606594fae8f6"
}
    
