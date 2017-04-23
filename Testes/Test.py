#$File created by Jorge Heleno
#October the 19th 02:07

import unittest;
#Trocar "main" pelo nome do ficheiro com o projecto
from main import *;

class AdvancedOperation(unittest.TestCase):
    testTuple=('a','A',' ','.',',',';','B','C','D','d','o','P');

    def test_Generate(self):
        print("Advanced Generate test Running");
        self.assertEqual(gera_chave2(self.testTuple),(('a','A',' ','.',','),(';','B','C','D','d'),('o','P')),"Error in gera_chave2");

    def test_getCode1(self):
        print("Advanced getCode1 test running");
        self.assertEqual(obtem_codigo1('a',gera_chave2(self.testTuple)),'00',"Erro on obtem-codigo2");
    def test_getCode2(self):
        print("Advanced getCode2 test running");
        self.assertEqual(obtem_codigo2('o',gera_chave2(self.testTuple)),'20',"Erro on obtem-codigo2");
    def test_getCode3(self):
        print("Advanced getCode3 test running");
        self.assertEqual(obtem_codigo2('+',gera_chave2(self.testTuple)),'XX',"Erro on obtem-codigo2");

    def test_codify1(self):
        print("Advanced codify1 test running");
        self.assertEqual(codifica2('BCa.oP',gera_chave2(self.testTuple)),'111200032021',"Erro on codifica2");

    def test_codify2(self):
        print("Advanced codify2 test running");
        self.assertEqual(codifica2('ddd',gera_chave2(self.testTuple)),'141414',"Erro on codifica2");
    def test_codify3(self):
        print("Advanced codify3 test running");
        self.assertEqual(codifica2(',AhxlPITYxpw;vqiFMLQcrQmFocNmxRtLRKHyHjaVVJeIKWvyZSpezKlUadjAREODhByOdwZVHepqCZwIQ;ChITNgHKcEHWuJDqqF,YzJCwO,CyvOGntEJpxKcJxYouMGxrRVCITlebhC,clqJKLnTTV;mMWHorYtUCU;SzEBMTxJLyNmBIintILyWuwfXnWJxTlTnOdmjAiMSNNDSLXqHyadPiJknVJsNDhVfQhuSHUGcgTrh;VwrBrxze;vCxDTgrqEvnT,DYzoJShRiIWTEAWL;DfRUSNRRRDlpYRMedKcw;YKzfdCZMRyoToOepfQJQAwfMAXKyIDfKnaFetKQSaxnmtLwqZUm;hZyjaQeZZmEzm,CwtEVQoNPGoQqujoLlcQACeOFrZctiQk,SbpRcHWfHVZH,wRSnMsSkXa,tbQKWKoDZhwBsNvclqSoByUhMKfgdOdqjNVIDzUApuRlUbSMPgsUjJYHyukjeIFxfrcgkMXvJB.',gera_chave1(self.testTuple)),'0401XXXXXXXXXXXXXXXXXXXX10XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX00XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0014XX01XXXXXX13XX11XXXX14XXXXXXXXXXXXXX12XXXXXXXX1012XXXXXXXXXXXXXXXXXXXXXXXXXX13XXXXXX04XXXXXX12XXXX0412XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX12XXXXXXXXXXXX1204XXXXXXXXXXXXXXXXXXXX10XXXXXXXXXXXXXXXXXX12XX10XXXXXX11XXXXXXXXXXXXXXXX11XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX14XXXX01XXXXXXXXXX13XXXXXXXXXXXX0014XXXXXXXXXXXXXXXXXX13XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX10XXXXXX11XXXXXXXX10XX12XX13XXXXXXXXXXXXXXXX0413XXXXXXXXXXXXXXXXXXXXXXXX01XXXX1013XXXXXXXXXXXXXXXX13XXXXXXXXXXXX14XXXXXX10XXXXXXXX1412XXXXXXXXXXXXXXXXXXXXXXXXXXXX01XXXXXX01XXXXXXXX13XXXXXX00XXXXXXXXXXXX00XXXXXXXXXXXXXXXXXXXX10XXXXXXXX00XXXXXXXXXXXXXXXX0412XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0112XXXXXXXXXXXXXXXXXXXX04XXXXXXXXXXXXXXXXXXXXXXXX04XXXXXXXXXXXXXXXXXX0004XXXXXXXXXXXXXX13XXXXXX11XXXXXXXXXXXXXXXX11XXXXXXXXXXXXXX14XX14XXXXXXXXXX13XXXX01XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1103',"Erro on codifica2");
    def test_getCar1(self):
        print("Advanced getCar1 test running");
        self.assertEqual(obtem_car2('00',gera_chave2(self.testTuple)),'a',"Erro on obtem_car2");
    def test_getCar2(self):
        print("Advanced getCar2 test running");
        self.assertEqual(obtem_car2('20',gera_chave2(self.testTuple)),'o',"Erro on obtem_car2");
    def test_getCar3(self):
        print("Advanced getCar3 test running");
        self.assertEqual(obtem_car2('XX',gera_chave2(self.testTuple)),'?',"Erro on obtem_car2");
    def test_decrypt(self):
        print("Advanced decrypt test running");
        self.assertEqual(descodifica2('04001414XX1404140412XX1303XX03XX13XX0304101214XXXX031010130311XX13XX04XXXXXX00001401XX1114110104XX140100140113101003XX1004XXXX041114XX1014140000030300XX1304XX12001014XX03XX000300131412XX1313XX11041312XXXX1304XX10XXXX03XX1204101001XX00XX00040404XX030301121201011414031304001310XX040010031211031304XXXX121300031214XX12140013111213XX1004XX1004031101100003XXXXXX031104111114XXXXXX0311XX121001120412XX10100012121401XX11111313XX00XX0103XX11031300030004XXXX1004XXXX01111012131014031000XX0403XXXX01XXXX10XX101010XXXX0300XX10XX0001040010XX100000XX04101313141201XX12XX031303031200100101101200XX110001101211040114XX031204110411XX14000104001103XX0101111010XX00XX131114XX13001110XX11000014001401040000111201XXXX1114XX03XXXX1104XX04XX1114111300XXXX11XX13131101XX111303041304031314011104XX100010XXXX1211130310XXXX1101XX00XX010112XX13121004041404XX1214121203131400XX001203111412XX120404130112120313XXXX04121414031103XX0110XX0410000413XX10011313121000XX14141210130013XX13XX101112100300041410XX03121310XX031414XXXXXXXX',gera_chave2(self.testTuple)),',add?d,d,C?D.?.?D?.,;Cd??.;;D.B?D?,???aadA?BdBA,?dAadAD;;.?;,??,Bd?;ddaa..a?D,?Ca;d?.?a.aDdC?DD?B,DC??D,?;??.?C,;;A?a?a,,,?..ACCAAdd.D,aD;?,a;.CB.D,??CDa.Cd?CdaDBCD?;,?;,.BA;a.???.B,BBd???.B?C;AC,C?;;aCCdA?BBDD?a?A.?B.Da.a,??;,??AB;CD;d.;a?,.??A??;?;;;??.a?;?aA,a;?;aa?,;DDdCA?C?.D..Ca;AA;Ca?BaA;CB,Ad?.C,B,B?daA,aB.?AAB;;?a?DBd?DaB;?BaadadA,aaBCA??Bd?.??B,?,?BdBDa??B?DDBA?BD.,D,.DdAB,?;a;??CBD.;??BA?a?AAC?DC;,,d,?CdCC.Dda?aC.BdC?C,,DACC.D??,Cdd.B.?A;?,;a,D?;ADDC;a?ddC;DaD?D?;BC;.a,d;?.CD;?.dd????',"Erro on descodifica1");





