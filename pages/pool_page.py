from pages.base_page import BasePage
from pages.staking_page import StakingPage


class PoolPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "staking/pools"




        # self. title = page.locator()
        #
        # # tabs on the POOlS page
        # self.overview_tab = page.locator()
        # self.all_pools_tab = page.locator()
        #
        # # Statistics section
        # self.active_pools = page.locator()
        # self.min_to_join_pool = page.locator()

        #Bonded Funds section

        # Pool membership overview

        # validators section



