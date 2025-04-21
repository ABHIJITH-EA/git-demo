"""
The url class will parse a url and find the constiting parts.

Classes:
    * url - Split url according to RFC 1738
"""

class URL:
    """
    Split the url into the parts which constitute a url
    according to the RF 1738 documentation.

    Methods:
        * scheme
    Variables:
        * url
    """
    def __init__(self, url: str):
        self.url = url

    def scheme(self):
        """
        Get the scheme of the url

        :returns str: The scheme part of the url
        """
        pass
