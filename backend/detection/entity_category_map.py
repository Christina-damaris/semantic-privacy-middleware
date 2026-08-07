"""
Maps every detected entity type to the category
defined in Hinja's rule_table.json.
"""

ENTITY_CATEGORY_MAP = {

    # ============================================================
    # PERSONAL IDENTITY
    # ============================================================
    "NAME": "PERSONAL_IDENTITY",
    "PERSON": "PERSONAL_IDENTITY",
    "FULL_NAME": "PERSONAL_IDENTITY",
    "FIRST_NAME": "PERSONAL_IDENTITY",
    "LAST_NAME": "PERSONAL_IDENTITY",
    "FATHER_NAME": "PERSONAL_IDENTITY",
    "MOTHER_NAME": "PERSONAL_IDENTITY",
    "DATE_OF_BIRTH": "PERSONAL_IDENTITY",
    "AGE": "PERSONAL_IDENTITY",
    "GENDER": "PERSONAL_IDENTITY",
    "NATIONALITY": "PERSONAL_IDENTITY",
    "RELIGION": "PERSONAL_IDENTITY",
    "MARITAL_STATUS": "PERSONAL_IDENTITY",
    "BLOOD_GROUP": "PERSONAL_IDENTITY",
    "PHOTO": "PERSONAL_IDENTITY",
    "SIGNATURE": "PERSONAL_IDENTITY",

    # ============================================================
    # CONTACT INFO
    # ============================================================
    "EMAIL": "CONTACT_INFO",
    "EMAIL_ADDRESS": "CONTACT_INFO",
    "PHONE_NUMBER": "CONTACT_INFO",
    "PHYSICAL_ADDRESS": "CONTACT_INFO",
    "IP_ADDRESS": "CONTACT_INFO",

    # ============================================================
    # GOVERNMENT ID
    # ============================================================
    "AADHAAR": "GOVERNMENT_ID",
    "PAN": "GOVERNMENT_ID",
    "PASSPORT": "GOVERNMENT_ID",
    "DRIVING_LICENSE": "GOVERNMENT_ID",
    "VOTER_ID": "GOVERNMENT_ID",
    "GSTIN": "GOVERNMENT_ID",
    "TIN": "GOVERNMENT_ID",
    "SSN": "GOVERNMENT_ID",
    "NATIONAL_ID": "GOVERNMENT_ID",
    "RATION_CARD": "GOVERNMENT_ID",

    # ============================================================
    # FINANCIAL INFO
    # ============================================================
    "BANK_ACCOUNT_NUMBER": "FINANCIAL_INFO",
    "IFSC": "FINANCIAL_INFO",
    "SWIFT": "FINANCIAL_INFO",
    "CREDIT_CARD": "FINANCIAL_INFO",
    "DEBIT_CARD": "FINANCIAL_INFO",
    "CVV": "FINANCIAL_INFO",
    "EXPIRY_DATE": "FINANCIAL_INFO",
    "UPI_ID": "FINANCIAL_INFO",
    "IBAN": "FINANCIAL_INFO",
    "WALLET_ID": "FINANCIAL_INFO",
    "TRANSACTION_ID": "FINANCIAL_INFO",

    # ============================================================
    # AUTHENTICATION
    # ============================================================
    "PASSWORD": "AUTHENTICATION",
    "PIN": "AUTHENTICATION",
    "OTP": "AUTHENTICATION",
    "SECRET": "AUTHENTICATION",
    "PRIVATE_KEY": "AUTHENTICATION",
    "PUBLIC_KEY": "AUTHENTICATION",
    "API_KEY": "AUTHENTICATION",
    "BEARER_TOKEN": "AUTHENTICATION",
    "JWT": "AUTHENTICATION",
    "OAUTH_TOKEN": "AUTHENTICATION",
    "REFRESH_TOKEN": "AUTHENTICATION",
    "COOKIE": "AUTHENTICATION",
    "SESSION_ID": "AUTHENTICATION",
    "ENCRYPTION_KEY": "AUTHENTICATION",
    "VAULT_SECRET": "AUTHENTICATION",

    # ============================================================
    # EMPLOYEE DATA
    # ============================================================
    "EMPLOYEE_ID": "EMPLOYEE_DATA",
    "EMPLOYEE_NAME": "EMPLOYEE_DATA",
    "SALARY": "EMPLOYEE_DATA",
    "JOINING_DATE": "EMPLOYEE_DATA",
    "MANAGER": "EMPLOYEE_DATA",
    "DEPARTMENT": "EMPLOYEE_DATA",
    "ROLE": "EMPLOYEE_DATA",
    "PERFORMANCE_REVIEW": "EMPLOYEE_DATA",
    "ATTENDANCE": "EMPLOYEE_DATA",
    "PAYROLL": "EMPLOYEE_DATA",
    "PROMOTION": "EMPLOYEE_DATA",
    "RESIGNATION": "EMPLOYEE_DATA",

    # ============================================================
    # CUSTOMER DATA
    # ============================================================
    "CUSTOMER_ID": "CUSTOMER_DATA",
    "CRM_NUMBER": "CUSTOMER_DATA",
    "CUSTOMER_NAME": "CUSTOMER_DATA",
    "CUSTOMER_ADDRESS": "CUSTOMER_DATA",
    "CUSTOMER_EMAIL": "CUSTOMER_DATA",
    "CUSTOMER_PHONE": "CUSTOMER_DATA",
    "PURCHASE_HISTORY": "CUSTOMER_DATA",
    "ORDER_HISTORY": "CUSTOMER_DATA",
    "SUBSCRIPTION": "CUSTOMER_DATA",
    "SUPPORT_TICKET": "CUSTOMER_DATA",

    # ============================================================
    # HEALTH DATA
    # ============================================================
    "DIAGNOSIS": "HEALTH_DATA",
    "MEDICINE": "HEALTH_DATA",
    "DOCTOR": "HEALTH_DATA",
    "HOSPITAL": "HEALTH_DATA",
    "PATIENT_ID": "HEALTH_DATA",
    "PRESCRIPTION": "HEALTH_DATA",
    "MEDICAL_REPORT": "HEALTH_DATA",
    "LAB_REPORT": "HEALTH_DATA",
    "MRI": "HEALTH_DATA",
    "XRAY": "HEALTH_DATA",
    "INSURANCE": "HEALTH_DATA",
    "CLAIM_ID": "HEALTH_DATA",
    "POLICY_NUMBER": "HEALTH_DATA",
    # ============================================================
    # LEGAL DATA
    # ============================================================
    "AGREEMENT": "LEGAL_DATA",
    "CONTRACT": "LEGAL_DATA",
    "NDA": "LEGAL_DATA",
    "LEGAL_NOTICE": "LEGAL_DATA",
    "SETTLEMENT": "LEGAL_DATA",
    "ARBITRATION": "LEGAL_DATA",
    "PATENT": "LEGAL_DATA",
    "TRADEMARK": "LEGAL_DATA",
    "COPYRIGHT": "LEGAL_DATA",
    "LICENSE": "LEGAL_DATA",

    # ============================================================
    # SOURCE CODE
    # ============================================================
    "PYTHON": "SOURCE_CODE",
    "JAVA": "SOURCE_CODE",
    "CPP": "SOURCE_CODE",
    "CSHARP": "SOURCE_CODE",
    "JAVASCRIPT": "SOURCE_CODE",
    "REACT": "SOURCE_CODE",
    "FLUTTER": "SOURCE_CODE",
    "NODEJS": "SOURCE_CODE",
    "SPRING": "SOURCE_CODE",
    "DJANGO": "SOURCE_CODE",
    "FASTAPI": "SOURCE_CODE",
    "SQL_QUERY": "SOURCE_CODE",
    "STORED_PROCEDURE": "SOURCE_CODE",

    # ============================================================
    # DATABASE
    # ============================================================
    "DATABASE": "DATABASE_INFO",
    "SQL": "DATABASE_INFO",
    "MONGODB": "DATABASE_INFO",
    "REDIS": "DATABASE_INFO",
    "POSTGRESQL": "DATABASE_INFO",
    "MYSQL": "DATABASE_INFO",
    "CONNECTION_STRING": "DATABASE_INFO",
    "ENVIRONMENT_VARIABLE": "DATABASE_INFO",
    "ENV_FILE": "DATABASE_INFO",
    "DOCKER_SECRET": "DATABASE_INFO",
    "KUBERNETES_SECRET": "DATABASE_INFO",
    "CONFIG_FILE": "DATABASE_INFO",

    # ============================================================
    # INFRASTRUCTURE
    # ============================================================
    "HOSTNAME": "INFRASTRUCTURE",
    "SERVER": "INFRASTRUCTURE",
    "FIREWALL": "INFRASTRUCTURE",
    "VPN": "INFRASTRUCTURE",
    "SSH": "INFRASTRUCTURE",
    "PORT": "INFRASTRUCTURE",
    "DNS": "INFRASTRUCTURE",
    "LOAD_BALANCER": "INFRASTRUCTURE",
    "CLOUD": "INFRASTRUCTURE",
    "AWS": "INFRASTRUCTURE",
    "AZURE": "INFRASTRUCTURE",
    "GCP": "INFRASTRUCTURE",
    "IAM": "INFRASTRUCTURE",
    "S3_BUCKET": "INFRASTRUCTURE",
    "EC2": "INFRASTRUCTURE",
    "LAMBDA": "INFRASTRUCTURE",

    # ============================================================
    # BUSINESS STRATEGY
    # ============================================================
    "ROADMAP": "BUSINESS_STRATEGY",
    "ACQUISITION_PLAN": "BUSINESS_STRATEGY",
    "PRODUCT_STRATEGY": "BUSINESS_STRATEGY",
    "MERGER": "BUSINESS_STRATEGY",
    "PLANNING": "BUSINESS_STRATEGY",
    "BUSINESS_PLAN": "BUSINESS_STRATEGY",

    # ============================================================
    # FINANCIAL REPORT
    # ============================================================
    "REVENUE": "FINANCIAL_REPORT",
    "PROFIT": "FINANCIAL_REPORT",
    "LOSS": "FINANCIAL_REPORT",
    "FORECAST": "FINANCIAL_REPORT",
    "BUDGET": "FINANCIAL_REPORT",
    "INVOICE": "FINANCIAL_REPORT",
    "PURCHASE_ORDER": "FINANCIAL_REPORT",
    "BONUS": "FINANCIAL_REPORT",
    "TAX": "FINANCIAL_REPORT",

    # ============================================================
    # INTELLECTUAL PROPERTY
    # ============================================================
    "ALGORITHM": "INTELLECTUAL_PROPERTY",
    "RESEARCH": "INTELLECTUAL_PROPERTY",
    "FORMULA": "INTELLECTUAL_PROPERTY",
    "BLUEPRINT": "INTELLECTUAL_PROPERTY",
    "ARCHITECTURE": "INTELLECTUAL_PROPERTY",
    "PROTOTYPE": "INTELLECTUAL_PROPERTY",
    "DESIGN_DOCUMENT": "INTELLECTUAL_PROPERTY",
    "TRADE_SECRET": "INTELLECTUAL_PROPERTY",

    # ============================================================
    # COMPANY CONFIDENTIAL
    # ============================================================
    "CONFIDENTIAL": "COMPANY_CONFIDENTIAL",
    "INTERNAL_ONLY": "COMPANY_CONFIDENTIAL",
    "RESTRICTED": "COMPANY_CONFIDENTIAL",
    "PRIVATE": "COMPANY_CONFIDENTIAL",
    "BOARD_MEETING": "COMPANY_CONFIDENTIAL",
    "ACQUISITION": "COMPANY_CONFIDENTIAL",
    "STRATEGY": "COMPANY_CONFIDENTIAL",

    # ============================================================
    # CLOUD CREDENTIALS
    # ============================================================
    "AWS_ACCESS_KEY": "CLOUD_CREDENTIALS",
    "AWS_SECRET_KEY": "CLOUD_CREDENTIALS",
    "AZURE_KEY": "CLOUD_CREDENTIALS",
    "GCP_SERVICE_ACCOUNT_KEY": "CLOUD_CREDENTIALS",

    # ============================================================
    # CRYPTO KEYS
    # ============================================================
    "RSA_KEY": "CRYPTO_KEYS",
    "SSH_KEY": "CRYPTO_KEYS",
    "CERTIFICATE": "CRYPTO_KEYS",
    "PRIVATE_KEY_FILE": "CRYPTO_KEYS",

    # ============================================================
    # AI / LLM
    # ============================================================
    "PROMPT": "AI_LLM_SPECIFIC",
    "SYSTEM_PROMPT": "AI_LLM_SPECIFIC",
    "EMBEDDING": "AI_LLM_SPECIFIC",
    "FINE_TUNING_DATA": "AI_LLM_SPECIFIC",
    "TRAINING_DATASET": "AI_LLM_SPECIFIC",
    "VECTOR_DATABASE": "AI_LLM_SPECIFIC",
    "RAG": "AI_LLM_SPECIFIC",
    "KNOWLEDGE_BASE": "AI_LLM_SPECIFIC",
    "PROMPT_TEMPLATE": "AI_LLM_SPECIFIC",
    "CONTEXT_WINDOW": "AI_LLM_SPECIFIC",
    "MODEL_WEIGHTS": "AI_LLM_SPECIFIC",
    "INFERENCE_ENDPOINT": "AI_LLM_SPECIFIC",

    # ============================================================
    # PUBLIC INFORMATION
    # ============================================================
    "PUBLIC_DOCUMENTATION": "PUBLIC_INFORMATION",
    "BLOG_POST": "PUBLIC_INFORMATION",
    "PRESS_RELEASE": "PUBLIC_INFORMATION",
    "MARKETING_COPY": "PUBLIC_INFORMATION",
}