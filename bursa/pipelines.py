from models import Company as CompanyModel
from models import MarketCap as MarketCapModel
from models import StakeHolders as StakeHolderModel
from models import Management as ManagementModel
import bursa.spiders as spiders

class SaveInfoItemToDB(object):
    def process_item(self, item, spider):
        if type(spider) is not spiders.info.InfoSpider:
            return item

        # process item
        company, created = CompanyModel.get_or_create(site_id=item['site_id'])
        company.update(**item).where(CompanyModel.site_id == company.site_id).execute()

        return created


class SaveMarketCapItemToDB(object):
    def process_item(self, item, spider):
        if type(spider) is not spiders.market_cap.MarketCapSpider:
            return item

        # process item
        if item['cap'] > 0:
            MarketCapModel.create(company=item['company_id'], cap=item['cap'])


class SaveStakeHolderItemsToDB(object):
    def process_item(self, item, spider):
        if type(spider) is not spiders.stake_holder.StakeHolderSpider:
            return item

        # process item
        StakeHolderModel.create(company=item.pop('company_id'), **item)


class SaveManagementItemsToDB(object):
    def process_item(self, item, spider):
        if type(spider) is not spiders.management.ManagementSpider:
            return item

        # process item
        ManagementModel.create(company=item.pop('company_id'), **item)