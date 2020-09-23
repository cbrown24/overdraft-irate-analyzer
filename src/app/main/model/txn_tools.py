from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict
import calendar

@dataclass
class Transaction:
    description: str
    amount: float
    balance: float
    timestamp: datetime
    institution: str = None
    display_name: str = None
    category: str = None
    type: str = None
    merchant: str = None
    underwriting_category: str = None
    underwriting_subcategory: str = None
    spend_cat_1: str = None
    spend_cat_2: str = None
    spend_class_1: str = None
    spend_merchant: str = None
    truelayer_category_1: str = None
    truelayer_category_2: str = None

@dataclass
class Result:
    date: datetime
    value: float

@dataclass
class Report:
    name: str
    data: List[Result] = field(default_factory=list)

@dataclass
class ODCharges:
    transactions: List[Transaction] = field(default_factory=list, repr=False)
    _od_marker = 'DAILY OD INT'

    def _apr(self, charges: List[int]):
        months = 12
        return (sum(charges) / len(charges)) / months

    def _update_transactions(self, t:Transaction, tx_by_month: Dict[int, List[float]]) -> None:
        y = datetime.strptime(t.timestamp, "%Y-%m-%d").year
        m = datetime.strptime(t.timestamp, "%Y-%m-%d").month
        last_date_of_month = calendar.monthrange(y,m)[1]
        date = datetime(y, m, last_date_of_month)
        tx_by_month.setdefault(date, []).append((t.amount/t.balance)*100)

    def createSummary(self) -> List[Report]:
        tx_by_month = {}
        for t in self.transactions:
            self._update_transactions(t, tx_by_month)

        apr_report = Report(name='apr')
        sum_report = Report(name='sum')
        for date, charges in tx_by_month.items():
            apr_report.data.append(Result(date, self._apr(charges)))
            sum_report.data.append(Result(date, sum(charges)))

        return [apr_report, sum_report]

