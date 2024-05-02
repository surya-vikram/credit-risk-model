# Domain Knowledge (Bank's Perspective)
## Assets & Liability
_An Asset (Loan or Trade Line) makes profit_
- House Loan
- Vehicle Loan
- Personal Loan
- Group Loan
- Education Loan
- Credit Card
---
_A Liability helps the bank sustain_
* CASA
    * Current Account
    * Savings Account

* Term Deposit
    * Fixed Deposit
    * Recurring Deposit

---

## NPA (Non-Performing Asset)
_Loan that is defaulted_
1. Disbursed Amount 
    - Total loan given to the customer
2. OSP (Out-Standing Principle) 
    - Amount yet to be payed by the customer
    - It should be zero at the end of loan cycle
3. DPD (Days Past Due)
    - Ideally, it should be zero
    - Defaulted if DPD > 0
4. PAR (Portfolio At Risk)
    - OSP when DPD > 0
5. NPA 
    - Loan account when DPD > 90

---

## Types of Credit Risk
1. DPD = 0 : NDA (Non-Delinquint Account)
2. 0 < DPD <= 30 : SMA1 (Standard Monitoring Account)
3. 30 < DPD <= 60 : SMA2
4. 60 < DPD <= 90 : SMA3
5. 90 < DPD <= 180 : NPA
6. DPD > 180 : Written-Off (Loan is removed from the records)

_A bank writes-off loans once the DPD crosses 180 to improve NPA. Due to this loan portfolio quality of the bank is better which positively impacts market sentiment._

---

### Types of NPA
1. GNPA (Gross NPA) : 
    - Percentage of defaulted OSP or PAR
    - Generally [3, 5]
2. NNPA (Net NPA) : 
    - Percentage of PAR after subtracting Provision Amount which bank carries
    - Generally [0.01, 0.06]

**_GNPA should be used for bank quality assessment._**

---
### Types of Datasets
1. Internal
2. External (CIBIL)

#### CIBIL (Credit Information Bureau India Limited)
- collects and maintains credit information of individuals and commercial entities, including loans & credit card details from banks and other financial institutions.

| Variable Name                | Description                                               |
|------------------------------|-----------------------------------------------------------|
| time_since_recent_payment    | Time since recent Payment made                            |
| time_since_first_deliquency  | Time since first Delinquency (missed payment)             |
| time_since_recent_deliquency | Time Since recent Delinquency                             |
| num_times_delinquent         | Number of times delinquent                                |
| max_delinquency_level        | Maximum delinquency level                                 |
| max_recent_level_of_deliq    | Maximum recent level of delinquency                       |
| num_deliq_6mts               | Number of times delinquent in last 6 months               |
| num_deliq_12mts              | Number of times delinquent in last 12 months              |
| num_deliq_6_12mts            | Number of times delinquent between last 6 and 12 months   |
| max_deliq_6mts               | Maximum delinquency level in last 6 months                |
| max_deliq_12mts              | Maximum delinquency level in last 12 months               |
| num_times_30p_dpd            | Number of times 30+ days past due                        |
| num_times_60p_dpd            | Number of times 60+ days past due                        |
| num_std                      | Number of standard Payments                              |
| num_std_6mts                 | Number of standard Payments in last 6 months             |
| num_std_12mts                | Number of standard Payments in last 12 months            |
| num_sub                      | Number of sub standard payments - not making full payments |
| num_sub_6mts                 | Number of sub standard payments in last 6 months         |
| num_sub_12mts                | Number of sub standard payments in last 12 months        |
| num_dbt                      | Number of doubtful payments                              |
| num_dbt_6mts                 | Number of doubtful payments in last 6 months             |
| num_dbt_12mts                | Number of doubtful payments in last 12 months            |
| num_lss                      | Number of loss accounts                                  |
| num_lss_6mts                 | Number of loss accounts in last 6 months                 |
| num_lss_12mts                | Number of loss accounts in last 12 months                |
| recent_level_of_deliq        | Recent level of delinquency                              |
| tot_enq                      | Total enquiries                                          |
| CC_enq                       | Credit card enquiries                                    |
| CC_enq_L6m                   | Credit card enquiries in last 6 months                   |
| CC_enq_L12m                  | Credit card enquiries in last 12 months                  |
| PL_enq                       | Personal Loan enquiries                                  |
| PL_enq_L6m                   | Personal Loan enquiries in last 6 months                 |
| PL_enq_L12m                  | Personal Loan enquiries in last 12 months                |
| time_since_recent_enq        | Time since recent enquiry                                |
| enq_L12m                     | Enquiries in last 12 months                              |
| enq_L6m                      | Enquiries in last 6 months                               |
| enq_L3m                      | Enquiries in last 3 months                               |
| MARITALSTATUS                | Marital Status                                           |
| EDUCATION                    | Education level                                          |
| AGE                          | Age                                                       |
| GENDER                       | Gender                                                    |
| NETMONTHLYINCOME             | Net Monthly Income                                       |
| Time_With_Curr_Empr          | Time with current Employer                               |
| pct_of_active_TLs_ever       | Percent active accounts ever                             |
| pct_opened_TLs_L6m_of_L12m   | Percent accounts opened in last 6 months to last 12 months|
| pct_currentBal_all_TL        | Percent current balance of all accounts                  |
| CC_utilization               | Credit card utilization                                  |
| CC_Flag                      | Credit card Flag                                         |
| PL_utilization               | Personal Loan utilization                                |
| PL_Flag                      | Personal Loan Flag                                       |
| pct_PL_enq_L6m_of_L12m       | Percent enquiries PL in last 6 months to last 12 months   |
| pct_CC_enq_L6m_of_L12m       | Percent enquiries CC in last 6 months to last 12 months   |
| pct_PL_enq_L6m_of_ever       | Percent enquiries PL in last 6 months to all enquiries   |
| pct_CC_enq_L6m_of_ever       | Percent enquiries CC in last 6 months to all enquiries   |
| max_unsec_exposure_inPct     | Maximum unsecured exposure in percent                    |
| HL_Flag                      | Housing Loan Flag                                        |
| GL_Flag                      | Gold Loan Flag                                           |
| last_prod_enq2               | Latest product enquired for                              |
| first_prod_enq2              | First product enquired for                               |
| Credit_Score                 | Applicant's credit score                                 |
| Approved_Flag                | Priority levels                                          |

