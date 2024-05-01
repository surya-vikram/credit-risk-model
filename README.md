# Domain Knowledge (Bank's Perspective)
## Assets & Liability
_An Asset makes profit_
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

## Types of Credit Risk
1. DPD = 0 : NDA (Non-Delinquint Account)
2. 0 < DPD <= 30 : SMA1 (Standard Monitoring Account)
3. 30 < DPD <= 60 : SMA2
4. 60 < DPD <= 90 : SMA3
5. 90 < DPD <= 180 : NPA
6. DPD > 180 : Written-Off (Loan is removed from the records)

_A bank writes-off loans once the DPD crosses 180 to improve NPA. Due to this loan portfolio quality of the bank is better which positively impacts market sentiment._

### Types of NPA
1. GNPA (Gross NPA) : 
    - Percentage of defaulted OSP or PAR
    - Generally [3, 5]
2. NNPA (Net NPA) : 
    - Percentage of PAR after subtracting Provision Amount which bank carries
    - Generally [0.01, 0.06]

**_GNPA should be used for bank quality assessment._**

