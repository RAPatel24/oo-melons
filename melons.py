"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if "christmas melon" in self.species :
            base_price *= 1.5
        if "international" in self.order_type and self.qty < 10 :
            total = ((1 + self.tax) * self.qty * base_price) + 3
        else :
            total = (1 + self.tax) * self.qty * base_price 
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species,qty,"domestic",0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
      super().__init__(species,qty,"international",0.17)
      self.country_code = country_code
        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super().__init__(species,qty,"goverment",0)
        self.pass_inspection = False

    def mark_inspection(self, passed):
        self.pass_inspection = True
