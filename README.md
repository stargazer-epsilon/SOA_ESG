# SOA_ESG
Python Refactor of C3 Phase III Economic Scenario Generator managed by The American Academy of Actuaries and the Society of Actuaries used in regulatory reserve and capital calculations

**Microsoft Excel Objects:**
Sheet1 (MRP)
Sheet11 (Historical Curves)
Sheet2 (Scenario Subsets)
Sheet3 (Scenario Generator)
Sheet4 (Settings)
Sheet6 (Parameters)
Sheet7 (Single Scenario)
Sheet8 (TestShocks)
Sheet9 (Change log)

**Forms:**
GetHistDateForm
ProgressForm

**Modules:**
DateModule
EconSMLModule
GlobalsModule
HelperRoutines
NewGenerator
SETModule

**Class Modules:**
C3RNG
Chloeski
DelimitedDataReader
DelimitedReaderSet
DelimitedString
EquityFundReturnClass
FixedFundReturnClass
FundScenarioClass
HistCurvesClass
IntScenarioClass
YieldCurveClass

**Macros:**
CloseEconSMLFile
GetParameters
MRP_Update
ProcessAllScenarios
ResetInitialVolatility
Sheet7.UpdateRandomDraws

**Original Documentation:**

From: https://www.soa.org/resources/tables-calcs-tools/2023-research-airg/

_Economic Scenario Generators Disclaimer
The Academy and the Society of Actuaries have taken reasonable steps to develop such scenarios and tools consistent with accepted actuarial principles and practices. However, the Academy and the SOA do not warrant these scenarios and tools as fit for use in any respect, and no warranty whatsoever should be assumed or implied by any individual of this product or its fitness for any particular purpose. Actuaries, insurers, regulators and other parties use these scenarios and tools at their own risk. The Academy and the SOA disclaim all responsibility for any party's use or misuse of its scenarios or tools and for any work product generated through use or misuse of the scenarios and tools.  _

FAQ: https://www.soa.org/49c5cd/globalassets/assets/files/static-pages/research/2023-academy-interest-rate-generator-faq.pdf

Practical Guide (1/2): https://www.soa.org/resources/research-reports/2016/2016-economic-scenario-generators/
Practical Guide (2/2): https://www.soa.org/493868/globalassets/assets/files/research/projects/research-2016-economic-scenario-generators.pdf

Equity Scenario Generation Details: https://www.actuary.org/content/c3-phase-ii-rbc-and-reserves-project
