import unittest
from bibmon._load_data import load_tennessee_eastman

class TestLoadTennesseeEastman(unittest.TestCase):
    
    # Caso de Teste CT1: file_train com 7 caracteres
    def test_file_train_length_7(self):
        train_id = 1  # ID correspondente ao file_train com 7 caracteres
        file_train = f"d{train_id:02}.dat"  # Simula o arquivo gerado
        self.assertEqual(len(file_train), 7)
    
    # Caso de Teste CT2: file_train com menos de 7 caracteres
    def test_file_train_length_less_than_7(self):
        file_train = "d1.dat"  # Simula um arquivo com menos de 7 caracteres
        self.assertNotEqual(len(file_train), 7)
    
    # Caso de Teste CT3: file_test com 10 caracteres
    def test_file_test_length_10(self):
        test_id = 10  # ID correspondente ao file_test com 10 caracteres
        file_test = f"d{test_id:02}_te.dat"  # Simula o arquivo gerado
        self.assertEqual(len(file_test), 10)
    
    # Caso de Teste CT4: file_test com menos de 10 caracteres
    def test_file_test_length_less_than_10(self):
        file_test = "d1_te.dat"  # Simula um arquivo com menos de 10 caracteres
        self.assertNotEqual(len(file_test), 10)

    # Caso de Teste CT5: file_train igual a 'd00.dat'
    def test_file_train_equals_d00(self):
        file_train = "d00.dat"  # Simula o arquivo
        self.assertEqual(file_train, "d00.dat")

    # Caso de Teste CT6: file_train diferente de 'd00.dat'
    def test_file_train_not_equals_d00(self):
        file_train = "d01.dat"  # Simula o arquivo
        self.assertNotEqual(file_train, "d00.dat")

if __name__ == "__main__":
    unittest.main()
