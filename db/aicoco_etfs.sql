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
-- Table structure for table `etfs`
--

DROP TABLE IF EXISTS `etfs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `etfs` (
  `ticker` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `etfName` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expenseRatio` decimal(6,2) NOT NULL,
  `YTDreturn` decimal(6,2) NOT NULL,
  `yrReturn1` decimal(6,2) NOT NULL,
  `yrReturn3` decimal(6,2) NOT NULL,
  `yrReturn5` decimal(6,2) NOT NULL,
  `StdDev` decimal(6,2) NOT NULL,
  `SharpeRatio` decimal(6,2) NOT NULL,
  PRIMARY KEY (`ticker`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etfs`
--

LOCK TABLES `etfs` WRITE;
/*!40000 ALTER TABLE `etfs` DISABLE KEYS */;
INSERT INTO `etfs` VALUES ('AGG','iShares Core US Aggregate Bond ETF','usBond',0.06,-2.39,-0.63,0.92,1.36,2.73,0.14),('BND','Vanguard Total Bond Market ETF','usBond',0.05,-1.59,1.15,1.12,1.73,2.86,0.19),('BNDX','Vanguard Total International Bond ETF','worldBond',0.11,0.69,2.73,2.60,3.69,2.72,0.69),('EFA','iShares MSCI EAFE ETF','worldStock',0.32,0.61,13.89,4.94,5.72,12.14,0.40),('IBND','SPDR Blmbg Barclays Intl Corp Bd ETF','worldBond',0.50,-0.32,10.57,3.11,0.43,7.40,0.38),('IEMG','iShares Core MSCI Emerging Markets ETF','emerStock',0.14,-0.09,19.66,5.58,4.31,15.65,0.40),('IXUS','iShares Core MSCI Total Intl Stk ETF','worldStock',0.12,0.38,15.89,5.74,5.81,12.08,0.47),('LQD','iShares iBoxx Invmt Grade Corp Bd ETF','usBond',0.15,-4.42,-0.04,1.95,2.24,4.54,0.32),('QQQ','PowerShares QQQ ETF','usStock',0.20,2.98,22.01,16.03,19.69,13.79,1.11),('SPEM','SPDR Portfolio Emerging Markets ETF','emerStock',0.59,3.01,23.98,8.76,5.71,16.34,0.52),('SPY','SPDR S&P 500 ETF','usStock',0.09,-0.48,13.22,10.47,12.86,10.24,0.96),('VEU','Vanguard FTSE All-Wld ex-US ETF','worldStock',0.11,-0.35,16.88,6.72,6.34,11.83,0.56),('VUG','Vanguard Growth ETF','usStock',0.05,1.41,15.67,11.20,14.02,11.35,0.94),('VWO','Vanguard FTSE Emerging Markets ETF','emerStock',0.14,2.52,21.21,7.57,4.64,15.92,0.50),('XLF','Financial Select Sector SPDR ETF','sectorStock',0.14,-0.86,18.08,14.19,15.30,15.24,0.91),('XLK','Technology Select Sector SPDR ETF','sectorStock',0.14,2.62,24.50,18.43,18.74,13.09,1.32),('XLV','Health Care Select Sector SPDR ETF','sectorStock',0.14,-0.16,10.61,6.30,13.40,13.00,0.48);
/*!40000 ALTER TABLE `etfs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-06 14:31:20
