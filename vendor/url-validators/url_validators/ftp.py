"""
This modules contains functionalities related to FTP url shcemes

Classes:
    * FTP
"""

from url import URL

class FTP(URL):
    """
    Split the ftp url into the parts which constitute the url

    Methods:
        * scheme
    Variable:
        * url

    """
    def __init__(self, url):
        self.url = url

    def scheme(self):
        """
        Get the scheme of the url

        :returns str: The scheme part of the url
        """
        pass
