chron_conditions = [
    'CC_NONE',     # 'No Chronic Conditions'
    'CC_ALZHDMTA', # 'Alzheimer\'s Disease and Related Disorders or Senile Dementia'
    'CC_CANCER',   # 'Cancer'
    'CC_CHF',      # 'Heart Failure'
    'CC_CHRNKIDN', # 'Chronic Kidney Disease'
    'CC_COPD',     # 'Chronic Obstructive Pulmonary Disease'
    'CC_DEPRESSN', # 'Depression'
    'CC_DIABETES', # 'Diabetes'
    'CC_ISCHMCHT', # 'Ischemic Heart Disease'
    'CC_OSTEOPRS', # 'Osteoporosis'
    'CC_RA_OA',    # 'Rheumatoid Arthritis/Osteoarthritis Arthritis'
    'CC_STRKETIA', # 'Stroke/Transient Ischemic Attack'
]


var_map = {
    'BENE_SEX_IDENT_CD' : 'Gender',
    'BENE_AGE_CAT_CD'   : 'Age',

    'CC_NONE'           : 'No Chronic Conditions',
    'CC_ALZHDMTA'       : 'Alzheimer\'s Disease',
    'CC_CANCER'         : 'Cancer',
    'CC_CHF'            : 'Heart Failure',
    'CC_CHRNKIDN'       : 'Chronic Kidney Disease',
    'CC_COPD'           : 'Chronic Obstructive Pulmonary Disease',
    'CC_DEPRESSN'       : 'Depression',
    'CC_DIABETES'       : 'Diabetes',
    'CC_ISCHMCHT'       : 'Ischemic Heart Disease',
    'CC_OSTEOPRS'       : 'Osteoporosis',
    'CC_RA_OA'          : 'Rheumatoid Arthritis',
    'CC_STRKETIA'       : 'Stroke/Transient Ischemic Attack',
    'CC_2_OR_MORE'      : 'Two or More Chronic Conditions',

    'DUAL_STUS' : 'Dual Eligibility Status', #  (eligible for both Medicare and Medicaid)

    # (Part A < 12)
    'BENE_COUNT_PA_LT_12'   : 'Count of Beneficiaries (Part A < 12)',
    'AVE_MO_EN_PA_LT_12'    : 'Average Months of Enrollment (Part A < 12)',
    'AVE_PA_PAY_PA_LT_12'   : 'Average Medicare Payment for Part A per Beneficiary (Part A < 12)',
    'AVE_IP_PAY_PA_LT_12'   : 'Average Medicare Payment for IP per Beneficiary (Part A < 12)',
    'AVE_SNF_PAY_PA_LT_12'  : 'Average Medicare Payment for SNF per Beneficiary (Part A < 12)',
    'AVE_OTH_PAY_PA_LT_12'  : 'Average Medicare Payment for other services per Beneficiary (Part A < 12)',
    'AVE_IP_ADM_PA_LT_12'   : 'Average IP Admissions per Beneficiary (Part A < 12)',
    'AVE_SNF_DAYS_PA_LT_12' : 'Average SNF Covered Days per Beneficiary (Part A < 12)',

    # (Part A = 12)
    'BENE_COUNT_PA_EQ_12'   : 'Count of Beneficiaries (Part A = 12)',
    'AVE_PA_PAY_PA_EQ_12'   : 'Average Medicare Payment for Part A per Beneficiary (Part A = 12)',
    'AVE_IP_PAY_PA_EQ_12'   : 'Average Medicare Payment for IP per Beneficiary (Part A = 12)',
    'AVE_SNF_PAY_PA_EQ_12'  : 'Average Medicare Payment for SNF per Beneficiary (Part A = 12)',
    'AVE_OTH_PAY_PA_EQ_12'  : 'Average Medicare Payment for other services per Beneficiary (Part A = 12)',
    'AVE_IP_ADM_PA_EQ_12'   : 'Average IP Admissions per Beneficiary (Part A = 12)',
    'AVE_SNF_DAYS_PA_EQ_12' : 'Average SNF Covered Days per Beneficiary (Part A = 12)',

    # (Part B < 12)
    'BENE_COUNT_PB_LT_12'   : 'Count of Beneficiaries (Part B < 12)',
    'AVE_MO_EN_PB_LT_12'    : 'Average Months of Enrollment (Part B < 12)',
    'AVE_PB_PAY_PB_LT_12'   : 'Average Medicare Payment for Part B per Beneficiary (Part B < 12)',
    'AVE_CA_PAY_PB_LT_12'   : 'Average Medicare Payment for CA per Beneficiary (Part B < 12)',
    'AVE_OP_PAY_PB_LT_12'   : 'Average Medicare Payment for OP per Beneficiary (Part B < 12)',
    'AVE_OTH_PAY_PB_LT_12'  : 'Average Medicare Payment for other services per Beneficiary (Part B < 12)',
    'AVE_CA_VST_PB_LT_12'   : 'Average CA Visits per Beneficiary (Part B < 12)',
    'AVE_OP_VST_PB_LT_12'   : 'Average OP Visits per Beneficiary (Part B < 12)',

    # (Part B = 12)
    'BENE_COUNT_PB_EQ_12'   : 'Count of Beneficiaries (Part B = 12)',
    'AVE_PB_PAY_PB_EQ_12'   : 'Average Medicare Payment for Part B per Beneficiary (Part B = 12)',
    'AVE_CA_PAY_PB_EQ_12'   : 'Average Medicare Payment for CA per Beneficiary (Part B = 12)',
    'AVE_OP_PAY_PB_EQ_12'   : 'Average Medicare Payment for OP per Beneficiary (Part B = 12)',
    'AVE_OTH_PAY_PB_EQ_12'  : 'Average Medicare Payment for other services per Beneficiary (Part B = 12)',
    'AVE_CA_VST_PB_EQ_12'   : 'Average CA Visits per Beneficiary (Part B = 12)',
    'AVE_OP_VST_PB_EQ_12'   : 'Average OP Visits per Beneficiary (Part B = 12)',

    # (Part C < 12)
    'BENE_COUNT_PC_LT_12'   : 'Count of Beneficiaries (Part C < 12)',
    'AVE_MO_EN_PC_LT_12'    : 'Average Months of Enrollment (Part C < 12)',

    # (Part C = 12)
    'BENE_COUNT_PC_EQ_12'   : 'Count of Beneficiaries (Part C = 12)',

    # (Part D < 12)
    'BENE_COUNT_PD_LT_12'   : 'Count of Beneficiaries (Part D < 12)',
    'AVE_MO_EN_PD_LT_12'    : 'Average Months of Enrollment (Part D < 12)',
    'AVE_PDE_CST_PD_LT_12'  : 'Average Drug Cost per Beneficiary (Part D < 12)',
    'AVE_PDE_PD_LT_12'      : 'Average Prescriptions per Beneficiary (Part D < 12)',

    # (Part D = 12)
    'BENE_COUNT_PD_EQ_12'   : 'Count of Beneficiaries (Part D = 12)',
    'AVE_PDE_CST_PD_EQ_12'  : 'Average Drug Cost per Beneficiary (Part D = 12)',
    'AVE_PDE_PD_EQ_12'      : 'Average Prescriptions per Beneficiary (Part D = 12)',
}