class NormalOperation(unittest.TestCase):
    testTuple=('a','A',' ','.',',',';','B','C','D','d');

    def test_Generate(self):
        print("Generate test Running");
        self.assertEqual(gera_chave1(self.testTuple),(('a','A',' ','.',','),(';','B','C','D','d')),"Error in gera_chave");
    def test_getCode1(self):
        print("getCode1 test running");
        self.assertEqual(obtem_codigo1('a',gera_chave1(self.testTuple)),'00',"Erro on obtem-codigo1");
    def test_getCode2(self):
        print("getCode2 test running");
        self.assertEqual(obtem_codigo1(';',gera_chave1(self.testTuple)),'10',"Erro on obtem-codigo1");

    def test_getCode3(self):
        print("getCode3 test running");
        self.assertEqual(obtem_codigo1('d',gera_chave1(self.testTuple)),'14',"Erro on obtem-codigo1");
    def test_codify1(self):
        print("codify1 test running");
        self.assertEqual(codifica1('BCa.',gera_chave1(self.testTuple)),'11120003',"Erro on codifica1");

    def test_codify2(self):
        print("codify2 test running");
        self.assertEqual(codifica1('ddd',gera_chave1(self.testTuple)),'141414',"Erro on codifica1");

    def test_getCar1(self):
        print("getCar1 test running");
        self.assertEqual(obtem_car1('00',gera_chave1(self.testTuple)),'a',"Erro on obtem_car1");
    def test_getCar2(self):
        print("getCar2 test running");
        self.assertEqual(obtem_car1('14',gera_chave1(self.testTuple)),'d',"Erro on obtem_car1");
    def test_getCar3(self):
        print("getCar3 test running");
        self.assertEqual(obtem_car1('11',gera_chave1(self.testTuple)),'B',"Erro on obtem_car1");
    def test_decrypt(self):
        print("decrypt test running");
        self.assertEqual(descodifica1('120014',gera_chave1(self.testTuple)),'Cad',"Erro on descodifica1");



if __name__ == '__main__':
    unittest.main()
