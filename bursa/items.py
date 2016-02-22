import scrapy


class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    site_id = scrapy.Field()
    description = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    corporate_number = scrapy.Field()
    issuer_number = scrapy.Field()
    industry = scrapy.Field()
    sector = scrapy.Field()
    niche = scrapy.Field()
    location = scrapy.Field()

class MarketCapItem(scrapy.Item):
    cap = scrapy.Field()
    company_id = scrapy.Field()

class StakeHolderItem(scrapy.Item):
    company_id = scrapy.Field()
    name = scrapy.Field()
    note = scrapy.Field()
    update_date = scrapy.Field()
    site_id = scrapy.Field()
    security_name = scrapy.Field()
    stock_count = scrapy.Field()
    capital_rate = scrapy.Field()
    proxy_rate = scrapy.Field()
    market_cap = scrapy.Field()

class ManagementItem(scrapy.Item):
    company_id = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    security_name = scrapy.Field()
    stock_count = scrapy.Field()
    capital_rate = scrapy.Field()
    proxy_rate = scrapy.Field()
    expertise = scrapy.Field()
    audit_committee = scrapy.Field()

class FinancialReportItem(scrapy.Item):
    year = scrapy.Field()
    total_balance = scrapy.Field()
    current_assets = scrapy.Field()
    long_term_assets = scrapy.Field()
    shareholders_equity = scrapy.Field()
    minority_equity = scrapy.Field()
    current_liabilities = scrapy.Field()
    long_term_liabilities = scrapy.Field()
    revenues = scrapy.Field()
    gross_profit = scrapy.Field()
    operating_income = scrapy.Field()
    income_before_tax = scrapy.Field()
    net_income = scrapy.Field()
    net_income_attributable_to_shareholders = scrapy.Field()
    net  = scrapy.Field()
    dividend = scrapy.Field()
    operating_activities_cash = scrapy.Field()
    capital_market = scrapy.Field()
    multiplier = scrapy.Field()
    capital_to_balance_sheet_ratio = scrapy.Field()
    return_on_equity = scrapy.Field()