#### Internal TL
- details on internal loan products of customer

| Variable Name          | Description                                             |
|------------------------|---------------------------------------------------------|
| Total_TL               | Total trade lines/accounts in Bureau                    |
| Tot_Closed_TL          | Total closed trade lines/accounts                       |
| Tot_Active_TL          | Total active accounts                                   |
| Total_TL_opened_L6M    | Total accounts opened in last 6 Months                  |
| Tot_TL_closed_L6M      | Total accounts closed in last 6 months                  |
| pct_tl_open_L6M        | Percent accounts opened in last 6 months                |
| pct_tl_closed_L6M      | Percent accounts closed in last 6 months               |
| pct_active_tl          | Percent active accounts                                 |
| pct_closed_tl          | Percent closed accounts                                 |
| Total_TL_opened_L12M   | Total accounts opened in last 12 Months                |
| Tot_TL_closed_L12M     | Total accounts closed in last 12 months                 |
| pct_tl_open_L12M       | Percent accounts opened in last 12 months               |
| pct_tl_closed_L12M     | Percent accounts closed in last 12 months               |
| Tot_Missed_Pmnt        | Total missed Payments                                   |
| Auto_TL                | Count Automobile accounts                               |
| CC_TL                  | Count of Credit card accounts                           |
| Consumer_TL            | Count of Consumer goods accounts                       |
| Gold_TL                | Count of Gold loan accounts                             |
| Home_TL                | Count of Housing loan accounts                          |
| PL_TL                  | Count of Personal loan accounts                         |
| Secured_TL             | Count of secured accounts                               |
| Unsecured_TL           | Count of unsecured accounts                             |
| Other_TL               | Count of other accounts                                 |
| Age_Oldest_TL          | Age of oldest opened account                            |
| Age_Newest_TL          | Age of newest opened account                            |

***

### Multiclass Classification
- target column - Approved_Flag 
- labels - P1, P2, P3, P4 
- values signify different priority levels for the customer
- P1 being the best customer to provide loan
- P4 being the worst customer to provide loan

***
#### Facts
- _Bank wishes to lend money to people who don't need money_
- _Credit Card Utilization & bank rewards are directly proportional_
- _CC Utilization & Credit Score are inversely proportional_
    
