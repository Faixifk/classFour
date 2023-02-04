from wallet import Wallet

import unittest

class test(unittest.TestCase):

     def testWallet(self):

        w = Wallet(200)
        self.assertEqual(w.getAccount(), 200)


unittest.main()
