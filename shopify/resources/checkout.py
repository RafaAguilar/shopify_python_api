from ..base import ShopifyResource
from shopify import mixins

class Checkout(ShopifyResource):

    @classmethod
    def search(cls, **kwargs):
        """
        Search for checkouts matching supplied query

        Args:
           order: Field and direction to order results by (default: last_order_date DESC)
           query: Text to search for checkouts
           page: Page to show (default: 1)
           limit: Amount of results (default: 50) (maximum: 250)
           fields: comma-seperated list of fields to include in the response
        Returns:
           An array of checkouts.
        """
        return cls._build_list(cls.get("search", **kwargs))
