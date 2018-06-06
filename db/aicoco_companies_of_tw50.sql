-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: aicoco
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `companies_of_tw50`
--

DROP TABLE IF EXISTS `companies_of_tw50`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies_of_tw50` (
  `CompanyID` int(10) NOT NULL,
  `CompanyName` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Abbreviation` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies_of_tw50`
--

LOCK TABLES `companies_of_tw50` WRITE;
/*!40000 ALTER TABLE `companies_of_tw50` DISABLE KEYS */;
INSERT INTO `companies_of_tw50` VALUES (1101,'台泥',NULL),(1102,'亞泥',NULL),(1216,'統一',NULL),(1301,'台塑',NULL),(1303,'南亞',NULL),(1326,'台化',NULL),(1402,'遠東新',NULL),(1722,'台肥',NULL),(2002,'中鋼',NULL),(2015,'正新',NULL),(2201,'裕隆',NULL),(2207,'和泰車',NULL),(2301,'光寶科',NULL),(2303,'聯電',NULL),(2308,'台達電',NULL),(2311,'2311',NULL),(2317,'鴻海',NULL),(2324,'仁寶',NULL),(2325,'2325',NULL),(2330,'TSMC','TSMC'),(2347,'聯強',NULL),(2353,'宏碁',NULL),(2354,'鴻準',NULL),(2357,'華碩',NULL),(2382,'廣達',NULL),(2409,'友達',NULL),(2412,'中華電',NULL),(2454,'聯發科',NULL),(2474,'可成',NULL),(2498,'宏達電',NULL),(2801,'彰銀',NULL),(2880,'華南金',NULL),(2881,'富邦金',NULL),(2882,'國泰金',NULL),(2883,'開發金',NULL),(2885,'元大金',NULL),(2886,'兆豐金',NULL),(2890,'永豐金',NULL),(2891,'中信金',NULL),(2892,'第一金',NULL),(2912,'統一超',NULL),(3008,'大立光',NULL),(3045,'台灣大',NULL),(3231,'緯創',NULL),(3481,'群創',NULL),(3673,'TPK-KY',NULL),(3697,'3697',NULL),(4904,'遠傳',NULL),(5880,'合庫金',NULL),(6505,'台塑化',NULL);
/*!40000 ALTER TABLE `companies_of_tw50` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-06 13:40:12
